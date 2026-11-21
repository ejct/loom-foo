# Findings and Severity

Use findings to express a defect/risk independently from any proposed implementation fix.

## Finding fields
- id when repeated cycles matter;
- severity;
- confidence when material;
- category/scope;
- claim;
- evidence;
- consequence/failure path;
- affected requirement/invariant/scenario;
- resolution criterion;
- status.

## Severity
- CRITICAL — invalidates the primary change objective or creates unacceptable correctness/safety/authority risk.
- MAJOR — material defect/regression/risk; candidate may remain viable after remediation.
- MODERATE — bounded meaningful weakness.
- MINOR — low-risk quality/polish issue.

Severity is consequence, not certainty.

## Confidence
Use HIGH/MEDIUM/LOW only when it adds value. Low confidence can still accompany high potential severity and justify targeted validation.

## Resolution criteria
Say what must become true, not necessarily how to implement it.

## Status
OPEN | RESOLVED | REJECTED | ACCEPTED_RISK.

Do not create findings merely to demonstrate review activity.
