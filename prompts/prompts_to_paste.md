# Prompts to paste

Generated from `data/questions_ground_truth.csv` by `analysis/build_questions.py`.
Paste each block into a FRESH chat for each model. See `prompt_template.md` for the protocol.

## Q001  (financial_statements, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Northvale Foods reports total assets of $1,850 million and total liabilities of $1,120 million. Calculate total shareholders' equity in $ millions. End with: Answer: <value>
```

## Q002  (financial_statements, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Brightline Software had revenue of $5,200 million and cost of goods sold of $3,380 million. Calculate gross profit in $ millions. End with: Answer: <value>
```

## Q003  (financial_statements, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Harbor Logistics began the year with retained earnings of $640 million, earned net income of $215 million, and paid dividends of $80 million. Calculate ending retained earnings in $ millions. End with: Answer: <value>
```

## Q004  (financial_statements, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Granite Manufacturing began the year with net PP&E of $900 million, spent $210 million on capital expenditures, and recorded depreciation of $150 million. There were no disposals. Calculate ending net PP&E in $ millions. End with: Answer: <value>
```

## Q005  (financial_statements, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Summit Retail reports revenue of $8,400 million, cost of goods sold of $5,040 million, SG&A of $1,260 million, depreciation and amortization of $420 million, and interest expense of $180 million. The tax rate is 25%. Calculate net income in $ millions. End with: Answer: <value>
```

## Q006  (financial_statements, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Pinecrest Energy reports net income of 7,842 (in thousands of U.S. dollars) and has 2,614,000 shares outstanding. Calculate earnings per share in U.S. dollars, to two decimal places. End with: Answer: <value>
```

## Q007  (financial_statements, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Alder Health reports cash of $320 million, accounts receivable of $480 million, inventory of $610 million, prepaid expenses of $40 million, accounts payable of $390 million, accrued liabilities of $210 million, and short-term debt of $150 million. All other balance sheet items are non-current. Calculate net working capital (current assets minus current liabilities) in $ millions. End with: Answer: <value>
```

## Q008  (financial_statements, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Meridian Apparel has a fiscal year ending March 31. Quarterly revenue in $ millions: FY2025 (April 2024 to March 2025): Q1 410, Q2 450, Q3 520, Q4 480. FY2026 (April 2025 to March 2026): Q1 430, Q2 470, Q3 540, Q4 500. Calculate revenue for calendar year 2025 (January to December 2025) in $ millions. End with: Answer: <value>
```

## Q009  (financial_statements, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Cobalt Cloud signs a 12-month contract on October 1 for $2,400 thousand, paid in full on that date, and recognizes revenue evenly over the 12 months starting October 1. Its fiscal year ends December 31. Calculate revenue recognized in that fiscal year from this contract, in $ thousands. End with: Answer: <value>
```

## Q010  (financial_statements, hard)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Redwood Supply began the period with 100 units at $10 each. It then purchased 200 units at $12 each, followed by 150 units at $14 each, and sold 300 units. Using the periodic LIFO method, calculate cost of goods sold in U.S. dollars. End with: Answer: <value>
```

## Q011  (financial_statements, hard)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Fernwood Industries began the year with cash of $230 million. During the year: net income $300 million; depreciation $80 million; accounts receivable increased by $45 million; inventory decreased by $20 million; accounts payable increased by $35 million; capital expenditures $150 million; dividends paid $60 million; new debt issued $100 million. Calculate ending cash in $ millions. End with: Answer: <value>
```

## Q012  (financial_statements, hard)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Quillon Aerospace buys equipment for $500 thousand with a salvage value of $50 thousand and a 5-year useful life. Using the double-declining-balance method, calculate depreciation expense for year 2 in $ thousands. End with: Answer: <value>
```

