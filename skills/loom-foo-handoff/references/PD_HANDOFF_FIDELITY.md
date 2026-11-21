# handoff — detailed conditional method (PD_HANDOFF_FIDELITY.md)

> Source: exact private Loom-foo 0.35.1 `SKILL.md`. L1 retains activation, goal and authority precedence. Below sections are preserved in full, in source order; `references/...` paths refer to the owning skill root. Read this file only when its explicit L1 trigger applies.

## 9. Handoff Quality Gate

Read `references/HANDOFF_QUALITY_CONTRACT.md`.

Before final emission, test whether H0 faithfully restores the workstream.

Review H0 for:
- missing accepted decisions;
- missing constraints/invariants;
- missing material semantic/domain invariants;
- blurred scope/ownership boundaries;
- false completion;
- lost authority boundaries;
- lost persistence state;
- missing blockers;
- missing material negative knowledge;
- lost active reasoning frontier;
- stale external state;
- missing provenance;
- ambiguous resumption;
- overcompression;
- overinclusion.
## 10. Restoration Fidelity Test

For consequential handoffs, perform:

`REFERENCE CHECKPOINT -> H0 -> RECEIVER RECONSTRUCTION R0 -> COMPARE -> H1 if needed -> regression check`

The reference checkpoint must be built from explicit conversation/project evidence, not hidden reasoning.

Prefer a genuinely fresh evaluator/context when available.

If the same context performs the test, call it a **fresh receiver simulation** or **fidelity self-review**, not an independent receiver.

The receiver should be able to answer from H0:
- What is the current state?
- What is accepted?
- Which semantic/domain invariants and scope boundaries must remain true?
- What is pending/deferred/blocked?
- What must not be done or silently reintroduced from rejected alternatives?
- What authority exists for the next transition?
- Where should work legitimately resume?
- If the workstream is mid-exploration, what unresolved reasoning frontier is currently active?

If material reconstruction differs from the reference, revise H0.

Usually one fidelity revision plus one fresh regression check is sufficient; continue only while material information is changing.
## 11. Fidelity disposition

Use internally:

### `HANDOFF_READY`
Material operational state can be reconstructed without inventing authority or losing the resumption point.

### `HANDOFF_DEGRADED`
A usable handoff can be emitted, but material unknown/unverified state must be explicit.

### `HANDOFF_BLOCKED`
The checkpoint cannot be safely compiled because ambiguity or missing material evidence prevents a defensible transfer.

These are skill-local dispositions, not Kernel lifecycle states.
## 12. Context Receipt boundary

The handoff states what the producer transfers.

The receiver Context Receipt records what the receiver actually read, verified, excluded, corrected, or leaves unresolved.

Do not make the producer handoff pretend to be the receiver's Context Receipt.

When material external verification occurs, prefer claim-level receipt evidence:

```yaml
verification:
  - subject: <material claim or tightly related claim group>
    source: <source locator>
    result: CONFIRMED | CORRECTED | UNVERIFIED | CONFLICTING
    note: <optional concise material detail>
```

`CORRECTED` requires a source authoritative for the relevant dimension. Mere disagreement is not enough. If material disagreement cannot be resolved by authority, preserve it as `CONFLICTING`.

If no material external verification is needed, do not emit a ceremonial verification section.
