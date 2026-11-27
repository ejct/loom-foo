---
name: loom-foo-evidence-acquisition
description: "Execute a bounded evidence plan, preserving source fidelity, raw results and provenance. Not research-method design or evidence interpretation."
compatibility: Agent Skills-compatible clients. Web/search tools, project sources, code/browser/device runtimes, experiment harnesses, connected apps, and specialist executors are optional. The skill remains runtime-neutral and must represent unavailable capabilities rather than invent results.
metadata:
  family: "research"
  project: "loom-foo"
  version: "0.8.0"
---

<!-- loom-foo Answer Receipt v0.3: compact standalone projection -->
**Answer Receipt.** Finish user-facing prose with one compact receipt naming only actually consulted/applied skills and versions, `SKILL.md` model-visible delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered L2 coverage, sources, checks, actions and limits. `FULL` requires complete contiguous exact text to EOF; a successful tool fetch alone is insufficient. Use ordered **Process Trail** for actual material review/repair/recheck stages, with artifact identity and honest `SAME_CONTEXT` versus observed separate actors. Never invent independent reviews, tests, host routing, publication or external effects. Omit the footer only for strict machine/code-only output contracts.

# Evidence Acquisition

## Critical contract — read first

- **Goal fidelity:** Preserve the owner's real result, required actors, source identity, constraints and scope. Do not treat an intermediate result as completion unless it is the exact outcome the user requested and meets its acceptance criteria.
- **Authority and verification:** Tool access cannot grant new action authority. Keep evidence proportional to the actual claim and honor the scope, refusal, resource and acceptance boundaries detailed below. Load conditional references when their trigger applies.

Execute a bounded evidence-acquisition contract faithfully and return the evidence in a form that a later reviewer can inspect without reconstructing the run from chat or tool history.

The primary artifact is the **Evidence Package**.

Core boundary:

**Research design decides what evidence should be acquired and how. Evidence acquisition executes that contract and records what actually happened. Evidence review decides what the resulting evidence means.**

## L1 — ordinary execution and L2 selection

Execute the exact current acquisition contract under independently checked action authority, preserve raw/recoverable results and source identity, distinguish valid zero from failure, and report gaps and deviations without interpreting the underlying claim. A ready package is not sufficient evidence for a decision.

**Conditional method index (read the selected file before its detailed method is needed):**

- **Multiple planned items, transformed/raw lineage, reproducibility, provenance or substantial package integrity require detailed handling** → `references/PD_ACQUISITION_PROVENANCE.md` (source H2 sections 6,10,11,12,13).
- **Retry, source substitution, missing natural executor or capability failure may change what the evidence means** → `references/PD_ACQUISITION_RECOVERY.md` (source H2 sections 9,15).
- **A multi-party handoff, candidate test, special output or consequential completion requires detailed downstream disposition** → `references/PD_ACQUISITION_OUTPUT.md` (source H2 sections 18,19,20).

**No-trigger:** a short, resolved ordinary case does not require all detailed references merely because this skill was selected. Existing specialist references linked inside these materials remain conditional on their original situations. A moved section does not grant new permissions or replace the owning L1 safeguards.

**Conditional cross-language composition (L1).** If an already authorized acquired source passage is necessary for the evidence plan and must be rendered into the working language to be usable, consult `loom-foo-translation` on the exact readable passage, source locator/edition, language and context. Preserve the original/transcription and translated derivative separately, with provenance, translator/method when known, coverage and uncertainties; acquisition remains owner of the Evidence Package. Ordinary reading or collection of usable foreign-language evidence needs no full translation. If acquisition is itself answering a Translation/Analysis request for attestation or a source, return the actual source and locator rather than re-entering the same translation question. If specialist or readable source is unavailable, mark the translation gap and continue only with independently usable evidence. Do not exceed access, disclosure or plan authority.

## 1. Routing gate

Use `loom-foo-evidence-acquisition` when:

- a current Evidence Plan or equivalent bounded acquisition protocol already exists;
- the primary output is acquired evidence plus enough provenance and execution state for downstream review;
- the task involves material acquisition work rather than incidental citation gathering.

Typical triggers include:

- "execute this Evidence Plan";
- "collect the evidence specified by this protocol";
- "run these planned probes and package the results";
- "retrieve/measure/inspect these sources exactly as planned";
- "gather this evidence with provenance and report any gaps or deviations."

Do not use this skill as the primary owner when:

- the evidence method, comparator, population, oracle, or stopping rule still needs design -> `loom-foo-research-design`;
- the user wants interpretation/synthesis of already-collected evidence -> `loom-foo-evidence-review` when available;
- the primary output is one executable implementation/change task -> `loom-foo-agent-task-design`;
- the request is ordinary factual Q&A or a casual lookup with no durable acquisition contract;
- the task is a domain-specific acquisition workflow that already has a stronger owner and no generic package handoff is needed.

A domain-specific acquisition skill may execute the collection while this skill's Evidence Package contract is used only where useful. Do not create recursive ownership.

## 2. Preserve plan, project, and action authority

An Evidence Plan describes intended evidence acquisition. It does not automatically authorize every action named in it.

Keep separate:

- **method authority** — what the controlling Evidence Plan requires;
- **project/action authority** — what the current user/project permits;
- **runtime capability** — what the current execution environment can actually do.

Do not infer permission from capability or from the existence of a plan.

External outreach, participant recruitment, spending, production experiments, private-source access, destructive actions, credential use, disclosure, publication, or other consequential side effects require their own authority.

If a material action is not authorized, preserve the blocked acquisition item instead of silently substituting easier evidence.

## 3. Resolve the controlling acquisition contract

