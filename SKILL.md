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
4. For company-analysis tasks, proactively search the company’s most recent three months of news, announcements, press releases, investor updates, and external operating developments as a mandatory retrieval layer, not an optional extra.
5. Treat those news, announcements, press releases, and external operating updates as a default retrieval layer whenever they may help explain revenue change, major projects, recovery, industry position, or future potential. Search them proactively, then decide whether they belong in the report based on evidence strength and period fit.
6. Build a year-by-year source map before analysis whenever the user asks about multiple years, a year range, or phrases such as "from 2024 to 2025", "over the last two years", or similar. For each requested year, identify the official financial documents that actually cover that year.
7. Build a period map before analysis. State clearly whether each exhibit uses full-year, half-year, quarter, trailing-twelve-month, or point-in-time balance-sheet data.
8. Distinguish carefully between (a) financial data for a period, (b) documents disclosed in a later calendar year, and (c) outlook, guidance, financing plans, or management commentary. Do not treat a disclosure date in a later year as financial data for that later year.
9. When the latest full-year annual report has not yet been released, default to using the latest official disclosed financial statements—such as an interim report, results announcement, press release with financial tables, or official investor presentation with clearly reported figures—as the primary basis for current analysis.
10. In that situation, use the prior full-year annual report as baseline and structural background, not as a substitute for the latest financial period.
11. Treat comparative figures printed inside the current-year annual report, interim report, results announcement, presentation, or financial statements as official usable data for the prior period when the company itself presents them. Do not mark a prior-period KPI as "not disclosed" merely because the working note focused on the current year.
12. For every key KPI requested or likely to appear in a dashboard—such as revenue, attributable net profit, EPS, DPS, cash, debt, equity, CFO, and capex—check explicitly whether the source document shows both current-period and comparative-period columns. If the comparative column exists, capture it together with the current-period value.
13. Before drafting conclusions, verify that each requested year or period is represented by real financial data. If coverage is incomplete, state the gap explicitly and narrow the claim accordingly.
14. Before finalizing any table, chart, KPI card, exhibit, or period-labelled summary, validate every numeric value against its cited source and reporting period. Do not relabel prior-period figures as current-period figures, and do not infer reporting periods from file dates or disclosure dates alone.
15. If period-accurate figures for a requested table or chart are unavailable, incomplete, or extraction is uncertain, do not backfill the exhibit with another period’s numbers. State the gap explicitly, omit the exhibit, or downgrade it to a qualified text explanation.
16. Before writing "not disclosed", "not shown", "not included", or similar wording for a prior-period number, check at least the current-period results announcement and the current-period annual report or financial statements for comparative columns. Only use missing-data wording after those checks fail.
17. Build a segment map before charting. If company disclosures use parent buckets, sub-segments, overlapping labels, or changed classifications, explain the hierarchy first and avoid presenting them as directly parallel categories.
15. Search for key metrics by theme:
   - revenue and segment mix
   - EBITDA / EBIT / profit drivers
   - gross debt / net debt / gearing / net debt-to-equity
   - cash balances / undrawn facilities
   - borrowing cost / interest cover
   - financing instruments such as bonds, MTNs, perpetual capital securities, green finance
