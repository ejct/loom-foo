# evidence-review — detailed conditional method (PD_EVIDENCE_REVIEW_LENSES.md)

> Source: exact private Loom-foo 0.35.1 `SKILL.md`. L1 retains activation, goal and authority precedence. Below sections are preserved in full, in source order; `references/...` paths refer to the owning skill root. Read this file only when its explicit L1 trigger applies.

## 5. Verify package integrity only as needed

Evidence acquisition owns faithful collection. Evidence review may perform bounded verification of already-referenced evidence when necessary to assess integrity, for example:
- the cited source actually supports the reported observation;
- subject/version/time identity matches;
- raw -> transformed lineage is coherent;
- a reported `COMPLETE_ZERO` is not obviously a failed acquisition mislabeled as zero.

Do not silently rerun the acquisition campaign or broaden the source universe.

If a package integrity defect prevents credible review, return `ACQUISITION_REPAIR_REQUIRED` with the exact defect and affected claim surface.

A legitimately partial package is not automatically defective; it may simply constrain the assessment.
## 7. Use only material review lenses

Read `references/REVIEW_LENSES.md` when the review is consequential or evidence is heterogeneous/conflicting.

Candidate lenses include:
- relevance/directness;
- acquisition completeness;
- internal validity / bias / contamination;
- measurement validity / uncertainty;
- independence / provenance;
- consistency / contradiction;
- scope / external validity;
- counterevidence / unresolved alternatives;
- selective reporting / survivorship;
- temporal validity.

These are lenses, not a mandatory scorecard. Do not produce a universal composite confidence score.
## 9. Treat absence/equivalence claims carefully

A zero/null/non-significant result can support scoped absence/equivalence only when:
- the acquisition actually completed;
- the plan/measurement was capable of detecting a meaningful alternative;
- precision/discriminating power is sufficient for the scoped claim;
- relevant validity limits do not undermine that inference.

Otherwise use `INSUFFICIENT` or `NON_DISCRIMINATING` rather than claiming evidence of absence.
## 10. Evaluate independence claim-specifically

Do not count as independent corroboration merely because there are multiple:
- citations copying one upstream report;
- agents using the same source/context;
- reports produced from the same underlying run;
- endpoints over the same dataset;
- observations of the same immutable event.

Surface shared lineage or correlated failure modes when material.

Do not invent an independence score.
## 11. Preserve counterevidence and unfavorable results

Review the controlling evidence set, including material counterevidence already present.

Do not:
- suppress unfavorable evidence;
- weaken the assessment because results contradict expectations;
- search for rescue evidence after seeing results unless a separate evidence-acquisition step is authorized and the controlling plan permits adaptation.

The review may identify a specific evidence gap or alternative explanation. It does not automatically authorize another research cycle.
## 12. Specialist framework precedence

The generic skill supplies cross-domain evidence-review semantics, not specialist expertise.

When a validated specialist framework is required for a material judgment:
- use the specialist framework/owner for that judgment when available;
- preserve its native outputs and assumptions;
- map only the decision-relevant result/limits into the Evidence Assessment.

Do not replace domain-specific statistical, scientific, safety, security, or architecture review with generic LoomLoom labels.
