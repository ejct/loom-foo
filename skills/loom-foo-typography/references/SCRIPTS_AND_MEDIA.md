# Typography: scripts, localization and media

Load only the relevant sections for a task.

## Ukrainian and multilingual work

- Verify actual Ukrainian glyphs **і, ї, є, ґ, І, Ї, Є, Ґ** together with apostrophe variants, punctuation, digits, quotation marks and diacritics in the chosen face and fallback chain. A font name or generic “Cyrillic” label does not establish coverage or acceptable style consistency.
- Check contrast of glyph designs across Ukrainian and Latin, x-height, capital proportion, numeral form and weight; tests should include real bilingual strings, not just the alphabet.
- Preserve author's intended spelling, nonbreaking spaces/hyphens, dates and proper nouns. If normative language changes are requested, hand off to writing/editorial responsibility. Avoid silently replacing a typographic apostrophe with another character when it changes protected text.
- Use correct language tagging (`lang`) on web content where applicable; check real fallback and typographic variation after font loading. Don't assume all script glyphs are present in a variable-font subset.
- For other scripts, consider shaping, directionality, line-breaking conventions, diacritics and local writing practice; do not apply Cyrillic/Latin kerning assumptions universally.

## Web/UI

- Treat responsive text as part of behavior: increased text size, zoom, user-defined spacing, content expansion, reduced width, control states, tables, sticky regions and overflow.
- In WCAG 2.2, SC 1.4.12 checks that users can **override** spacing to specified levels without loss; its values are **not prescribed default spacing**. SC 1.4.4 concerns resize text to 200% without loss of content/functionality; SC 1.4.10 covers applicable reflow. Their applicability depends on the implementation.
- Use actual browser render and font-loading/network diagnostics when available; unsupported evidence must be marked unverified. Contrast calculations should use foreground/background at the actual rendered state; font smoothing, transparency and image backgrounds matter.
- Avoid selecting a fixed tiny type size simply to preserve a layout. Consider semantic roles, accessible controls and variable content length.

## Documents, slides, display, print

- Different media have different viewing distances, zoom, rasterization, embedding and pagination. Test the actual page/screen; do not reuse web CSS sizes as print specifications.
- In paged editorial, inspect page breaks, widows/orphans, captions, footnotes, hyphenation and real language-specific line breaking.
- On slides, check readability in presentation context and typical screen sizes; a PDF render is not the same as the editable source.
- On print/packaging, consult the production provider for font embedding/outline requirements and color/bleed constraints where material. Without production preflight mark as unverified.

## Primary references

- W3C WCAG 2.2 Text Spacing: https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html
- W3C WCAG 2.2 Resize Text: https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html
- W3C WCAG 2.2 Reflow: https://www.w3.org/WAI/WCAG22/Understanding/reflow.html
- W3C WCAG Contrast Minimum: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
