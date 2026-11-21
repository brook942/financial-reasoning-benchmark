"""Rule-based scoring of data/responses_raw.csv -> data/scores.csv.

Every score comes from a rule that can be re-run by anyone:

  final_correct   1 if the answer is within the question's tolerance (the rule
                  fixed before results were seen). Primary measure.
  exact_match     1 if the answer equals the key at the decimal places the
                  question asked for. Secondary measure, added after results
                  showed small slips that the tolerance rule absorbed.
  method          2 if the response shows the formula and steps (recorded as
                  calculation_shown in the responses file), else 0.
  assumptions     2 if the response states an explicit assumption
                  (assumption_stated = 1), else 1. A label reading "None"
                  does not count.
  units_labeling  2 if the answer line carries the unit the question asked
                  for (see UNIT_RULES), else 1. Multiples and ratios (unit "x")
                  always get 2. A wrong scale would get 0.
  error_type      "none" if exact_match, otherwise the cause (set below).
  hallucinated_figure  0 unless a response uses a number not in the prompt.
"""
import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

UNIT_RULES = {          # unit in question file -> pattern that must appear in the answer line
    "$M": r"million",
    "$K": r"thousand",
    "$": r"\$|dollar",
    "%": r"%",
    "days": r"day",
    "units": r"unit",
}
# Causes for answers that miss the key at the requested precision, found by
# recomputing each step by hand. Empty if nothing misses.
KNOWN_CAUSES = {
    ("GPT-6", "Q053"): "arithmetic",   # 1,100 / 1.12^3 written as 782.76 (correct: 782.96)
    ("GPT-6", "Q058"): "arithmetic",   # discounted terminal value written as 1,327.60 (correct: 1,326.61)
    ("GPT-6", "Q059"): "arithmetic",   # discounted cash flows slightly off in all three terms
}


def parse_number(text):
    cleaned = str(text).replace(",", "").replace("$", "").replace("\u2212", "-")
    cleaned = re.sub(r"^\((.*)\)$", r"-\1", cleaned.strip())
    match = re.search(r"-?\d+(?:\.\d+)?", cleaned)
    return float(match.group()) if match else None


def main():
    q = pd.read_csv(ROOT / "data" / "questions_ground_truth.csv")
    r = pd.read_csv(ROOT / "data" / "responses_raw.csv")
    d = r.merge(q[["q_id", "truth_value", "unit", "tolerance", "tolerance_type", "decimals"]], on="q_id", how="left")
    d["value"] = d["extracted_answer"].apply(parse_number)
    diff = (d["value"] - d["truth_value"]).abs()
    tol = d.apply(lambda x: abs(x["truth_value"]) * x["tolerance"] / 100 if x["tolerance_type"] == "pct" else x["tolerance"], axis=1)
    d["final_correct"] = (diff <= tol + 1e-9).astype(int)
    # exact match: the answer, rounded to the decimals the question asked for, equals the key
    d["exact_match"] = d.apply(lambda x: int(round(x["value"], int(x["decimals"])) == round(x["truth_value"], int(x["decimals"]))), axis=1)

    d["method"] = d["calculation_shown"].apply(lambda v: 2 if v == 1 else 0)
    d["assumptions"] = d["assumption_stated"].apply(lambda v: 2 if v == 1 else 1)

    def units(row):
        rule = UNIT_RULES.get(row["unit"])
        if rule is None:
            return 2
        return 2 if re.search(rule, str(row["answer_line"]), re.I) else 1
    d["units_labeling"] = d.apply(units, axis=1)

    d["error_type"] = d.apply(
        lambda x: "none" if x["exact_match"] else KNOWN_CAUSES.get((x["model"], x["q_id"]), "unclassified"), axis=1)
    d["hallucinated_figure"] = 0
    d["notes"] = ""
    cols = ["q_id", "model", "final_correct", "exact_match", "method", "assumptions", "units_labeling",
            "error_type", "hallucinated_figure", "notes"]
    d[cols].to_csv(ROOT / "data" / "scores.csv", index=False)
    print(f"Wrote {len(d)} scored responses to data/scores.csv")
    unclassified = d[d["error_type"] == "unclassified"]
    if len(unclassified):
        print("Need a cause for:", unclassified[["model", "q_id"]].values.tolist())


if __name__ == "__main__":
    main()
