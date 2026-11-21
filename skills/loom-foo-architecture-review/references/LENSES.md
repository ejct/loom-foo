# Architecture Review Lenses

Use adaptively.

## Correctness and invariants
Invalid states, ordering assumptions, lost updates, duplicated effects, domain invariants, recovery semantics. For quantitative or temporal systems also inspect units/dimensions, normalized vs absolute domains, coordinate/reference frames, canonical clocks/timebases and conversion, cyclic/wrapped vs unwrapped state, and event semantics across discontinuities.

## Boundaries and ownership
Canonical ownership, duplicate responsibility, split-brain ownership, boundary leakage, shared models, authority/versioning boundaries.

## State, consistency, concurrency
Source of truth vs derived state, stale reads, multiple writers, atomicity, retry/idempotency, races, ordering, reconciliation. Check whether one enum/state machine incorrectly collapses independent axes such as connectivity, authority, lifecycle, capacity, health, or relationship state.

## Dependencies and coupling
Cycles, hidden runtime coupling, dependency direction, provider assumptions, blast radius, replaceability, synchronous chains/fan-out.

## Failure and recovery
Partial success, crash between effects, retry storms, duplicate delivery, dependency unavailability/slowness, recovery source of truth, cancellation, operator intervention.

## Performance and capacity
Only when driven: bottleneck, queueing, fan-out, state growth, hot resources, latency budget, backpressure, scaling axis, cost curve.

## Security and trust
Only when relevant: trust boundaries, authentication/authorization, privilege/confused-deputy, secrets, sensitive data, tenant isolation, untrusted input, side effects.

## Operability and observability
Diagnosability, state visibility, distinguishing correctness/policy/infra failure, rollback/recovery, ownership/on-call, health/SLO signals, audit/provenance.

## Evolvability and complexity
Migration, compatibility/versioning, reversibility, speculative abstraction, duplicated primitives, replaceability, lifecycle justification, simplest sufficient structure.

Smells are probes. They become findings only when a consequence is demonstrated.
