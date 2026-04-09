# HKEX + IR Retrieval Workflow

Use this reference when analysing Hong Kong-listed companies and the task needs a repeatable way to find official filings, annual reports, interim reports, results announcements, and related IR materials.

## Goal

Combine external search speed with official-source discipline.

Use Brave to find the right doors quickly. Use company IR pages and HKEX disclosures as the actual evidence base.

## Retrieval order

1. Find the company investor-relations hub
2. Find the specific annual / interim / results document on the IR site
3. Check whether HKEX has the corresponding disclosure or announcement
4. Download the official PDF or save the official page text
5. Build the source-period map before analysis

## Why this order works

- IR hubs are usually easier to navigate for company-specific financial documents.
- HKEX disclosures help confirm timing, filing type, and completeness.
- Using both reduces the chance of missing a results announcement or relying on a stale PDF.

## Recommended Brave query patterns

### Find the IR hub
- `site:company-domain investor relations`
- `site:company-domain financial information`
- `site:company-domain annual report pdf`

### Find annual / interim / results documents
- `site:company-domain annual report 2024 pdf`
- `site:company-domain interim report 2025 pdf`
- `site:company-domain results announcement 2025 pdf`
- `site:company-domain investor presentation 2025 pdf`

### Find HKEX disclosures
- `site:hkexnews.hk <company name> annual results announcement`
- `site:hkexnews.hk <company name> interim results`
- `site:hkexnews.hk <ticker> results announcement`
- `site:hkexnews.hk <company name> annual report pdf`

## Practical workflow

### Step 1 — IR-first discovery

Use Brave to find the company IR hub first.

What to capture:
- IR landing page URL
- annual report page URL
- interim report page URL
- financial information page URL
- any investor presentation or results-announcement page URL

### Step 2 — HKEX cross-check

Use Brave again for HKEX disclosure discovery.

Use HKEX to confirm:
- the document exists as an official filing
- filing timing
- whether there are separate results announcements, circulars, or supplemental disclosures

### Step 3 — Pull official documents

Prefer these document types in order:
1. annual report / interim report PDF
2. results announcement PDF
3. official IR press release or presentation
4. HKEX disclosure page or attachment

### Step 4 — Build the evidence set

Before drafting, record:
- issuer
- document name
- URL
- disclosure date
- covered period
- period type
- what the document is safe to support

Use `scripts/build_source_period_map.py` where useful.

## What each source is best for

### Company IR
Best for:
- annual and interim reports
- investor presentations
- financial highlights pages
- management framing in a company-organised structure

### HKEX
Best for:
- filing confirmation
- announcement timing
- results announcements
- circulars and other statutory disclosures
- checking whether a document belongs to the company’s formal disclosure record

## Caution rules

- Do not assume the newest disclosure date means the newest operating period.
- Do not quote search snippets as evidence.
- Do not rely on third-party mirrors if the official IR or HKEX version is available.
- If IR and HKEX file naming differ, map them explicitly before analysis.

## For repeated Hong Kong company work

For recurring workflows, maintain a small source ledger containing:
- company name
- ticker
- IR hub
- HKEX search pattern
- preferred naming conventions for annual / interim / results documents

This reduces rediscovery time on future runs.
