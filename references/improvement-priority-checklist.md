# Improvement Priority Checklist

Use this checklist when iterating the `company-financial-analysis` skill after a real report draft, especially for reviewer-sensitive deliverables.

## P0 — Must fix before relying on the skill for delivery

- Correct any year / period mapping errors.
- Correct any chart, table, or KPI that mixes non-comparable metrics without an explicit warning.
- Correct any unsupported judgment claim that lacks nearby evidence.
- Correct any leverage explanation that ignores hybrid / perpetual capital or equity-base effects when relevant.
- Correct any segment hierarchy confusion before comparing segments.
- Remove any chart that looks visually broken, clipped, or patchy.

## P1 — High-value improvements for repeatable quality

- Add company-specific case notes when a company is easy to misread.
- Add metric keyword families for sector-specific extraction.
- Add stronger HTML report structure guidance for executive summary, evidence blocks, and references.
- Add explicit guidance for peer comparison when the user asks about distinctiveness or competitive position.
- Add clearer reader-facing definitions for technical metrics on first use.
- Add quality gates for language, units, and period notation consistency.

## P2 — Useful refinements after core reliability is stable

- Add reusable chart patterns for common financial exhibits.
- Add more sector notes beyond transport / rail / property-linked companies.
- Add extraction helpers beyond plain PDF text when layout quality becomes a recurring blocker.
- Add a stronger HTML template once the preferred report structure stabilises.
- Add example output snippets for especially fragile sections such as leverage interpretation or operating-model writeups.

## Suggested iteration workflow

1. Review the last deliverable and list reviewer objections.
2. Classify each issue into P0, P1, or P2.
3. Fix P0 items in SKILL.md or the most targeted reference file first.
4. Add or update references instead of bloating SKILL.md when details are company-specific or theme-specific.
5. Re-check the report against `references/zh-report-checklist.md` and `references/reviewer-sensitive-checklist.md` before packaging or reuse.
