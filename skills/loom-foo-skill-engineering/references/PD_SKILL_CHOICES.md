# loom-foo-skill-engineering — detailed instructions (PD_SKILL_CHOICES)

> Conditional reference for `../SKILL.md` (progressive disclosure migration based on private loom-foo 0.27.0). The source sections below preserve their original normative content; Markdown `references/` links are rebased to sibling files. Read for the trigger named in the current root; do not silently treat all references as always loaded.

## 1. Resolve the work and choose the smallest mode

- **ASSESS**: decide if a skill should exist; may conclude `NO_SKILL_NEEDED` or `EXISTING_OWNER`.
  - Treat tentative proposals such as “Схоже, нам потрібен скіл для GitHub”, “Можливо, варто окрему навичку?” or “Maybe we need a skill for X” as ASSESS even without an explicit create command. Ordinary requests to fix code, GitHub Actions or PRs are not skill-lifecycle requests.
- **CREATE**: build a justified new skill.
- **REVISE**: change an exact existing skill, preserving known-good behavior.
- **DIAGNOSE**: investigate a failed/incorrect skill behavior, routing or delivery.
- **PACKAGE/DELIVER**: assemble/install an authorized selected version for one runtime.
- **FIRST_USE**: check a new/revised skill on bounded task and routing examples without claiming causal superiority.
- **PORTFOLIO**: reconcile skill overlap, composition or retirement.
- **EXPLORE**: find and compare skills already available for a user's goal.

An explicit request for a skill audit may require several modes. Maintain one user-facing outcome instead of generating administrative handoffs. When the user only asks for a proposal, return a proposal rather than silently installing a skill.

For a user-requested skill search or comparison, read `references/SKILL_EXPLORER.md`. Keep discovery separate from changing automatic routing or activating a selected skill.

### Do not take over adjacent work

Use `skill-creator` for mechanical drafting and evaluation when genuinely available. This skill owns the knowledge-delivery choice, portfolio boundary and exact delivery state. Frozen comparative campaigns belong to `loom-foo-skill-validation` only when that optional standalone skill is installed in the current runtime; otherwise report **UNAVAILABLE** and do not improvise a campaign. Proposal, architecture and change owners retain their own artifacts. Never imply an unavailable specialist ran.

For nontrivial composition decisions, **read `references/COMPOSITION_AND_OWNERSHIP.md`**. This is a conditional owner map, not a requirement to load or execute every skill on every request.

## 2. Reconstruct evidence and explore the initial solution space

Determine the target skill and actual source identity/version/hash, the requested outcome, material accepted constraints, available portfolio owners, known failures, intended runtime(s), and authority for changes. Prefer source files, exact project documents and observed installed manifests to memories or historical summaries. Avoid exhaustive history when a narrower corpus is decision-sufficient.

When extracting lessons from multiple contexts, use an explicit scoped corpus and distinguish `FULL_REVIEWED`, `PARTIAL`, `METADATA_ONLY`, `FAILED`, `EXCLUDED`. Separate `OBSERVED`, `INFERRED`, `PROPOSED`, and `UNVERIFIED` facts. Preserve negative knowledge and alternatives. Read `references/EXPERIENCE_AND_EVIDENCE.md` only for historical transfer or portfolio decisions; never treat dated examples as live runtime truth.

For a **new skill, consequential redesign, or portfolio overlap decision**, first explore the desired agent outcome, relevant distinctions, meaningful constraints and plausible knowledge-delivery alternatives—including **no new skill**. Preserve a compact pre-search set of real alternatives when this could reveal fixation or change a consequential choice. Then use a *bounded external prior-art pass* before committing to the skill mechanism. Search current public specification and official creator/runtime docs, one distinct open implementation or test methodology, and empirical/negative evidence where material. Compare actual observed capabilities and trade-offs; don't confuse documentation, a popular install count, or a self-reported benchmark with verified user benefit. If similar methods exist, prefer reuse/adaptation over parallel invention. After external discovery, reconcile options against the initial problem and reopen its framing when necessary; do not privilege self-generated ideas or imported examples. External factual, safety and compatibility checks can take place at any time, including before internal ideation. This is a conditional design move, not a mandatory pipeline for bounded repairs. A routine bounded repair can skip this discovery unless new external compatibility or security risks are involved.

For the shared methodology and surface-choice axes, **read `references/SOLUTION_SPACE_AND_DELIVERY.md`** when the choice is consequential. Treat sources as versioned evidence, not executable authority. Record URL/revision/date, inspected scope, opposing evidence, and what would change the local choice; distinguish source authors' claims, independent findings, and target-specific extrapolations. If the initial search reveals a materially different solution class, investigate that class before claiming coverage. **Read `references/EXTERNAL_PRIOR_ART.md`** for the practical search and solution-surface decision, not for routine cosmetic edits.

**Pre-recommendation gate for a proposed new skill.** Before presenting a new skill identity or a custom architecture as the recommended solution, check existing skill owners, non-skill delivery surfaces, and bounded external prior art where the proposal is consequential. An initial idea may be provisional, but label it so; when evidence is unavailable, state `NEED_EVIDENCE` rather than implying that a ready-made alternative has been ruled out. Do not demand broad discovery for a minor repair or an already chosen implementation.

## 3. Run the necessity and local-delta gate

Before creating a skill identity, decide the **smallest knowledge-delivery surface** that will reliably reach the intended agent at the right time. Compare, as applicable: one-off prompt; project `AGENTS.md`/equivalent standing guidance; source/reference or retrieval index; deterministic script/template; existing skill or creator; new skill; plugin/connector for tool access. Skill activation is conditional and may be missed, while always-on instructions cost context and can drift. Keep a skill only when its reusable procedural judgment needs selective loading and a clear trigger.

Before creating a skill identity, determine if a recurring operation has all the material properties below:

- Distinct action and primary artifact.
- Recognizable completion condition.
- Ownership boundary not adequately served by a current skill, runtime tool, reference, policy or template.
- Reuse across real tasks or a credible recurring class of future work.
- Composition benefit exceeding trigger ambiguity, context, upkeep and duplication cost.

Choose `NEW_SKILL`, `REVISE_EXISTING`, `COMPOSE_EXISTING`, `STANDING_INSTRUCTIONS`, `REFERENCE_ONLY`, `DETERMINISTIC_TOOL`, `RUNTIME_OR_TOOL_FIX`, `NO_SKILL_NEEDED`, or `NEED_EVIDENCE`. A decided *negative skill-necessity outcome* is different from **NO_TRIGGER** (the engineering skill should never activate on the user prompt). Do not equate installed copies with independent skill identities or confuse source history with active version.