16. Compare only like-for-like periods and like-for-like metrics unless the purpose is explicitly explanatory rather than comparative.
17. Enforce chart discipline. Do not place non-comparable metrics in the same chart, ranking frame, or apparent winner-loser comparison and then rank, judge, or declare one segment superior. If non-comparable metrics must appear together for explanatory context, label the limitation explicitly.
18. Make charts presentation-ready. Avoid label overlap, clipped annotations, inconsistent bar or line styling, patch-like visual artifacts, or other UI issues that make the exhibit look unfinished or misleading.
19. When margins, profit, or leverage change, trace the driver from the filings. Distinguish among revenue mix, operating cost, staff cost, depreciation and amortization, concession or lease-style payments, financing cost, equity increase, hybrid/perpetual instruments, and accounting reclassification.
20. When leverage appears to improve, verify whether the change came from actual debt repayment, cash accumulation, equity issuance, perpetual or hybrid capital instruments, or presentation effects. Explain the accounting treatment and economic substance when they differ.
21. Define technical metrics in plain language on first use, especially for non-specialist readers. Explain not only what the metric means, but why it is relevant to the conclusion.
22. When the user asks about operating-model differences, company distinctiveness, competitive positioning, or relative strengths and weaknesses, consider peer comparison by default if time and source availability permit.
23. When peer comparison or industry positioning requires substantial multi-company research, delegate the peer-research layer to a subagent and have it return a short peer note; keep the main agent focused on the target company report and final integration.
24. Build conclusions from evidence, not from unstated assumptions.
25. Decide the delivery level before drafting: Level 1 (baseline deliverable), Level 2 (enhanced), or Level 3 (deep research). Default to Level 1 unless the user explicitly asks for more depth or the time/source budget clearly supports it.
26. If the deliverable includes a financial overview, KPI panel, or metrics dashboard, validate it against `references/financial-dashboard-minimum.md`. If the panel is incomplete, state the gap explicitly rather than silently presenting it as a full dashboard.
27. If the deliverable is a Traditional Chinese client-facing report, run one final pass against `references/final-cn-delivery-checklist.md` so the output reads like a finished Chinese report rather than a half-localized analysis draft.
28. Output a single-file HTML report when HTML is requested, with:
   - executive summary
   - sectioned analysis
   - evidence blocks
   - references
   - inline charts when requested
29. Before sending any client-delivery HTML that contains charts, run `scripts/chart_sanity_scan.py` on the final HTML, review warnings, and fix or simplify any misleading chart before export or delivery.

## Read these references when relevant

- Read `references/asset-heavy-companies.md` when the company is transport, infrastructure, utilities, telecom, property-linked, or otherwise asset-heavy, or when EBITDA and EBIT may tell materially different stories.
- Read `references/driver-analysis.md` when the task requires explaining why revenue, margin, leverage, or segment mix changed rather than merely describing the change.
- Read `references/plain-language-metrics.md` when the report should work for non-specialist readers and key metrics need clear plain-language explanation.
- Read `references/reviewer-sensitive-checklist.md` when the likely reviewer is detail-oriented, the user asks for a more defensible draft, or prior feedback criticised comparability, evidence discipline, wording precision, or formatting consistency.
- Read `references/external-retrieval-strategy.md` when the task needs broader source coverage, official IR discovery, results announcements, HKEX disclosures, or peer-company source discovery.
- Read `references/hkex-ir-retrieval.md` when the company is Hong Kong-listed and the task needs a repeatable Brave + IR + HKEX retrieval workflow.
- Read `references/peer-comparison.md` when the task asks how the target company differs from peers, or when peer comparison would materially improve the operating-model explanation.
- Read `references/html-report-structure.md` when the user asks for a direct-delivery HTML report rather than notes or rough analysis.
- Read `references/delivery-loop.md` when the task is a deliverable report and the workflow should include self-check → revise → self-check → revise → deliver.
- Read `references/internal-to-client-delivery.md` when the task should first produce an internal checked version and then a clean customer-facing delivery version.
- Read `references/v2-to-v3-acceptance-checklist.md` when validating whether a revised report really addresses reviewer feedback from an earlier draft.
- Read `references/delivery-levels.md` when the task boundary is ambiguous, when deciding whether to stop at a baseline deliverable or push into an enhanced/deep-research version, or when a reviewer is likely to judge a Level 1 draft by Level 2 or Level 3 standards.
- Read `references/financial-dashboard-minimum.md` when the deliverable includes a financial overview, KPI panel, detailed metrics page, or reviewer-sensitive dashboard completeness check.
- Read `references/final-cn-delivery-checklist.md` before delivering a Traditional Chinese client-facing report that must feel like a finished final draft rather than an analysis memo.
- Read `references/annual-report-openclaw-design-checklist.md` when the report should emphasize change, trend, peer comparison, and future positioning rather than a static description of current numbers.
- Read `references/report-style-light-theme.md` when producing or revising deliverable HTML so the default visual style remains light, reading-friendly, and PDF-friendly.
- Read `references/news-driver-validation.md` when using news or public reports to explain revenue change, major projects, operating recovery, or strategic shifts.
- Read `references/source-period-map.md` when the task spans multiple years, mixed period types, or documents disclosed in a later calendar year.
- Read `references/zh-report-checklist.md` before delivering a Traditional Chinese report.
- Read `references/chart-ui-quality.md` when the deliverable includes charts.
- Read `references/chart-final-sanity-check.md` right before client-facing delivery when charts are present.
- Read `references/chart-sanity-scan.md` when charts should be checked systematically rather than only by eye.
- Read `references/chart-templates.md` when the report needs reusable chart structures such as revenue mix, recurring vs non-recurring bridges, leverage/liquidity panels, or peer-framing snapshots.
- Read `references/cases/mtr-0066-notes.md` for 港鐵 / MTR / 0066 or similar rail-plus-property analysis tasks.
- Read `references/cases/utilities-notes.md` for regulated or semi-regulated utility companies.
- Read `references/cases/telecom-notes.md` for telecom, tower, broadband, or network-heavy communications businesses.
- Read `references/cases/property-platform-notes.md` for landlord-developer hybrids, rail-plus-property models, or other property-linked platforms.
- Read `references/improvement-priority-checklist.md` when iterating the skill after review feedback or when planning the next improvement batch.

