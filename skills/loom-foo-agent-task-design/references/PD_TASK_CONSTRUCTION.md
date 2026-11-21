# loom-foo-agent-task-design — detailed instructions (PD_TASK_CONSTRUCTION)

> Conditional reference for `../SKILL.md` (progressive disclosure migration based on private loom-foo 0.27.0). The source sections below preserve their original normative content; Markdown `references/` links are rebased to sibling files. Read for the trigger named in the current root; do not silently treat all references as always loaded.

## 1. Routing gate

Use this skill when the requested primary output is a concrete task for another agent: implementation, change, probe, remediation, validation, review/audit, or another bounded execution unit.

Do not use it as the primary owner when the user is asking for:

- a project proposal -> `loom-foo-proposal-refinement` owns;
- architecture creation/evolution -> `loom-foo-architecture-design` owns;
- architecture evaluation -> `loom-foo-architecture-review` owns;
- same-workstream context continuation -> `loom-foo-handoff` owns restoration first;
- lessons/mechanisms transferred across contexts -> `loom-foo-cross-context-transfer` owns the transfer findings;
- broad dependency-aware decomposition of many work units -> return `PLANNING_REQUIRED` rather than manufacturing a mega-prompt.

A prior owning workflow may supply the accepted/bounded intent. This skill compiles it for execution.

## 2. Authority boundary

Task formulation does not create authority that the user or controlling source did not grant.

Technical capability is not permission. The Task Brief must preserve distinctions between:

- read/inspect;
- create/modify/delete;
- execute local tools/tests;
- mutate external/shared state;
- push/merge/publish/deploy/release;
- accept/promote/canonicalize;
- disclose private information.

Never infer a stronger transition because it would make execution convenient.

If authority is materially unknown, narrow the task to what is clearly authorized or return `NEED_CONTEXT` / `BLOCKED` with the exact missing authority dimension.

## 3. Single-task gate

Before writing a Task Brief, determine whether the work is one coherent executable unit.

A single task normally has:

- one primary observable outcome;
- one authority envelope;
- one materially coherent subject/base;
- acceptance criteria that can be evaluated together;
- a meaningful stop boundary.

Return `PLANNING_REQUIRED` when the request materially depends on decomposition across multiple independently acceptable work units, owners, branches, sequencing gates, or incompatible authority envelopes.

Multiple execution stages do not by themselves make multiple tasks. A coherent unit may include `inspect -> modify -> build -> test -> diagnose -> repair -> retry -> verify -> finish` when outcome, subject, authority envelope, acceptance gate, and final stop boundary remain shared.

**Already accepted multi-unit Work Plan:** If the user is commissioning an authorized **root-coordinator execution episode** rather than asking this skill to decide how to decompose work, one Root Execution Brief may contain separately bounded worker instructions and root-owned launch/monitor/reconcile duties. It is one root-level execution contract over an **existing** Work Unit Set, not a worker supertask: preserve independent acceptance, dependencies, worktree boundaries and root-only sibling management. Do not invoke `PLANNING_REQUIRED` merely because the accepted plan contains A+B; do invoke it when allocation/acceptance/dependencies are not yet accepted and require planning. Never give a worker authority over sibling tasks from context alone.

Do not solve a planning problem by making the prompt longer.

## 4. Establish task class

Use the nearest class only to select relevant checks:

`BUILD_CHANGE`
`PROBE_EXPERIMENT`
`REPAIR_REMEDIATION`
`REVIEW_AUDIT`
`REPRODUCE_VALIDATE`
`OTHER_BOUNDED_TASK`

The class does not create a new workflow ontology and need not appear in the user-facing prompt unless useful.

## 5. Build the Task Brief from current authority

Resolve only the context needed to execute correctly.

Prefer stable source pointers over copied project history. Capture precedence when multiple sources matter.

The Task Brief should contain, when material:

1. **Outcome** — one primary observable *delegated* result, with parent owner goal and remaining gaps distinguishable when the work is an intermediate Work Unit.
2. **Subject** — exact repository/workspace/base/candidate/version/artifact identity when correctness depends on it.
3. **Context and authority pointers** — stable sources plus reading order/precedence; inline only task-local facts needed for execution.
4. **Authority envelope** — what may be read, changed, created, deleted, executed, or externally transitioned; explicit prohibitions when material.
5. **Scope and non-goals** — bounded work surface and excluded adjacent work.
6. **Protected invariants** — semantic/product/security/evidence properties the implementation must preserve.
7. **Acceptance criteria** — observable `done when` conditions that are sufficient for the delegated result; do not silently turn evidence from a probe/test into proof of a broader outcome.
8. **Verification** — evidence sufficient for the actual claims and risks, with environment/provenance when claim strength depends on it.
9. **Uncertainty / continuation policy** — distinguish execution-blocking uncertainty from claim-limiting or non-blocking uncertainty; continue safe independent work when authorized.
10. **Stop boundary** — where this particular Work Unit or root execution episode ends, whether its parent goal remains open, and which next transitions require separate authority.
11. **Return contract** — work backward from the actual next consumer/decision/action and explicitly request the **minimum consumable output**: needed artifacts/data, evidence or decision inputs, exact subject/revision identity, relevant limits/negative findings, and accessible durable location or a precise delivery-blocked state. Avoid report-only completion when the next actor needs more to proceed.

### Next-Step Readiness & Return Contract — consumer-first design

**Before choosing implementation steps**, determine the legitimate next consumer and what they must *do with* the result. The next consumer can be the root coordinator, another already accepted Work Unit, a reviewer, the project owner making a decision, or the same executor continuing within its scope. A downstream consumer does not automatically imply a new or authorized task. For a truly terminal task, a concise completed outcome is enough; if the next decision is not yet defined, give the owner a **decision-ready** account of findings, limits and actual artifacts, without manufacturing a future job.

Derive the return contract **backward** from that action or decision:

1. **Consumer and next legitimate operation:** Who needs the result and for what specific accepted integration, choice, check or continuation? Do not invent sibling authority or make a nonexistent downstream task a mandatory gate.
2. **Required return payload:** Which exact candidate, patch/ref, analysis/data, reproducible evidence, remaining failures, assumptions, or decision alternatives must exist for that consumer to act? Distinguish required deliverables from optional verbose reports. Return the *actual* product of the work, not merely its narrative summary.
3. **Verification and provenance:** Identify the minimum evidence that supports the handoff claim, including negative/inconclusive experiment data where it affects a downstream choice. A `PASS` label alone does not give the next consumer missing inputs or certify a parent goal.
4. **Reachability and authority:** Specify where artifacts will live and how the next consumer can retrieve them, using actual allowed project-native surfaces. Include exact revision/commit/IDs where correctness depends on them; do not presume shared connectors/worktrees or broaden private data visibility.
5. **Continuation boundary:** What remains open or blocks the next step? A valid negative result may be fully sufficient for a decision even when an engineering improvement remains unmet. If the same executor can finish the authorized next phase, prefer normal continuation over a ceremonial inter-agent relay.

**Counterexample / acceptance test:** Assume the executor has satisfied every `done when` criterion and returned **only** the items actually requested in the Task Brief. Can the identified next consumer now perform the next legitimate action without recreating analysis, asking for missing artifacts, guessing unrecorded limitations, or making the user manually courier information? If no, repair the *same* Task Brief: add the specific absent result, evidence, retrievable identity or accountable blocker. Do not add a generic long report, a universal schema, a mandatory independent reviewer or an extra approval step.

**Examples:**
- A semantic bug patch with local tests but no exact source revision/fixture/evidence needed for the root's regression cannot satisfy an explicitly required integration handoff until those items are supplied.
- A controlled speed experiment that found **no** improvement can return the raw/reproducible measurements and restrictions needed for the owner's next decision; do not invent a speedup or require more experiments solely to make the result positive.
- A root episode whose children returned `PASS` but omitted an accepted integration input is not ready for root closure. Root must request the needed return **in the original worker contract**, not launch a surprise sibling task to recover it.
- A tiny self-contained rename with no real downstream consumer can end with the changed revision and scoped confirmation; do not force a handoff package.

This supplements **Goal Fidelity** (right delegated result) and **output materialization** (reachable bytes): neither implies the other. Producer success, consumer readiness and later owner acceptance must remain distinct.

### Semantic preservation during compression

Before removing detail from the source intent, derive an internal **Semantic Preservation Set**. This is a compilation control, not a mandatory user-facing artifact.

Preserve the smallest exact information whose omission could materially change execution correctness, authority, accepted product/architecture meaning, scope, user-visible behavior, acceptance, or downstream interpretation.

