---
name: loom-foo-identity-design
description: "Design or revise cohesive visual brand identities: marks, type, color, usage and controlled revisions of approved identity assets. Not standalone app icons or review-only critique."
metadata:
  family: "design"
  version: "0.5.0"
  project: "loom-foo"
compatibility: "Agent Skills-compatible; trademark searching, licensing verification, vector editing and production exports require actual tools/evidence."
---

<!-- loom-foo Answer Receipt v0.3: shared response provenance and Process Trail projection -->
**Answer Receipt.** When this skill is directly consulted or materially applied in preparing a user-facing answer, include one compact truthful receipt naming only actually consulted/applied skills and versions, model-visible SKILL.md delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered references, sources, checks, actions and limitations. `FULL` requires complete contiguous exact text through EOF; a tool fetch alone is insufficient. For material review/repair/recheck stages show an ordered Process Trail with source identity and `SAME_CONTEXT` versus actually observed separate actors. Never fabricate independent reviews, runtime telemetry, tests, publication, installation or other effects. Respect strict machine-only outputs.

# Identity Design

## Result contract

Turn an approved brand brief and constraints into a recognizable, coherent **visual identity system**, with actual files/rules at the fidelity requested. For a revision, deliver the **requested change to the existing approved asset**, not an unsolicited replacement concept. A logo preview alone is not a full identity. Do not assert a mark is legally unique, registrable, protected or commercially cleared without a proper legal/trademark process.

## Own this / adjacent owners

Use for new or revised visual identities, brand marks/wordmarks, coherent signature systems, symbol/color/type rules, identity applications, icon-of-brand integration and identity guidelines. This includes an **exact scoped revision to an existing brand mark/wordmark** where preserving accepted brand properties is central.

- One product icon/app launcher or family of action glyphs -> `loom-foo-icon-design` unless tied to larger identity strategy.
- Typography craft or detailed type system -> `loom-foo-typography`; identity owns approved brand voice/role and brand-wide constraints. A purely typographic adjustment without brand-system implications belongs to Typography.
- Standalone poster/campaign visual -> `loom-foo-graphic-design` following any supplied identity. Graphic Design applies the brand without silently redesigning its mark.
- Token/component design-system across products -> `loom-foo-design-systems` for system semantics, after identity decisions.
- Review-only brand critique -> `loom-foo-design-review`.
- Brand copywriting/narrative architecture -> Writing specialists; don't invent positioning research or audience quotes.

## Procedure

1. **Clarify identity subject.** Brand/product, audience, desired attributes, competitive/category references, language/scripts, existing marks, legal constraints, touchpoints and required deliverables. Distinguish existing accepted direction from open design space. If editing an accepted asset, identify its exact available baseline and current instruction; don't restart ideation by default.
2. **Develop a coherent visual proposition when the concept is open.** Define visual principles specific enough to distinguish alternatives (geometry, visual rhythm, contrast, symbolism, material and typographic voice), not generic 'minimal, modern, bold'. Read `references/IDENTITY_CONCEPT_AND_SYSTEM.md` for a substantive new identity or system-level change. For a precise accepted edit, preserve the concept and skip needless alternative directions.
3. **Design marks and system or make the scoped change.** For a new identity construct a usable family: mark/wordmark/lockups, monochrome and reversed variants, typographic/color roles and requested applications. Consider Ukrainian/Latin names and glyph coverage. Do not redraw third-party logos as original marks. For a **targeted edit to an approved existing mark/wordmark**, apply the revision boundary below and read `references/CONTROLLED_IDENTITY_REVISION.md` before production; use a source-preserving tool when exact properties must remain fixed.
4. **Produce real assets.** Use requested vector/native sources and controlled export; include guidelines only when requested. Read `references/IDENTITY_DELIVERY_AND_QA.md` for optical and production-specific details. If only an image concept exists, call it a concept. A generated image alone is not proof that underlying letterforms, anchor points or brand assets were preserved exactly.
5. **Validate across touchpoints.** Inspect actual sizes, negative-space collapse, one-color/reversed use, locale, UI graphics and backgrounds, consistency between lockups and recognizability of the primary mark. For an edit, compare the changed property and relevant unchanged properties against the baseline at matching size. Separate optical judgment, objective file checks and unsupported assumptions.
6. **Deliver and stop.** Provide the requested assets or scoped identity decision, reference version, exact changed scope, preservation evidence and outstanding rights/production checks. Do not imply trademark clearance, font licenses or finished full-system work without evidence.

## Controlled revision boundary — when editing accepted work

When the user says “keep the font,” “move only the spiral center,” “preserve these letters,” or gives another narrow change to an accepted identity:

- Resolve the **latest approved visible/source baseline**. If unavailable, state which exact fidelity cannot be verified; use the best available reference without inventing continuity.
- Interpret `PRESERVE` (named accepted properties and unmentioned identity invariants), `CHANGE` (the exact requested property), and `OPEN` (genuinely flexible incidental choices). Do this briefly in working context; do not force a user form or bureaucratic artifact.
- **Preserve previous accepted decisions cumulatively.** New feedback updates the named dimension only unless the user explicitly reopens another. If requirements conflict, flag the concrete conflict instead of silently changing unrelated parts.
- Choose a controllable vector/layer/path edit for hard geometry, font, spacing or lockup invariants when such source/tools are accessible. Image generation may make a useful approximate revision, but cannot establish byte- or vector-exact preservation.
- Inspect the actual result. If a protected property changed, restore or report the drift; never call it unchanged solely because the prompt requested preservation. When exact editing is unsupported, label the result `APPROXIMATE_REVISION`, identify what is unverified, and provide a bounded path to exact production if feasible.

## Internal QA

Check identity coherence and real use cases rather than just one attractive mockup. Separate visual distinctiveness from legal clearance. Optional standalone Design Review for consequential external critique; no compulsory review stage for a tiny export fix. Do not require a second skill to apply this revision boundary.

## Examples

- “Створи цілісну двомовну айдентику продукту” -> Identity Design, actual mark/usage family where requested.
- “Посунь центр спіралі лівіше, але залиш затверджений шрифт і літери” -> Identity Design, controlled revision; unchanged glyphs require evidence.
- “Зроби набір стандартних toolbar icons” -> Icon Design.
- “Підбери шрифтові пари для наявного бренд-гіда” -> Typography unless new brand-system decisions are requested.
- “Порівняй два готові логотипи, без змін” -> Design Review.
- “Застосуй цей логотип до афіші, не змінюючи саму айдентику” -> Graphic Design.

## Conditional references

- `references/IDENTITY_CONCEPT_AND_SYSTEM.md` — distinct brand visual principles, marks and family cohesion; read for new or materially redesigned identity systems.
- `references/IDENTITY_DELIVERY_AND_QA.md` — file/size/language/rights checks and honest output status; read when producing or checking final identity files.
- `references/CONTROLLED_IDENTITY_REVISION.md` — baseline locking, cumulative acceptance, exact vs approximate editing and delta verification; read when modifying an already accepted identity asset.