## Output discipline

- Default to Traditional Chinese for the full deliverable unless the user explicitly requests English or a bilingual deliverable.
- Keep the report in one language. Do not mix Simplified Chinese, Traditional Chinese, and English narrative in the same deliverable.
- If source terminology is commonly cited in English, keep the English term in brackets on first use after the Traditional Chinese explanation.
- For Traditional Chinese client-facing delivery, localize page titles, section headings, KPI labels, chart titles, and annotations as far as practical; do not leave the page looking like a partially translated analyst workpaper.
- Avoid draft-like page labels such as "company analysis", "FY2025 analysis", "FY2024 baseline", "notes", or similar packaging language in the final deliverable unless the user explicitly wants an internal memo style.
- If English abbreviations remain necessary, avoid clustering too many of them in the same sentence or heading; prefer a Chinese lead term with the English term or abbreviation in brackets on first use.
- When a page is presented as a detailed metrics overview or dashboard, do not treat a small subset of metrics as if it were a complete panel; either meet the minimum dashboard standard or state clearly that the panel is partial.
- Write for a reader who does not already know the company, industry, or metric set.
- Do not place non-comparable metrics on the same chart or in the same ranking frame without an explicit warning that they are not directly comparable.
- Treat the following as non-comparable by default unless the company explicitly discloses them on a like-for-like basis: revenue, EBITDA, EBIT, recurrent EBIT, net profit, post-tax profit, distributable profit, and point-in-time balance-sheet metrics.
- Do not use revenue, EBITDA, EBIT, recurrent EBIT, or post-tax profit in the same apparent winner-loser comparison, ranking frame, or segment superiority claim. If they must appear in the same section for explanatory purposes, add an explicit note that they serve different analytical purposes and are not directly comparable.
- When the user asks about operating model, explain the business logic linking segments rather than only listing segment numbers.
- If possible, add peer comparison when the goal is to explain how the company differs from its industry rather than merely describing its own trend.
- When explaining changes in margin, EBIT, EBITDA, leverage, or earnings quality, trace the driver to the most specific disclosed cause available. Do not stop at vague phrases such as "cost pressure" or "expenses increased" when the filing discloses a more concrete driver such as staff cost, depreciation, maintenance, financing cost, lease-style payments, concession payments, or accounting reclassification.
- For judgment-heavy claims such as "business weakened", "income mix shifted", "resilience improved", "the company relied more on local assets", or similar strategic interpretations, require nearby numeric or textual evidence. If direct support is incomplete, downgrade the wording to a qualified interpretation rather than a hard conclusion.
- Unify units, labels, and period notation across charts, KPI cards, and tables. Do not mix styles such as bn, HK$bn, 百萬港元, 十億港元, FY, full year, H1, and 1H inconsistently within the same deliverable. Use `scripts/normalize_units_and_labels.py` for a first-pass normalization when useful.

