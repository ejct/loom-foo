---
name: loom-foo-graphic-design
description: "Create or revise posters, campaigns, covers and editorial compositions with exact content, format adaptations and controlled local edits. Not identity-system redesign, infographics or critique-only tasks."
metadata:
  family: "design"
  version: "0.5.0"
  project: "loom-foo"
compatibility: "Agent Skills-compatible guidance; actual editing, illustration, page layout and export tools vary by host."
---

<!-- loom-foo Answer Receipt v0.3: shared response provenance and Process Trail projection -->
**Answer Receipt.** When this skill is directly consulted or materially applied in preparing a user-facing answer, include one compact truthful receipt naming only actually consulted/applied skills and versions, model-visible SKILL.md delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered references, sources, checks, actions and limitations. `FULL` requires complete contiguous exact text through EOF; a tool fetch alone is insufficient. For material review/repair/recheck stages show an ordered Process Trail with source identity and `SAME_CONTEXT` versus actually observed separate actors. Never fabricate independent reviews, runtime telemetry, tests, publication, installation or other effects. Respect strict machine-only outputs.

# Graphic Design

## Result contract

Transform a communication brief and **real content** into a coherent visual composition in the requested medium. Primary result: an actual graphic, editable layout, production candidate, multi-format adaptation or targeted revision as requested. A moodboard, adjectives, or image-model approximation does not substitute for an editable source. Preserve supplied exact copy, units, logos, brand restrictions and attribution. For an approved design, keep accepted parts stable while modifying the named aspect.

## Own this / exclude this

Use for posters, banners, covers, presentation visuals, campaign systems, editorial spreads, communication-focused cards, packaging graphics at concept/layout level and visual hierarchy problems in static media. Own art direction, visual grammar, message hierarchy, image/type interplay, spacing, channel adaptations and **localized composition changes to an approved graphic**.

- Pure type system, typeface selection, line setting or glyph problems -> `loom-foo-typography`; however, Graphic Design still owns composition-wide headline placement and its local QA.
- Precise quantitative or evidence topology -> `loom-foo-information-design` (Data owns numerical derivation).
- A new or changed brand identity, mark/wordmark or brand usage policy -> `loom-foo-identity-design`; Graphic Design uses an approved logo without silently changing its shape.
- A set of production icons or symbols -> `loom-foo-icon-design`.
- An existing design needing critique without editing -> `loom-foo-design-review`.
- Multidisciplinary product strategy, physical/3D/motion production or undefined design task -> `loom-foo-design` unless a specific owner fits.

No sibling skill is mandatory. Use relevant techniques without claiming another skill ran. Choose host-native slide/document/Figma/vector/image tools based on requested output and availability.

## Working method

1. **Extract the communication task.** Who should understand or do what, at what viewing distance, channel and format? Resolve the required message hierarchy, authoritative text/assets and forbidden substitutions. Prefer a small explicit brief over invented audience research. If this is a revision, locate the latest accepted layout and keep the existing idea unless changed.
2. **Find an organizing idea only if unresolved.** Decide message/concept/visual metaphor. Sketch materially different concepts only when worth comparing; avoid superficial color-only options or default gradient-and-card layouts. A narrow local edit does not reopen art direction.
3. **Build or adjust visual structure.** Select attention path, focal proportion, grid or deliberate departure, negative space, image framing, typography, color contrast and grouping. Read `references/COMPOSITION_AND_ART_DIRECTION.md` for complex hierarchy, cross-format and image/type cases. Let real copy determine line breaks and sizes; do not invent or omit words to fit the page.
4. **Produce the requested artifact or revision.** Preserve editability when requested; use independently controlled text for exact names, dates and numbers. For a multi-format set define invariant **meaning/brand/message priority** and permitted reflow, not one pixel-identical layout for all ratios. Read `references/OUTPUT_AND_PRODUCTION.md` for medium/export issues. For an approved local graphic edit or multi-format derivation with protected properties, read `references/CONTROLLED_GRAPHIC_REVISION.md` and follow the change boundary below.
5. **Inspect and correct actual output.** Examine normal-size and thumbnail renderings, target crops, exact text and language, relevant logo source, hierarchy and visual coherence. Compare the specified change and protected aspects against the right baseline(s); repair unwanted drift when feasible. Use physical-print preflight if actually available; absent printer specs or proof, do not call a PDF print-ready.
6. **Deliver.** Supply real artifacts, source when required, format details, exact changes, checked invariants and what remained unverified. Stop when the scoped deliverable is usable.

## Controlled revision and multi-format boundary

When the user asks to “make the spacing wider,” “move only this element,” “keep the supplied headline,” or “adapt this A3 poster to Stories”:

- Start from the latest approved layout/source. Preserve fixed source copy, brand mark, key image identity, legal text and accepted layout relationships not reopened by the user; identify the exact changed dimension.
- For a **local edit**, operate on the smallest controllable element/layer or constrained region. Do not globally regenerate an accepted composition to fix one offset when an exact edit path exists. If only generative editing is possible, acknowledge possible collateral drift and verify with a before/after comparison.
- For **new ratios or languages**, keep information priority, voice, brand grammar and specified assets invariant; permit necessary reflow, crop and new line breaks. Never pretend all pixel positions or line breaks can remain identical across different ratios/text lengths.
- Keep exact text outside a visual generation step where possible; inspect every delivered variant for actual characters, amounts, citations/attribution, crop and safe areas. Distinguish editable final source from raster concept output.
- If the requested accuracy cannot be reached by available tools, return the strongest honest artifact and identify the exact unsatisfied property; do not claim preservation or production verification without checks.

## Embedded QA, not a review pipeline

Self-check real content, focal message, rendered type, spacing/crop, target dimensions and exported artifacts. Standalone Design Review is for explicit independent critique or material cross-disciplinary challenge, not a required second pass. A changed pixel is not by itself a visual defect; compare against what must be invariant.

## Example ownership

- “Зроби афішу з повним текстом для A3 і Stories” -> Graphic Design: actual layouts in both ratios, copy/crop verified.
- “Пересунь блок ціни, а логотип і весь текст не змінюй” -> Graphic Design: local layer adjustment with before/after comparison.
- “Виправ лише кернінг у заголовку” -> Typography.
- “Зміни геометрію самого фірмового логотипа” -> Identity Design.
- “Порівняй ці дві афіші, не змінюй їх” -> Design Review.
- “Перевір числову інфографіку та її масштаби” -> Information Design plus numerical provenance owner.

## Conditional references

- `references/COMPOSITION_AND_ART_DIRECTION.md` — hierarchy, concept, image/type and campaigns.
- `references/OUTPUT_AND_PRODUCTION.md` — assets, dimensions, cross-format production and delivery.
- `references/CONTROLLED_GRAPHIC_REVISION.md` — preservation of approved composition during scoped edits and format adaptations.