## Q013  (profitability, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Vantage Electronics reports revenue of $3,600 million, cost of goods sold of $2,160 million, and operating expenses of $540 million. Calculate the operating margin as a percentage, to one decimal place. End with: Answer: <value>
```

## Q014  (profitability, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Lumen Textiles reports net income of $180 million on revenue of $2,400 million. Calculate the net profit margin as a percentage, to one decimal place. End with: Answer: <value>
```

## Q015  (profitability, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Orchard Beverages reports revenue of $7,500 million and cost of goods sold of $4,950 million. Calculate the gross margin as a percentage, to one decimal place. End with: Answer: <value>
```

## Q016  (profitability, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Tidewater Shipping reports operating income of $640 million and depreciation and amortization of $210 million. Calculate EBITDA in $ millions. End with: Answer: <value>
```

## Q017  (profitability, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Crestline Insurance earned net income of $420 million. Shareholders' equity was $2,000 million at the start of the year and $2,200 million at the end. Calculate return on equity using average equity, as a percentage to one decimal place. End with: Answer: <value>
```

## Q018  (profitability, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Fairmont Foods earned net income of $156 million. Total assets were $1,200 million at the start of the year and $1,400 million at the end. Calculate return on assets using average total assets, as a percentage to one decimal place. End with: Answer: <value>
```

## Q019  (profitability, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company has a net profit margin of 8%, an asset turnover of 1.5x, and an equity multiplier of 2.0x. Using the DuPont formula, calculate return on equity as a percentage, to one decimal place. End with: Answer: <value>
```

## Q020  (profitability, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Silverton Media reports EBITDA of 96,500 (in thousands of U.S. dollars) and revenue of $482.5 million. Calculate the EBITDA margin as a percentage, to one decimal place. End with: Answer: <value>
```

## Q021  (profitability, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Kestrel Devices sells a product for $40 per unit. Variable cost is $24 per unit and fixed costs are $480,000 per year. Calculate the break-even sales volume in units. End with: Answer: <value>
```

## Q022  (profitability, hard)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Bayview Industrial reports EBIT of $1,200 million and a tax rate of 21%. Invested capital was $5,000 million at the start of the year and $5,400 million at the end. Calculate ROIC as NOPAT divided by average invested capital, as a percentage to one decimal place. End with: Answer: <value>
```

## Q023  (profitability, hard)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Atlas Holdings has two segments. Segment A has revenue of $900 million and operating income of $135 million. Segment B has revenue of $600 million and operating income of $48 million. Unallocated corporate costs of $30 million are not included in the segment results. Calculate the consolidated operating margin as a percentage, to one decimal place. End with: Answer: <value>
```

## Q024  (profitability, hard)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Marlow Tools sells 10,000 units at $50 each with a unit cost of $32. The price rises 5% and the volume falls 8%. Unit cost is unchanged. Calculate new total gross profit in U.S. dollars. End with: Answer: <value>
```

## Q025  (cash_flow, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Quarry Mining reports cash flow from operations of $540 million and capital expenditures of $180 million. Calculate free cash flow in $ millions. End with: Answer: <value>
```

## Q026  (cash_flow, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company has net income of $250 million and depreciation of $70 million, with no other adjustments or working capital changes. Calculate cash flow from operations in $ millions. End with: Answer: <value>
```

## Q027  (cash_flow, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company reports cash flow from operating activities of $400 million, from investing activities of -$260 million, and from financing activities of -$90 million. Calculate the net change in cash in $ millions. End with: Answer: <value>
```

## Q028  (cash_flow, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Net PP&E rose from $1,200 million to $1,350 million during the year. Depreciation was $160 million and there were no disposals. Calculate capital expenditures in $ millions. End with: Answer: <value>
```

## Q029  (cash_flow, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Dunmore Chemicals reports net income of $480 million and depreciation of $120 million. During the year accounts receivable increased by $60 million, inventory increased by $40 million, and accounts payable decreased by $25 million. Calculate cash flow from operations in $ millions. End with: Answer: <value>
```

## Q030  (cash_flow, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Ellison Packaging has cash flow from operations of $600 million, capital expenditures of $220 million, and net borrowing (debt issued minus debt repaid) of $80 million. Calculate free cash flow to equity in $ millions. End with: Answer: <value>
```

