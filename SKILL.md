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
4. Build a year-by-year source map before analysis whenever the user asks about multiple years, a year range, or phrases such as "from 2024 to 2025", "over the last two years", or similar. For each requested year, identify the official financial documents that actually cover that year.
5. Build a period map before analysis. State clearly whether each exhibit uses full-year, half-year, quarter, trailing-twelve-month, or point-in-time balance-sheet data.
6. Distinguish carefully between (a) financial data for a period, (b) documents disclosed in a later calendar year, and (c) outlook, guidance, financing plans, or management commentary. Do not treat a disclosure date in a later year as financial data for that later year.
7. If the later requested year does not yet have a full-year report, default to the latest official in-period financial report for that year, such as an interim report, quarterly report, or operating update, rather than substituting outlook language or a prior-year annual results announcement released in that later year.
8. Before drafting conclusions, verify that each requested year is represented by real financial data. If coverage is incomplete, state the gap explicitly and narrow the claim accordingly.
9. Before finalizing any table, chart, KPI card, exhibit, or period-labelled summary, validate every numeric value against its cited source and reporting period. Do not relabel prior-period figures as current-period figures, and do not infer reporting periods from file dates or disclosure dates alone.
10. If period-accurate figures for a requested table or chart are unavailable, incomplete, or extraction is uncertain, do not backfill the exhibit with another period’s numbers. State the gap explicitly, omit the exhibit, or downgrade it to a qualified text explanation.
11. Build a segment map before charting. If company disclosures use parent buckets, sub-segments, overlapping labels, or changed classifications, explain the hierarchy first and avoid presenting them as directly parallel categories.
12. Search for key metrics by theme:
   - revenue and segment mix
   - EBITDA / EBIT / profit drivers
   - gross debt / net debt / gearing / net debt-to-equity
   - cash balances / undrawn facilities
   - borrowing cost / interest cover
   - financing instruments such as bonds, MTNs, perpetual capital securities, green finance
13. Compare only like-for-like periods and like-for-like metrics unless the purpose is explicitly explanatory rather than comparative.
14. Enforce chart discipline. Do not place non-comparable metrics in the same chart, ranking frame, or apparent winner-loser comparison and then rank, judge, or declare one segment superior. If non-comparable metrics must appear together for explanatory context, label the limitation explicitly.
15. When margins, profit, or leverage change, trace the driver from the filings. Distinguish among revenue mix, operating cost, staff cost, depreciation and amortization, concession or lease-style payments, financing cost, equity increase, hybrid/perpetual instruments, and accounting reclassification.
16. When leverage appears to improve, verify whether the change came from actual debt repayment, cash accumulation, equity issuance, perpetual or hybrid capital instruments, or presentation effects. Explain the accounting treatment and economic substance when they differ.
17. Define technical metrics in plain language on first use, especially for non-specialist readers. Explain not only what the metric means, but why it is relevant to the conclusion.
18. When the user asks about operating-model differences, company distinctiveness, competitive positioning, or relative strengths and weaknesses, consider peer comparison by default if time and source availability permit.
19. Build conclusions from evidence, not from unstated assumptions.
20. Output a single-file HTML report when HTML is requested, with:
   - executive summary
   - sectioned analysis
   - evidence blocks
   - references
   - inline charts when requested

## Read these references when relevant

- Read `references/asset-heavy-companies.md` when the company is transport, infrastructure, utilities, telecom, property-linked, or otherwise asset-heavy, or when EBITDA and EBIT may tell materially different stories.
- Read `references/driver-analysis.md` when the task requires explaining why revenue, margin, leverage, or segment mix changed rather than merely describing the change.
- Read `references/cases/mtr-0066-notes.md` when the company is MTR / 港鐵 / 0066, or when a rail-plus-property model, station commercial monetisation, or hybrid-capital-driven leverage optics look similar.

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
- `references/zh-report-checklist.md` — Traditional Chinese pre-delivery checklist for report quality control

## Notes

- Prefer official primary sources over third-party summaries.
- If search APIs are unavailable, navigate from the company IR hub manually.
- For charted HTML, prefer inline SVG or self-contained HTML with no external JS dependency.
- For heavy-asset, infrastructure, transport, utility, telecom, or property-linked companies, check whether EBITDA and EBIT tell materially different stories before concluding which segment is more profitable or more cash generative.
- Treat perpetual capital securities and other hybrid instruments carefully. A filing may classify them as equity while readers still need an explanation of their financing role and why leverage ratios may look better without equivalent economic deleveraging.
