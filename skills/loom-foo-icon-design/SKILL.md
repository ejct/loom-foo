---
name: loom-foo-icon-design
description: "Create or production-check interface/app icons and pictograms at actual optical sizes. Not full identity work or review-only critique."
metadata:
  family: "design"
  version: "0.4.0"
  project: "loom-foo"
compatibility: "Agent Skills-compatible; raster/icon source, image editing, SVG and native-platform export support depend on available tools."
---

<!-- loom-foo Answer Receipt v0.3: shared response provenance and Process Trail projection -->
**Answer Receipt.** When this skill is directly consulted or materially applied in preparing a user-facing answer, include a compact **Answer Receipt** as the final section. List only actually used/consulted skills (including external skills when evidenced), exact versions if known, `SKILL.md` delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered reference coverage, actual sources, checks, actions and material limitations. `FULL` requires model-visible contiguous delivery of the exact source through EOF, not a reader success flag. **Process Trail:** for substantive multi-stage work, including repeated proposal/task reviews, corrections, verifications or genuine cross-agent/artifact handoffs, show an ordered breadcrumb sequence such as `DRAFT1 → REVIEW1 → REVISE1 → REVIEW2 → READY`, with a brief result, exact artifact identity when established, and provenance for consequential stages. Preserve distinct repeated passes in their original order; do not invent unseen stages, file revisions, handoffs, independence or runtime events. Different consulted skills in the same agent context are not separate agent executions. An internally reconstructed review is `MODEL_REPORTED`, not independently verified. Keep one footer, not a second Processing Receipt. No new tests or logging merely for the footer. Follow `docs/ANSWER_RECEIPT_V0.3.md` when accessible; this clause works standalone. Preserve JSON-only, machine payload, code-only and strict producer handoff formats when a footer is forbidden.

# Icon Design

## Result contract

Produce icons/symbols that convey their function or identity at the intended real sizes. A large beauty rendering does not validate an app icon at launcher size or a toolbar glyph at 16 px. A raster export does not satisfy an explicitly editable vector request. Preserve platform and brand requirements, source assets and requested formats.

## Domain boundaries

Use for app icons, UI pictograms, icon systems, control affordance symbols and optically refined mark variants. Distinguish **app icon / product symbol**, **interface action icon**, **system pictogram** and **logo mark** in the brief; they may share form but differ in context, semantic burden and platform specification.

- Brand architecture, identity system or mark in a broader brand program -> `loom-foo-identity-design`; this skill may handle icon exports and optical adaptation.
- Vector illustration/comic or poster concept -> `loom-foo-graphic-design`/`loom-foo-design` unless a repeatable icon language is the goal.
- Review-only design critique -> `loom-foo-design-review`.
- Exact platform icon specification/version must be checked against current platform docs when production compliance is claimed; do not assume universal px sets.

## Design procedure

1. **Resolve icon kind and context.** Where will it appear, against what background, at which effective sizes, with which semantic neighbors? Determine platform mask/safe area, variant/state needs, source requirement and whether it is functional or identifying.
2. **Design the silhouette and semantic core.** Prioritize immediate recognition, shape distinctiveness, internal spaces and feature priority. Avoid relying on material textures, tiny engravings or miniature text as the only differentiator. In UI icon sets establish stroke, cap/join, corner, optical center and relative visual weight. Read `references/OPTICAL_GEOMETRY.md`.
3. **Construct coherent variants.** Draw the core at realistic target size, then refine separate optical-size masters only when necessary; consider filled/outlined, active/inactive, monochrome/reversed, local color state and adaptive platform constraints. Do not just uniformly downsample and claim every size was redesigned.
4. **Produce requested source and exports.** Use native vector paths/SVG when required, real raster exports otherwise. Preserve crisp edges, transparency, non-destructive sources where requested, and platform guidelines. Read `references/EXPORT_AND_REVIEW.md`.
5. **Inspect actual use.** Review target-size mosaics against realistic backgrounds, grayscale and small-scale behavior, ambiguous metaphor, negative-space collapse and anti-alias artifacts. Repair the **small-size** defect rather than polishing the large rendering only.
6. **Deliver.** Provide files and sizes/variants, precise quality limits, and what was actually visually checked.

## Internal QA

Check silhouette at smallest meaningful size, glyph weights, negative space, grid/optical center, background/mask collisions, semantic consistency and exact export dimensions. A standalone critique request routes to Design Review; no mandatory second review agent.

## Examples

- “Намалюй iOS-іконку та перевір її у маленькому розмірі” -> Icon Design, target-size inspection.
- “Створи 24 узгоджені UI-іконки для navigation” -> Icon Design; establish coherent grammar and checks across a representative set.
- “Побудуй бренд-систему з логотипом” -> Identity Design.
- “Оціни цей знак без редагування” -> Design Review.

## Conditional references

- `references/OPTICAL_GEOMETRY.md` — optical compensation, silhouettes, icon families and semantics.
- `references/EXPORT_AND_REVIEW.md` — platform/source/export and target-size QA.