## Q031  (cash_flow, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company has days sales outstanding of 45, days inventory outstanding of 60, and days payables outstanding of 38. Calculate the cash conversion cycle in days. End with: Answer: <value>
```

## Q032  (cash_flow, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company has accounts receivable of $520 million and annual revenue of $4,380 million. Using a 365-day year and ending receivables, calculate days sales outstanding, to one decimal place. End with: Answer: <value>
```

## Q033  (cash_flow, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company reports cash flow from operations of $450 million on revenue of $3,000 million. Calculate the operating cash flow margin as a percentage, to one decimal place. End with: Answer: <value>
```

## Q034  (cash_flow, hard)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Garnet Systems has net income of $300 million, depreciation of $90 million, interest expense of $60 million, a tax rate of 25%, capital expenditures of $140 million, and an increase in net working capital of $35 million. Calculate free cash flow to the firm (FCFF = net income + depreciation + interest x (1 - tax rate) - capital expenditures - increase in net working capital) in $ millions. End with: Answer: <value>
```

## Q035  (cash_flow, hard)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Halcyon Retail has EBIT of $700 million, a tax rate of 30%, depreciation of $100 million, and capital expenditures of $160 million. Net working capital decreased by $50 million during the year. Calculate free cash flow to the firm in $ millions. End with: Answer: <value>
```

## Q036  (cash_flow, hard)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Ironbark Trading's balance sheet changed as follows between year-end dates: accounts receivable rose from $300 million to $360 million; inventory fell from $200 million to $180 million; accounts payable rose from $250 million to $290 million; accrued liabilities fell from $90 million to $80 million. Calculate the net cash flow effect of these working capital changes in $ millions. Use a negative number for a net cash outflow. End with: Answer: <value>
```

## Q037  (ratios, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company has current assets of $1,260 million and current liabilities of $700 million. Calculate the current ratio to two decimal places. End with: Answer: <value>
```

## Q038  (ratios, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company has total debt of $900 million and shareholders' equity of $1,500 million. Calculate the debt-to-equity ratio to two decimal places. End with: Answer: <value>
```

## Q039  (ratios, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company has EBIT of $840 million and interest expense of $120 million. Calculate the interest coverage ratio (times interest earned) to one decimal place. End with: Answer: <value>
```

## Q040  (ratios, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company has cash of $150 million, accounts receivable of $250 million, inventory of $400 million, and current liabilities of $500 million. Calculate the quick ratio (excluding inventory) to two decimal places. End with: Answer: <value>
```

## Q041  (ratios, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company has cost of goods sold of $6,300 million. Inventory was $700 million at the start of the year and $800 million at the end. Calculate inventory turnover using average inventory, to one decimal place. End with: Answer: <value>
```

## Q042  (ratios, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company has revenue of $9,000 million. Total assets were $4,200 million at the start of the year and $4,800 million at the end. Calculate total asset turnover using average total assets, to two decimal places. End with: Answer: <value>
```

## Q043  (ratios, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company has total debt of $2,400 million, cash of $600 million, and EBITDA of $900 million. Calculate the net debt to EBITDA ratio to two decimal places. End with: Answer: <value>
```

## Q044  (ratios, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company reports net income of $640 million and has 200 million shares outstanding. Its share price is $48. Calculate the price-to-earnings ratio to one decimal place. End with: Answer: <value>
```

## Q045  (ratios, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company has a return on equity of 15% and a dividend payout ratio of 30%. Calculate the sustainable growth rate (ROE x retention ratio) as a percentage, to one decimal place. End with: Answer: <value>
```

## Q046  (ratios, hard)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company has cost of goods sold of $5,475 million. Accounts payable was $420 million at the start of the year and $480 million at the end. Using average accounts payable and a 365-day year, calculate days payables outstanding, to one decimal place. End with: Answer: <value>
```

