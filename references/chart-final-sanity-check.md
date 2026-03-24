# Chart Final Sanity Check

Use this reference right before delivering a client-facing report with charts.

## Goal

Catch the last-mile chart errors that can survive correct analysis but still break trust in delivery.

## Must-check items

### 1. Visual height / length must match the number
- [ ] A higher value must not render as a lower bar or shorter line point.
- [ ] A lower value must not render as a taller bar just because of reused styling or fixed-height artifacts.
- [ ] If labels and geometry disagree, fix the geometry first.

### 2. Label-value agreement
- [ ] Numeric labels must match the plotted values.
- [ ] Axis direction, bar order, legend, and labels must all tell the same story.
- [ ] Do not assume the label is enough if the shape is misleading.

### 3. Negative / low-value handling
- [ ] Very small positive values should still look clearly smaller than higher values.
- [ ] Negative values should not appear visually above positive values unless explicitly intended by the axis.

### 4. Series consistency
- [ ] Reused chart components must be re-scaled with new data.
- [ ] Decorative rounded bars or capsules must not override real proportionality.

### 5. Delivery rule
- [ ] Before external delivery, visually inspect every chart against its source numbers.
- [ ] If a chart is even slightly misleading, replace it with a simpler chart or a compact table.

## Preferred fallback

If chart proportionality is fragile, use:
- a simple table
- or a minimalist bar chart with explicit numeric labels

Clarity beats ornament.
