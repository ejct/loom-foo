---
name: loom-foo-design-systems
description: "Architect, audit or evolve design tokens, components, semantics and governance across a system. Not a single screen/component build."
metadata:
  family: "design"
  version: "0.6.0"
  project: "loom-foo"
compatibility: "Agent Skills-compatible design-system reasoning; Figma, code repositories and token converters are optional tool-bound specialists."
---

<!-- loom-foo Answer Receipt v0.3: shared response provenance and Process Trail projection -->
**Answer Receipt.** When this skill is directly consulted or materially applied in preparing a user-facing answer, include a compact **Answer Receipt** as the final section. List only actually used/consulted skills (including external skills when evidenced), exact versions if known, `SKILL.md` delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered reference coverage, actual sources, checks, actions and material limitations. `FULL` requires model-visible contiguous delivery of the exact source through EOF, not a reader success flag. **Process Trail:** for substantive multi-stage work, including repeated proposal/task reviews, corrections, verifications or genuine cross-agent/artifact handoffs, show an ordered breadcrumb sequence such as `DRAFT1 → REVIEW1 → REVISE1 → REVIEW2 → READY`, with a brief result, exact artifact identity when established, and provenance for consequential stages. Preserve distinct repeated passes in their original order; do not invent unseen stages, file revisions, handoffs, independence or runtime events. Different consulted skills in the same agent context are not separate agent executions. An internally reconstructed review is `MODEL_REPORTED`, not independently verified. Keep one footer, not a second Processing Receipt. No new tests or logging merely for the footer. Follow `docs/ANSWER_RECEIPT_V0.3.md` when accessible; this clause works standalone. Preserve JSON-only, machine payload, code-only and strict producer handoff formats when a footer is forbidden.

# Design Systems — system-level design architecture


**Conditional project-knowledge composition (L1).** When auditing/evolving a multi-consumer design system and accepted token definitions, migration decisions or project-wide constraints are materially missing, consult `loom-foo-knowledge-retrieval` from authorized canonical sources before proposing propagation or a breaking change. Keep source-of-truth precedence and read-only retrieval explicit; a retrieved proposal is not accepted system policy. Do not retrieve an archive for a local, source-complete component/token task. Design Systems retains ownership of the system contract and its verification.

**Conditional content-pattern collaboration (L1).** When a system-wide component or pattern contract needs reusable UI terminology, action labels, feedback/state copy or content rules that materially affect user decisions, consult `loom-foo-ux-writing` for the content contract. Design Systems retains ownership of component semantics, tokens, cross-product governance and versioning; UX Writing owns in-product wording and reusable content patterns. A local text edit or token-only change does not require either an additional owner or mandatory handoff.

## Result contract

Own the **design system as a versioned set of reusable decisions and contracts**, not merely a collection of styled UI elements. Produce the requested foundations/architecture, component specification, governance change, system audit or migration plan, with a traceable source of truth and a scoped completion condition. Keep design source, code/runtime and Figma/library state distinguishable.

## When to activate

Use for system creation/evolution, token/alias strategy, cross-platform themes, component and pattern contracts, product design-system consistency, design-to-code reconciliation, contribution/deprecation policy, or consequences of a breaking change across multiple consumers.

- Single standalone UI component, Figma variable or complete Figma library **building** from code -> existing `figma-generate-library` + `figma-use` when connected. This skill owns a *system-level design question* only when it exists.
- Product user-flow / experience decisions -> `loom-foo-experience-design`.
- Typographic craft or type scale specimen -> `loom-foo-typography`; this skill owns its systemic role/contract only.
- Brand identity definition -> `loom-foo-identity-design`; this skill may map approved brand decisions into semantic tokens.
- Standalone critique of one supplied screenshot or component **as visual/interaction design** -> `loom-foo-design-review` when available. **Read-only system-level audit** of token dependencies, alias drift, mappings, multi-consumer contracts and change impact remains Design Systems; writing is not required to make this a system task.
- Software architecture, code testing and deployment -> engineering owners; designs do not authorize mutation of codebases or published libraries.

Do not scaffold a full system when the user asks for a single component or reusable token. Prefer existing conventions and real upstream authorities.

## Work procedure

1. **Resolve target and source authority.** Identify products/platforms, consumers, existing Figma/code/docs/library versions, brand/product decisions and authority for updates. Establish whether a design system is warranted at the requested scale. Read `references/SYSTEM_FOUNDATIONS.md` for system models. Avoid declaring Figma or code canonical without evidence.
2. **Specify the stable semantics.** Distinguish primitive vs semantic vs component tokens, themes and accessibility modes, component roles and user tasks. Use meaningful names, dependency/alias graph, locale/platform semantics, responsive rules. When exchanging tokens, distinguish DTCG 2025.10 Format correctness from Resolver sets/modifiers/context resolution; map Figma variable modes explicitly instead of equating them to DTCG contexts. Do not claim conformance without testing the applicable module and format.
3. **Define component/pattern contracts.** For each requested family specify anatomy, purpose, state/variant surface, properties, constraints, interactions, accessibility, content and localization, dependencies and anti-patterns. Decide when a repeated composition is a pattern rather than a component. Read `references/COMPONENTS_AND_GOVERNANCE.md`.
4. **Map implementations and ownership.** Trace design tokens/styles to Figma variable IDs and code names when supplied, record divergences, design intent and expected propagation. Use authorized native Figma/code tools to execute mutations when separately requested; this skill itself does not pretend to operate them.
5. **Assess evolution impact.** For a change, identify dependents, affected brands/modes/platforms, breaking naming/semantic changes, deprecations, fallback and migration order. Keep backward compatibility explicit; one-off fixes should not silently retheme every product.
6. **Verify within scope.** Check token graph (unresolved aliases/cycles), mode values, type correctness, component state coverage, naming, contrast and content for relevant examples, actual tool synchronization only if inspected. No claim of cross-tool parity from a written map.
7. **Deliver.** Provide the scoped design-system contract or actionable delta, affected consumer map and evidence gaps; stop rather than automatically building a full library.

## Built-in QA and authority

Use proportional consistency and dependency checks. Do not require Design Review for ordinary token edits. A published library change, Figma write, code commit or forced consumer migration requires its own authorization; review-only requests do not mutate.

## Quick routing

- “Спроєктуй систему токенів та компонентів для трьох платформ” -> Design Systems.
- “Зістав Figma і CSS, знайди drift семантичних токенів” -> Design Systems (tool-backed read if connected).
- “Створи одну кнопку у Figma із варіантами” -> native Figma specialist; do not bootstrap a system.
- “Виправ мікротипографіку в одному текстовому блоці” -> Typography.
- “Оціни красу двох кнопок” -> Design Review.
- “Перевір узгодженість alias graph і тем в CSS та Figma без редагування” -> Design Systems, focused system-level audit.

## Conditional references

- `references/SYSTEM_FOUNDATIONS.md` — tokens, modes, authority, mappings, verification.
- `references/COMPONENTS_AND_GOVERNANCE.md` — component/pattern contracts, versioning and migration.
