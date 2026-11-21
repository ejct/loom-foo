# Proposal Scope — conditional methodology

> Applies only when the owning `SKILL.md` conditional index selects it. Moved from the v0.29.0 root. References mentioned as `references/X.md` inside quoted historical text are relative to the *owning skill directory*, not this file. General L1 authority and current use-first instructions prevail over superseded historical clauses.

## Critical contract — read first

- **Goal fidelity:** Do not make proof of value a gate before the requested useful proposal. Preserve the owner's real result, required actors, source identity, constraints and scope. Do not treat an intermediate result as completion unless it is the exact outcome the user requested and meets its acceptance criteria.
- **Authority and verification:** Tool access cannot grant new action authority. Keep evidence proportional to the actual claim and honor the scope, refusal, resource and acceptance boundaries detailed below. Load conditional references when their trigger applies.

Treat a proposal request as a request for an actionable, appropriately scrutinized artifact. Deliver the useful proposal without making auditing a separate project.

A strong run has two distinct responsibilities:

1. **construct a strong proposal before auditing it**;
2. **adversarially refine that proposal until a justified terminal state**.

Do not use the audit loop as a substitute for basic proposal construction quality.

Complete the appropriate level of construction and checking in one episode. One focused challenge is usually enough; repeat only for an unresolved material finding or changed premise. Do not require review rounds, formal freezes, or a test campaign as routine completion prerequisites.
## Durable documentation format and provenance

When the outcome is a **durable text-first document**, prefer real Markdown (`.md`) if the project's current conventions and the available authoring surface support it. Preserve the project-native destination and controlling source; an explicit format request, pinned/project policy, or a material need for rich layout, native comments, collaborative controls, or structured data overrides this preference. Do not create a file merely because the workflow produced an answer. Existing native documents stay native unless a separately authorized migration has a material benefit. Exports are derived copies, not automatic replacement authorities.

For substantive new or revised durable artifacts, record the artifact's own version/date where appropriate and the **actually loaded contributing skill IDs and versions** (or `unexposed` when unknowable). Distinguish execution from reference consultation; never fabricate historical skill provenance. Prefer short YAML frontmatter in raw Markdown or a compact native-format provenance note. Keep source IDs/links, substantive headings and semantic status intact. Materialization and status/canon transitions remain separate authorized operations.
## 1. Determine mode

Default to **proportionate**: answer a bounded proposal directly with a brief construction check and, where warranted, one targeted claim challenge. Use **deep** only for consequential, ambiguous, long-lived, high-cost or explicitly audit-heavy decisions. Honor quick/rough/no-audit requests; perform only required correctness, evidence and safety checks, without covertly adding an audit. Do not treat proposal drafting as a request for independent validation or benchmarks.

This skill is specifically for project proposals. Do not silently generalize its lifecycle or convergence rules to PRDs, architecture decisions, migration plans, research syntheses, or other artifact classes unless the current task explicitly treats them as the proposal subject.
## 2. Reconstruct the Proposal Charter

Before proposing a solution, establish a compact working charter containing:

- **problem** — the condition that should change;
- **desired outcome** — what success means;
- **scope** — what the proposal is responsible for;
- **non-goals** — nearby problems deliberately excluded;
- **hard constraints** — constraints the proposal may not silently violate;
- **accepted decisions** — existing decisions treated as fixed unless explicitly reopened;
- **material assumptions** — claims that affect the design but are not established;
- **evidence** — relevant project evidence and externally verified facts;
- **open uncertainties** — unknowns that could change the proposal;
- **validation criteria** — observable conditions that could later show the proposal works or fails.

The Proposal Charter is working state, not a mandatory user-facing preamble. Do not dump the charter or a checklist before the proposal unless the user asks for it or a material blocker/assumption must be surfaced. Carry decision-relevant content into the proposal itself.

When project sources exist, resolve current authority/state before relying on old proposals, archived material, or remembered context. Load only sources that could materially change the charter, proposal, audit, or authority interpretation; do not retrieve the whole project just in case.

Do not ask for clarification when a bounded working assumption allows useful progress. State the assumption and continue. Escalate only when the missing input materially changes the decision and cannot be inferred responsibly.

If a later audit shows that the problem framing itself is wrong, revise the charter explicitly and re-evaluate the proposal against the revised charter.

### Goal Fidelity gate (owner objective before proof)

Before freezing a project proposal or setting its milestones, restate the actual owner-desired capability, experience or functional outcome. Inspect whether the proposed plan silently substitutes a secondary goal such as proving comparative usefulness, producing benchmark evidence, completing audits or obtaining methodological validation. If the user asks to build/improve a personal tool, prioritize the tool and proportionate correctness/functional feedback; do not require comparative superiority evidence absent an explicit request or a specific consequential decision that depends on it.

`UNVERIFIED`, `VALIDATION_REQUIRED` and evidence gaps are epistemic descriptions, not automatic stop gates, priority changes or new research tasks. Before including any proof/benchmark/validation stage, require a concrete link to the owner's objective, material risk, correctness or live choice, and prefer the smallest direct check. Keep three check types separate: (1) operation correctness/safety, (2) normal functional feedback/dogfood, (3) comparative or confirmatory validation. Never waive mandatory integrity, safety, authority or source-fidelity checks.

Regression principle: planning functional development must produce a usable roadmap without imposing comparative proof experiments. A distinct explicit request to prove an advantage legitimately routes to research-design. Cite the accepted LoomLoom Agent Operating Behavior GOAL FIDELITY amendment dated 2026-10-11. This is a composition guard, not an extra proposal artifact or audit round.
## 3. Preserve authority and side-effect boundaries

A request to create or refine a proposal authorizes analysis and production of the proposal artifact. It does **not** by itself authorize:

- accepting the proposal as a project decision;
- modifying canonical project documentation or source code;
- changing project state or configuration;
- committing, merging, publishing, deploying, releasing, or promoting anything;
- reopening an accepted decision unless the proposal explicitly argues for that reconsideration.

Perform persistence or implementation only when the user has separately authorized that action or the governing project authority already permits it. Keep proposal status distinct from accepted/implemented/released status.

Audit and adjudication can recommend an authority transition but cannot manufacture one.

### Skill lifecycle simplification

When proposing updates to reusable Agent Skills, do not impose `candidate`/promotion status as an additional maturity workflow. Distinguish the active version installed in each runtime, ordinary source revision, immutable historical evaluation subjects and separately authorized publication/release. Require evidence and review proportional to consequences; do not recommend a new registry or migration campaign without a demonstrated gap. A skill stored in Drive or GitHub is not necessarily installed or discoverable in a target runtime.
## 4. Apply the evidence gate

Classify material claims as one of:

- established by current project authority/evidence;
- externally verifiable;
- empirically testable;
- working assumption;
- currently unresolved.

Verify current, technical, market, legal, standards, product, competitive, or other externally consequential claims when practical and when they could materially affect the proposal.

Never convert a missing fact into an invented fact to keep the workflow moving.

If the dominant uncertainty can no longer be resolved by reasoning and requires a prototype, benchmark, user research, implementation probe, security review, or another real-world test, still construct the strongest bounded proposal supported by current evidence. Then stop further theoretical refinement with `VALIDATION_REQUIRED`, naming the smallest useful validation step and what result would change the decision. Do not mistake an empirical boundary for permission to omit the proposal artifact.
