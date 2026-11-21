# loom-foo-agent-task-design — detailed instructions (PD_TASK_ASSURANCE)

> Conditional reference for `../SKILL.md` (progressive disclosure migration based on private loom-foo 0.27.0). The source sections below preserve their original normative content; Markdown `references/` links are rebased to sibling files. Read for the trigger named in the current root; do not silently treat all references as always loaded.

## 14. Task quality review

Verify the owner's outcome, actor/execution path, exact subject, authority, acceptance evidence, accessible delivery and stop boundary. For complex tasks read the full [task quality checklist](TASK_PROFILES_AND_ASSURANCE.md#14-task-quality-review).

## 15. Adversarial checks

For consequential tasks read [adversarial checks](TASK_PROFILES_AND_ASSURANCE.md#15-adversarial-checks), including goal fragmentation, projection drift and authority leaks.

## 15A. Adaptive multi-pass task refinement

Use the L1 **event-conditioned assurance** rule to decide whether to load this method. Do not infer activation from an unmeasured adjective such as *complex*, from mere source/file count, or from risk labels alone. Refine the **same semantic Task Brief** through distinct evidence-seeking checks only when explicitly requested or after a material issue survives the smallest available local resolution, crosses accepted dependencies/invariants, or a consequential repair requires cross-property reinspection. Read [adaptive task refinement](TASK_REFINEMENT.md) when triggered. This is not a new skill, reviewer service, approval stage, extra deliverable or fixed-pass rule. Keep the compact fast path for ordinary work.

### Trigger → local resolution → escalation

| Observable signal | Smallest first action | Escalate to multi-pass only if |
| --- | --- | --- |
| `EXPLICIT_REFINEMENT` | Apply the requested proportionate method to the actual artifact | The owner explicitly requested meaningful multi-pass review (not extra authority) |
| `SOURCE_CONFLICT` | Compare actual controlling source, precedence and exact versions | Conflict is material across accepted constraints/decisions; preserve unresolved authority boundary |
| `ACCEPTANCE_GAP` | Restore an objective done-when from accepted intent | Missing criterion reflects a material semantic/scope gap, not a minor wording edit |
| `GOAL_SUBSTITUTION` | Apply the L1 Goal Fidelity Check to owner goal, accepted delegated outcome and acceptance evidence; repair wrong closure locally | A material goal/authority mismatch persists or fixing it affects dependent accepted units/invariants |
| `CONTRACT_IMPACT` | Identify and directly check affected consumers/contracts | Direct checks cannot establish dependent invariants or compatibility |
| `REPAIR_PROPAGATION` | Recheck changed property and relevant nearby regression | Repair materially changes dependent meanings/constraints, requiring a different check lens |
| `REPEATED_DISTINCT_FAILURE` | Diagnose new actual failures and changed premises | Sequential repairs reveal different material flaws with no stable resolution |
| `RUNTIME_BOUNDARY_GAP` | Verify source reachability/permissions/output materialization | Repairing transfer risks changing goal, visibility, authority or acceptance semantics |

A `COMPLETION_CLAIM` with no tool proof belongs to a local Sanity Check or exact-scope readback, not automatic multi-pass. A simple Goal Fidelity mismatch repaired in construction is not by itself a new mandatory review pass. One failed test requires repair and targeted retest, not a new audit. An unavailable private source may produce `NEED_CONTEXT`; it is not permission to reconstruct it. A high-risk external action still needs its **existing** approval/risk gate even if no refinement cycle applies; refinement never substitutes for authorization.


**Construct before challenging.** First resolve the bounded owner outcome, controlling sources, authority and target-runtime source reachability, including any conditionally relevant skills/references. Verify full, contiguous model-visible skill/source delivery before claiming FULL; a successful reader call or a quoted snippet is insufficient. Do not expand into every installed skill or block independent authorized work for an optional source.

**Rotate discriminating lenses** as applicable: (1) semantic/source fidelity, owner vs delegated outcome, child vs parent closure and acceptance sufficiency; (2) executor feasibility and source/input/output delivery across runtime boundaries; (3) adversarial misexecution, authority/goal/scope leakage and counterexamples; (4) repair impact and regression against earlier findings. A fresh pass must ask a materially different question, test a specific suspected failure, or inspect new evidence. Same-context self-review is not an independent audit. Use an actual distinct reviewer/context only when supported, proportionate and useful.

**Optional role-separated refinement.** When a real distinct reviewer context would improve defect discovery or evidence quality, read [adaptive delegation](ADAPTIVE_DELEGATION.md) and use the target runtime's actually available agents/roles. This is a conditional *execution topology*, not a new skill, mandatory reviewer, agent count or prerequisite for TASK_READY. Keep the Root/owning agent accountable for the owner outcome and adjudication. Give a Reviewer the exact candidate plus controlling intent and sources to search for unknown defects; give a Verifier explicit criteria and the exact candidate to establish scoped PASS/FAIL/INCONCLUSIVE/NOT_COVERED. Separate these from author repair. Prefer parallel review/verification only when both can examine the same stable subject independently, and rerun affected checks after a substantive repair. Confirm actual context separation, source reachability, permission boundaries and tool events before reporting an independent review or successful spawn. A custom Codex role preset is optional and never installed by this Task Brief.

**Adjudicate findings and repair the artifact**, not merely add cautionary prose. For a material finding, establish evidence and consequence; resolve, reject as invalid with reason, or bound the remaining uncertainty. Recheck affected properties and preserved constraints after a substantive repair. If corrections repeatedly uncover material failures without progress, revisit the framing/source authority rather than cycling mechanically. Do not invent a fixed number of passes, formal freezes, findings registry, agent roles or test campaigns.

**Executor boundary.** Task Design can inspect its own skill use and source coverage and can *require* executor skill discovery, full loading and observed verification in the Task Brief. It cannot certify that a future executor already selected/read/applied those skills. Separate SKILL.md delivery, actual application, runtime activation and candidate-specific verification; use the existing Answer Receipt and available execution trace rather than a second Skill Application Evidence registry. Mark missing observations NOT_CONFIRMED/UNVERIFIED, never PASS.

Stop when the Task Brief remains faithful and executable, identified material defects have dispositions, necessary sources can reach the target runtime, and additional passes have low expected information value. If a controlling source or authority is truly unavailable, use the existing NEED_CONTEXT/BLOCKED contract; do not announce TASK_READY on an invented prerequisite.

### Process Trail for multi-pass task refinement

When §15A is actually used, preserve a **minimal stage record** for each material pass over the same Task Brief: method/lens or skill consulted, real executor identity (same-context vs separate agent), exact input/output brief revisions only if observed, material finding and disposition, and the evidence class. Use this to render the final Answer Receipt `Process Trail` in execution order. Different lenses in one uninterrupted self-review are not necessarily distinct independent reviews. Do not create extra files, force named versions, or imply that the future executor already followed the Task Brief. No trail is required for the compact single-pass fast path.
