---
name: loom-foo-project-knowledge-stewardship
description: "Reconcile an accepted durable change into project-native knowledge/status sources. Not deciding acceptance, retrieval or new canon."
compatibility: Agent Skills-compatible clients. Project-native documents, repositories, Drive/workspace sources, indexes, decision logs, registries, and continuity surfaces are optional. The skill must adapt to existing project conventions rather than require a universal storage model.
metadata:
  family: "knowledge"
  project: "loom-foo"
  version: "0.5.0"
---

<!-- loom-foo Answer Receipt v0.3: compact standalone projection -->
**Answer Receipt.** Finish user-facing prose with one compact receipt naming only actually consulted/applied skills and versions, `SKILL.md` model-visible delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered L2 coverage, sources, checks, actions and limits. `FULL` requires complete contiguous exact text to EOF; a successful tool fetch alone is insufficient. Use ordered **Process Trail** for actual material review/repair/recheck stages, with artifact identity and honest `SAME_CONTEXT` versus observed separate actors. Never invent independent reviews, tests, host routing, publication or external effects. Omit the footer only for strict machine/code-only output contracts.

# Project Knowledge Stewardship

## Critical contract — read first

- **Goal fidelity:** Preserve the owner's real result, required actors, source identity, constraints and scope. Do not treat an intermediate result as completion unless it is the exact outcome the user requested and meets its acceptance criteria.
- **Authority and verification:** Tool access cannot grant new action authority. Keep evidence proportional to the actual claim and honor the scope, refusal, resource and acceptance boundaries detailed below. Load conditional references when their trigger applies.

Reconcile an **already-authorized durable knowledge transition** into the project's existing durable knowledge surfaces without creating authority, rewriting history, or inventing a new knowledge system.

Primary artifact: **Project Knowledge Delta**.

Core boundary:

`authorized durable transition -> project-native reconciliation -> Project Knowledge Delta`

## L1 — ordinary execution and L2 selection

Resolve accepted persistence authority, discover the existing native current/index/status surfaces, update only the minimum consistency set, preserve history/supersession, verify provider-specific writes, and emit the Project Knowledge Delta. No decision or passing test can create new canon authority.

**Conditional method index (read the selected file before its detailed method is needed):**

- **Multiple durable surfaces, authority conflicts, supersession or derived/current-view drift require reconciliation** → `references/PD_STEWARDSHIP_CONSISTENCY.md` (source H2 sections 8,9,10).
- **Runtime projections, evidence trails, skill-producing changes or partial/no-delta integration require specialist treatment** → `references/PD_STEWARDSHIP_INTEGRATION.md` (source H2 sections 11,12,13,14,16).
- **Consequential reconciliation needs exact dispositions, candidate regressions and completeness checks** → `references/PD_STEWARDSHIP_ASSURANCE.md` (source H2 sections 19,20).

**No-trigger:** a short, resolved ordinary case does not require all detailed references merely because this skill was selected. Existing specialist references linked inside these materials remain conditional on their original situations. A moved section does not grant new permissions or replace the owning L1 safeguards.

## Documentation representation and provenance guard

When applying an authorized durable knowledge change, preserve the established project-native source and file identity. Markdown-first is a **prospective format preference** for genuinely new text-first artifacts; never convert accepted Google Docs or historical evidence simply to conform to the preference. Choose provider-native formats where collaboration, rich structure or structured data materially justify them. A Markdown export is a derived representation until explicitly reconciled and authorized. For material new/revised durable artifacts, record the actual contributing skill identities/versions (or `unexposed` if not observable) and document version/date, without inventing historical provenance. Reconcile only navigation affected by real changes; no mandatory new registry, index or document is implied.

## 1. Routing gate

Use this skill when all are materially true:
- a durable project transition has already been accepted/authorized, or project policy already authorizes the persistence class;
- one or more project-native current/index/status/supersession/continuity surfaces may now be stale;
- the requested primary action is durable integration/reconciliation rather than creation, review, decision, handoff, or retrieval.

