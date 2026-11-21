# Financial Reasoning & Numerical Accuracy Benchmark

A small, fully documented benchmark that tests how accurately AI models answer
finance and accounting calculation questions. Every answer is checked against
an independently defined ground truth, every error is classified, and every
rule used for scoring is published.

**Author:** Biruk Hadera | [LinkedIn](https://www.linkedin.com/in/biruk-hadera-tesfay/)
Finance and accounting professional working in AI data quality and evaluation.

> **Status:** v1.0 results complete. Author verification of the answer key and
> of a sample of scores is listed under "Verification status" below.

## Headline results

| Model | Setting | Run date | Within tolerance (primary) | Exact match at requested precision (secondary) | Avg rubric score (max 6) |
|---|---|---|---|---|---|
| DeepSeek V4.1 | DeepThink on | 2026-11-21 | 60/60 (100%) | 60/60 (100%) | 4.85 |
| Gemini 4 Hydrogen | Google AI Studio, thinking level high, code execution off | 2026-11-20 | 60/60 (100%) | 60/60 (100%) | 5.82 |
| GPT-6 | Instant mode | 2026-11-21 | 60/60 (100%) | 57/60 (95.0%) | 5.30 |

**Key findings**

1. **The benchmark did not separate the models on the primary measure.** All
   three answered all 60 questions within tolerance, including the eleven trap
   questions on units, fiscal periods, sign conventions, net vs. gross debt, and
   unallocated costs. Clean, fully specified calculations are not hard for
   these models.
2. **The only differences appear at the requested decimal place.** GPT-6
   (Instant) missed the key on 3 of 12 valuation questions (Q053, Q058, Q059).
   Each used the correct method and made an arithmetic slip in a discounting
   step, for example writing 1,100 / 1.12^3 as 782.76 instead of 782.96. Both
   other models matched the key on all three. The three misses were inside the
   pre-set tolerance, which is why the secondary measure was added. The cause
   is not established: OpenAI describes GPT-6 as able to think while answering,
   so Instant mode is not necessarily a no-reasoning setting.
3. **Rubric differences come from presentation, not correctness.** Gemini
   stated an explicit assumption on 59 of 60 questions, against about 30% for
   DeepSeek and GPT-6. GPT-6 labeled units on every answer, Gemini on 83%, and
   DeepSeek on 53%. The rubric counts an assumption statement even when a
   question needs none, so treat these as style differences.

Full tables: [`analysis/results_tables.md`](analysis/results_tables.md) |
Written summary: [`analysis/results_summary.md`](analysis/results_summary.md) |
Charts: [`analysis/charts/`](analysis/charts/)

## What was tested

- **60 questions** in five categories (12 each): financial statements,
  profitability, cash flow, ratios, and valuation
- Three difficulty levels per category (4 easy, 5 medium, 3 hard)
- Eleven deliberate "trap" questions: units/scale (2), fiscal vs. calendar
  period (1), sign convention (3), net vs. gross debt (3), mid-year discounting
  (1), unallocated costs (1), counted across the five categories
- **Fictional company data** written for this benchmark, so every question has
  exactly one verifiable answer (formula stored in the `calculation` column)
- **3 models**, one attempt per question, questions run in batches of 10 in a
  new chat per batch, 180 responses in total

## Method in brief

1. 60 questions with all data in the prompt (`analysis/build_questions.py`)
2. Ground truth computed from the formula stored with each question
3. Identical prompt text for every model
   ([`prompts/batches_to_paste.md`](prompts/batches_to_paste.md))
4. Rule-based scoring by script (`analysis/score.py`, rules in
   [`rubric/scoring_rubric.md`](rubric/scoring_rubric.md)): within tolerance,
   exact match, method, assumptions, units
5. Error classification by recomputing each missed answer by hand

Details and exact settings: [`METHODOLOGY.md`](METHODOLOGY.md)

## Verification status

- Answer key recomputed independently in Excel by the author: [N] of 60
  questions on [DATE]; differences found: [N]
- Author review of AI-assigned scores: [N] responses checked on [DATE];
  disagreements: [N]

Scoring was done by an AI assistant (Claude) following the published rules; it
was not blind to model names. The final-answer scores come directly from the
answer key and can be re-run with `python analysis/score.py`.

## Repository layout

```
.
├── README.md
├── METHODOLOGY.md
├── data/
│   ├── questions_ground_truth.csv   60 questions, answers, formulas
│   ├── responses_raw.csv            verbatim final answer lines, 180 rows
│   ├── scores.csv                   scores for all 180 responses
│   ├── rescore.csv                  empty: consistency re-score not performed
│   └── example_questions.csv        six illustrative questions
├── rubric/scoring_rubric.md
├── prompts/
│   ├── prompt_template.md           test protocol
│   ├── prompts_to_paste.md          all 60 prompts, one per block
│   └── batches_to_paste.md          the same 60 in 6 batches of 10
├── analysis/
│   ├── build_questions.py           regenerates questions and prompts
│   ├── score.py                     rule-based scoring
│   ├── analyze.py                   tables and charts
│   ├── auto_grade.py                optional numeric check
│   ├── blind.py                     optional blind-scoring helper (not used in v1.0)
│   ├── results_tables.md            generated output
│   ├── results_summary.md           written summary
│   └── charts/
├── requirements.txt
├── LICENSE                          MIT (code)
└── DATA_LICENSE.md                  CC BY 4.0 (data and rubric)
```

## Reproduce the analysis

```bash
pip install -r requirements.txt
python analysis/score.py      # data/responses_raw.csv -> data/scores.csv
python analysis/analyze.py    # writes analysis/results_tables.md and charts
```

## Limitations

- **Small sample:** 60 questions, 3 models, one run each. A 3-question
  difference is not statistically meaningful.
- **Ceiling effect:** all three models scored 100% on the primary measure, so
  the questions are too easy to rank these models.
- **Loose tolerance:** the ±0.5% tolerance on valuation questions let small
  slips pass. The secondary exact-match measure was added after seeing results.
- **Rubric rules written after collection:** scoring rules were finalized after
  responses were collected. The method component is 2 for every response and
  does not separate the models; the assumptions component rewards stating an
  assumption even where none is needed.
- **Not blind:** the scorer knew each response's model.
- **Different settings across models:** DeepSeek and Gemini ran with thinking
  on; GPT-6 ran in Instant mode, which may still include some reasoning. The
  comparison is therefore not one-variable.
- **Batching:** questions were run 10 per chat, not one per chat.
- **Only final answer lines are published,** not the full responses.
- **Fictional data:** questions do not test retrieval from real filings.
- **Model versions change over time;** results reflect 20-21 November 2026.

## License

Code: MIT. Data and rubric: CC BY 4.0 (see `DATA_LICENSE.md`).
