# Failure Case — minimum evidence contract v0.1.1

This is an operational incident artifact, not a psychological or user-profile record. Populate only material fields supported by currently accessible evidence. Prefer an existing project-local incident or response receipt over copying an entire conversation.

```yaml
case_id:                   # stable project-local identifier, if persisted
trigger:
  kind: EXPLICIT_REPORT | OBSERVED_MATERIAL_ERROR | CONTEXTUAL_FRICTION_CUE | PORTFOLIO_REQUEST
  description:             # neutral summary; avoid reproducing insults
  source_locator:          # optional; only with access/permission
expected:
  behavior:
  authority:               # user instruction, accepted project rule, verified current skill
actual:
  behavior:
  evidence_locator:
  prior_failed_repairs: []  # only if material; do not invent inaccessible history
impact:
  task:
  recovery: RECOVERED | PARTIAL | BLOCKED | NOT_REQUIRED
observations: []
hypotheses: []             # include plausible rivals, never treat tone as root cause
unknowns: []
attribution:
  candidate_locus: UNKNOWN # or SKILL_SEMANTICS/ROUTING/COMPOSITION/etc.
  confidence: low | medium | high
learning:
  state: LOCAL_FIX_ONLY | FINDING_READY | EVIDENCE_REQUIRED | IMPROVEMENT_PROPOSED | NO_LOCAL_DELTA | ESCALATED
  proposed_delta:          # minimal owner-specific change, if justified
  candidate_owner:
  regression_test:
authority:
  external_write: NOT_AUTHORIZED | AUTHORIZED_AND_VERIFIED | NOT_APPLICABLE
  destination:
  disclosure_review:
```

## Evidence and privacy rules

- User criticism is evidence of a *reported* problem. The observed mismatch, verified mechanism and prevalence require their own evidence.
- Frustration, profanity, sarcasm and other interpersonal cues may motivate checking for an operational defect, but must never be stored as psychological data, inferred stable traits or a severity multiplier.
- Distinguish initial error from errors introduced by attempted repair. Verify against the original task and previously correct output.
- De-identify or minimize user quotations in portable test fixtures; no transfer to unrelated personal-assessment or profiling workflows.
- If a case is not persisted, leave `case_id` unset. Do not claim an external write because an artifact was drafted.
- If a case is based on a past inaccessible chat, use `NOT_OBSERVABLE` for the missing parts and do not backfill from assumptions.
