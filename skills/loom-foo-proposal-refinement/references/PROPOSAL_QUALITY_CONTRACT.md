# Proposal Quality Contract

This is a local construction contract inside the `loom-foo-proposal-refinement` skill. It does not create project-wide authority, a Kernel primitive, or an independently accepted project policy. Its purpose is to keep known proposal-quality defects out of P0 so adversarial review can focus on harder defects.

This reference expands the construction rules used before Proposal P0 enters adversarial refinement.

The contract is intentionally artifact-oriented rather than template-oriented. A proposal can use different headings or formats while still satisfying the contract. The checks are working discipline, not required visible sections: compress or combine them whenever clarity is preserved.

## 1. Decision requested

A proposal should enable a concrete disposition. State what is being asked now: for example, authorize an experiment, choose a direction, accept a bounded architecture change, adopt a policy revision, defer a decision pending evidence, or reject a proposed mechanism.

Do not let the proposal drift into a research essay whose requested decision is implicit.

A proposal can recommend a decision without possessing authority to make it.

## 2. Trigger / why now

State the change, defect, evidence, opportunity, or pressure that makes the proposal worth considering now.

If nothing material changed and no established problem exists, that is evidence against introducing change.

## 3. Current state

Describe only the current state needed to evaluate the decision:

- existing owners/primitives/mechanisms;
- accepted constraints/decisions;
- relevant observed behavior;
- current failure or limitation;
- existing evidence and uncertainty.

Do not duplicate project documentation merely to make the proposal look self-contained. Link or reference authoritative background where the runtime supports it.

## 4. Local delta gate

This is a short construction gate, not a new project primitive and not a mandatory visible proposal section. Before designing a change, compare the triggering idea or lesson against the project’s current state. This is especially important when the proposal originates from:

- an external repository, product, paper, standard, or competitor;
- another project;
- a newly observed architecture pattern;
- a retrospective or audit lesson;
- a proposed reusable abstraction.

Ask in order:

1. What principle, failure, or opportunity was observed?
2. Which current owners, mechanisms, or accepted decisions already cover it locally?
3. What exact gap remains after that comparison?
4. Does closing that gap require a project change at all?

If the comparison finds no material uncovered gap, use `NO_LOCAL_DELTA` as the proposal disposition. Explain the no-op conclusion with enough evidence to be reviewable, then avoid canonical edits, new abstractions, implementation work, or artificial follow-up tasks.

`NO_LOCAL_DELTA` is not a new terminal state. It can lead to `CONVERGED` when the no-change conclusion is sufficiently established, or to `VALIDATION_REQUIRED`/`BLOCKED` when the existence of a local gap itself still depends on evidence or authority.

Do not confuse “this source contains a useful idea” with “this project must change.”

## 5. Proposed delta

Express the proposal as a delta from current state.

Prefer the smallest change that can plausibly produce the desired outcome. A proposal that cannot say what changes is not decision-ready.

For each important delta, identify the existing owner it modifies or explain why no existing owner is suitable.

## 6. Simplest credible baseline

Before adding machinery, describe the simplest credible alternative. Depending on the subject this may be:

- do nothing;
- keep the current mechanism;
- improve an existing owner;
- use ordinary links/manual process/native runtime behavior;
- run a one-off experiment without canonicalizing a new concept.

Include the baseline only when it is genuinely plausible. If no credible baseline exists, say why briefly rather than inventing one. Do not manufacture a weak status-quo straw man.

The proposed delta should beat the baseline on explicit decision drivers rather than by rhetorical framing.

## 7. Real alternatives

Use real alternatives that differ materially in mechanism, ownership, scope, timing, or risk.

Two real options are better than four padded options.

For consequential choices, compare options using decision drivers that actually separate them. A matrix is useful when several criteria matter, but not mandatory.

## 8. Decision drivers and constraints

State the criteria that explain why one option is preferable. Examples:

- correctness;
- user value;
- reversibility;
- operational burden;
- implementation cost;
- time-to-learning;
- migration risk;
- privacy/security;
- compatibility with accepted architecture;
- maintainability;
- evidence quality.

Do not introduce generic criteria that do not affect the decision.

## 9. Trade-offs and consequences

For the preferred option, state both benefits and costs.

At minimum, ask:

- What becomes possible or easier?
- What becomes harder, more expensive, or more constrained?
- What becomes impossible or is deliberately given up?
- What new failure modes or dependencies appear?

A proposal with only benefits is advocacy, not analysis.

