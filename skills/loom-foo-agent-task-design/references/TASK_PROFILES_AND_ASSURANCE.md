# Task profiles and assurance checks

Read the relevant full profile or quality checks for a review, repair or consequential task. All detailed rules are retained below from v0.1.6.

## 11. Reviewer / audit profile








For `REVIEW_AUDIT` tasks:








- freeze the exact subject under review;
- state evaluator mutation authority explicitly, normally read-only unless remediation is requested;
- treat Builder-provided results as claims to challenge, not inherited truth;
- provide current controlling authority and known findings without the Builder reasoning transcript when independence matters;
- define blocking scope so the reviewer does not expand into unlimited exploration;
- require findings to distinguish candidate defects, test/probe defects, environment limitations, authority/input gaps, and genuine authority conflicts where material.








A review PASS does not automatically accept, merge, publish, or promote the subject.









### P4 — role permissions and oracle boundaries

When a delegated review depends on independence or read-only operation, preserve the actual host capability and allowed mutating tools in the Task Brief. A role named reviewer, a no-edits prompt, fresh context or lack of Write/Edit tools is only `INSTRUCTION_ONLY` unless the host truly prevents mutation via shell and other interfaces. Use host sandbox/permissions where supported, report `NOT_CONFIRMED` when enforcement cannot be observed, and check the protected oracle's pre/post baseline when material. Never call a simulated reviewer a host-enforced one. Review independence and test immutability are different properties.

## 12. Repair / remediation profile








For remediation tasks:








- bind the exact failed finding(s) and current base/candidate when material;
- preserve unaffected accepted semantics;
- allow local correction in place when authority, scope, immutable subject identity, and product semantics remain unchanged;
- require rerunning the affected gate and relevant regressions;
- create a new lineage only when a real immutable/authority/scope/semantic boundary requires it.








Do not turn an ordinary implementation defect into a governance transition. When a defect can be repaired locally without changing authority, scope, immutable subject identity, accepted semantics, or an experimental treatment, repair it, rerun the affected gate and relevant regressions, and continue the same task.









## 14. Task quality review








Before returning the task, challenge it:








- Is there exactly one primary result?
- Is this actually one coherent task?
- Does each mandatory instruction protect a real requirement?
- Did any technical capability become accidental authority?
- Are stable project facts referenced instead of copied unnecessarily?
- Are material source precedence and subject identity clear?
- Are scope/non-goals sufficient to prevent obvious expansion?
- Are acceptance criteria observable rather than aspirational?
- Does each verification step establish a distinct property?
- Is the task prescribing method where outcome/boundary would suffice?
- Can a normal local defect be corrected without inventing a new governance task?
- Does any intermediate stop correspond to a real authority, subject, scope, input, or material execution-method boundary?
- Am I forcing an owner interruption where the executor can safely continue under already-granted authority?
- If one human input is unavoidable, does the brief explicitly resume the same task afterward?
- Is the stop boundary explicit enough to prevent accidental next-phase work?
- Would a competent agent know what to return and when it is done?
- What decision-bearing information was removed during compression, and why is each omission safe?
- Could a competent executor now invent materially different behavior because an accepted decision, semantic distinction, or relevant edge case became invisible?
- Did a precise conditional/future relationship become a vague possibility?
- Are controlling source pointers actually reachable from the target runtime, or has source identity been preserved while source access was lost?
- For each material external input, who can retrieve it and how does it reach the executor?
- Am I making the user act as a courier even though an authorized machine path exists?
- If coordinator staging is used, are exact identity, disclosure authority, and per-worker visibility preserved?
- Which outputs have a downstream consumer outside this runtime, and where can that consumer resolve them?
- Am I returning only a local path for a continuation-bearing artifact?
- Is the natural durable owner selected by semantic ownership/project convention rather than file extension?
- Does materialization require authority not granted by this task?
- If raw experimental/review evidence is materialized, is the raw output preserved verbatim?








