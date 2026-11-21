---
name: loom-foo-work-decomposition
description: "Split accepted multi-unit work into coherent Work Units with real gates. Not one executable Task Brief or unaccepted proposals."
compatibility: Agent Skills-compatible clients. Can consume accepted specifications, architectures, research plans, decisions, review findings, and project constraints from inline or connected sources.
metadata:
  family: "planning"
  project: "loom-foo"
  version: "0.5.0"
---

<!-- loom-foo Answer Receipt v0.3: compact standalone projection -->
**Answer Receipt.** Finish user-facing prose with one compact receipt naming only actually consulted/applied skills and versions, `SKILL.md` model-visible delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered L2 coverage, sources, checks, actions and limits. `FULL` requires complete contiguous exact text to EOF; a successful tool fetch alone is insufficient. Use ordered **Process Trail** for actual material review/repair/recheck stages, with artifact identity and honest `SAME_CONTEXT` versus observed separate actors. Never invent independent reviews, tests, host routing, publication or external effects. Omit the footer only for strict machine/code-only output contracts.

# Work Decomposition

## Critical contract — read first

- **Goal fidelity:** Preserve the owner's real result, required actors, source identity, constraints and scope. Do not treat an intermediate result as completion unless it is the exact outcome the user requested and meets its acceptance criteria.
- **Authority and verification:** Tool access cannot grant new action authority. Keep evidence proportional to the actual claim and honor the scope, refusal, resource and acceptance boundaries detailed below. Load conditional references when their trigger applies.

Transform accepted many-unit work into a bounded **Work Plan** containing coherent **Work Units** and material dependencies/gates.

Core boundary:

`accepted multi-unit work -> Work Plan / Work Unit Set -> agent-task-design per executable unit`

## L1 — ordinary execution and L2 selection

Split only accepted many-unit scope when outcomes or authority/acceptance boundaries truly differ; prefer the fewest coherent Work Units, represent genuine dependencies and integration gates, preserve Goal Fidelity, then pass each bounded unit to Agent Task Design. A gate or open research question is not automatically an executable task.

**Conditional method index (read the selected file before its detailed method is needed):**

- **The accepted scope has multiple executors, independent gates, dependencies, plan-level integration or justified probe units** → `references/PD_UNIT_STRUCTURE.md` (source H2 sections 8,9,10,12).
- **An execution episode spans multiple accepted units or a substantial Work Plan requires detailed artifact-level closure** → `references/PD_UNIT_EXECUTION.md` (source H2 sections 13,14).

**No-trigger:** a short, resolved ordinary case does not require all detailed references merely because this skill was selected. Existing specialist references linked inside these materials remain conditional on their original situations. A moved section does not grant new permissions or replace the owning L1 safeguards.

## 1. Routing gate

Use this skill when the accepted work materially depends on multiple independently acceptable work units, prerequisites, sequencing gates, parallel branches, different owners/executors, or incompatible authority envelopes.

Do **not** use as primary owner for:
- one coherent executable task -> `loom-foo-agent-task-design`;
- proposal formation -> `loom-foo-proposal-refinement`;
- specification work -> `loom-foo-specification-design`;
- architecture creation/comparison -> `loom-foo-architecture-design`;
- research/evidence-method design -> `loom-foo-research-design`;
- live task dispatch/scheduling/monitoring -> runtime/project-management layer.

## 2. Single-task gate

Before decomposing, test whether the work is already one coherent executable unit.

A coherent unit normally has:
- one primary observable outcome;
- one coherent subject/base;
- one compatible authority envelope;
- acceptance criteria evaluable together;
- one meaningful stop boundary.

If yes, return `SINGLE_TASK` and route directly to `loom-foo-agent-task-design`. Do not create a ceremonial one-node plan.

## 3. Resolve controlling accepted sources

Plan from current accepted authority, not from superseded proposals or remembered intent.

Resolve only the sources that materially govern:
- target outcome/scope;
- specification/architecture/research semantics;
- hard constraints/invariants;
- current accepted decisions;
- authority boundaries;
- known blockers/gates.

