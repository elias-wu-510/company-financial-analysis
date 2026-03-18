---
name: company-financial-analysis
description: Analyze listed companies using official investor-relations materials such as annual reports, interim reports, results announcements, and financial-report PDFs. Use when the user asks for company financial analysis, operating-model analysis, segment revenue breakdown, leverage/debt review, financing structure, or a cited HTML report with evidence chain and charts.
---

# company-financial-analysis

Analyze a listed company from official filings and produce a cited HTML report.

## Workflow

1. Prefer official investor-relations pages, annual/interim reports, and official results announcements.
2. Download the official PDFs when possible.
3. Extract text from PDFs.
4. Search for key metrics by theme:
   - revenue and segment mix
   - EBITDA / EBIT / profit drivers
   - gross debt / net debt / gearing / net debt-to-equity
   - cash balances / undrawn facilities
   - borrowing cost / interest cover
   - financing instruments such as bonds, MTNs, perpetual capital securities, green finance
5. Build conclusions from evidence, not from unstated assumptions.
6. Output a single-file HTML report with:
   - executive summary
   - sectioned analysis
   - evidence blocks
   - references
   - inline charts when requested

## Bundled resources

- `scripts/extract_pdf_text.py` — extract PDF text for local analysis
- `assets/report_template.html` — starter HTML template
- `references/metric-keywords.md` — reusable keyword patterns for IR documents

## Notes

- Prefer official primary sources over third-party summaries.
- If search APIs are unavailable, navigate from the company IR hub manually.
- For charted HTML, prefer inline SVG or self-contained HTML with no external JS dependency.
