---
name: loom-foo-graphic-design
description: "Design or revise posters, campaigns, covers or editorial compositions. Not typography-only, infographics, identity or critique-only tasks."
metadata:
  family: "design"
  version: "0.4.0"
  project: "loom-foo"
compatibility: "Agent Skills-compatible guidance; actual editing, illustration, page layout and export tools vary by host."
---

<!-- loom-foo Answer Receipt v0.3: shared response provenance and Process Trail projection -->
**Answer Receipt.** When this skill is directly consulted or materially applied in preparing a user-facing answer, include a compact **Answer Receipt** as the final section. List only actually used/consulted skills (including external skills when evidenced), exact versions if known, `SKILL.md` delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered reference coverage, actual sources, checks, actions and material limitations. `FULL` requires model-visible contiguous delivery of the exact source through EOF, not a reader success flag. **Process Trail:** for substantive multi-stage work, including repeated proposal/task reviews, corrections, verifications or genuine cross-agent/artifact handoffs, show an ordered breadcrumb sequence such as `DRAFT1 → REVIEW1 → REVISE1 → REVIEW2 → READY`, with a brief result, exact artifact identity when established, and provenance for consequential stages. Preserve distinct repeated passes in their original order; do not invent unseen stages, file revisions, handoffs, independence or runtime events. Different consulted skills in the same agent context are not separate agent executions. An internally reconstructed review is `MODEL_REPORTED`, not independently verified. Keep one footer, not a second Processing Receipt. No new tests or logging merely for the footer. Follow `docs/ANSWER_RECEIPT_V0.3.md` when accessible; this clause works standalone. Preserve JSON-only, machine payload, code-only and strict producer handoff formats when a footer is forbidden.

# Graphic Design

## Result contract

Transform a communication brief and real content into a coherent visual composition **in the requested medium**. Primary result: an actual graphic, editable layout, production candidate, or targeted revision as requested. A moodboard, set of adjectives, or image-model approximation does not substitute for an editable source. Keep author's exact supplied copy, units, logos, brand restrictions and attribution.

## Own this / exclude this

Use for posters, banners, covers, presentation visuals, campaign systems, editorial spreads, communication-focused cards, packaging graphics at concept/layout level and visual hierarchy problems in static media. Own art-direction concept, visual grammar, message hierarchy, image/type interplay, spacing and format adaptations.

- Pure type system, typeface selection, line setting or glyph problems -> `loom-foo-typography`.
- Precise quantitative or evidence topology -> `loom-foo-information-design` (Data owns numerical derivation).
- System of brand identity and usage rules -> `loom-foo-identity-design`.
- A set of production icons or symbols -> `loom-foo-icon-design`.
- An existing design needs critique *without* editing -> `loom-foo-design-review`.
- Multidisciplinary product strategy, physical/3D/motion production or undefined design task -> `loom-foo-design` unless a specific owner fits.

No sibling skill is mandatory. Use relevant techniques without claiming another skill ran. Choose host-native slide/document/Figma/vector/image tools based on requested output and availability.

## Working method

1. **Extract the communication task.** Who should understand or do what, at what glance distance, on which channel and format? Resolve the required message hierarchy, authoritative text/assets and forbidden substitutions. Prefer a small explicit brief over invented audience research.
2. **Find an organizing idea.** Decide the relation between message, concept and visual metaphor. Sketch materially different concepts only when a decision warrants comparison; avoid superficial color-only options or default gradient-and-card layouts.
3. **Build the visual structure.** Select attention path, focal proportion, grid or deliberate departure, negative space, image framing, typography, color contrast and content grouping. Read `references/COMPOSITION_AND_ART_DIRECTION.md` for complex hierarchy, cross-format and image/type cases. Let real copy determine line breaks and sizes.
4. **Produce the correct artifact.** Preserve editability where requested; use controlled text for exact names/dates/numbers. For a multi-format set, define what remains invariant and what legitimately reflows. Read `references/OUTPUT_AND_PRODUCTION.md` for medium/export issues. Do not generate just one attractive raster when source files or multiple sizes are required.
5. **Inspect and correct.** Look at actual-size and thumbnail previews, target crops, text and image integrity, hierarchy and aesthetic coherence. Use appropriate preflight for physical production; absent printer specs or real preflight, do not label a PDF print-ready. Repair consequential defects and inspect the correction.
6. **Deliver.** Provide real artifacts, source where required, format details, key design choice and checks performed vs missing. Stop when the user's scoped deliverable is usable.

## Embedded QA, not a review pipeline

Self-check real content, focal message, typographic rendering, spacing/crop, requested dimensions and exports. A separate `loom-foo-design-review` is for explicit standalone critique or materially consequential cross-disciplinary challenge, not a required second pass after every design.

## Example ownership

- “Зроби афішу з повним текстом для A3 і Stories” -> Graphic Design: actual layouts in both ratios, copy and crop verified.
- “Виправ лише кернінг у заголовку” -> Typography.
- “Порівняй ці дві афіші, не змінюй їх” -> Design Review.
- “Перевір числову інфографіку та її масштаби” -> Information Design plus numerical provenance owner.

## Conditional references

- `references/COMPOSITION_AND_ART_DIRECTION.md` — visual hierarchy, composition, idea, image/type and series.
- `references/OUTPUT_AND_PRODUCTION.md` — assets, dimensions, cross-format adaptation and delivery.
