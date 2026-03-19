---
name: company-financial-analysis
description: Analyze listed companies using official investor-relations materials such as annual reports, interim reports, results announcements, and financial-report PDFs. Use when the user asks for company financial analysis, operating-model analysis, segment revenue breakdown, leverage/debt review, financing structure, or a cited HTML report with evidence chain and charts. Default output language is Traditional Chinese unless the user explicitly requests English or a bilingual deliverable.
---

# company-financial-analysis

Analyze a listed company from official filings and produce a cited report grounded in primary sources.

## Workflow

1. Prefer official investor-relations pages, annual/interim reports, and official results announcements.
2. Download the official PDFs when possible.
3. Extract text from PDFs.
4. Build a period map before analysis. State clearly whether each exhibit uses full-year, half-year, quarter, trailing-twelve-month, or point-in-time balance-sheet data.
5. Build a segment map before charting. If company disclosures use parent buckets, sub-segments, overlapping labels, or changed classifications, explain the hierarchy first and avoid presenting them as directly parallel categories.
6. Search for key metrics by theme:
   - revenue and segment mix
   - EBITDA / EBIT / profit drivers
   - gross debt / net debt / gearing / net debt-to-equity
   - cash balances / undrawn facilities
   - borrowing cost / interest cover
   - financing instruments such as bonds, MTNs, perpetual capital securities, green finance
7. Compare only like-for-like periods and like-for-like metrics unless the purpose is explicitly explanatory rather than comparative.
8. When margins, profit, or leverage change, trace the driver from the filings. Distinguish among revenue mix, operating cost, staff cost, depreciation and amortization, concession or lease-style payments, financing cost, equity increase, hybrid/perpetual instruments, and accounting reclassification.
9. When leverage appears to improve, verify whether the change came from actual debt repayment, cash accumulation, equity issuance, perpetual or hybrid capital instruments, or presentation effects. Explain the accounting treatment and economic substance when they differ.
10. Define technical metrics in plain language on first use, especially for non-specialist readers. Explain not only what the metric means, but why it is relevant to the conclusion.
11. Build conclusions from evidence, not from unstated assumptions.
12. Output a single-file HTML report when HTML is requested, with:
   - executive summary
   - sectioned analysis
   - evidence blocks
   - references
   - inline charts when requested

## Output discipline

- Default to Traditional Chinese for the full deliverable unless the user explicitly requests English or a bilingual deliverable.
- Keep the report in one language. Do not mix Simplified Chinese, Traditional Chinese, and English narrative in the same deliverable.
- If source terminology is commonly cited in English, keep the English term in brackets on first use after the Traditional Chinese explanation.
- Write for a reader who does not already know the company, industry, or metric set.
- Do not place non-comparable metrics on the same chart or in the same ranking frame without an explicit warning that they are not directly comparable.
- If the user asks about operating model, explain the business logic linking segments rather than only listing segment numbers.
- If possible, add peer comparison when the goal is to explain how the company differs from its industry rather than merely describing its own trend.

## Bundled resources

- `scripts/extract_pdf_text.py` — extract PDF text for local analysis
- `assets/report_template.html` — starter HTML template
- `references/metric-keywords.md` — reusable keyword patterns for IR documents

## Notes

- Prefer official primary sources over third-party summaries.
- If search APIs are unavailable, navigate from the company IR hub manually.
- For charted HTML, prefer inline SVG or self-contained HTML with no external JS dependency.
- For heavy-asset, infrastructure, transport, utility, telecom, or property-linked companies, check whether EBITDA and EBIT tell materially different stories before concluding which segment is more profitable or more cash generative.
- Treat perpetual capital securities and other hybrid instruments carefully. A filing may classify them as equity while readers still need an explanation of their financing role and why leverage ratios may look better without equivalent economic deleveraging.