## Pre-delivery execution checklist

Before final delivery, execute this checklist explicitly. If any item fails, revise the affected section before delivering.

1. **Source and period map**
   - Confirm each requested year or period is covered by a real official filing.
   - Confirm each table, chart, and KPI card is labeled with the correct period type: FY, H1, quarter, TTM, or point-in-time.
   - Remove or qualify any exhibit that backfills missing-period figures with another period's data.

2. **Comparability gate**
   - Scan every table, chart, summary box, and conclusion for mixed metric levels.
   - Reject any section that compares or ranks revenue, EBITDA, EBIT, recurrent EBIT, post-tax profit, or balance-sheet point-in-time metrics as if they were directly comparable.
   - If mixed metrics remain for explanatory context, add an explicit warning that they are not directly comparable and explain why each metric is shown.

3. **Evidence gate for judgment claims**
   - For each qualitative conclusion, ask: what nearby table, numeric value, or cited text supports this exact claim?
   - Rewrite or weaken claims that cannot be tied to nearby evidence.
   - Prefer "may reflect", "suggests", or "can be read as" over a hard conclusion when support is partial.

4. **Driver-analysis gate**
   - For each explanation of margin, profit, leverage, or earnings change, identify the most specific disclosed driver available.
   - If the filing identifies staff cost, depreciation, maintenance, financing cost, hybrid capital, reclassification, or another named driver, use that instead of a generic phrase.
   - When leverage improves, verify whether the change came from debt repayment, cash build, equity increase, perpetual capital securities, or another presentation effect.

5. **Reader-clarity gate**
   - Define technical metrics in plain language on first use.
   - Explain why the metric matters to the conclusion, not only what it means.
   - Check that a non-specialist reader can understand the causal chain from data to conclusion.

6. **Dashboard completeness gate**
   - If the deliverable contains a financial overview, KPI page, or metrics dashboard, check it against `references/financial-dashboard-minimum.md`.
   - If the panel is incomplete, state the missing metrics and why they are absent instead of silently implying completeness.
   - Do not claim a dashboard is "detailed" or "complete" unless it broadly meets the minimum panel standard.

7. **Unit, language, and label consistency gate**
   - Use one language consistently for narrative, chart labels, annotations, and table headings.
   - Use one unit style consistently within the deliverable.
   - Use one period-labeling style consistently within the deliverable.

8. **Chart-discipline gate**
   - Ensure each chart answers one clear question.
   - Remove duplicate or highly overlapping charts unless each serves a distinct analytical purpose.
   - Confirm the chart title, unit, period, and metric level are explicit.

9. **Operating-model gate**
   - If the task is about operating model, check that the report explains the linkage among traffic, monetisation, recurring income, cyclical profit, and financing structure rather than only listing segment figures.
   - Separate recurring earnings logic from timing-sensitive development or disposal gains.

10. **Final challenge**
   - Ask: would a detail-oriented reviewer challenge this sentence, chart, comparison, dashboard title, or page heading for mixed periods, mixed metrics, unsupported judgment, incomplete metric coverage, draft-like language, or inconsistent labels?
   - If yes, revise before delivery.

## Bundled resources

