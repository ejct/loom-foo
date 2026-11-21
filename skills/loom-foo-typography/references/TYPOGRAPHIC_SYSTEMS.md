# Typography: system design and optical judgment

Use when designing type systems, pairings, hierarchy or substantial typesetting. These are choices, not fixed prescriptions.

## Hierarchy as semantics

Start with reading tasks: primary action, heading, lead/dek, body, caption, navigation, input label, code/numeric data, warning, source note. Give each role an identifiable function and avoid type tokens chosen solely to complete a symmetric scale. Roles may share sizes when semantics and context allow.

For each role decide as needed: family; actual loaded face/style/axis; weight; size; line height; measure; tracking; casing; emphasis; responsive behavior; localization; digital/print units. A design token is a reusable semantic decision, not proof that the type was optically tested.

## Typefaces and pairing

- Evaluate by actual required script and content, not brand popularity. Check readability, punctuation, numeral forms, glyph distinctiveness, language-specific diacritics and fallback before locking a choice.
- Pair for a credible functional contrast: not all work needs multiple families. Contrast may come from weight, style, size, width, optical axis or composition within one family.
- Variable fonts offer axes only when confirmed by the actual file; CSS `font-optical-sizing: auto` depends on font support and environment. Never fabricate `opsz` or variable axis coverage.
- Respect source licensing, embedding and export terms. Fonts are not automatically redistributable with an artifact.

## Micro- and macrotypography

- **Micro:** optical kerning, tracking, punctuation, quotation marks, hyphen/minus/en/em dash, superscripts, numerals, accent marks, abbreviations, ligatures and script-specific spacing. Preserve source wording; apply available OpenType features only after confirming font/runtime support.
- **Macro:** line length/measure, rag, reading rhythm, section proximity, hanging headings, paragraph separation, column structures, baseline relationships, captions and grids. Preserve a clear scan path; don't insist on a fixed characters-per-line target.
- Evaluate display text at its intended size independently from body copy. A striking headline treatment may be wrong for dense UI data.
- For tables and values test widths, decimal alignment, sign and currency glyphs and semantic grouping. Tabular numerals are useful only when the font supports them and alignment needs them.

## Creative tension

Typography conveys voice as well as content. Distinctive choices are acceptable when intentional and not in conflict with reading tasks. Avoid defaulting to generic SaaS type ramps or imposing corporate neutrality on expressive work. Compare possible treatments at the target size, then select with explicit trade-offs.
