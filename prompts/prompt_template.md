# Prompt Protocol (v1.0)

Every model receives the same prompt text for a given question.

## Rules

- One question per fresh chat. No prior context.
- Web search, code execution and file tools: OFF.
- One attempt per question per model. No regenerating.
- Record the model name, version label and date in `responses_raw.csv`.
- Do not edit the prompt for any individual model.

## Template

```
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
{prompt}
```

## Extracting the answer

Copy the value after "Answer:" into `extracted_answer`. If the model gives no
"Answer:" line, record what it presented as its final number, or leave blank
and mark `no_answer` when scoring.
