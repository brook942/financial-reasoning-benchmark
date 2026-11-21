"""Draft the 'final answer correct' check against ground truth.

Reads data/questions_ground_truth.csv and data/responses_raw.csv, compares each
extracted_answer with truth_value using the question's tolerance, and writes
data/auto_grade_draft.csv.

This is only a first pass. Review every row by hand: the human score in
data/scores.csv is the one used in the analysis.
"""
import argparse
import re
from pathlib import Path

import pandas as pd


def parse_number(text):
    """Pull the first number out of a string such as '$17.5%' or '1,234.5x'."""
    if pd.isna(text):
        return None
    cleaned = str(text).replace(",", "").replace("$", "").replace("\u2212", "-")
    cleaned = re.sub(r"^\((.*)\)$", r"-\1", cleaned.strip())  # (10) means -10
    match = re.search(r"-?\d+(?:\.\d+)?", cleaned)
    return float(match.group()) if match else None


def within_tolerance(value, truth, tol, tol_type):
    if value is None or pd.isna(truth) or pd.isna(tol):
        return None
    diff = abs(value - truth)
    if tol_type == "pct":
        return diff <= abs(truth) * tol / 100.0
    return diff <= tol


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", default=str(Path(__file__).resolve().parent.parent / "data"))
    parser.add_argument("--questions", default="questions_ground_truth.csv")
    args = parser.parse_args()

    data = Path(args.data_dir)
    questions = pd.read_csv(data / args.questions)
    responses = pd.read_csv(data / "responses_raw.csv")

    merged = responses.merge(
        questions[["q_id", "truth_value", "unit", "tolerance", "tolerance_type"]],
        on="q_id",
        how="left",
    )
    merged["parsed_answer"] = merged["extracted_answer"].apply(parse_number)
    merged["auto_correct"] = merged.apply(
        lambda r: within_tolerance(r["parsed_answer"], r["truth_value"], r["tolerance"], r["tolerance_type"]),
        axis=1,
    )
    out = merged[["q_id", "model", "extracted_answer", "parsed_answer", "truth_value", "unit", "auto_correct"]]
    out_path = data / "auto_grade_draft.csv"
    out.to_csv(out_path, index=False)
    print(f"Wrote {len(out)} rows to {out_path}")
    unmatched = int(out["truth_value"].isna().sum())
    if unmatched:
        print(f"Warning: {unmatched} responses have no matching question in {args.questions}")


if __name__ == "__main__":
    main()
