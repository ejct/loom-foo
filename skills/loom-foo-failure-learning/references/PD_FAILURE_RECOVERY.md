# loom-foo-failure-learning — detailed instructions (PD_FAILURE_RECOVERY)

> Conditional reference for `../SKILL.md` (progressive disclosure migration based on private loom-foo 0.27.0). The source sections below preserve their original normative content; Markdown `references/` links are rebased to sibling files. Read for the trigger named in the current root; do not silently treat all references as always loaded.

## 2. Separate recovery from learning

Maintain independent outcomes:
- `TASK_RECOVERY`: `RECOVERED` | `PARTIAL` | `BLOCKED` | `NOT_REQUIRED`;
- `LEARNING`: `LOCAL_FIX_ONLY` | `FINDING_READY` | `EVIDENCE_REQUIRED` | `IMPROVEMENT_PROPOSED` | `NO_LOCAL_DELTA` | `ESCALATED`.

Immediately stop a risky or unauthorized action. Repair the active task first when safe and practical, preserving known-good output. If a fix requires additional user authority, explain the exact boundary and complete all permissible preparatory work. Check that the recovery preserves previously correct work and satisfies the **original** instruction; do not turn an angry correction into permission for broad rewriting. A task can be recovered while the systemic cause remains unknown; do not collapse their states.

Never run an unbounded audit loop while a live user task is blocked. For an ordinary one-episode request, complete proportionate analysis in the same response when feasible. Do not promise later background follow-up.

## 3. Capture the minimum recoverable Failure Case

Collect only available, material information:
- exact or minimally paraphrased user signal, date/context if available;
- concrete expected behavior and the authority for that expectation;
- actual observed behavior, including tool errors, failed-repair sequence if material, and the exact skill identity/version **if verified**;
- scope, impact and task-recovery result;
- bounded source pointers, evidence gaps and privacy classification;
- rival explanations, attribution confidence, candidate owner and next discriminating check; distinguish observed failure from emotional-language discovery cue;
- proposed local correction or a negative/no-change finding when justified;
- a regression check if a durable change is proposed.

Read `references/FAILURE_CASE_CONTRACT.md` for substantive incidents or when preparing a durable artifact. For a trivial case, a compact conversational account is enough. Prefer links to existing project-local evidence trails or episode receipts; never duplicate complete transcripts, private data, or tool logs just for completeness. A user report is always an admissible trigger; independent details may require accessible records.

Available context is not full account history. If the relevant episode is in another chat or connected source, retrieve only when available and necessary; otherwise mark `NOT_OBSERVABLE` rather than invent evidence. Retrospective marker-based episode search covers completed, retrievable episodes only; an absent marker does not prove no episode or failure occurred.

## 4. Reconstruct and classify without forcing a culprit

Express separately:
1. **OBSERVED** — user statement, visible exchange/tool output, or source-backed record;
2. **EXPECTED** — actual user instruction, governing contract, accepted project decision, or otherwise explicit expectation;
3. **INFERRED** — hypothesis supported by observations and competing explanations;
4. **UNKNOWN** — material gap requiring another source or test.

Choose the narrowest evidenced primary locus, or `UNKNOWN`. Candidate loci: `SKILL_SEMANTICS`, `ROUTING`, `COMPOSITION`, `CONTEXT_DELIVERY`, `TOOL_OR_SOURCE`, `RUNTIME`, `MODEL_VARIATION`, `EVALUATION_OR_ORACLE`, `POLICY_OR_AUTHORITY`, `USER_INPUT_AMBIGUITY`, `UNKNOWN`. Multiple loci may remain live. Reuse the governing campaign's existing attribution vocabulary in its own reports; do not silently redefine frozen taxonomy or scoring.

Never revise a skill from a single surprising output before checking routing, missing context, tool limitations, task ambiguity and simpler correctives. One incident can justify a narrowly scoped repair when the causal path is explicit; it does not, by itself, establish prevalence or generalization.

## 5. Choose minimum intervention

Perform the local-delta check against current owners, project state and accepted decisions:
- Is the observed requirement already covered?
- Did the failure arise from non-use or incorrect use of an existing capability?
- Can a single instruction, routing rule, prompt/test fixture, tool fix, context handoff, policy clarification or project-local change suffice?
- Is a new skill/component warranted by independent semantic responsibility and repeated evidence?

Possible outputs:
- `LOCAL_FIX_ONLY`: one-time repair and no project change;
- `FINDING_READY`: grounded incident with no accepted intervention yet;
- `EVIDENCE_REQUIRED`: insufficient source/causal basis; specify the smallest discriminating check;
- `IMPROVEMENT_PROPOSED`: bounded project-native delta, responsible owner, evidence and regression case;
- `NO_LOCAL_DELTA`: existing authority/mechanism already covers the behavior and no durable project change is justified;
- `ESCALATED`: hand to the owning workflow with stable incident input.

For substantial project proposals, route the frozen incident and improvement hypothesis to current `loom-foo-proposal-refinement` (load its current canonical SKILL.md) rather than running its complete iterative audit here. For unsettled empirical method, use `loom-foo-research-design`; for evidence interpretation, `loom-foo-evidence-review`; for already-frozen C0/C1/C2 execution, `loom-foo-skill-validation` only when installed; otherwise report the optional owner unavailable and stop that campaign; after *authorized acceptance/persistence transition*, project-native reconciliation may use `loom-foo-project-knowledge-stewardship`. No nested skill runs solely to make a trivial case look rigorous.
