# Proposal Construction — conditional methodology

> Applies only when the owning `SKILL.md` conditional index selects it. Moved from the v0.29.0 root. References mentioned as `references/X.md` inside quoted historical text are relative to the *owning skill directory*, not this file. General L1 authority and current use-first instructions prevail over superseded historical clauses.

## 5. Construct the proposal against the Proposal Quality Contract

Before optional consequential review, ensure the proposal is clear enough to support a meaningful challenge.

The proposal should make the following decision structure explicit when material to the subject:

- **decision requested** — what decision this artifact is intended to enable now;
- **trigger / why now** — what problem, change, evidence, or pressure makes the decision relevant;
- **current state** — what already exists, including relevant owners, mechanisms, constraints, and accepted decisions;
- **local delta gate** — whether any project-local change is actually required after comparing the idea with current owners, mechanisms, and decisions;
- **proposed delta** — the smallest sufficient change from the current state, when a delta remains;
- **simplest credible baseline** — including status quo / do-nothing / existing-mechanism behavior when it is a real alternative;
- **real alternatives** — materially different options, without padding the set with straw men;
- **decision drivers** — constraints and criteria that distinguish the options;
- **trade-offs and consequences** — what becomes possible, harder, more expensive, constrained, or impossible;
- **reversibility** — when material, how costly it is to undo or change course;
- **evidence / assumptions / unknowns** — make epistemic status visible rather than burying it in prose;
- **validation / falsifier** — what evidence would support, weaken, or invalidate the proposal;
- **revisit condition** — for persistent decisions, an observable condition that should reopen the decision;
- **authority boundary** — what can be decided now and what still requires validation, approval, or another authority transition;
- **next transition** — what follows from plausible dispositions such as accept, experiment-first, defer, or reject.

Do not force every item into a named section. The contract describes information quality, not a universal document template. Satisfy it compactly: one sentence, table row, or integrated paragraph may cover several items when that is clear. Do not expose the construction checklist as ceremony.

For detailed construction guidance and conditional checks, read `references/PROPOSAL_QUALITY_CONTRACT.md` when the proposal is consequential, architecture/process-heavy, introduces new reusable concepts, or the first draft remains ambiguous.

### Local delta gate

Treat this as a short yes/no construction check, not a mandatory proposal section. Before elaborating a change, compare the observed idea, lesson, external pattern, or proposed mechanism against the project’s current state. Ask:

1. What useful principle or pressure triggered this proposal?
2. What does the project already provide through existing owners, mechanisms, or accepted decisions?
3. What exact local gap remains?
4. Is a project-local delta actually required?

If no material gap remains, record `NO_LOCAL_DELTA`, explain the comparison briefly, and do not manufacture a canonical change, new abstraction, or implementation task merely to preserve the proposal. `NO_LOCAL_DELTA` is a proposal disposition/construction outcome, not a fifth terminal state. Continue only with proportionate audit needed to justify the no-change conclusion, then use the existing terminal-state rules.

A useful external idea does not imply that the current project needs to change.

### Initial problem and solution-space sketch (conditional)

For a materially open design choice, first clarify the user outcome, relevant semantic distinctions, hard constraints, existing capabilities and a plausible simplest baseline. Sketch genuinely different mechanism families **before consulting external implementations as proposed solutions**, when this could prevent premature fixation. This is a provisional pre-search orientation, not a claim of cognitive independence from previous examples; do not require an extra document, fixed number of options, or new approval stage. Do not reopen a settled user decision or manufacture alternatives when the choice is already constrained. If a blocking ambiguity prevents a defensible proposal, use `loom-foo-problem-understanding` only for that ambiguity.

**Context and constraint research is different from prior-art solution discovery.** Verify externally controlling facts, current requirements, standards, legal/safety constraints or existing system behavior whenever needed, including before this sketch. The ordering applies to open-ended solution exemplars, not to factual verification. In small or reversible tasks, proceed directly with the simplest useful step.

### Solution-space discovery (conditional)

After the initial problem/solution sketch, when a proposal introduces substantial new capability, a custom mechanism, a product direction, or a consequential technical choice, check whether a ready-made solution, component, adjacent-domain mechanism, or simpler substitute could materially improve the owner's outcome before investing in detailed custom design. If the user explicitly requests an external landscape or current technology verification, research it directly instead of imposing a pre-search sketch.

- Frame the search from the user outcome/problem, not only the initially favored implementation or vocabulary.
- Look beyond direct competitors when material: adjacent categories, substitutes, reusable components, prior art, and instructive failures. Use independent discovery channels where one channel could hide viable approaches; follow new terminology or material references adaptively.
- Distinguish what has actually been inspected from what is only inferred from snippets or vendor claims. Prefer a short actionable comparison or direct trial over a research program.
- State material coverage gaps without claiming an exhaustive landscape. Stop when further discovery is unlikely to change the next practical choice, or when a cheap reversible implementation gives faster useful learning.
- If a simpler known solution is already adequate, proceed with it. Do not impose a mandatory discovery gate on bounded implementation, routine repairs, or owner-directed work whose relevant choice is settled.

After material external discovery, **reconcile** the initial mechanisms and frames with the observed alternatives against the same owner goals and constraints. Retain, adapt, combine, discard or reopen the problem framing when the evidence warrants it. Record consequential changes or the fact that prior art did not change the choice. Use `NO_LOCAL_DELTA` only when the project itself needs no material change; neither the initial idea nor an external precedent receives preference by default. For agent-facing proposals, compare appropriate instruction, skill, retrieval, deterministic tool, live connector, and no-new-surface mechanisms when knowledge delivery materially affects the choice.

This is a proportionate extension of construction and the local-delta check, not a separate skill, permanent artifact, independent approval step, mandatory benchmark, or requirement to prove comparative superiority. `loom-foo-research-design` remains the owner of an Evidence Plan when the real next task is methodological evidence planning.

### New concept identity test

When an architecture/process proposal introduces a new named reusable concept, primitive, layer, service, registry, contract, or framework, require it to earn an independent identity. Ask whether it owns a distinct semantic responsibility that cannot be represented cleanly by an existing owner, and whether an independent lifecycle/authority/versioning boundary is actually useful.

Otherwise prefer a smaller materialization such as a field, rule, view, fixture, policy clause, experiment artifact, or implementation detail.

### Composition test

If the proposal contains multiple independently decidable deltas, separate them enough that one can be accepted, rejected, deferred, or validated without forcing the same disposition on unrelated parts.

Do not split tightly coupled mechanics merely to manufacture modularity.
