# Spec Quality — conditional methodology

> Applies only when the owning `SKILL.md` conditional index selects it. Moved from the v0.29.0 root. References mentioned as `references/X.md` inside quoted historical text are relative to the *owning skill directory*, not this file. General L1 authority and current use-first instructions prevail over superseded historical clauses.

## 10. Quality gate before SPEC_READY


Challenge the artifact before returning it.


### Necessity


Does each material obligation have legitimate intent/provenance?


### Ambiguity


Could competent downstream readers derive materially different behavior?


### Singularity


Does one statement hide several independently decidable obligations?


### Completeness


Are material states, transitions, negative paths, failures, cancellation, boundaries, or compatibility effects missing?


### Consistency


Do requirements conflict with each other or accepted constraints?


### Verifiability


Can conforming and non-conforming behavior be distinguished in principle?


### Solution leakage


Has an architectural convenience been elevated into required semantics?


### Overconstraint


Does the Specification unnecessarily eliminate valid solution space?


### Delta regression


For EVOLVE_SPEC, does the new semantic state preserve unaffected accepted obligations and expose changed ones clearly?


Repair authoring defects before declaring readiness.


This is author-owned quality validation. Do not describe it as an independent audit.
## 11. Handle uncertainty without inventing semantics


Use this order:


1. resolve from current authoritative context;


2. derive only when the implication is logically required;


3. use a bounded explicit assumption only when it does not choose a materially different product/system behavior;


4. ask for or route to the missing owner when the ambiguity changes the semantic contract.


If the unresolved question is empirical, return `VALIDATION_REQUIRED` and identify the exact semantic uncertainty that requires evidence.


If the unresolved question is an authority/product decision, return `NEED_CONTEXT` or `BLOCKED` as appropriate.


Do not hide ambiguity by writing more prose.
## 12. Minimize the artifact


A small, obvious, reversible change should produce a small Specification or Delta.


Do not optimize for:


- requirement count;


- document length;


- number of headings;


- number of scenarios;


- traceability volume;


- formal notation.


Retain only structure that protects semantic clarity, conformance, compatibility, authority, or downstream reuse.
## 13. Emit the semantic artifact


The output should make these dimensions recoverable when material:


- `status`;


- subject and baseline;


- authority/provenance;


- scope/non-goals;


- actors/external systems;


- requirements / obligations;


- state/transition semantics;


- invariants;


- constraints;


- failure/edge behavior;


- acceptance conditions;


- assumptions/unresolved decisions;


- delta classification when evolving a current Specification;


- downstream implications or handoff.


Do not force empty sections.
## 14. Output states


Use exactly one primary skill-local disposition.


### `SPEC_READY`


A Specification, Specification Delta, or Delta Set is sufficiently precise for downstream use.


### `NO_SPEC_DELTA`


The accepted requested semantics are already represented by the current Specification.


### `VALIDATION_REQUIRED`


A material semantic decision depends on empirical evidence. Preserve the strongest bounded contract possible and identify the uncertainty that should go to `loom-foo-research-design`.


### `NEED_CONTEXT`


A specific authoritative source, subject identity, baseline, or product decision is missing.


### `PLANNING_REQUIRED`


The request actually contains several materially independent semantic subjects whose authority or contract boundaries must be separated before a defensible specification can be produced.


Do not use this merely because a coherent Specification is large.


### `BLOCKED`


Conflicting authority or another non-empirical prerequisite prevents a defensible semantic contract.


These are skill-local workflow states and do not accept, canonicalize, publish, or release the Specification.
