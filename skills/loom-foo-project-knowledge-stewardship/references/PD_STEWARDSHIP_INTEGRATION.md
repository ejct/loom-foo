# project-knowledge-stewardship — detailed conditional method (PD_STEWARDSHIP_INTEGRATION.md)

> Source: exact private Loom-foo 0.35.1 `SKILL.md`. L1 retains activation, goal and authority precedence. Below sections are preserved in full, in source order; `references/...` paths refer to the owning skill root. Read this file only when its explicit L1 trigger applies.

## 9. Runtime projection boundary

If an accepted change makes a runtime routing/memory/instruction projection stale:
- identify the projection as a downstream durable surface only when project policy requires it;
- preserve its non-canonical status;
- require the relevant action authority before applying it;
- never claim an account/runtime setting or memory update happened unless it actually did.

A runtime projection is not a substitute for canonical project sources.
## 10. Relation to Project Evidence Trail

Decision 07 owns compact project-local evidence/continuity policy.

This skill may update PROJECT_STATE or equivalent when a durable transition changes continuation-relevant state, but:
- PROJECT_STATE is not a universal database;
- observations.jsonl is not duplicated into Project Knowledge Delta;
- Project Knowledge Delta is not a new evidence trail.
## 11. Relation to K12 Reconciliation

K12 remains the Kernel lifecycle primitive. This skill is a project-level procedural projection of durable reconciliation.

It must add value beyond “remember to update docs” by:
- resolving project-native owners/surfaces;
- respecting authority and supersession;
- minimizing the consistency surface;
- preserving history;
- making the actual durable delta inspectable.

No K13, knowledge registry, or reconciliation service is created.
## 12. Relation to producing skills

Producing a proposal/specification/architecture/review/verification/Decision Surface does not canonize it.

After an explicit authority transition, this skill may perform durable integration so producing skills do not each duplicate supersession/index/status mechanics.
## 14. Partial reconciliation

If only part of the authorized consistency set can be updated:
- preserve correct completed updates;
- identify exact stale/inaccessible remaining surfaces;
- distinguish missing action authority from missing capability;
- give the smallest repair path.

Do not pretend full consistency or roll back useful changes solely to simulate atomicity when the project storage model does not support it.
