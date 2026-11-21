"""Blind scoring helper.

Step 1  python analysis/blind.py make
        Shuffles data/responses_raw.csv, hides model names, and writes
        data/blind_scoring_sheet.csv (fill in the score columns) and
        data/blind_key.csv (the secret mapping; do not open until you finish).

Step 2  Fill in the score columns of blind_scoring_sheet.csv:
        final_correct (0/1), method (0-2), assumptions (0-2),
        units_labeling (0-2), error_type, hallucinated_figure (0/1), notes.

Step 3  python analysis/blind.py merge
        Joins your scores with the key and writes data/scores.csv.
"""
import argparse
import random
import sys
from pathlib import Path

import pandas as pd

SCORE_COLS = ["final_correct", "method", "assumptions", "units_labeling",
              "error_type", "hallucinated_figure", "notes"]


def make(data, seed):
    responses = pd.read_csv(data / "responses_raw.csv")
    if responses.empty:
        sys.exit("data/responses_raw.csv has no rows yet.")
    questions = pd.read_csv(data / "questions_ground_truth.csv")
    merged = responses.merge(questions[["q_id", "prompt", "truth_value", "unit"]], on="q_id", how="left")
    order = list(range(len(merged)))
    random.Random(seed).shuffle(order)
    merged = merged.iloc[order].reset_index(drop=True)
    merged.insert(0, "blind_id", [f"B{i + 1:03d}" for i in range(len(merged))])
    key = merged[["blind_id", "q_id", "model"]]
    sheet = merged[["blind_id", "q_id", "prompt", "truth_value", "unit", "extracted_answer", "answer_line"]].copy()
    for col in SCORE_COLS:
        sheet[col] = ""
    sheet.to_csv(data / "blind_scoring_sheet.csv", index=False)
    key.to_csv(data / "blind_key.csv", index=False)
    print(f"Wrote {len(sheet)} rows to blind_scoring_sheet.csv and blind_key.csv")


def merge(data):
    sheet = pd.read_csv(data / "blind_scoring_sheet.csv")
    key = pd.read_csv(data / "blind_key.csv")
    required = ["final_correct", "method", "assumptions", "units_labeling", "error_type"]
    incomplete = sheet[sheet[required].isna().any(axis=1)]
    if len(incomplete):
        sys.exit(f"{len(incomplete)} rows are missing scores (first: {incomplete['blind_id'].iloc[0]}). "
                 "Fill every required column first.")
    if "hallucinated_figure" in sheet and sheet["hallucinated_figure"].isna().any():
        sheet["hallucinated_figure"] = sheet["hallucinated_figure"].fillna(0)
    scores = sheet.merge(key[["blind_id", "model"]], on="blind_id", how="left")
    cols = ["q_id", "model", "final_correct", "method", "assumptions", "units_labeling",
            "error_type", "hallucinated_figure", "notes"]
    scores[cols].to_csv(data / "scores.csv", index=False)
    print(f"Wrote {len(scores)} rows to scores.csv")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["make", "merge"])
    parser.add_argument("--data-dir", default=str(Path(__file__).resolve().parent.parent / "data"))
    parser.add_argument("--seed", type=int, default=2026)
    args = parser.parse_args()
    data = Path(args.data_dir)
    make(data, args.seed) if args.command == "make" else merge(data)


if __name__ == "__main__":
    main()