Restore the smallest exact semantic slice when a compression-loss check fails. Do not respond by restoring the entire original prompt.








Remove instructions that fail this review.









## 15. Adversarial checks








For consequential tasks, explicitly probe for:








- `AUTHORITY_LEAK` — permission inferred from capability/context;
- `SCOPE_EXPANSION` — adjacent work pulled into the task;
- `CONTEXT_DUPLICATION` — stable docs recopied into the prompt;
- `STALE_AUTHORITY` — superseded or mutable source treated as controlling;
- `METHOD_OVERPRESCRIPTION` — execution mechanics frozen without requirement;
- `ACCEPTANCE_AMBIGUITY` — “make it good” without observable done-when;
- `VERIFICATION_CEREMONY` — checks that prove no distinct property;
- `REVIEW_BIAS` — evaluator inherits Builder conclusions as truth;
- `HIDDEN_TRANSITION` — push/merge/publish/acceptance/disclosure implied by implementation wording;
- `MEGA_TASK` — decomposition pressure hidden inside a large prompt;
- `PROJECTION_DRIFT` — runtime-specific rendering weakens the semantic task.
- `SEMANTIC_COMPRESSION_LOSS` — decision-bearing source information disappears during simplification.
- `EDGE_CASE_ERASURE` — a canonical edge case relevant to the requested work is omitted, forcing the executor to invent behavior.
- `DISTINCTION_COLLAPSE` — authority-distinct states/outcomes are projected as one coarser state.
- `INACCESSIBLE_AUTHORITY_POINTER` — the brief depends on a controlling source that the target runtime cannot reliably dereference.
- `USER_AS_COURIER` — manual relay is imposed even though an authorized reliable machine delivery path exists.
- `DELIVERY_PATH_ASSUMPTION` — the brief assumes connector/staging capability that has not been established.
- `DELIVERY_IDENTITY_DRIFT` — staged material cannot be tied to the intended exact subject/version when identity matters.
- `DELIVERY_AUTHORITY_LEAK` — coordinator access is treated as permission to disclose material to the executor.
- `TREATMENT_LEAKAGE` — treatment-specific material is exposed to a control execution or otherwise weakens an intended experimental visibility boundary.
- `GATE_PROLIFERATION` — one coherent executable task is split into multiple owner approval, planning, or return cycles even though intermediate actions remain inside the same authority envelope.
- `PREMATURE_BLOCK` — `BLOCKED`, `NEED_CONTEXT`, or equivalent is returned even though an authorized, proportionate local continuation path remains available.
- `AUTHORITY_SHRINKAGE` — the compiler discards already-granted compatible local execution authority and invents a return/approval boundary.
- `RECOVERY_REDELEGATION` — an ordinary intermediate failure triggers a new narrower Task Brief although outcome, subject, authority, acceptance and stop boundaries have not materially changed.
- `GOAL_FRAGMENTATION` — a necessary internal operation is accepted as the final delegated outcome while the user-authorized result remains unowned.
- `OUTPUT_USER_AS_COURIER` — manual output relay is requested although an authorized reliable machine path exists.
- `OUTPUT_LOCAL_ONLY_LEAK` — a continuation-bearing artifact is returned only as a local path inaccessible to its intended next consumer.
- `OUTPUT_DESTINATION_ASSUMPTION` — the brief assumes a destination/write capability that has not been established.
- `OUTPUT_MATERIALIZATION_AUTHORITY_LEAK` — production/write capability is treated as permission to publish externally.
- `OUTPUT_IDENTITY_DRIFT` — materialized output cannot be tied to the produced subject/version when identity matters.
- `OUTPUT_DUPLICATE_TRUTH` — competing durable copies are created instead of one natural owner plus cross-reference.
- `RAW_OUTPUT_MUTATION` — materialization changes raw experimental/audit output rather than preserving it verbatim.








