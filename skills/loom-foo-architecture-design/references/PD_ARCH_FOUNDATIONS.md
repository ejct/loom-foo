# Arch Foundations — conditional methodology

> Applies only when the owning `SKILL.md` conditional index selects it. Moved from the v0.29.0 root. References mentioned as `references/X.md` inside quoted historical text are relative to the *owning skill directory*, not this file. General L1 authority and current use-first instructions prevail over superseded historical clauses.

## Critical contract — read first

- **Goal fidelity:** Preserve the owner's real result, required actors, source identity, constraints and scope. Do not treat an intermediate result as completion unless it is the exact outcome the user requested and meets its acceptance criteria.
- **Authority and verification:** Tool access cannot grant new action authority. Keep evidence proportional to the actual claim and honor the scope, refusal, resource and acceptance boundaries detailed below. Load conditional references when their trigger applies.

Produce the smallest coherent architecture that satisfies the actual system forces, not a preferred pattern.

This skill owns architecture creation and change. It may perform bounded adversarial self-review and may use `loom-foo-architecture-review` as a stronger evaluator when the runtime genuinely supports it, but it must remain fully usable without cross-skill invocation.
## Durable documentation format and provenance

When the outcome is a **durable text-first document**, prefer real Markdown (`.md`) if the project's current conventions and the available authoring surface support it. Preserve the project-native destination and controlling source; an explicit format request, pinned/project policy, or a material need for rich layout, native comments, collaborative controls, or structured data overrides this preference. Do not create a file merely because the workflow produced an answer. Existing native documents stay native unless a separately authorized migration has a material benefit. Exports are derived copies, not automatic replacement authorities.

For substantive new or revised durable artifacts, record the artifact's own version/date where appropriate and the **actually loaded contributing skill IDs and versions** (or `unexposed` when unknowable). Distinguish execution from reference consultation; never fabricate historical skill provenance. Prefer short YAML frontmatter in raw Markdown or a compact native-format provenance note. Keep source IDs/links, substantive headings and semantic status intact. Materialization and status/canon transitions remain separate authorized operations.
## 1. Determine mode

Use the narrowest mode matching the requested artifact:

- **GREENFIELD** — create architecture where none meaningfully exists.
- **EVOLUTION** — change an existing architecture for a new pressure, requirement, failure, or evidence.
- **COMPARISON** — compare supplied/generated candidates and recommend/select.

If the user only wants findings/audit/readiness/conformance without redesign, route to `loom-foo-architecture-review` when available.

For mixed "review and redesign" requests, this skill is primary because the requested output includes a changed architecture.
## Authority and side-effect boundary

An architecture-design request authorizes analysis and production/refinement of an architecture artifact. It does **not** by itself:

- accept that architecture as canonical project architecture;
- supersede accepted project decisions;
- modify canonical documentation, source code, configuration, schemas, or infrastructure;
- commit, merge, deploy, migrate, release, or otherwise implement the design.

A candidate may be `SELECTED_FOR_REFINEMENT` inside this workflow without being accepted by project authority.

Perform persistence or implementation only when separately authorized.
## 2. Establish the Architecture Design Charter

Build compact working state:

- system intent and desired outcomes;
- scope and non-goals;
- hard constraints and accepted decisions;
- surrounding ecosystem/integration constraints;
- architecture drivers;
- critical invariants;
- workload assumptions/growth axes;
- semantic domains, units, clocks/timebases or reference frames when they can change behavior;
- critical flows;
- evidence/current project authority;
- material assumptions/unknowns;
- validation criteria.

Do not expose the charter as ceremony unless materially useful.

Do not ask for clarification when a bounded assumption allows useful progress. Mark it and continue. Escalate only when missing input can materially change the architecture and cannot be inferred responsibly.
## 3. Resolve current architecture truth for EVOLUTION

Distinguish intended architecture, observed implementation/runtime behavior, accepted temporary deviations, stale documentation, and unresolved ambiguity.

Use current project authority and current implementation evidence when available.
## 4. Local architecture delta gate

Before opening a design space in EVOLUTION ask:

1. What pressure triggered the work?
2. What does the current architecture already provide?
3. What exact architecture-local gap remains?
4. Is an architectural delta actually required?

If no material gap remains, return `NO_ARCHITECTURE_DELTA`. Do not manufacture a new service, layer, registry, framework, or migration task.

If the no-delta conclusion is well-supported and no material uncertainty remains, close the design run as `CONVERGED` with a no-change disposition. If whether a delta exists depends on empirical evidence, use `VALIDATION_REQUIRED`.
## 5. Drivers before patterns

Derive only drivers that materially shape architecture: correctness, availability, latency, throughput, consistency, security/privacy, modifiability, evolvability, operability, portability, cost, locality/offline behavior, regulatory/hardware constraints, etc.

Do not optimize for a driver without evidence that it matters.

Use generic quality frameworks as vocabulary/coverage aids, not a scorecard.
## 6. Make critical claims scenario-shaped

When useful, convert material quality claims into:

`source -> stimulus -> environment -> artifact -> response -> response measure`

Prefer falsifiable behavior over adjectives like "scalable" or "robust".

**Claim Challenge for load-bearing assumptions.** For a consequential assumption that could invalidate the selected architecture, identify its exact claim/scope and a counterexample, boundary scenario or alternative explanation capable of changing the decision. Use the cheapest available trustworthy probe, independent source or negative test if authorized. Verify apparent contradictions against the actual claim and test oracle; unsupported assumptions and refuted assumptions are different. Keep this local to architecture design; no dedicated falsification phase, generic evidence plan or reviewer panel is required. If no credible test is available, bound the uncertainty without manufacturing a pass.
