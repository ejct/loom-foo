# Truthfulness and QA for information graphics

## Evidence and quantitative fidelity

- Bind labels, values, units and dates to authoritative data, including time-zone and denominator where material. Do not manually retype rounded numbers without validating them.
- Verify data grain, totals, sort direction, percentages, null handling and whether the chart's comparison is meaningful. Ask Data owner if inference or transformations are unresolved.
- Avoid deceptive truncation for magnitude bars; note when a nonzero axis is intentional and justified. Do not use 3D extrusions, area bubbles or perspective as default quantitative encodings.
- Distinguish a sample, estimate, forecast, measurement and a user-reported number. Annotate uncertainty when present. Don't invent narrow confidence intervals.
- Validate coordinate semantics, arrow direction, grouping and causality assertions in non-numeric diagrams; incorrect relations are factual defects.

## Actual visual QA

Inspect output at target size; confirm readable exact labels, proper diacritics, consistent legend and symbol meaning, no line crossings that misrepresent edges, no unlabeled unit changes, accessible use of color plus secondary cues when important. For interactive visuals, test the actual interaction; a static export cannot establish hover/focus correctness.

Record evidence separately: `SOURCE_CHECKED`, `CALCULATION_CHECKED_BY_DATA_OWNER`, `RENDER_VIEWED`, `NOT_TESTED`. Do not claim the first from the presence of a source URL alone. Do not treat generated images with invented labels as controlled diagrams.
