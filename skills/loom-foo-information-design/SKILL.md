---
name: loom-foo-information-design
description: "Design evidence-grounded diagrams, infographics or technical explanations with truthful visual encoding. Not general posters or data analysis."
metadata:
  family: "design"
  version: "0.5.0"
  project: "loom-foo"
compatibility: "Agent Skills-compatible; can use verified tables/charts/SVG/document tools, or provide bounded explanations when rendering is unavailable."
---

<!-- loom-foo Answer Receipt v0.3: shared response provenance and Process Trail projection -->
**Answer Receipt.** When this skill is directly consulted or materially applied in preparing a user-facing answer, include a compact **Answer Receipt** as the final section. List only actually used/consulted skills (including external skills when evidenced), exact versions if known, `SKILL.md` delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered reference coverage, actual sources, checks, actions and material limitations. `FULL` requires model-visible contiguous delivery of the exact source through EOF, not a reader success flag. **Process Trail:** for substantive multi-stage work, including repeated proposal/task reviews, corrections, verifications or genuine cross-agent/artifact handoffs, show an ordered breadcrumb sequence such as `DRAFT1 → REVIEW1 → REVISE1 → REVIEW2 → READY`, with a brief result, exact artifact identity when established, and provenance for consequential stages. Preserve distinct repeated passes in their original order; do not invent unseen stages, file revisions, handoffs, independence or runtime events. Different consulted skills in the same agent context are not separate agent executions. An internally reconstructed review is `MODEL_REPORTED`, not independently verified. Keep one footer, not a second Processing Receipt. No new tests or logging merely for the footer. Follow `docs/ANSWER_RECEIPT_V0.3.md` when accessible; this clause works standalone. Preserve JSON-only, machine payload, code-only and strict producer handoff formats when a footer is forbidden.

# Information Design


**Conditional knowledge/evidence composition (L1).** If the diagram depends on materially missing accepted definitions, entity relationships or decisions from an authorized project history, consult `loom-foo-knowledge-retrieval` read-only. If a bounded existing evidence package supports consequential quantitative/causal claims and its meaning is unsettled, consult `loom-foo-evidence-review` (or the stronger domain/data specialist for underlying calculations) before asserting the claims visually. Information Design remains responsible for accurate information topology and production. A source-complete illustration or straightforward data display needs no extra skill.

## Result contract

Turn *grounded* information into a truthful, comprehensible visual structure and requested artifact. The design must preserve quantities, qualifiers, definitions, relationships, times, geography, source provenance and uncertainty. The deliverable is the graphic or editable diagram when requested — not an invented dataset, unvalidated iconography or an art-direction description.

## Routing and boundaries

Use when the central challenge is to explain, compare, connect or show a process, relationship, hierarchy, location or measured change. Typical outputs: annotated figure, infographic, technical diagram, data story, process map, taxonomy, timeline, explanatory poster.

- Data/analytics specialists own calculation, statistics, joins, missing data, units, quantitative inference and source checking. Verify these upstream before visually asserting claims.
- `loom-foo-graphic-design` owns message-first expressive poster/campaign communication without exact information-topology requirements.
- `loom-foo-typography` owns detailed type systems; legible accurate labels remain this skill's duty.
- `loom-foo-design-review` owns critique-only requests.
- Product flows as interactive behavior belong to `loom-foo-experience-design`; explanatory flow diagrams can belong here.

## Procedure

1. **Declare the message and evidence.** Identify audience/question, one primary claim or explanation, data grain, sources and reliability. Tag observed facts, derived figures, assumptions and unknowns. Never fill missing evidence with plausible values.
2. **Choose information topology.** Select comparison, hierarchy, sequence, process, geographic relation, distribution, network or causality-claim mapping from actual semantics. Read `references/INFORMATION_TOPOLOGIES.md` for diagram/chart choice. Do not impose an exciting flowchart on a simple comparison.
3. **Design correct encodings.** Choose axes, units, baseline, scales, ordering, direct labels, color semantics, annotations and confidence treatments. Check denominators, sampling, timebase and whether form implies causality. Read `references/TRUTH_AND_VISUAL_QA.md` for common distortions.
4. **Create real artifact.** Prefer deterministic controlled text/data layers (e.g. chart definitions, SVG, presentation or vector tools) over a generative picture when numerical precision matters. Use a separate image-generation layer only for non-factual illustration. Supply source editability where requested.
5. **Validate what viewers actually see.** Compare all labels/numbers with evidence. Inspect chart geometry, legends, ambiguous links, grouping, readability, clipping and small-size rendering; test whether the visual supports the claimed takeaway. Repair material defects and re-inspect if feasible.
6. **Deliver.** Give actual figure/source, concise interpretation, source identities, visible uncertainties and tested vs untested properties. For unsupported precision constraints provide an honest bounded alternative.

## Proportionate internal QA

Every consequential figure gets source-number correspondence, semantic truth and artifact check. This is not a mandatory standalone Design Review activation. Never claim a chart is scientifically verified because it looks polished.

## Examples

- “Зроби схему залежностей сервісів з наданої архітектури” -> Information Design: faithful edges/direction, names and source trace.
- “Зобрази ці продажі по роках, не змінюючи дані” -> Information Design after numeric provenance is established.
- “Зроби емоційний постер без чисел” -> Graphic Design.
- “Оціни готову інфографіку, не змінюй її” -> Design Review.

## Conditional references

- `references/INFORMATION_TOPOLOGIES.md` — relation-to-visual mapping and choice.
- `references/TRUTH_AND_VISUAL_QA.md` — numeric/semantic integrity and media-level checks.
