# Chart Sanity Scan

Use this reference when a report contains charts and should be checked systematically rather than only by eye.

## Goal

Detect chart mistakes that can survive analysis but still mislead the reader, especially in client-facing deliverables.

## What the scan should check

### 1. Value-to-geometry consistency
- A larger value must not render as a shorter / lower bar when bars are meant to be proportional.
- A smaller value must not render as a taller / higher bar when bars are meant to be proportional.
- Labels, legends, and geometry must agree.

### 2. Scaling assumptions
- Confirm whether bars are drawn from a shared baseline.
- Confirm whether the intended axis is linear and comparable within the same chart.
- Flag charts that use decorative fixed-height shapes while implying numeric comparison.

### 3. Label / order consistency
- Category labels should match the associated value labels.
- Left-to-right order should not imply the opposite of the underlying data.

### 4. Delivery decision
- If scan fails, either fix the chart geometry or replace the chart with a simpler version or a table.

## Recommended workflow

1. Generate chart.
2. Run chart sanity scan.
3. Review warnings.
4. Fix or simplify the chart.
5. Only then export client-facing HTML / PDF.

## Typical fail examples
- 0.9% rendered higher than 3.7%
- label says decline, bar height implies growth
- parent and child segments plotted as if directly parallel
- FY and H1 bars shown as if same-period ranking without warning
