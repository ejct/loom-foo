# Typography: artifact-level verification

## Evidence order

1. Actual source/content and font assets/metadata where permitted.
2. Rendered specimen at intended use size, plus relevant alternate viewport / zoom / language / print page.
3. Deterministic checks (font file presence, glyph coverage via font tools, static style extraction, calculated contrasts, text/container bounds) **where available**.
4. Human/agent perceptual judgment for hierarchy, texture, voice, optical rhythm and line breaks; label as judgment rather than a measured fact.

A source file parser cannot guarantee rendered typography. A screenshot cannot prove font licensing or reflow behavior. Do not conflate these.

## Focused quality checks

- **Copy and glyphs:** exact text, dates, localized strings, diacritics, symbols, numbers; no missing glyphs/fallback surprises.
- **Hierarchy and composition:** role clarity, coherent scale, contrast, line breaks and rag, paragraph rhythm; read at realistic scale, not only zoomed-in proof.
- **Responsive and dynamic text:** long labels, changed locale, zoom/spacing overrides, values and errors; verify affected states.
- **Fonts:** exact family/style installed or embedded, font licensing/embedding rights when needed, fallback verified if used.
- **Artifact contract:** requested editable source actually exists, no accidental conversion to flattened raster; print/slide preflight only claimed if performed.

## Finding format

For each consequential issue record location and scenario; what was *seen*; why it matters for reading/meaning; measured fact versus design judgment; suggested repair; verification after repair. Report `UNVERIFIED` for unavailable devices, files or target formats. A review checklist alone is not a pass.

## Stop rule

Do not run every test on every task. One title correction does not need an exhaustive screen-reader audit or a font-security review; a production-ready brand guideline may need broader checks. Stop once the requested artifact is usable and material remaining uncertainties are explicit.