Do not use as primary owner when:
- the artifact is still proposed/reviewed/unaccepted -> owning proposal/design/review/decision workflow;
- the question is what evidence means -> `loom-foo-evidence-review`;
- the question is what decision to make -> `loom-foo-decision-reconciliation`;
- context must be restored/read -> bootstrap/context mechanisms;
- continuation must be transferred -> `loom-foo-handoff`;
- no durable project state is intended -> no stewardship run.

`CONVERGED`, `PASS`, `VERIFIED_WITHIN_SCOPE`, merge existence, newer timestamps, and assistant authorship do not create persistence/canonicalization authority.

## 2. Resolve the authority transition first

Before any durable mutation, establish:
- exact triggering artifact/decision/change;
- exact authority source;
- what persistence/canonicalization/integration transition is authorized;
- project-native destination/owner conventions when known.

Keep separate:
- artifact creation authority;
- acceptance/canon authority;
- persistence/update authority;
- technical capability to edit a source.

If durable mutation is not authorized, return `NEED_AUTHORITY`. When useful, identify the proposed consistency surface and exact changes for approval, but do not apply them.

## 3. Discover project-native durable surfaces

Use non-mutating discovery first. Prefer existing project mechanisms such as:
- canonical/current source map;
- documentation index;
- decision log / ADR set;
- status/overview document;
- project registry;
- PROJECT_STATE or equivalent continuity surface;
- accepted routing/instruction projection.

Do not create a new registry, knowledge graph, ADR folder, PROJECT_STATE, database, or metadata schema merely because this skill exists.

## 4. Classify surfaces before changing them

Distinguish when material:

**AUTHORITATIVE** — source whose semantic authority changes through the accepted transition.

**DERIVED CURRENT VIEW** — index, status map, overview, active registry/view, navigation, PROJECT_STATE.

**HISTORICAL / EVIDENCE** — prior proposal, decision, run, audit, evidence package, previous accepted record.

**RUNTIME PROJECTION** — memory, routing instruction, agent/runtime projection; never project canon merely because it steers a runtime.

Derived views must remain derived. Historical/evidence artifacts must not be rewritten to look as if they were produced under the new state.

## 5. Compute the minimum consistency set

Update only surfaces whose stale state could materially cause:
- wrong authority/current-version selection;
- invalid continuation;
- duplicated/conflicting implementation;
- broken navigation/discovery;
- false project status;
- wrong routing/policy/profile selection.

Do not search-and-replace every textual mention. Historical descriptions may remain historically accurate.

For detailed rules read `references/CONSISTENCY_SURFACE.md`.

## 13. No-delta fast path

Use `NO_DURABLE_DELTA` when:
- the accepted artifact is already the authoritative durable source;
- no material current/index/status/continuity surface becomes stale;
- no supersession/navigation update is required.

Do not mutate anything merely to demonstrate skill activity.

## 15. Emit Project Knowledge Delta

Read `references/PROJECT_KNOWLEDGE_DELTA_CONTRACT.md` for the full artifact contract.

Keep it small. When material include:
- triggering transition and authority basis;
- authoritative source now in force;
- surfaces changed;
- supersession/current-state changes;
- derived views updated;
- historical/provenance preserved;
- intentionally untouched historical material;
- remaining gaps/conflicts;
- disposition.

The delta references project-native truth; it does not become a competing source of truth.

## 16. Skill-local dispositions

Use one primary disposition:

### `PROJECT_KNOWLEDGE_RECONCILED`
The authorized transition is reflected across the smallest material project-native consistency set.

### `NO_DURABLE_DELTA`
No project-knowledge mutation is warranted.

### `PARTIAL_RECONCILIATION`
Useful authorized updates were applied, but known material stale surfaces remain.

### `NEED_AUTHORITY`
The durable mutation/persistence transition is not authorized.

### `NEED_CONTEXT`
A resolvable source map, target surface, supersession relation, or project convention is missing.

### `AUTHORITY_CONFLICT`
Controlling project authority is genuinely contradictory.

### `BLOCKED`
A material authorized durable surface cannot be accessed/updated and no equivalent authorized path exists.
