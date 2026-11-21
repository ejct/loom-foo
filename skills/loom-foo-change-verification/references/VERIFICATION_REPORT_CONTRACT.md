# Verification Report Contract

## Primary question
For this exact candidate, what specified properties can be established relative to the controlling contract/acceptance criteria?

## Primary artifact
Verification Report.

## Material fields
- exact candidate and base;
- controlling contract/criteria;
- verification surface;
- property -> check/evidence -> result;
- environment/fidelity;
- verifier/oracle provenance when material;
- regression surface;
- NOT_COVERED / unsupported claims;
- disposition;
- claim limits.

## Property results
PASS | FAIL | INCONCLUSIVE | NOT_COVERED.

## Core invariants
`PASS != ACCEPTED`
`PASS != DEFECT_FREE`
`NOT_COVERED != PASS`

## Completion
Verification closes when the declared material verification surface has honest criterion-level results and evidence/limits for the exact subject.
