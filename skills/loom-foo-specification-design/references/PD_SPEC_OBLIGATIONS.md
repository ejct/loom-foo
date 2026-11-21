# Spec Obligations — conditional methodology

> Applies only when the owning `SKILL.md` conditional index selects it. Moved from the v0.29.0 root. References mentioned as `references/X.md` inside quoted historical text are relative to the *owning skill directory*, not this file. General L1 authority and current use-first instructions prevail over superseded historical clauses.

## 5. Derive obligations from authoritative intent


Translate intent into obligations that downstream work can reference.


When material, cover:


- observable behavior;


- state and transition semantics;


- preconditions and triggers;


- constraints;


- invariants;


- external/interface semantics;


- compatibility requirements;


- failure behavior;


- cancellation/interruption behavior;


- edge and boundary cases;


- privacy/security obligations;


- quality/performance obligations only when they are semantically required;


- acceptance conditions.


Do not force every category into every Specification.


Prefer one independently checkable obligation per requirement statement.


For detailed quality checks, read `references/REQUIREMENT_QUALITY.md`.
## 6. Separate required semantics from solution choice


Remove implementation choices that are not themselves accepted constraints.


Bad:


"Store revoked grants in Redis."


Better:


"A revoked grant must no longer authorize future access within the accepted propagation bound."


An implementation property may remain when the property itself is authoritative, for example:


- must operate fully offline;


- must preserve protocol v2 compatibility;


- must use an existing mandated storage format;


- must satisfy a regulator/vendor/platform constraint.


When unsure whether a detail is semantic or architectural, ask:


"If another implementation could satisfy the same externally required behavior without this detail, is the detail still required by authority?"


If not, keep it out of the Specification.
## 7. Use the narrowest useful representation


The semantic contract is primary; notation is conditional.


Possible representations include:


- concise normative prose;


- EARS-like event/condition/response requirements;


- Given / When / Then scenarios;


- state-transition tables or diagrams;


- interface/schema contracts;


- invariants or properties;


- examples and counterexamples;


- formal models when consequence and complexity justify them.


Do not require user stories, EARS, Gherkin, SHALL syntax, formal methods, or numeric IDs by default.


Read `references/BEHAVIORAL_PATTERNS.md` when ordinary prose is not enough to represent the behavior cleanly.
## 8. Make acceptance decidable


For each material obligation, make it possible in principle to distinguish conforming from non-conforming behavior.


Specification owns:


- the required observable condition;


- allowed/disallowed states;


- semantic tolerance/bounds when they are part of the requirement.


Specification does not automatically own:


- sample size;


- benchmark design;


- measurement harness;


- repetition count;


- statistical method;


- evaluator independence.


If proving the requirement needs non-trivial evidence design, preserve the acceptance contract and hand the empirical-method question to `loom-foo-research-design`.


If an exact candidate later needs to be checked against the contract, that belongs to `loom-foo-change-verification`.
## 9. Preserve traceability proportionally


Every durable Specification should make recoverable:


- subject identity;


- baseline/version identity;


- controlling authority/provenance;


- stable referenceability of material obligations.


Use semantic identifiers when practical, for example:


- `access-revocation`;


- `unauthorized-history-visibility`;


- `context-restoration-fidelity`.


Opaque numeric IDs are optional.


Backward trace should answer:


"Why does this obligation exist?"


Shared provenance can be declared once at Specification level. Add requirement-level provenance only when the source materially differs.


Do not manufacture future trace links before downstream artifacts exist. Forward trace should grow incrementally as architecture decisions, work units, tasks, and verification evidence appear.


Read `references/TRACEABILITY.md` for consequential or evolving specifications.
