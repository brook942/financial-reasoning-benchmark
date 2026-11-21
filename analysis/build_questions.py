"""Build the 60-question benchmark.

Every question uses FICTIONAL company data written for this benchmark, so each
has exactly one correct answer. Ground truth is computed from the `calc`
expression stored beside each question, and that expression is written to the
`calculation` column so anyone can re-verify it in Excel.

Outputs:
  data/questions_ground_truth.csv
  prompts/prompts_to_paste.md
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FS, PR, CF, RT, VL = ("financial_statements", "profitability", "cash_flow", "ratios", "valuation")
E, M, H = "easy", "medium", "hard"

# (category, difficulty, trap, prompt, calc, unit, decimals, tolerance, tol_type)
Q = [
 # ---------------- Financial statements ----------------
 (FS,E,"none","Northvale Foods reports total assets of $1,850 million and total liabilities of $1,120 million. Calculate total shareholders' equity in $ millions.","1850-1120","$M",0,0.5,"pct"),
 (FS,E,"none","Brightline Software had revenue of $5,200 million and cost of goods sold of $3,380 million. Calculate gross profit in $ millions.","5200-3380","$M",0,0.5,"pct"),
 (FS,E,"none","Harbor Logistics began the year with retained earnings of $640 million, earned net income of $215 million, and paid dividends of $80 million. Calculate ending retained earnings in $ millions.","640+215-80","$M",0,0.5,"pct"),
 (FS,E,"none","Granite Manufacturing began the year with net PP&E of $900 million, spent $210 million on capital expenditures, and recorded depreciation of $150 million. There were no disposals. Calculate ending net PP&E in $ millions.","900+210-150","$M",0,0.5,"pct"),
 (FS,M,"none","Summit Retail reports revenue of $8,400 million, cost of goods sold of $5,040 million, SG&A of $1,260 million, depreciation and amortization of $420 million, and interest expense of $180 million. The tax rate is 25%. Calculate net income in $ millions.","(8400-5040-1260-420-180)*(1-0.25)","$M",0,0.5,"pct"),
 (FS,M,"units_scale","Pinecrest Energy reports net income of 7,842 (in thousands of U.S. dollars) and has 2,614,000 shares outstanding. Calculate earnings per share in U.S. dollars, to two decimal places.","7842*1000/2614000","$",2,0.01,"abs"),
 (FS,M,"none","Alder Health reports cash of $320 million, accounts receivable of $480 million, inventory of $610 million, prepaid expenses of $40 million, accounts payable of $390 million, accrued liabilities of $210 million, and short-term debt of $150 million. All other balance sheet items are non-current. Calculate net working capital (current assets minus current liabilities) in $ millions.","(320+480+610+40)-(390+210+150)","$M",0,0.5,"pct"),
 (FS,M,"period_mixup","Meridian Apparel has a fiscal year ending March 31. Quarterly revenue in $ millions: FY2025 (April 2024 to March 2025): Q1 410, Q2 450, Q3 520, Q4 480. FY2026 (April 2025 to March 2026): Q1 430, Q2 470, Q3 540, Q4 500. Calculate revenue for calendar year 2025 (January to December 2025) in $ millions.","480+430+470+540","$M",0,0.5,"pct"),
 (FS,M,"none","Cobalt Cloud signs a 12-month contract on October 1 for $2,400 thousand, paid in full on that date, and recognizes revenue evenly over the 12 months starting October 1. Its fiscal year ends December 31. Calculate revenue recognized in that fiscal year from this contract, in $ thousands.","2400*3/12","$K",0,0.5,"pct"),
 (FS,H,"none","Redwood Supply began the period with 100 units at $10 each. It then purchased 200 units at $12 each, followed by 150 units at $14 each, and sold 300 units. Using the periodic LIFO method, calculate cost of goods sold in U.S. dollars.","150*14+150*12","$",0,0.5,"pct"),
 (FS,H,"sign_convention","Fernwood Industries began the year with cash of $230 million. During the year: net income $300 million; depreciation $80 million; accounts receivable increased by $45 million; inventory decreased by $20 million; accounts payable increased by $35 million; capital expenditures $150 million; dividends paid $60 million; new debt issued $100 million. Calculate ending cash in $ millions.","230+300+80-45+20+35-150-60+100","$M",0,0.5,"pct"),
 (FS,H,"none","Quillon Aerospace buys equipment for $500 thousand with a salvage value of $50 thousand and a 5-year useful life. Using the double-declining-balance method, calculate depreciation expense for year 2 in $ thousands.","(500-500*0.4)*0.4","$K",0,0.5,"pct"),
 # ---------------- Profitability ----------------
 (PR,E,"none","Vantage Electronics reports revenue of $3,600 million, cost of goods sold of $2,160 million, and operating expenses of $540 million. Calculate the operating margin as a percentage, to one decimal place.","(3600-2160-540)/3600*100","%",1,0.1,"abs"),
 (PR,E,"none","Lumen Textiles reports net income of $180 million on revenue of $2,400 million. Calculate the net profit margin as a percentage, to one decimal place.","180/2400*100","%",1,0.1,"abs"),
 (PR,E,"none","Orchard Beverages reports revenue of $7,500 million and cost of goods sold of $4,950 million. Calculate the gross margin as a percentage, to one decimal place.","(7500-4950)/7500*100","%",1,0.1,"abs"),
 (PR,E,"none","Tidewater Shipping reports operating income of $640 million and depreciation and amortization of $210 million. Calculate EBITDA in $ millions.","640+210","$M",0,0.5,"pct"),
 (PR,M,"none","Crestline Insurance earned net income of $420 million. Shareholders' equity was $2,000 million at the start of the year and $2,200 million at the end. Calculate return on equity using average equity, as a percentage to one decimal place.","420/((2000+2200)/2)*100","%",1,0.1,"abs"),
 (PR,M,"none","Fairmont Foods earned net income of $156 million. Total assets were $1,200 million at the start of the year and $1,400 million at the end. Calculate return on assets using average total assets, as a percentage to one decimal place.","156/((1200+1400)/2)*100","%",1,0.1,"abs"),
 (PR,M,"none","A company has a net profit margin of 8%, an asset turnover of 1.5x, and an equity multiplier of 2.0x. Using the DuPont formula, calculate return on equity as a percentage, to one decimal place.","8*1.5*2.0","%",1,0.1,"abs"),
 (PR,M,"units_scale","Silverton Media reports EBITDA of 96,500 (in thousands of U.S. dollars) and revenue of $482.5 million. Calculate the EBITDA margin as a percentage, to one decimal place.","96.5/482.5*100","%",1,0.1,"abs"),
 (PR,M,"none","Kestrel Devices sells a product for $40 per unit. Variable cost is $24 per unit and fixed costs are $480,000 per year. Calculate the break-even sales volume in units.","480000/(40-24)","units",0,0.5,"pct"),
 (PR,H,"none","Bayview Industrial reports EBIT of $1,200 million and a tax rate of 21%. Invested capital was $5,000 million at the start of the year and $5,400 million at the end. Calculate ROIC as NOPAT divided by average invested capital, as a percentage to one decimal place.","1200*(1-0.21)/((5000+5400)/2)*100","%",1,0.1,"abs"),
 (PR,H,"unallocated_costs","Atlas Holdings has two segments. Segment A has revenue of $900 million and operating income of $135 million. Segment B has revenue of $600 million and operating income of $48 million. Unallocated corporate costs of $30 million are not included in the segment results. Calculate the consolidated operating margin as a percentage, to one decimal place.","(135+48-30)/(900+600)*100","%",1,0.1,"abs"),
 (PR,H,"none","Marlow Tools sells 10,000 units at $50 each with a unit cost of $32. The price rises 5% and the volume falls 8%. Unit cost is unchanged. Calculate new total gross profit in U.S. dollars.","(50*1.05-32)*(10000*0.92)","$",0,0.5,"pct"),
 # ---------------- Cash flow ----------------
 (CF,E,"none","Quarry Mining reports cash flow from operations of $540 million and capital expenditures of $180 million. Calculate free cash flow in $ millions.","540-180","$M",0,0.5,"pct"),
 (CF,E,"none","A company has net income of $250 million and depreciation of $70 million, with no other adjustments or working capital changes. Calculate cash flow from operations in $ millions.","250+70","$M",0,0.5,"pct"),
 (CF,E,"none","A company reports cash flow from operating activities of $400 million, from investing activities of -$260 million, and from financing activities of -$90 million. Calculate the net change in cash in $ millions.","400-260-90","$M",0,0.5,"pct"),
 (CF,E,"none","Net PP&E rose from $1,200 million to $1,350 million during the year. Depreciation was $160 million and there were no disposals. Calculate capital expenditures in $ millions.","1350-1200+160","$M",0,0.5,"pct"),
 (CF,M,"none","Dunmore Chemicals reports net income of $480 million and depreciation of $120 million. During the year accounts receivable increased by $60 million, inventory increased by $40 million, and accounts payable decreased by $25 million. Calculate cash flow from operations in $ millions.","480+120-60-40-25","$M",0,0.5,"pct"),
 (CF,M,"none","Ellison Packaging has cash flow from operations of $600 million, capital expenditures of $220 million, and net borrowing (debt issued minus debt repaid) of $80 million. Calculate free cash flow to equity in $ millions.","600-220+80","$M",0,0.5,"pct"),
 (CF,M,"none","A company has days sales outstanding of 45, days inventory outstanding of 60, and days payables outstanding of 38. Calculate the cash conversion cycle in days.","45+60-38","days",0,0.5,"abs"),
 (CF,M,"none","A company has accounts receivable of $520 million and annual revenue of $4,380 million. Using a 365-day year and ending receivables, calculate days sales outstanding, to one decimal place.","520/4380*365","days",1,0.1,"abs"),
 (CF,M,"none","A company reports cash flow from operations of $450 million on revenue of $3,000 million. Calculate the operating cash flow margin as a percentage, to one decimal place.","450/3000*100","%",1,0.1,"abs"),
 (CF,H,"none","Garnet Systems has net income of $300 million, depreciation of $90 million, interest expense of $60 million, a tax rate of 25%, capital expenditures of $140 million, and an increase in net working capital of $35 million. Calculate free cash flow to the firm (FCFF = net income + depreciation + interest x (1 - tax rate) - capital expenditures - increase in net working capital) in $ millions.","300+90+60*(1-0.25)-140-35","$M",0,0.5,"pct"),
 (CF,H,"sign_convention","Halcyon Retail has EBIT of $700 million, a tax rate of 30%, depreciation of $100 million, and capital expenditures of $160 million. Net working capital decreased by $50 million during the year. Calculate free cash flow to the firm in $ millions.","700*(1-0.3)+100-160+50","$M",0,0.5,"pct"),
 (CF,H,"sign_convention","Ironbark Trading's balance sheet changed as follows between year-end dates: accounts receivable rose from $300 million to $360 million; inventory fell from $200 million to $180 million; accounts payable rose from $250 million to $290 million; accrued liabilities fell from $90 million to $80 million. Calculate the net cash flow effect of these working capital changes in $ millions. Use a negative number for a net cash outflow.","-60+20+40-10","$M",0,0.5,"abs"),
 # ---------------- Ratios ----------------
 (RT,E,"none","A company has current assets of $1,260 million and current liabilities of $700 million. Calculate the current ratio to two decimal places.","1260/700","x",2,0.01,"abs"),
 (RT,E,"none","A company has total debt of $900 million and shareholders' equity of $1,500 million. Calculate the debt-to-equity ratio to two decimal places.","900/1500","x",2,0.01,"abs"),
 (RT,E,"none","A company has EBIT of $840 million and interest expense of $120 million. Calculate the interest coverage ratio (times interest earned) to one decimal place.","840/120","x",1,0.1,"abs"),
 (RT,E,"none","A company has cash of $150 million, accounts receivable of $250 million, inventory of $400 million, and current liabilities of $500 million. Calculate the quick ratio (excluding inventory) to two decimal places.","(150+250)/500","x",2,0.01,"abs"),
 (RT,M,"none","A company has cost of goods sold of $6,300 million. Inventory was $700 million at the start of the year and $800 million at the end. Calculate inventory turnover using average inventory, to one decimal place.","6300/((700+800)/2)","x",1,0.1,"abs"),
 (RT,M,"none","A company has revenue of $9,000 million. Total assets were $4,200 million at the start of the year and $4,800 million at the end. Calculate total asset turnover using average total assets, to two decimal places.","9000/((4200+4800)/2)","x",2,0.01,"abs"),
 (RT,M,"net_vs_gross_debt","A company has total debt of $2,400 million, cash of $600 million, and EBITDA of $900 million. Calculate the net debt to EBITDA ratio to two decimal places.","(2400-600)/900","x",2,0.01,"abs"),
 (RT,M,"none","A company reports net income of $640 million and has 200 million shares outstanding. Its share price is $48. Calculate the price-to-earnings ratio to one decimal place.","48/(640/200)","x",1,0.1,"abs"),
 (RT,M,"none","A company has a return on equity of 15% and a dividend payout ratio of 30%. Calculate the sustainable growth rate (ROE x retention ratio) as a percentage, to one decimal place.","15*(1-0.30)","%",1,0.1,"abs"),
 (RT,H,"none","A company has cost of goods sold of $5,475 million. Accounts payable was $420 million at the start of the year and $480 million at the end. Using average accounts payable and a 365-day year, calculate days payables outstanding, to one decimal place.","((420+480)/2)/5475*365","days",1,0.1,"abs"),
 (RT,H,"none","A company has a tax burden (net income / pre-tax income) of 0.75, an interest burden (pre-tax income / EBIT) of 0.90, an EBIT margin of 20%, an asset turnover of 1.25, and an equity multiplier of 2.0. Using the five-step DuPont decomposition, calculate ROE as a percentage, to two decimal places.","0.75*0.90*20*1.25*2.0","%",2,0.05,"abs"),
 (RT,H,"net_vs_gross_debt","A company has a market capitalization of $5,400 million, total debt of $1,800 million, cash of $300 million, minority interest of $100 million, and EBITDA of $900 million. Calculate the EV/EBITDA multiple to two decimal places.","(5400+1800-300+100)/900","x",2,0.01,"abs"),
 # ---------------- Valuation ----------------
 (VL,E,"none","Calculate the present value of $1,000 received in 3 years, discounted at 8% per year with annual compounding. Give the answer in U.S. dollars to two decimal places.","1000/1.08**3","$",2,0.5,"pct"),
 (VL,E,"none","Calculate the future value of $5,000 invested for 5 years at 6% per year with annual compounding. Give the answer in U.S. dollars to two decimal places.","5000*1.06**5","$",2,0.5,"pct"),
 (VL,E,"none","A stock is expected to pay a dividend of $4.20 next year. Dividends are expected to grow at 3% per year forever and the required return is 9%. Using the Gordon growth model, calculate the stock's value per share in U.S. dollars.","4.20/(0.09-0.03)","$",2,0.5,"pct"),
 (VL,E,"none","An asset pays $250 million per year forever, starting one year from now. The discount rate is 10%. Calculate its present value in $ millions.","250/0.10","$M",0,0.5,"pct"),
 (VL,M,"none","A project costs $2,000 million today and returns $700 million, $900 million and $1,100 million at the end of years 1, 2 and 3. Using a 12% discount rate, calculate the NPV in $ millions to one decimal place.","-2000+700/1.12+900/1.12**2+1100/1.12**3","$M",1,0.5,"pct"),
 (VL,M,"none","A company has equity of $750 million at a cost of 11% and debt of $250 million at a pre-tax cost of 5%. The tax rate is 20%. Calculate WACC as a percentage, to two decimal places.","0.75*11+0.25*5*(1-0.2)","%",2,0.05,"abs"),
 (VL,M,"none","The risk-free rate is 4%, the equity risk premium is 5.5%, and a stock's beta is 1.2. Using CAPM, calculate the cost of equity as a percentage, to one decimal place.","4+1.2*5.5","%",1,0.1,"abs"),
 (VL,M,"none","A company's free cash flow in year 5 is $150 million. Free cash flow grows at 2.5% per year after that, and WACC is 9%. Using the Gordon growth formula, calculate the terminal value at the end of year 5 in $ millions, to one decimal place.","150*1.025/(0.09-0.025)","$M",1,0.5,"pct"),
 (VL,M,"none","An investment of $1,000 returns a single payment of $1,210 exactly 2 years later. Calculate the internal rate of return as a percentage, to one decimal place.","((1210/1000)**0.5-1)*100","%",1,0.1,"abs"),
 (VL,H,"none","A company is expected to generate free cash flow of $100 million, $110 million and $120 million at the end of years 1, 2 and 3. After year 3, free cash flow grows at 3% per year forever. WACC is 10%. Calculate the enterprise value today in $ millions, to one decimal place.","100/1.1+110/1.1**2+120/1.1**3+(120*1.03/(0.10-0.03))/1.1**3","$M",1,0.5,"pct"),
 (VL,H,"mid_year_discounting","A project costs $800 million today (t = 0). It returns $300 million, $350 million and $400 million in years 1, 2 and 3, received evenly through each year and treated as arriving at the middle of each year (t = 0.5, 1.5, 2.5). Using a 9% discount rate, calculate the NPV in $ millions to one decimal place.","-800+300/1.09**0.5+350/1.09**1.5+400/1.09**2.5","$M",1,0.5,"pct"),
 (VL,H,"net_vs_gross_debt","A company has EBITDA of $250 million and is valued at 9.0x EBITDA. It has total debt of $700 million, cash of $150 million, minority interest of $50 million, and 110 million shares outstanding. Calculate the equity value per share in U.S. dollars, to two decimal places.","(250*9-700+150-50)/110","$",2,0.5,"pct"),
]

COLUMNS = ["q_id","category","difficulty","trap_type","prompt","source","truth_value","unit",
           "tolerance","tolerance_type","calculation","decimals"]


def main():
    assert len(Q) == 60, f"expected 60 questions, got {len(Q)}"
    rows = []
    for i, (cat, diff, trap, prompt, calc, unit, dec, tol, tt) in enumerate(Q, start=1):
        truth = round(eval(calc, {"__builtins__": {}}, {}), dec)
        truth = int(truth) if dec == 0 else truth
        full_prompt = prompt + " End with: Answer: <value>"
        rows.append({
            "q_id": f"Q{i:03d}", "category": cat, "difficulty": diff, "trap_type": trap,
            "prompt": full_prompt, "source": "Fictional company data written for this benchmark",
            "truth_value": truth, "unit": unit, "tolerance": tol, "tolerance_type": tt,
            "calculation": calc, "decimals": dec,
        })
    data_dir = ROOT / "data"
    with open(data_dir / "questions_ground_truth.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)

    template = ("You are answering a financial calculation question. Use only the data given.\n"
                "Show your calculation steps briefly, state any assumptions, and finish with\n"
                "the final result on its own line in the format requested.\n\nQUESTION:\n")
    out = ["# Prompts to paste\n",
           "Generated from `data/questions_ground_truth.csv` by `analysis/build_questions.py`.",
           "Paste each block into a FRESH chat for each model. See `prompt_template.md` for the protocol.\n"]
    for r in rows:
        out.append(f"## {r['q_id']}  ({r['category']}, {r['difficulty']})\n")
        out.append("```text\n" + template + r["prompt"] + "\n```\n")
    (ROOT / "prompts" / "prompts_to_paste.md").write_text("\n".join(out), encoding="utf-8")

    header = ("Answer each question separately. For each, show your calculation steps briefly, "
              "state any assumptions, and finish with a line in the format 'Answer: <value>'. "
              "Label each answer with its question number. Use only the data given.")
    b = ["# Batches to paste (10 questions per batch)\n",
         "Use a NEW chat for each batch. Do the same for every model. Turn off web search and code tools if the app has a switch.",
         "Copy everything inside one box, paste it, and save the full reply under the batch number and model name.\n"]
    for n in range(6):
        chunk = rows[n * 10:(n + 1) * 10]
        b.append(f"## Batch {n + 1} (Q{n * 10 + 1:03d} to Q{n * 10 + 10:03d})\n")
        body = header + "\n\n" + "\n\n".join(f"{r['q_id']}. {r['prompt']}" for r in chunk)
        b.append("```text\n" + body + "\n```\n")
    (ROOT / "prompts" / "batches_to_paste.md").write_text("\n".join(b), encoding="utf-8")
    print(f"Wrote {len(rows)} questions and prompts_to_paste.md")


if __name__ == "__main__":
    main()
