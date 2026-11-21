# Traceability


This reference defines the minimum traceability discipline for specification-design. The goal is useful lineage and impact analysis, not a documentation bureaucracy.


## 1. Traceability purposes


Traceability should answer practical questions such as:
- Why does this requirement exist?
- Which current obligation is this delta changing?
- Which downstream architecture/work/verification artifacts depend on this obligation?
- Which accepted behavior may be affected by a proposed change?
- Is an implementation feature unsupported by any accepted requirement?
- Is a requirement unimplemented or unverified?


Do not maintain trace data that cannot answer a real question.


## 2. Universal minimum


For a durable Specification, preserve:
- semantic subject identity;
- baseline/version identity;
- controlling authority/provenance;
- stable identities for material obligations.


This is the minimum needed for later composition.


## 3. Backward provenance


A material requirement should be able to answer:
"Why does this obligation exist?"


Possible sources:
- accepted proposal/decision;
- explicit owner instruction;
- accepted external standard;
- regulatory/platform contract;
- current compatibility obligation;
- derived requirement from another accepted obligation;
- accepted architecture constraint.


If most requirements share one source, declare that provenance at Specification level.


Add requirement-level provenance when:
- the source differs;
- the authority differs;
- the derivation is non-obvious;
- the source may be independently revised;
- later impact analysis benefits from the link.


Do not duplicate the same source citation on every line without value.


## 4. Stable obligation identity


Prefer semantic keys that survive wording edits.


Example:


`access-revocation`
`history-immutability`
`unknown-field-tolerance`


An identity should change only when:
- the obligation is replaced by a materially different semantic concept; or
- preserving the old identity would misrepresent lineage.


For a semantic modification, normally retain the identity and record a new version/delta.


## 5. Delta lineage


A Specification Delta should link every material change to the current obligation it affects.


For each delta item, preserve as needed:
- operation: ADD / MODIFY / REMOVE / RENAME;
- target obligation identity;
- controlling change authority;
- prior semantic state where review requires it;
- new semantic state;
- derived affected obligations;
- compatibility impact.


Textual line diffs are not semantic lineage.


## 6. Forward trace grows later


Do not create empty placeholders for artifacts that do not yet exist.


Forward trace can accumulate:


Requirement
→ Architecture decision/component
→ Work unit
→ Task Brief
→ implementation surface
→ verification evidence


Each downstream owner is responsible for adding the link it creates.


specification-design should make the source obligation stable enough to reference.


## 7. Trace strength by consequence


### Lightweight


For a small reversible change:
- Specification source;
- stable requirement names;
- delta links.


### Normal


For shared or persistent behavior:
- requirement-level provenance where sources differ;
- architecture/work references as they appear;
- explicit delta lineage.


### High assurance


For safety/security/regulatory/compatibility-critical contracts, consider:
- bidirectional coverage checks;
- explicit verification association;
- versioned external normative sources;
- derived-requirement rationale;
- orphan detection;
- change-impact review.


Use stronger rigor only when it protects a material property.


## 8. Orphan checks


Two useful anomaly classes:


### Requirement orphan
A material implementation/architecture obligation exists with no accepted semantic or constraint source.


Possible causes:
- gold plating;
- hidden architecture constraint;
- missing requirement;
- stale implementation.


Do not assume which cause applies.


### Downstream orphan
A material accepted requirement has no downstream realization or verification when one should exist.


This is a later project-state observation, not necessarily a defect in specification-design.


## 9. Cross-artifact consistency


Traceability enables later checks such as:
- requirement changed but architecture/task still references old semantics;
- task acceptance criterion is weaker than its source requirement;
- verification tests only an example, not the normative rule;
- architecture introduces an unsupported behavioral restriction.


specification-design does not own these later audits. It provides stable semantic anchors.


## 10. Authority transitions


Trace links do not create authority.


A candidate Specification can cite an accepted decision, but the Specification itself remains candidate until accepted through the project’s authority process.


Likewise:
- implementation is not accepted because it links to a requirement;
- a verification result does not canonicalize the Specification;
- a reviewer link does not supersede source authority.


## 11. Traceability anti-patterns


Avoid:
- requirement IDs with no semantic stability;
- giant trace matrices populated with future placeholders;
- duplicating entire source documents instead of referencing them;
- treating implementation location as the source of requirement truth;
- silently changing requirement identity to avoid recording a delta;
- forward links that are guessed rather than observed;
- one numeric "coverage" score that hides missing critical obligations;
- treating traceability as proof of correctness rather than lineage.