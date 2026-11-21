# Evidence Assessment Contract

Status: candidate reference for `evidence-review v0.1.0-candidate`.

An Evidence Assessment is a bounded evaluation of what an existing Evidence Package/body can defensibly establish for a defined evidence question. It is not the final project decision.

## Required recoverability when material

A competent downstream decision-maker should be able to recover:
- exact evidence question/claim/outcome;
- reviewed package/body identity;
- applicable scope/population/environment/timeframe;
- material evidence mapped to the claim;
- support relation;
- material counterevidence/contradictions;
- validity/measurement/provenance/independence limits;
- uncertainty and scope limits;
- unresolved alternatives/evidence gaps;
- assessment disposition and stop reason.

## Claim-level relation

Prefer a scoped semantic relation over a binary verdict:
- `SUPPORTED_WITHIN_SCOPE`;
- `CONTRADICTED_WITHIN_SCOPE`;
- `MIXED`;
- `INSUFFICIENT`;
- `NON_DISCRIMINATING`.

The vocabulary is guidance, not a mandatory serialized enum.

## Assessment vs decision

An Evidence Assessment answers:
> What does this evidence defensibly establish, and with what limits?

It does not answer:
> What should the project do?

Do not convert evidence support into acceptance, promotion, release, architecture selection, product choice, or another authority transition.

## Package completeness

Package completeness and evidence support are distinct.

Examples:
- complete package + non-discriminating evidence -> `EVIDENCE_ASSESSMENT_READY` with `NON_DISCRIMINATING`;
- partial but high-quality package -> may still support some claims, but assessment scope must narrow;
- invalid/mislabeled acquisition state -> `ACQUISITION_REPAIR_REQUIRED` when it prevents credible review.

## Pointwise before body-level synthesis

For heterogeneous or consequential evidence:
1. identify material claims/outcomes;
2. map relevant evidence items;
3. assess each item enough to understand relevance/validity/provenance/scope;
4. identify correlated lineage and contradictions;
5. synthesize only after those distinctions are visible.

## No composite score by default

Do not combine relevance, validity, independence, consistency, precision, generalizability, or recency into a generic number.

A score is allowed only when a controlling domain/plan defines and validates it.

## Confidence

If useful, confidence refers to confidence in the assessment under the stated evidence and scope, not metaphysical confidence that the claim is globally true.

Explain the material basis. Avoid fake numerical precision.

## Evidence gaps

An assessment may identify the smallest evidence gap that prevents stronger inference. This does not itself authorize collection or create a new Evidence Plan.