- `scripts/extract_pdf_text.py` — extract PDF text for local analysis
- `scripts/chart_sanity_scan.py` — simple scan for value-to-geometry consistency in HTML/SVG bar charts
- `assets/report_template.html` — single-file HTML report starter template
- `references/metric-keywords.md` — reusable keyword patterns for IR documents
- `references/plain-language-metrics.md` — reusable plain-language explanations for key financial metrics
- `references/source-period-map.md` — how to map disclosure date, covered period, and period type safely
- `references/external-retrieval-strategy.md` — how to use external search for source discovery without weakening evidence quality
- `references/hkex-ir-retrieval.md` — Brave + official IR + HKEX workflow for Hong Kong-listed company retrieval
- `references/peer-comparison.md` — lightweight framework for meaningful peer comparison
- `references/peer-research-subagent-workflow.md` — split peer research into subagent output plus main-agent integration
- `references/delivery-loop.md` — self-check → revise → self-check → revise → deliver workflow
- `references/internal-to-client-delivery.md` — workflow for separating internal checked versions from clean client-facing deliverables
- `references/v2-to-v3-acceptance-checklist.md` — acceptance checklist for validating whether a revised report actually addresses prior review comments
- `references/delivery-levels.md` — define whether the task is a baseline deliverable, enhanced version, or deep-research version
- `references/financial-dashboard-minimum.md` — minimum completeness standard for metrics overview, KPI panel, or dashboard pages
- `references/final-cn-delivery-checklist.md` — final Traditional Chinese delivery polish checklist for headings, labels, terminology, and tone
- `references/annual-report-openclaw-design-checklist.md` — design checklist for annual-report-style deliverables focused on change, trend, comparison, and future position
- `references/revenue-growth-and-upside.md` — default emphasis on current revenue growth and future growth potential
- `references/report-style-light-theme.md` — default light-theme visual guidance for deliverable reports
- `references/recent-news-window.md` — mandatory recent-three-month news / announcement retrieval rule for company analysis
- `references/news-driver-validation.md` — how to use news/public reporting for driver explanation without distorting period logic
- `references/latest-financial-statements-first.md` — use the latest official financial statements as the current-analysis base when no newer annual report exists
- `references/zh-report-checklist.md` — Traditional Chinese pre-delivery checklist for report quality control
- `references/chart-ui-quality.md` — chart presentation and UI consistency checks for deliverable-quality HTML exhibits
- `references/chart-final-sanity-check.md` — last-mile chart accuracy checks before client-facing delivery
- `references/chart-templates.md` — reusable chart patterns for revenue mix, leverage, recurring vs non-recurring, and peer framing
- `references/html-report-structure.md` — delivery-oriented HTML report section order and evidence-block pattern
- `references/improvement-priority-checklist.md` — prioritised skill iteration checklist after report feedback
- `references/cases/mtr-0066-notes.md` — MTR-specific pitfalls and framing guidance
- `references/cases/utilities-notes.md` — pitfalls and framing for utility companies
- `references/cases/telecom-notes.md` — pitfalls and framing for telecom and network-heavy businesses
- `references/cases/property-platform-notes.md` — pitfalls and framing for property-linked platform businesses

## Notes

- Prefer official primary sources over third-party summaries.
- If search APIs are unavailable, navigate from the company IR hub manually.
- Use external search for discovery and official sources for evidence.
- For company-analysis tasks, treat news, announcements, and external operating updates as a default retrieval layer; include them in the report only when evidence strength and period fit are adequate.
- Default to a light, reading-friendly visual style unless the user explicitly asks for a dark theme.
- For charted HTML, prefer inline SVG or self-contained HTML with no external JS dependency.
- For heavy-asset, infrastructure, transport, utility, telecom, or property-linked companies, check whether EBITDA and EBIT tell materially different stories before concluding which segment is more profitable or more cash generative.
- Treat perpetual capital securities and other hybrid instruments carefully. A filing may classify them as equity while readers still need an explanation of their financing role and why leverage ratios may look better without equivalent economic deleveraging.
