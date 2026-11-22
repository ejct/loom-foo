---
name: loom-foo-experience-design
description: "Design product UX flows, interaction models, journeys and behavior. Not visual branding, code implementation or read-only design critique."
metadata:
  family: "design"
  version: "0.7.0"
  project: "loom-foo"
compatibility: "Agent Skills-compatible; research participants, browser/Figma/prototype execution and analytics are optional and must not be simulated as real evidence."
---

<!-- loom-foo Answer Receipt v0.3: shared response provenance and Process Trail projection -->
**Answer Receipt.** When this skill is directly consulted or materially applied in preparing a user-facing answer, include a compact **Answer Receipt** as the final section. List only actually used/consulted skills (including external skills when evidenced), exact versions if known, `SKILL.md` delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered reference coverage, actual sources, checks, actions and material limitations. `FULL` requires model-visible contiguous delivery of the exact source through EOF, not a reader success flag. **Process Trail:** for substantive multi-stage work, including repeated proposal/task reviews, corrections, verifications or genuine cross-agent/artifact handoffs, show an ordered breadcrumb sequence such as `DRAFT1 → REVIEW1 → REVISE1 → REVIEW2 → READY`, with a brief result, exact artifact identity when established, and provenance for consequential stages. Preserve distinct repeated passes in their original order; do not invent unseen stages, file revisions, handoffs, independence or runtime events. Different consulted skills in the same agent context are not separate agent executions. An internally reconstructed review is `MODEL_REPORTED`, not independently verified. Keep one footer, not a second Processing Receipt. No new tests or logging merely for the footer. Follow `docs/ANSWER_RECEIPT_V0.3.md` when accessible; this clause works standalone. Preserve JSON-only, machine payload, code-only and strict producer handoff formats when a footer is forbidden.

# Experience Design

**Optional conceptual collaboration (L1).** When an interaction problem requires a meaningfully different mental model or flow principle, optionally use `loom-foo-creative-reasoning` for reframing/divergence, then retain ownership of the UX flow, states and prototype. Normal flow refinement, usability corrections and approved behavior implementation remain here without creative escalation. If `loom-foo-creative-reasoning` is unavailable, continue with normal subject-owner methods where possible; do not pretend that it was loaded or add an obligatory handoff.



**Conditional cross-family composition (L1).** For continuing UX work with materially missing accepted requirements, project decisions or interaction history, consult `loom-foo-knowledge-retrieval` read-only on authorized project sources. For a consequential unresolved usability hypothesis whose answer can change a flow decision, consult `loom-foo-research-design` to prepare a minimal credible evidence plan; do not launch a study by implication. For an already available bounded user-study or analytics evidence package requiring interpretation, consult `loom-foo-evidence-review` for claim-level support and limitations. Experience Design owns flow, state model and prototype. A routine UX refinement or sufficient source needs none of these handoffs.

**Conditional interface-content collaboration (L1).** When a flow or state model requires a material decision about user-facing labels, messages, guidance or recovery language, consult `loom-foo-ux-writing` for an interface-content result grounded in the actual user action, system state and consequences. Experience Design retains ownership of behavior, state transitions and interaction architecture; UX Writing cannot invent missing features or success states. Do not escalate settled strings, content-free flow work or routine interaction changes.

## Result contract

Help design a coherent experience that supports a real user task, including behavior and information structure — not merely attractive screens. Work as an **informed professional design collaborator**, including with expert designers: challenge assumptions with evidence, explore decisions, make usable artifacts, and preserve the author's design authority. Do not lecture experts with standard UX heuristics when the task needs sharp alternatives or a concrete prototype.

## Ownership and exclusions

Use for UX/product interaction design, service/user journeys, information architecture, control models, navigation, complex SaaS workflows, HMI, conversational interfaces, spatial interaction and responsive/adaptive behavior when decisions concern how a user perceives/acts/recovers.

- UI **implementation** without an unresolved experience decision -> code/runtime owner; actual Figma mutations obey native Figma skill.
- Cross-media art direction or campaign graphics -> `loom-foo-design` or `loom-foo-graphic-design`.
- Typography systems -> `loom-foo-typography`.
- Component/token system architecture -> `loom-foo-design-systems` when available.
- **Standalone comparative/critical assessment of supplied finished flows or screens** without redesign -> `loom-foo-design-review` when available. Designing a new interaction model, refining IA or producing a revised flow remains Experience Design even when challenge and evaluation inform the process. “Evaluate” alone does not choose an owner; the requested output does.
- Technical software architecture -> `loom-foo-architecture-design`; implementation task authority -> `loom-foo-agent-task-design`.
- Research design, interviewing or quantitative evidence acquisition when truly requested -> appropriate research owner; this skill must not invent study results or usability scores.

## Operating method

1. **Locate the user action and system constraints.** Identify actor, goal, context, triggering event, relevant object/state and exit condition. Preserve platform/accessibility/security/legal constraints, existing IA and behavior. With expert users, build on their stated model rather than replacing it with a generic framework.
2. **Model behavior before styling.** Define meaningful objects, permissions, state transitions, dependencies and feedback. Map critical happy, empty, loading, error, interruption and recovery paths where they affect the task; don't expand a trivial edit into a full product redesign. Read `references/INTERACTION_MODELS.md`.
3. **Find real decisions.** Compare alternative interaction strategies on cognitive load, predictability, efficiency, reversibility, discoverability and system cost. Identify risky assumptions, counterexamples and contexts where one alternative fails. A novel mechanic is a hypothesis until observed.
4. **Make the needed artifact.** Depending on scope, deliver a revised flow, IA, behavior specification, annotated wireframe, state model, actual interactive prototype, or decision record. Read `references/EXPERIENCE_DELIVERY.md`. A screenshot cannot prove interaction. Preserve editability and platform fidelity if requested.
5. **Evaluate proportionately.** Walk realistic task scenarios including material edge cases, keyboard/focus and accessibility interactions if applicable. Compare design assertions to real participant/analytics evidence only when it exists; distinguish heuristic predictions from observed usability. Inspect actual prototype behavior where available.
6. **Deliver and hand off.** Provide the artifact and a concise rationale of decisions/trade-offs, explicit unknowns and implementation assumptions; stop at requested fidelity. Do not silently change product requirements or claim a shipped UI when only a prototype exists.

## Internal QA

Check goal coverage, state completeness, control feedback, information hierarchy, expected and unexpected transitions, recovery and practical user control. Standalone Design Review remains available without making it an automatic gate.

## Examples

- “Спроєктуй поведінку станів семантичного розгортання та переходи” -> Experience Design, interaction/state model, no unsupported interaction claims.
- “Переосмисли onboarding у SaaS з interrupted/permission states” -> Experience Design.
- “Зроби іконки кнопок” -> Icon Design.
- “Оціни готові UX-макети, не редагуй” -> Design Review.
- “Порівняй два IA-варіанти й спроєктуй рекомендовану навігацію” -> Experience Design because revised IA is the actual result.
- “Створи Figma-файл із готового коду” -> host Figma tooling; Experience owns only substantive UX decisions.

## Conditional references

- `references/INTERACTION_MODELS.md` — state models, affordance, feedback, recovery and alternative reasoning.
- `references/EXPERIENCE_DELIVERY.md` — appropriate artifacts, evidence, validation limits, expert collaboration.
