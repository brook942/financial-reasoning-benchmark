# Scoring Rubric (v1.1, rule-based)

This version replaces the v1.0 plan of hand-scoring every response. The rules
below were written after the responses were collected, so they are described
here exactly as applied. All scores are produced by `analysis/score.py`, which
anyone can re-run on `data/responses_raw.csv`.

## 1. Final answer correct (0 or 1) - primary measure

1 if the answer is within the question's tolerance of `truth_value`
(`tolerance` and `tolerance_type` columns: `abs` = absolute difference, `pct` =
percent of the true value). The tolerances were set before any model was run.

## 2. Exact match at requested precision (0 or 1) - secondary measure

1 if the answer, rounded to the number of decimals the question asked for (the
`decimals` column), equals the key rounded the same way.

This measure was added after the results were seen. Three valuation answers
fell inside the ±0.5% tolerance yet differed from the key at the requested
decimals, so the tolerance alone hid a real difference. Report both measures.

## 3. Method (0 or 2)

2 if the response shows the formula and the steps leading to its answer
(`calculation_shown` = 1). A correct method with an arithmetic slip still
scores 2; the slip is recorded under error type. All 180 responses showed a
calculation, so this component does not separate the models.

## 4. Assumptions (1 or 2)

2 if the response contains an explicit assumption statement
(`assumption_stated` = 1), such as an "Assumption:" line, or a shared
"Assumptions used throughout" preamble covering that question. A label that
says "None" does not count. Otherwise 1.

Limitation: this rule rewards stating an assumption even on questions that
need none, so it measures presentation habits, not reasoning quality.

## 5. Units and labeling (1 or 2)

2 if the final answer line carries the unit the question asked for:
"million" for $M, "thousand" for $K, "$" for dollars, "%" for percent, "days"
for days, "units" for units. Multiples and ratios ("x") always score 2.
Otherwise 1. A wrong scale would score 0 (none occurred).

Rubric total = method + assumptions + units/labeling (maximum 6).

## Error types (for answers that miss the key at requested precision)

| Code | Meaning |
|---|---|
| arithmetic | Correct method, calculation slip |
| wrong_formula | Wrong formula or financial concept |
| wrong_input | Used the wrong figure from the prompt |
| unit_scale | Thousands/millions or percent/decimal confusion |
| period_mixup | Wrong fiscal year, period, or timing convention |
| rounding | Rounding moved the answer off the key |
| sign_error | Sign convention error |
| misread_question | Answered a different question |
| no_answer | Refused, or no final value given |
| none | Matched the key |

Causes were identified by recomputing each step of the response by hand.

## Hallucinated figure (0 or 1)

1 if a response uses a number that is neither in the prompt nor derived from
it. None occurred.