If a material upstream design/decision is unresolved, do not silently solve it during decomposition.

### Goal Fidelity and non-task status of open questions

Preserve the user-authorized primary outcome when decomposing accepted work. An `OPEN QUESTION`, `VALIDATION_REQUIRED`, missing benchmark, evidence gap or proposal research suggestion is not an accepted Work Unit or execution gate. Introduce research/validation units only when explicitly commissioned or when their result is necessary for an actual impending choice, correctness, safety or authority boundary. Otherwise retain them as optional notes, not blocking dependencies. Do not promote 'prove this instrument works' into a prerequisite when the accepted outcome is 'improve the instrument'.

Distinguish (1) scoped engineering correctness/integrity checks included within their owning unit, (2) lightweight functional feedback during implementation, and (3) comparative outcome studies requiring their own objective. Preserve all material security, data-integrity and irreversible-action gates. When splitting would create proof phases instead of productive work, prefer the coherent functional unit. Regression principle: development planning preserves the owner's functional priorities; optional comparative benchmarking stays deferred unless independently requested or authorized.

## 4. Coherence-first split

Split only when a real boundary exists, such as:
- outcomes can be accepted/rejected independently;
- prerequisites/gates differ;
- work can proceed in parallel without hidden coupling;
- authority envelopes differ;
- natural owners/executors differ;
- verification/acceptance boundaries differ materially;
- one combined task would have multiple independent stop conditions;
- sequencing prevents invalid/wasted downstream work.

Do not split tightly coupled mechanics merely to increase task count.

Read `references/UNIT_BOUNDARIES.md` for consequential decomposition.

## 5. Prefer the minimum sufficient unit set

The goal is not maximum granularity.

Prefer the fewest units that:
- preserve semantic coherence;
- expose real dependencies/gates;
- permit independent acceptance where useful;
- prevent mega-task scope drift;
- are bounded enough for downstream Task Brief compilation.

If two units must always change, verify, and accept together, keep them together unless another real boundary applies.

## 6. Define work units at planning resolution

A Work Unit should make recoverable when material:
- unit outcome;
- bounded subject/scope;
- acceptance boundary;
- materially distinct authority boundary;
- prerequisites/dependencies;
- produced artifact/result used downstream;
- natural next owner/executor class when useful.

Do **not** normally include:
- full Task Brief;
- runtime-specific prompt;
- shell/tool-call order;
- implementation micro-steps;
- agent/model assignment;
- dates/story points/estimates.

`loom-foo-agent-task-design` owns the executable Task Brief.

## 10. Preserve upstream ownership

Do not silently change:
- requirements;
- architecture;
- product decisions;
- evidence/research method;
- accepted claim limits;
- authority semantics.

If decomposition requires such a change, return `UPSTREAM_DECISION_REQUIRED` and name the appropriate owner (`loom-foo-decision-reconciliation`, `loom-foo-specification-design`, `loom-foo-architecture-design`, `loom-foo-research-design`, etc.).

## 14. Skill-local dispositions

Use the narrowest applicable state:

- `WORK_PLAN_READY` — accepted multi-unit work is covered by coherent units with sufficient dependency/gate semantics for downstream task compilation.
- `SINGLE_TASK` — no decomposition artifact is warranted; route directly to `loom-foo-agent-task-design`.
- `UPSTREAM_DECISION_REQUIRED` — a material product/specification/architecture/research decision must be resolved first.
- `NEED_CONTEXT` — a resolvable scope/subject/dependency/authority input is missing.
- `BLOCKED` — controlling source/authority state is inaccessible or materially contradictory enough that no reliable plan can be produced.

## 15. Final checks

Before returning:
- current accepted sources were used;
- no hidden redesign occurred;
- plan uses the minimum sufficient unit set;
- SINGLE_TASK was used when appropriate;
- gates were not fabricated into tasks;
- dependencies have real semantics;
- integration points are visible where needed;
- no Task Brief/runtime/orchestration details leaked in unnecessarily;
- each executable unit is bounded enough for agent-task-design;
- no project-management mutation or execution occurred without separate authority.
