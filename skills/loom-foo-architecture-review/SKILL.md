---
name: loom-foo-architecture-review
description: "Critically assess an existing software architecture through grounded scenarios and failure risks. Not architecture redesign or change verification."
compatibility: Agent Skills-compatible clients. Can use project/repository sources, connected tools, empirical probes, and separate evaluator contexts when available.
metadata:
  family: "engineering"
  project: "loom-foo"
  version: "0.5.0"
---

<!-- loom-foo Answer Receipt v0.3: compact standalone projection -->
**Answer Receipt.** Finish user-facing prose with one compact receipt naming only actually consulted/applied skills and versions, `SKILL.md` model-visible delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered L2 coverage, sources, checks, actions and limits. `FULL` requires complete contiguous exact text to EOF; a successful tool fetch alone is insufficient. Use ordered **Process Trail** for actual material review/repair/recheck stages, with artifact identity and honest `SAME_CONTEXT` versus observed separate actors. Never invent independent reviews, tests, host routing, publication or external effects. Omit the footer only for strict machine/code-only output contracts.

# Architecture Review

## Critical contract — read first

- **Goal fidelity:** Preserve the owner's real result, required actors, source identity, constraints and scope. Do not treat an intermediate result as completion unless it is the exact outcome the user requested and meets its acceptance criteria.
- **Authority and verification:** Tool access cannot grant new action authority. Keep evidence proportional to the actual claim and honor the scope, refusal, resource and acceptance boundaries detailed below. Load conditional references when their trigger applies.

Evaluate architecture as a system of decisions under forces. Do not grade diagrams, reward fashionable patterns, or redesign the system by default.

## L1 — ordinary execution and L2 selection

Inspect the actual architecture and the authority for its claims; choose a bounded review mode, compare one or a few relevant operating/failure scenarios, distinguish evidence from inference, and return findings plus genuine non-risks. Review findings are proposals to address defects, not authority to redesign or accept architecture.

**Conditional method index (read the selected file before its detailed method is needed):**

- **A consequential review needs adversarial framing, adaptive lenses, scenario/decision analysis, failure walks or specialist lenses** → `references/PD_REVIEW_SCENARIOS.md` (source H2 sections 7,8,9,10,11,12).
- **Material findings, redesign trade-offs, empirical uncertainty, implementation conformance or reviewer independence need detailed handling** → `references/PD_REVIEW_FINDINGS.md` (source H2 sections 13,14,15,16,17,18,19).

**No-trigger:** a short, resolved ordinary case does not require all detailed references merely because this skill was selected. Existing specialist references linked inside these materials remain conditional on their original situations. A moved section does not grant new permissions or replace the owning L1 safeguards.

## 1. Determine mode

Choose the narrowest applicable mode:

- **DESIGN_REVIEW** — evaluate a frozen proposed architecture.
- **IMPLEMENTATION_REVIEW** — compare intended architecture with observed implementation/runtime/config/deployment.
- **CHANGE_REVIEW** — evaluate a bounded architecture delta against affected invariants/scenarios.
- **READINESS_REVIEW** — evaluate architecture before launch/scale/major operational transition.

If the user wants a new or changed architecture, route to `loom-foo-architecture-design` when available.

For mixed "review and redesign" requests, design is primary because the output includes changed architecture.

## Authority and side-effect boundary

A review request authorizes evaluation and production of review findings. It does **not** by itself authorize:

- accepting or rejecting the architecture as a project decision;
- changing canonical architecture documentation;
- modifying source code, configuration, schemas, infrastructure, or deployment state;
- applying remediation.

Perform mutations only under separate explicit authority.

## 2. Establish Review Charter

Capture working state:
- mode;
- scope/exclusions;
- system intent;
- hard constraints;
- declared drivers;
- critical invariants;
- workload assumptions;
- critical flows;
- accepted decisions;
- evidence sources;
- known unknowns;
- review depth.

## 3. Architecture is not its description

A weak/missing diagram or stale document is not proof of weak architecture.

When evidence allows, reconstruct a sufficient architecture model from current decisions/docs, code, schemas, tests, configuration, deployment, runtime evidence, interfaces, traces/logs/metrics.

Record documentation/evidence gaps separately from architecture defects.

## 4. Evidence semantics

Classify material inputs:

- `AUTHORITATIVE` — accepted project decision/governing contract;
- `OBSERVED` — current implementation/runtime fact;
- `INFERRED` — conclusion reasoned from evidence;
- `ASSUMED` — working assumption;
- `UNKNOWN` — unresolved.

Authority and observation are independent.

Do not issue high-severity conclusions from weak evidence without lowering confidence or requesting validation.

## 18. Closure

Choose one:

### `COMPLETE`
Requested review scope completed; findings/evidence gaps reported. Does not mean "architecture approved."

### `VALIDATION_REQUIRED`
A material conclusion requires empirical evidence.

### `BLOCKED`
Scope/evidence/authority is insufficient for a defensible review.

Return:
- mode/scope;
- evidence coverage;
- Critical/Major findings;
- relevant Moderate findings;
- non-risks;
- sensitivity/trade-offs;
- evidence gaps;
- validation requirements;
- fitness-function candidates;
- next actions.

Do not redesign unless the requested artifact changes.
