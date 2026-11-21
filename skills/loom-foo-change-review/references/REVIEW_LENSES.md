# Review Lenses

Use selectively.

## Functional / semantic correctness
Does changed behavior match controlling intent? Are edge states handled?

## Regression / compatibility
What previously working behavior could plausibly break? Are interfaces/data formats/backward compatibility affected?

## State / data / concurrency
Ownership, lifecycle, retries, idempotency, races, partial state, migrations.

## Failure / recovery
Timeouts, partial success, retry, rollback, restart, degraded states.

## Security / privacy / trust
Privileges, untrusted inputs, secrets, data exposure, trust-boundary changes. Escalate to specialist review when needed.

## Performance / resources
Only where the change plausibly alters load, latency, memory, network, cost, or capacity.

## Operability
Observability, diagnostics, safe recovery, configuration, rollout.

## Maintainability / accidental complexity
Coupling, duplicated truth, hidden ownership, brittle special cases, unnecessary abstraction.

## UX / product / accessibility
User-visible flow, error recovery, state clarity, regression, accessibility when material.

## Scope / authority / provenance
Unrequested changes, changed canonical artifacts, generated artifacts, unauthorized side effects, wrong base/subject.

## Migration / rollback
Forward/backward transition safety when stateful changes exist.

A smell is not a finding until consequence is demonstrated.
