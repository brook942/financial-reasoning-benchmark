"""Summarize benchmark results.

Inputs (in data/):
  questions_ground_truth.csv  one row per question
  scores.csv                  one row per scored response (human scores)
  rescore.csv                 optional re-scored sample for the consistency check

Outputs (in analysis/):
  results_tables.md           all result tables in Markdown
  charts/*.png                bar charts (if matplotlib is installed)
"""
import argparse
from pathlib import Path

import pandas as pd

VALID_ERRORS = {
    "arithmetic", "wrong_formula", "wrong_input", "unit_scale", "period_mixup",
    "rounding", "sign_error", "misread_question", "no_answer", "none",
}
RUBRIC_COLS = ["method", "assumptions", "units_labeling"]
RUBRIC_MAX = 6


def to_markdown(df, index=True):
    """Minimal DataFrame to Markdown table, no extra dependencies."""
    frame = df.reset_index() if index else df.copy()
    frame = frame.astype(object).where(frame.notna(), "")
    header = "| " + " | ".join(str(c) for c in frame.columns) + " |"
    divider = "|" + "|".join("---" for _ in frame.columns) + "|"
    rows = ["| " + " | ".join(str(v) for v in row) + " |" for row in frame.itertuples(index=False)]
    return "\n".join([header, divider] + rows)


def load(data_dir, questions_file):
    questions = pd.read_csv(data_dir / questions_file)
    scores = pd.read_csv(data_dir / "scores.csv")
    if scores.empty:
        raise SystemExit("data/scores.csv has no rows yet. Score some responses first.")
    scores["rubric_total"] = scores[RUBRIC_COLS].sum(axis=1)
    merged = scores.merge(
        questions[["q_id", "category", "difficulty", "trap_type"]], on="q_id", how="left"
    )
    missing = merged["category"].isna().sum()
    if missing:
        print(f"Warning: {missing} scored rows have a q_id not found in the questions file.")
    bad = set(scores["error_type"].dropna()) - VALID_ERRORS
    if bad:
        print(f"Warning: unrecognized error_type values: {sorted(bad)}")
    return merged


def summarize(df, by):
    grouped = df.groupby(by)
    out = pd.DataFrame({
        "responses": grouped.size(),
        "accuracy_%": (grouped["final_correct"].mean() * 100).round(1),
    })
    if "exact_match" in df.columns:
        out["exact_match_%"] = (grouped["exact_match"].mean() * 100).round(1)
    out["avg_rubric_/6"] = grouped["rubric_total"].mean().round(2)
    return out


def consistency(df, data_dir):
    path = data_dir / "rescore.csv"
    if not path.exists():
        return None
    re = pd.read_csv(path)
    if re.empty:
        return None
    re["rubric_total"] = re[RUBRIC_COLS].sum(axis=1)
    joined = df.merge(re, on=["q_id", "model"], suffixes=("", "_re"))
    if joined.empty:
        return None
    n = len(joined)
    return {
        "responses_rescored": n,
        "final_correct_agreement_%": round((joined["final_correct"] == joined["final_correct_re"]).mean() * 100, 1),
        "exact_rubric_agreement_%": round((joined["rubric_total"] == joined["rubric_total_re"]).mean() * 100, 1),
        "mean_abs_rubric_diff": round((joined["rubric_total"] - joined["rubric_total_re"]).abs().mean(), 2),
    }


def make_charts(tables, out_dir):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not installed; skipping charts.")
        return
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, table in tables.items():
        col = "exact_match_%" if "exact_match_%" in table.columns else "accuracy_%"
        data = table[col]
        fig, ax = plt.subplots(figsize=(7, 4))
        data.plot(kind="bar", ax=ax)
        ax.set_ylabel("Exact match at requested precision (%)" if col == "exact_match_%" else "Accuracy (%)")
        ax.set_ylim(0, 100)
        ax.set_title(f"Exact-match accuracy by {name.replace('_', ' ')}" if col == "exact_match_%" else f"Accuracy by {name.replace('_', ' ')}")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        fig.savefig(out_dir / f"accuracy_by_{name}.png", dpi=150)
        plt.close(fig)


def main():
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", default=str(root / "data"))
    parser.add_argument("--questions", default="questions_ground_truth.csv")
    parser.add_argument("--out-dir", default=str(root / "analysis"))
    args = parser.parse_args()

    data_dir, out_dir = Path(args.data_dir), Path(args.out_dir)
    df = load(data_dir, args.questions)

    tables = {
        "model": summarize(df, "model"),
        "category": summarize(df, "category"),
        "difficulty": summarize(df, "difficulty"),
        "trap_type": summarize(df, "trap_type"),
        "model_and_category": summarize(df, ["model", "category"]),
    }
    miss = df[df["exact_match"] == 0] if "exact_match" in df.columns else df[df["final_correct"] == 0]
    errors = (
        miss.groupby(["model", "error_type"]).size().rename("responses_missing_key").to_frame()
        if len(miss) else pd.DataFrame({"responses_missing_key": []})
    )
    components = df.groupby("model").agg(
        explicit_assumption_rate=("assumptions", lambda s: round((s == 2).mean() * 100, 1)),
        unit_labeled_rate=("units_labeling", lambda s: round((s == 2).mean() * 100, 1)),
    )
    halluc = pd.DataFrame({
        "responses": df.groupby("model").size(),
        "invented_figure_rate_%": (df.groupby("model")["hallucinated_figure"].mean() * 100).round(1),
    })
    cons = consistency(df, data_dir)

    parts = ["# Results Tables (generated by analyze.py)\n",
             f"Scored responses: {len(df)}\n"]
    for name, table in tables.items():
        parts += [f"\n## Accuracy and rubric score by {name.replace('_', ' ')}\n", to_markdown(table)]
    parts += ["\n## Answers missing the key at the requested precision (by cause)\n", to_markdown(errors)]
    parts += ["\n## Assumption and unit labeling (rule-based)\n", to_markdown(components)]
    parts += ["\n## Invented figures by model\n", to_markdown(halluc)]
    if cons:
        parts += ["\n## Scoring consistency (re-score check)\n",
                  to_markdown(pd.DataFrame([cons]), index=False)]
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "results_tables.md").write_text("\n".join(parts) + "\n", encoding="utf-8")
    make_charts({k: v for k, v in tables.items() if k != "model_and_category"}, out_dir / "charts")
    print(f"Wrote {out_dir / 'results_tables.md'}")


if __name__ == "__main__":
    main()
