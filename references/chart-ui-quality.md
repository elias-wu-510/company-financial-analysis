# Chart UI Quality

Use this reference when producing charted HTML reports, especially when the output is intended for direct delivery rather than internal drafting.

## Goal

Charts should be presentation-ready, not merely technically correct.

A chart with correct numbers can still fail as a deliverable if labels overlap, annotations are clipped, bar styles are inconsistent, or the exhibit looks visibly patched together.

## Core checks

### 1. Label readability

- Do not let numeric labels overlap bars, lines, legends, or other annotations unless the contrast is clearly readable.
- Prefer placing value labels above bars or in a safe whitespace area when the bar is narrow or dark.
- If labels are placed inside a chart element, ensure contrast is high enough and the label is not visually cramped.
- Re-check small values and negative values; these are the easiest to misplace.

### 2. Visual consistency

Within the same chart:
- use consistent corner radius for the same bar type
- use consistent bar widths and spacing
- keep colour logic stable
- avoid one element looking patched while others follow a different style
- keep axis labels, series labels, and numeric labels aligned to a common visual standard

### 3. Annotation safety

- Avoid clipped labels near the chart boundary.
- Leave enough top and side padding for value labels.
- If a label would extend beyond the viewBox, move the label or expand the canvas.
- Do not place explanatory notes where they compete with the data marks.

### 4. Comparability signalling

UI should help the reader understand comparability.

- If a chart is explanatory rather than directly comparable, state that visibly in a note or subtitle.
- Include period and unit in the title or subtitle.
- If the chart mixes metric types for explanation, add an explicit warning and avoid visual ranking cues.

### 5. Simplicity over decorative complexity

If the chart becomes fragile or visually messy:
- simplify the chart
- reduce labels
- switch to a table plus one smaller explanatory chart
- prefer clarity over density

## Practical failure modes to catch

- A value label is partially hidden by a bar.
- A dark bar uses a dark label with weak contrast.
- One bar loses rounded corners after a quick patch.
- A negative value label sits on the axis line and becomes hard to read.
- A chart looks visually inconsistent because one element was manually adjusted without rechecking the whole figure.

## Delivery rule

Before shipping an HTML report, visually sanity-check every chart for:
- label overlap
- label clipping
- inconsistent shapes
- inconsistent colours
- obvious patch artifacts
- period/unit/title clarity

If a chart still looks unfinished, revise it before delivery.
