# Handoff Quality Contract

## Purpose

Framing validity is necessary but insufficient. A handoff is high quality only when a receiver can reconstruct the material operational state accurately enough to continue without inventing authority, losing constraints, or reopening settled work.

## Reference checkpoint

Before fidelity review, establish a compact reference model from explicit evidence:

```yaml
current_intent:
accepted_decisions:
constraints:
scope_boundaries: # when material
semantic_invariants: # when material
completed:
persistence:
pending:
deferred:
blocked:
authority_boundaries:
negative_knowledge:
active_reasoning_frontier: # when material
dynamic_external_state:
artifacts:
resumption_point:
unknowns:
```

Do not fill absent categories merely for completeness.

## Producer completeness review

Compare H0 against the reference checkpoint.

Failure classes:

- `MISSING_DECISION`
- `MISSING_CONSTRAINT`
- `MISSING_SEMANTIC_INVARIANT`
- `SCOPE_BOUNDARY_BLUR`
- `FALSE_COMPLETION`
- `LOST_AUTHORITY_BOUNDARY`
- `LOST_PERSISTENCE_STATE`
- `MISSING_BLOCKER`
- `MISSING_NEGATIVE_KNOWLEDGE`
- `LOST_REASONING_FRONTIER`
- `STALE_STATE`
- `MISSING_PROVENANCE`
- `MISSING_PRODUCER_VERIFICATION_TRACE`
- `VERSION_IDENTITY_AMBIGUITY`
- `AMBIGUOUS_RESUMPTION`
- `OVERCOMPRESSION`
- `OVERINCLUSION`


## Claim-driven verification

Source availability does not create a requirement to read every referenced artifact.

Verify a source only when it can materially change:
- current state;
- action/transition authority;
- persistence;
- blocker / unknown / conflict status;
- resumption point.

Prioritize verification when claims are `UNKNOWN`, `UNVERIFIED`, `STALE`, or `CONFLICTING`, when they describe mutable external state, when currentness/authority is uncertain, or when observed and prescribed state disagree.

Inspect the smallest source slice sufficient to resolve the claim.

Distinguish producer verification from receiver verification.

If the producer materially reads external/current sources while compiling H0, preserve a compact producer-owned trace in the handoff itself:

```yaml
producer_verification:
  - subject:
    source:
    result: CONFIRMED | CORRECTED | UNVERIFIED | CONFLICTING
    as_of: # optional when currentness matters
    note:
```

If the receiver materially verifies claims after restoration, keep that result in the receiver-owned Context Receipt:

```yaml
verification:
  - subject:
    source:
    result: CONFIRMED | CORRECTED | UNVERIFIED | CONFLICTING
    note:
```

`CORRECTED` requires dimension-specific authority. Mere disagreement is not correction. Preserve unresolved authoritative disagreement as `CONFLICTING`.

If no material external verification is needed on a given side, do not add a ceremonial verification section for that side. A producer source list alone is not a producer verification trace.

For Chat/Text, also verify representation identity:
- `Protocol` identifies the Chat/Text transport contract;
- `Compiler` identifies the handoff skill/compiler version;
- differing numeric versions are allowed because these are independent version lines;
- missing/ambiguous identity is a representation defect, not evidence that one version should be silently normalized to the other.

Additional failure classes:
- `OVER_VERIFICATION`
- `UNJUSTIFIED_CORRECTION`
- `CONFLICT_NORMALIZATION`
- `OUTPUT_BOUNDARY_LEAK`
- `AUTHORITY_DUPLICATION`
- `AUTHORITY_AMBIGUITY`

## Receiver reconstruction

Give only H0 to the fresh receiver/simulation.

Reconstruct:

```yaml
current_state:
accepted:
material_scope_boundaries: # when material
material_semantic_invariants: # when material
material_negative_knowledge: # when material
pending_deferred_blocked:
forbidden_or_unauthorized_transitions:
next_authorized_or_legitimate_transition:
resumption_point:
active_reasoning_frontier: # when material
material_unknowns:
verification: # only when material external verification occurred
  - subject:
    source:
    result:
```

Compare with the reference checkpoint.

A fact may be worded differently and still match. Judge operational meaning, not textual identity.

## Revision

Adjudicate each material mismatch before editing.

Revise the smallest affected part of H0.

Regression-check previously correct high-risk fields:
- accepted decisions;
- material semantic invariants;
- scope/ownership boundaries;
- authority;
- persistence;
- blockers;
- material negative knowledge;
- resumption and active reasoning frontier.

## Stop

Use `HANDOFF_READY` when no material mismatch remains and another pass has low expected information value.

Use `HANDOFF_DEGRADED` when unknown/unverified state remains but is represented safely.

Use `HANDOFF_BLOCKED` when missing/ambiguous evidence prevents safe transfer.

## Compactness

A larger handoff is not automatically more faithful.

Treat receiver reread burden and duplicated project state as costs.

Prefer references to authoritative retrievable artifacts over copying large bodies when the receiver can retrieve them safely.

Do not treat a source list as a verification checklist.

For design-heavy or research-heavy workstreams, preserve semantic invariants and the active reasoning frontier only when losing them could change the next decision, permit a previously rejected interpretation, or cause the receiver to resume at the wrong conceptual boundary. Do not copy exploratory prose merely to preserve “context”.

Prefer one generic authority invariant plus one checkpoint-specific authority section. Repetition is justified only when it adds a materially different action-specific boundary.

For Chat/Text, receiver output after `END OPERATIONAL HANDOFF` is a separate artifact and must not be folded back into TRANSFERRED STATE. HANDOFF CONTROL may instruct the receiver to create a later Context Receipt; the instruction itself is not receiver output.