The set normally includes, when task-relevant:

- authority-bearing semantics and precedence;
- already accepted/chosen decisions;
- protected distinctions between outcomes, states, or authority levels;
- explicit exclusions and negative knowledge where rediscovery pressure is plausible;
- already-decided conditional/future relationships, including attachment points or triggers;
- canonical edge cases that materially constrain the requested interaction/output;
- acceptance dimensions without which a plausible but semantically wrong result could pass review.

Compression may remove duplicated history, report ceremony, repeated examples, stale explanation, and method prescription. It must not remove a Semantic Preservation Set item.

When a detailed source decision can be represented compactly, preserve its relationship rather than its prose. For example, an accepted future path `public → preview → authenticated claim` may be compressed to that relation plus its future-only boundary; reducing it to “a future path may attach later” is semantic loss.

### Goal Fidelity & Outcome Integrity — local construction check

Before finalizing, distinguish **Owner Goal**, **Delegated Outcome**, and **Completion Evidence**. Ask whether the proposed `done when` could all be true while the *delegated* outcome is unachieved. Correct the acceptance or outcome wording locally. Do not confuse failure of a **particular tactic** with failure to complete an explicitly authorized **feasibility experiment**, and never classify that valid negative experiment as a realized engineering improvement.

- **Owner Goal** — what the user wants ultimately; preserve it as context and do not silently expand worker authority to solve everything.
- **Delegated Outcome** — the exact approved Work Unit or accepted root episode, including its class (repair, build, experiment, review) and independent stop/authority boundary.
- **Completion Evidence** — property-specific observations proving that outcome. Passing unit tests, a generated artifact, reviewer approval, candidate changes or returned worker reports can support narrower claims; they do not automatically prove a product-level goal.

Apply the following **counterexample checks** internally, not as a new required output or audit round:

1. Could every acceptance criterion pass but a required *delegated* result still be missing? **Repair** the criterion/brief (e.g. a claimed semantic improvement has only static route tests and no candidate-level semantic observation).
2. Could a child Work Unit pass and make the root/parent goal look finished? **Keep its result independently accepted or negatively concluded, and label parent/root closure separately**; require root integration/reconciliation evidence if that is its actual authorized outcome.
3. Is the worker explicitly commissioned only to repair one bug? That narrow repair **is sufficient** for that worker; do not expand it to all product correctness or invent a new study.
4. Is the task an **experiment to determine whether** a performance change helps? A source-grounded, controlled negative finding can complete the experiment; a task to **improve** performance is *not achieved* merely by showing the candidate did not help. Respect the accepted scope and resource limit; do not require impossible gains or endless retries.
5. Did Task Design itself narrow the agreed outcome to what is easy to test? Restore the **accepted delegated** scope and continue normal QA. If the **upstream accepted plan** is too narrow for the owner's current goal, report that gap to the appropriate planning/decision owner without silently rewriting its Work Units or declaring the parent closed.

If a mismatch can be fixed locally, correct it before `TASK_READY`. A concrete goal-substitution issue is also an observable `GOAL_SUBSTITUTION` signal for L1 event-conditioned assurance; use multi-pass only when local correction leaves material competing requirements, dependent invariants or consequential regressions. A missing criterion alone does not justify adding review ceremony.

## 6. Compact fast path

For a small, low-ambiguity, reversible local task, use the smallest sufficient brief. Usually this is issue-like prose containing:

- outcome;
- relevant scope/context pointer;
- material boundary;
- done-when / verification.

Do not force eleven headings when four sentences are sufficient.

Escalate detail only when consequence, ambiguity, irreversibility, evidence sensitivity, authority complexity, or review needs justify it. If existing project rigor is already defined for the workstream, reuse it rather than inventing a second risk taxonomy.

## 7. Preserve implementation discretion

Specify mechanisms only when they are themselves part of the requirement, experiment, fragile operation, or accepted architecture.

By default do not prescribe:

- number of agents, chats, reasoning passes, or correction rounds;
- model routing outside an explicit experiment;
- exact tool-call or shell-command order;
- temporary directory/worktree mechanics;
- report heading trees;
- duplicate evidence packages;
- speculative abstractions;
- implementation details a competent agent can choose safely within the contract.

Prefer protected boundaries and observable outcomes over micromanagement.
