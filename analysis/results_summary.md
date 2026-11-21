# Results Summary

Generated tables: [`results_tables.md`](results_tables.md). Numbers below are
copied from those tables.

**Overall.** DeepSeek V4.1, Gemini 4 Hydrogen, and GPT-6 each answered all 60
questions within tolerance (100%). At the requested decimal place, DeepSeek and
Gemini matched the key on 60 of 60, and GPT-6 on 57 of 60 (95.0%).

**By category.** Every category scored 100% on the primary measure. On exact
match, valuation was the only category below 100% (91.7% across models; GPT-6
alone scored 75.0% there, 9 of 12).

**By difficulty and trap type.** All easy questions matched exactly. Hard
questions scored 95.6% and medium questions 98.7% on exact match, and all of
the misses were GPT-6 valuation answers. The mid-year discounting question
(Q059) was the only trap question with a miss (2 of 3 model answers matched
exactly). Units, fiscal-period, sign-convention, net-debt, and unallocated-cost
traps were all handled correctly by all three models.

**Errors.** The three GPT-6 misses (Q053, Q058, Q059) were arithmetic slips
inside the discounting steps. The formulas and inputs were correct.

**Invented figures.** None for any model.

**Assumptions and units.** Explicit assumption statements: Gemini 98.3%,
DeepSeek 31.7%, GPT-6 30.0%. Units labeled on the answer line: GPT-6 100%,
Gemini 83.3%, DeepSeek 53.3%. These are style differences under the rubric.

**Scoring consistency.** Not measured in v1.0.