Identify the current Evidence Plan/version or an explicit bounded acquisition contract.

It should be sufficiently clear about the material dimensions needed for execution, such as:

- decision/uncertainty or evidence objective;
- exact subject/population/case set when material;
- requested evidence;
- method/source family;
- comparator/control when applicable;
- measure/oracle when applicable;
- selection/exclusion rules when applicable;
- environment when it changes the claim;
- stop/adaptation rules;
- claim limits.

Do not redesign the method merely to make the acquisition executable.

If method choice is materially unresolved, route to `loom-foo-research-design`.

If the plan conflicts with a newer controlling constraint or references a materially different/stale subject, surface the conflict. A locator repair to the same exact subject is an execution-binding issue; a changed subject or method is not.

## 4. Preflight subject, access, capability, and authority

Before material acquisition, establish only the prerequisites needed by the plan.

Distinguish:

- subject identified but not located/bound in this runtime;
- subject located but inaccessible;
- capability unavailable;
- action possible but not authorized;
- state unknown;
- plan itself materially incomplete or stale.

Use non-mutating discovery before asking for information that can reasonably be resolved from authorized sources.

Do not run a general capability census.

## 6. Execute with proportional fidelity

Use the cheapest authorized mechanism that satisfies the evidence property defined by the plan.

Where material, preserve:

- exact source/subject identity;
- relevant revision/version/time window;
- environment;
- acquisition method/tool and material configuration;
- request/query/input actually used;
- returned raw result or a durable/recoverable pointer;
- failures and retries that change completeness or reproducibility.

Do not force runtime-specific mechanics into the portable skill.

For detailed fidelity rules, read `references/ACQUISITION_FIDELITY.md`.

## 7. Preserve acquisition outcome semantics

Do not collapse all empty or unsuccessful-looking results into one state.

When relevant distinguish:

- `ACQUIRED` — requested evidence was obtained;
- `COMPLETE_ZERO` — acquisition completed correctly and found no matching evidence;
- `PARTIAL` — only part of the planned evidence was obtained;
- `ACCESS_BLOCKED` / `UNAVAILABLE` — target evidence could not currently be accessed;
- `FAILED` — acquisition action failed technically;
- `NOT_RUN` — planned acquisition was not attempted;
- `EXCLUDED` — the plan deliberately excluded it;
- `SUBSTITUTED` — planned source/method was replaced.

These are semantic distinctions, not mandatory universal schema enums.

Critical invariant:

`COMPLETE_ZERO != FAILED`.

A valid zero result may be important evidence.

## Conditional coverage and execution continuity

For material multi-item or interrupted acquisition, preserve planned obligation identity and actual source/version/segment, method/fidelity, inspected vs remaining extent, outcome and evidence locator. A search hit, metadata read, failed access or plan is not completed inspection. Count valid complete-zero only for its actually checked scope; do not double-count overlap or mix unit kinds. Keep new material leads as candidates for reconciliation, not authority to expand the plan. While authorized actionable items remain, continue within the current execution episode instead of stopping for a progress report; prioritize neglected or partially checked items when useful, avoid duplicate attempts unless a changed method/subject justifies them. On genuine interruption or blocker return recoverable remaining items, reasons and next actions through the existing Evidence Package; separate execution completion, acquisition coverage and claim sufficiency. Do not invent background execution or a new registry; preserve the fast path.

**Conditional inspected-evidence binding.** For a consequential source-derived observation or coverage claim, record the actual inspected source segment or a recoverable pointer that resolves to that segment and its material revision/representation. Verify that the recorded observation is supported by the delivered content, not merely a URL, citation identifier, retrieval success, preview, metadata or model-authored summary. If the exact support cannot be recovered, narrow the evidence state and mark the affected obligation unresolved; never reconstruct a missing source span or treat the label `ACQUIRED` as proof. Preserve privacy and copyright through a minimal authorized excerpt or stable locator rather than unnecessary full capture.

## 13. Keep package readiness separate from evidence sufficiency

`EVIDENCE_PACKAGE_READY` means the acquisition contract reached its required execution boundary.

It does **not** mean:

- the hypothesis was supported;
- the proposal should be accepted;
- the evidence is high quality;
- contradictions were resolved;
- the decision is ready;
- a positive/negative verdict exists.

An Evidence Package can be fully ready even when the acquired evidence contradicts the expected hypothesis.

## 15. Proportional fast path

For one low-risk direct source check, a sufficient package may be only:

- controlling question/plan pointer;
- exact source/version/date;
- observed result or source pointer;
- acquisition outcome;
- one material limitation if any.

Do not manufacture attempt tables, trace exports, provenance graphs, registries, or multiple artifacts for a trivial check.

Expand structure only when it protects completeness, reproducibility, cost, authority, safety, or reviewability.

## 16. Skill-local dispositions

Use exactly one primary disposition.

### `EVIDENCE_PACKAGE_READY`

The controlling acquisition contract has been executed to its required acquisition boundary, including valid `COMPLETE_ZERO` results.

### `PARTIAL_EVIDENCE_PACKAGE`

Useful attributable evidence exists, but material planned acquisition remains incomplete. State the missing items and claim/execution limits.

### `PLAN_REVISION_REQUIRED`

Credible continuation requires a material change to the acquisition/research contract that this skill should not silently make.

### `NEED_CONTEXT`

A specific resolvable plan parameter, subject identity, locator, credential/permission decision, or other required input is missing.

### `BLOCKED`

A current capability, authority, safety, technical, or natural-executor boundary prevents credible acquisition and cannot be resolved inside the current run.

These are skill-local workflow states. They do not accept or reject the underlying claim.
