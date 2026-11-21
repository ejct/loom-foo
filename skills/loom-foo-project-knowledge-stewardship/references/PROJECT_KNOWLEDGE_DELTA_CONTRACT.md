# Project Knowledge Delta Contract

A Project Knowledge Delta is the compact logical closure of one authorized durable reconciliation.

## Required when material

- Triggering accepted/authorized transition.
- Authority basis for durable mutation.
- Exact authoritative source now governing the changed knowledge.
- Material project-native surfaces considered.
- Surfaces changed and their durable locators/identities.
- Supersession/current relation changed.
- Derived current views updated.
- Historical/provenance material preserved.
- Material surfaces intentionally untouched and why.
- Known remaining stale/inaccessible/conflicting surfaces.
- Primary disposition.

## Invariants

- It is not a database or second source of truth.
- It need not be persisted as a standalone file.
- It does not create acceptance/canonicalization authority.
- It does not duplicate Project Evidence Trail observations.
- `NO_DURABLE_DELTA` may require only a compact explanation.

## Example compact shape

Trigger: owner accepted Architecture v0.4 as current.
Authority: explicit owner decision D-17.
Changed: `00 Project Overview`, `01 Current Source Map`.
Superseded: Architecture v0.3 -> v0.4; v0.3 preserved.
Untouched: historical audit against v0.3 (historically accurate).
Remaining gaps: none.
Disposition: PROJECT_KNOWLEDGE_RECONCILED.
