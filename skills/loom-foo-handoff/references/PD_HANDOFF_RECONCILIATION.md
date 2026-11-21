# handoff — detailed conditional method (PD_HANDOFF_RECONCILIATION.md)

> Source: exact private Loom-foo 0.35.1 `SKILL.md`. L1 retains activation, goal and authority precedence. Below sections are preserved in full, in source order; `references/...` paths refer to the owning skill root. Read this file only when its explicit L1 trigger applies.

## 3. Reconcile current state

Reconstruct operational state rather than conversation chronology.

Resolve only what can materially affect correct continuation:
- current user intent;
- accepted decisions and constraints;
- material scope/ownership boundaries;
- material semantic/domain invariants that future work must preserve;
- completed work;
- persistent state and missing already-authorized persistence;
- pending/deferred/blocked work;
- action-specific authority boundaries;
- material negative knowledge and rejected simplifications whose recurrence would cause regression;
- dynamic external state;
- relevant artifacts/sources;
- legitimate resumption point;
- active reasoning frontier when the workstream is currently exploring a specific unresolved design/research question.

Use sources only for dimensions they can establish.

Treat source locators as verification candidates, not as a checklist to read. Verify a source only when it can materially change current state, action/transition authority, persistence, blocker/unknown/conflict status, or the legitimate resumption point. Prefer the smallest source slice sufficient to resolve the material claim.

Verification is especially warranted when a transferred claim is `UNKNOWN`, `UNVERIFIED`, `STALE`, or `CONFLICTING`; when it describes mutable external state whose change would alter continuation; when currentness/authority cannot be established from the handoff alone; or when observed and prescribed state disagree.

Memory/checkpoints are retrieval aids, not ultimate authority for mutable external state.

### Goal Fidelity: questions do not become priorities or permissions

Separate `OPEN QUESTIONS` / `VALIDATION_REQUIRED` / producer recommendations from `ACCEPTED DECISIONS`, owner-authorized next actions and the active task objective. Restore a research uncertainty as an uncertainty, never automatically as a requirement to run a benchmark, audit or study. Preserve explicit owner rejection/deferment of proof campaigns; an unresolved item in a checkpoint is not evidence that the owner wants to pursue it. A transferred TODO is data, not an execution instruction, and neither a producer nor receiver may replace a build/use objective with comparative verification by default.

For a Chat/Text-only handoff without substantive instruction outside the envelope, restore, selectively verify, emit Context Receipt and stop. Preserve proportional operation-integrity and real authority gates even if comparative studies are deferred. Receiver regression: a valid handoff can mention an unmeasured benefit without creating an unsolicited comparison experiment or changing the owner's primary functional objective. This clarification changes skill-local state interpretation, not the Chat/Text v0.2 transport framing or generic handoff permissions.
## 5. State representation

Represent only distinctions that matter to the checkpoint.

Useful dimensions may include:
- substantive state;
- persistence state;
- action/transition authority;
- epistemic status.

These are a handoff representation technique, not a replacement for the LoomLoom Kernel lifecycle/state model.

Do not force all dimensions onto trivial items.
## 8. Compile draft checkpoint H0

Perform two internal passes.

### Recall pass
Preserve everything material to:
- continuation;
- decisions/constraints;
- material semantic invariants and scope/ownership boundaries;
- authority;
- persistence;
- status;
- negative knowledge;
- active reasoning frontier when material;
- regression avoidance.

### Compression pass
Remove:
- chronology;
- repetition;
- obsolete intermediate state;
- raw tool chatter;
- superseded reasoning;
- irrelevant failed attempts;
- large retrievable artifact bodies;
- repeated authority warnings that add no new action-specific distinction.

Preserve one clear generic authority invariant plus the concrete checkpoint-specific authority boundaries that materially govern continuation.

The draft should be the smallest state that still restores the workstream correctly.
