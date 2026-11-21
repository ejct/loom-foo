# Decision Surface Contract

A Decision Surface is a bounded decision-support artifact, not the decision authority record itself.

## Required semantic questions

When material, a reader should be able to answer:
- What exact decision is being made?
- What subject/version/scope does it bind to?
- Who has authority to decide?
- What alternatives are actually viable?
- What current baseline/status quo exists?
- Which hard constraints eliminate options?
- Which owner criteria/preferences distinguish the remaining options?
- What does current evidence establish for each material alternative/criterion?
- What assumptions remain?
- What uncertainty could change the recommendation?
- Is the decision reversible and what is the cost of delay/lock-in?
- What option/disposition is recommended, or what exact owner choice remains unresolved?
- What authority transition follows?

## Recommendation semantics

Recommendation can be:
- one preferred option;
- ACCEPT / REVISE / REJECT / DEFER / EXPERIMENT_FIRST / NO_LOCAL_DELTA;
- explicit unresolved owner choice when alternatives remain non-dominated.

Recommendation is advisory unless a separate authority mechanism accepts it.

## Fast path

Small reversible decisions should avoid matrices and long memos. Preserve only the decisive inputs, recommendation/unresolved choice, switch condition, and authority boundary.
