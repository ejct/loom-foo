# Specification Contract


This reference defines the semantic artifact owned by `loom-foo-specification-design`. It does not create project authority or prescribe a universal document template.


## 1. Artifact family


The skill can emit:


- **Specification** — current semantic contract for one coherent subject.
- **Specification Delta** — explicit semantic change against one current Specification.
- **Specification Delta Set** — several related deltas across materially independent semantic subjects.


A Specification is about required semantics, not implementation structure.


## 2. Minimum recoverable contract


When material, a Specification should make recoverable:


- subject identity;
- baseline/version identity;
- controlling authority/provenance;
- scope and non-goals;
- relevant actors/external systems;
- required behavior;
- state/transition semantics;
- invariants;
- constraints;
- failure/edge behavior;
- compatibility obligations;
- acceptance conditions;
- assumptions/unresolved decisions;
- stable referenceability of material obligations.


Do not force empty headings.


## 3. Coherent semantic subject


Treat a Specification as one contract when its obligations share a meaningful semantic boundary.


Split when parts have materially independent:
- authority;
- version/lifecycle;
- compatibility/conformance boundary;
- semantic subject;
- downstream consumers.


Do not split based on implementation components alone.


Example:
A "Private Sharing" specification may contain grant, revoke, visibility, unauthorized-access and history-preservation obligations if they form one shared contract.


## 4. Requirement identity


A material obligation should be independently addressable.


Prefer stable semantic keys when practical, such as:
- `access-revocation`;
- `share-token-expiry`;
- `history-immutability`.


Use opaque IDs only when tooling, scale or governance benefits from them.


Changing wording without changing semantics should not require a new identity.


A materially changed obligation should preserve lineage to the prior identity where useful.


## 5. NEW_SPEC


Use when there is no current authoritative Specification for the subject.


Inputs:
- authoritative intent;
- accepted constraints;
- relevant existing project context.


Output:
a Specification describing the intended semantic state.


Do not invent requirements merely to make the artifact look complete.


## 6. EVOLVE_SPEC


Use when a current Specification exists.


First compare the accepted requested change with the current contract.


Possible outcomes:
- no semantic difference -> `NO_SPEC_DELTA`;
- one subject changes -> Specification Delta;
- several legitimate subjects change -> Specification Delta Set.


## 7. Delta semantics


Represent semantic effects, not text patches.


Useful delta operations:
- **ADD** — new obligation or allowed/required behavior;
- **MODIFY** — existing obligation changes semantics;
- **REMOVE** — existing obligation ceases to apply;
- **RENAME** — identity/name changes without intended semantic change, only when lineage matters.


A MODIFY entry should make recoverable:
- target obligation;
- prior semantics when needed for review;
- new semantics;
- reason/authority;
- affected acceptance conditions when material.


Do not use MODIFY when the behavior is actually unchanged and only prose is improved.


## 8. Preserve unaffected semantics


A delta should not silently reopen unrelated obligations.


For EVOLVE_SPEC:
- identify affected obligations;
- preserve unaffected accepted requirements;
- surface any compatibility consequence;
- distinguish direct changes from derived implications.


If the accepted change logically forces another obligation to change, mark that implication explicitly rather than silently rewriting it.


## 9. Acceptance contract


Acceptance conditions state what observable outcome distinguishes conformity from non-conformity.


They may be:
- state-based;
- event/response-based;
- invariant-based;
- boundary/tolerance-based;
- schema/interface-based;
- scenario-based.


They should not automatically prescribe the experimental method used to establish conformity.


## 10. Current truth vs proposal


A candidate Specification produced by this skill is not automatically the current accepted specification.


Keep separate:
- candidate semantic artifact;
- accepted/canonical Specification;
- implementation state.


Integration into durable project authority requires the appropriate project transition.


## 11. Fresh-reader test


A competent downstream reader with access to referenced authoritative sources should be able to answer:


- What subject is specified?
- Which source authorizes these semantics?
- What behavior is required?
- What behavior is forbidden or out of scope?
- What states/failures/boundaries matter?
- What must remain invariant?
- How can conformity be recognized in principle?
- For a delta, what exactly changed from the prior contract?


If these require hidden conversation reasoning, the artifact is not ready.