## Q047  (ratios, hard)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company has a tax burden (net income / pre-tax income) of 0.75, an interest burden (pre-tax income / EBIT) of 0.90, an EBIT margin of 20%, an asset turnover of 1.25, and an equity multiplier of 2.0. Using the five-step DuPont decomposition, calculate ROE as a percentage, to two decimal places. End with: Answer: <value>
```

## Q048  (ratios, hard)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company has a market capitalization of $5,400 million, total debt of $1,800 million, cash of $300 million, minority interest of $100 million, and EBITDA of $900 million. Calculate the EV/EBITDA multiple to two decimal places. End with: Answer: <value>
```

## Q049  (valuation, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Calculate the present value of $1,000 received in 3 years, discounted at 8% per year with annual compounding. Give the answer in U.S. dollars to two decimal places. End with: Answer: <value>
```

## Q050  (valuation, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
Calculate the future value of $5,000 invested for 5 years at 6% per year with annual compounding. Give the answer in U.S. dollars to two decimal places. End with: Answer: <value>
```

## Q051  (valuation, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A stock is expected to pay a dividend of $4.20 next year. Dividends are expected to grow at 3% per year forever and the required return is 9%. Using the Gordon growth model, calculate the stock's value per share in U.S. dollars. End with: Answer: <value>
```

## Q052  (valuation, easy)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
An asset pays $250 million per year forever, starting one year from now. The discount rate is 10%. Calculate its present value in $ millions. End with: Answer: <value>
```

## Q053  (valuation, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A project costs $2,000 million today and returns $700 million, $900 million and $1,100 million at the end of years 1, 2 and 3. Using a 12% discount rate, calculate the NPV in $ millions to one decimal place. End with: Answer: <value>
```

## Q054  (valuation, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company has equity of $750 million at a cost of 11% and debt of $250 million at a pre-tax cost of 5%. The tax rate is 20%. Calculate WACC as a percentage, to two decimal places. End with: Answer: <value>
```

## Q055  (valuation, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
The risk-free rate is 4%, the equity risk premium is 5.5%, and a stock's beta is 1.2. Using CAPM, calculate the cost of equity as a percentage, to one decimal place. End with: Answer: <value>
```

## Q056  (valuation, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company's free cash flow in year 5 is $150 million. Free cash flow grows at 2.5% per year after that, and WACC is 9%. Using the Gordon growth formula, calculate the terminal value at the end of year 5 in $ millions, to one decimal place. End with: Answer: <value>
```

## Q057  (valuation, medium)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
An investment of $1,000 returns a single payment of $1,210 exactly 2 years later. Calculate the internal rate of return as a percentage, to one decimal place. End with: Answer: <value>
```

## Q058  (valuation, hard)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company is expected to generate free cash flow of $100 million, $110 million and $120 million at the end of years 1, 2 and 3. After year 3, free cash flow grows at 3% per year forever. WACC is 10%. Calculate the enterprise value today in $ millions, to one decimal place. End with: Answer: <value>
```

## Q059  (valuation, hard)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A project costs $800 million today (t = 0). It returns $300 million, $350 million and $400 million in years 1, 2 and 3, received evenly through each year and treated as arriving at the middle of each year (t = 0.5, 1.5, 2.5). Using a 9% discount rate, calculate the NPV in $ millions to one decimal place. End with: Answer: <value>
```

## Q060  (valuation, hard)

```text
You are answering a financial calculation question. Use only the data given.
Show your calculation steps briefly, state any assumptions, and finish with
the final result on its own line in the format requested.

QUESTION:
A company has EBITDA of $250 million and is valued at 9.0x EBITDA. It has total debt of $700 million, cash of $150 million, minority interest of $50 million, and 110 million shares outstanding. Calculate the equity value per share in U.S. dollars, to two decimal places. End with: Answer: <value>
```