## 10. Reversibility and lock-in

When the decision has meaningful persistence, characterize reversal cost qualitatively (for example easy / costly / effectively one-way) and explain why.

Pay special attention to:

- persistent data models;
- public APIs/contracts;
- migrations;
- vendor lock-in;
- canonical process/policy changes;
- cross-project abstractions;
- irreversible user-facing commitments.

Prefer reversible probes before irreversible architecture when they answer the same uncertainty.

## 11. Evidence, assumptions, and unknowns

Keep epistemic states distinguishable.

A useful local classification is:

- **Established** — supported by current authority/evidence;
- **Externally verifiable** — can be checked against current sources;
- **Empirically testable** — requires a real probe/experiment;
- **Assumed** — bounded working assumption with stated basis;
- **Unknown** — unresolved and potentially decision-changing.

Do not promote agreement, repetition, or confident prose into evidence.

## 12. Validation and falsifiers

A proposal should say how it can fail.

Identify:

- evidence that would support the proposal;
- evidence that would weaken or falsify it;
- the smallest useful validation step for the dominant uncertainty;
- which decision changes under each material result.

If validation is cheaper than further reasoning, finish the strongest bounded proposal supported by current evidence, then stop further theorizing and return `VALIDATION_REQUIRED` with the smallest useful validation step and the result that would change the decision.

## 13. Revisit condition

For persistent decisions, state an observable condition that should reopen the decision: new evidence, changed constraint, threshold breach, repeated failure class, scale boundary, or dependency change.

Do not use vague permanence such as “never revisit” or a calendar cadence with no observable trigger.

For an explicitly temporary experiment proposal, the experiment result itself may own the revisit/next-decision boundary; do not force a separate field.

## 14. Authority boundary and next transition

Distinguish recommendation from authority.

State what plausible dispositions mean:

- **ACCEPT** — what is authorized next, if the decision-maker accepts;
- **EXPERIMENT_FIRST / VALIDATION_REQUIRED** — what bounded evidence comes next;
- **DEFER** — what missing condition blocks decision now;
- **REJECT** — what is closed and what remains possible.

The proposal must not silently implement its own recommendation.

## 15. New concept identity test

Apply this test to architecture/process proposals that introduce a named reusable entity such as a primitive, layer, service, registry, framework, contract, or policy object.

A new identity is stronger when all or most are true:

1. It owns a distinct semantic responsibility.
2. Existing owners cannot represent that responsibility cleanly without distortion.
3. It has a meaningful independent lifecycle, authority, versioning, state, or validation boundary.
4. Multiple concrete uses or observed recurrence justify reuse rather than speculative generalization.
5. Removing the new identity would make the model less clear or less correct, not merely less elegant.

If these do not hold, prefer a smaller materialization: field, rule, view, fixture, profile clause, experiment artifact, implementation detail, or extension of an existing owner.

## 16. Composition test

A proposal may bundle several deltas when they are causally coupled and need one decision.

Split or clearly isolate deltas when they can be evaluated independently and may reasonably receive different dispositions.

Warning signs of accidental bundling:

- one part is evidence-ready while another needs research;
- one part modifies policy while another only changes implementation;
- rejecting one part does not invalidate the others;
- benefits attributed to the bundle actually come from one small component.

Do not fragment one coherent mechanism into artificial micro-decisions.

## 17. Fresh-reader test

The proposal should survive a competent reader who has access to referenced project sources but not the author's hidden chain of thought.

A reader should be able to reconstruct:

- requested decision;
- trigger/problem;
- current state;
- proposed delta;
- baseline and alternatives;
- rationale/trade-offs;
- material assumptions/unknowns;
- validation/next transition.

Reader confusion is a construction defect even when the underlying idea is sound.

## 18. Construction anti-patterns

Repair these before Audit A0 when visible:

- solution before problem/trigger;
- proposal with no explicit decision;
- current architecture ignored or duplicated;
- useful external idea treated as proof that a local project delta exists;
- status quo omitted even though it is viable;
- fake alternatives added only to make the preferred option look strong;
- new named abstraction without a distinct owner/lifecycle need;
- benefits listed without costs;
- irreversible choice treated like a cheap experiment;
- assumption phrased as fact;
- empirical uncertainty “resolved” by more prose;
- several independent decisions bundled under one acceptance gate;
- implementation detail elevated into architecture without decision value;
- proposal depends on conversation-only context that the intended reviewer will not have.
