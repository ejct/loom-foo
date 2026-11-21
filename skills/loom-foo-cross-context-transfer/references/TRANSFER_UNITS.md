# Transfer Units & Structural Mapping

A Transfer Unit preserves a relationship, not a noun.

```yaml
id:
type:
source_context:
problem:
forces:
mechanism:
consequence:
invariants:
boundary_conditions:
assumptions:
evidence_status:
authority_status:
failure_history:
rejected_alternatives:
source_support:
source_conflicts:
source_version:
transfer_hypothesis:
```

Useful types:
`PRINCIPLE | INVARIANT | DECISION | MECHANISM | METHOD | CONTRACT | EVIDENCE | FAILURE_LESSON | ANTI_PATTERN | VALIDATION_METHOD`

Map:

```text
source problem      <-> target concern
source forces       <-> target forces
source invariant    <-> target invariant
source mechanism    <-> possible target mechanism
source consequence  <-> expected target consequence
boundary conditions <-> target conditions
```

Context mismatch probes:
scale, lifecycle, trust/authority, persistence, concurrency, deployment, organization, users, regulation/platform, time/cost, data semantics.

If the source implementation exists mainly because of a force absent in target, prefer transferring the principle rather than the implementation.

Negative knowledge is first-class.
