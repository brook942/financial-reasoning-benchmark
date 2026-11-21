# Methodology

## 1. Objective

Measure how accurately current AI models answer finance and accounting
calculation questions when all required data is supplied, and document every
rule used to score them.

## 2. Question design

- Total questions: 60
- Categories (12 each): financial statements, profitability, cash flow, ratios,
  valuation
- Difficulty per category: 4 easy, 5 medium, 3 hard
- Trap questions (11): units/scale (2), fiscal vs. calendar period (1), sign
  convention (3), net vs. gross debt (3), mid-year discounting (1), unallocated
  costs (1)
- Data: fictional companies with invented figures; no real filings were used
- Each prompt gives every input, the unit, the rounding rule, and ends with
  "End with: Answer: <value>", so each question has one correct answer

## 3. Ground truth

Each answer is computed from the formula stored in the `calculation` column of
`data/questions_ground_truth.csv`, using `analysis/build_questions.py`.
Independent verification by the author in Excel: [N] of 60 questions recomputed
on [DATE]; differences found: [N]. *(To be completed by the author.)*

## 4. Models and protocol

| Model | Version label shown | Settings | Run date |
|---|---|---|---|
| DeepSeek | DeepSeek V4.1 | DeepThink on; web search and memory not recorded | 2026-11-21 |
| Gemini | Gemini 4 Hydrogen | Google AI Studio; thinking level high; code execution off | 2026-11-20 |
| ChatGPT | GPT-6 | Instant mode; no Sol or Luna label shown; web search and memory not recorded | 2026-11-21 |

Protocol (`prompts/prompt_template.md`, `prompts/batches_to_paste.md`):

- Identical text for every model, no per-model edits
- Questions run in 6 batches of 10, a new chat for each batch
- First reply only; no regenerating and no follow-up questions
- Run dates are as reported by the author

Deviation to disclose: Gemini Batch 1 was first run in the Gemini app, where the
model executed code before answering. That run was discarded and Batch 1 was
re-run in Google AI Studio with code execution off, so that Gemini matched the
other models. Only the AI Studio responses are used.

## 5. Scoring

Rules are in `rubric/scoring_rubric.md` and implemented in `analysis/score.py`.

- **Primary measure:** answer within the question's tolerance (set before any
  model was run)
- **Secondary measure:** exact match at the requested decimals, added after the
  results showed three small slips that fell inside the tolerance
- **Rubric components:** method, assumptions, units/labeling (maximum 6 total)
- **Error causes:** found by recomputing each step of a missed answer by hand

Scoring was performed by an AI assistant (Claude) applying the published rules.
It was not blind to model names. The same assistant helped design the benchmark
and write the scripts. No Claude model was tested. The author's review of a
sample of scores is recorded in the README under "Verification status".

## 6. Consistency check

Not performed in v1.0. `data/rescore.csv` is empty. A re-score of a random
sample after at least 7 days would measure scoring stability.

## 7. Analysis

`analysis/analyze.py` computes accuracy, exact-match rate, and average rubric
score by model, category, difficulty, and trap type, plus error causes, the
rates of explicit assumptions and unit labeling, and the invented-figure rate.

## 8. Limitations

See the README. In short: small sample, a ceiling effect, a loose tolerance on
valuation questions, scoring rules finalized after data collection, non-blind
scoring, different reasoning settings across models, batching of 10 questions
per chat, and fictional data.

## 9. Changelog

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-11-21 | Initial release: 60 questions, 3 models, 180 scored responses |
