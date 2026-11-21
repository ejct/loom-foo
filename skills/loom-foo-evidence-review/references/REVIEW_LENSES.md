# Evidence Review Lenses

Status: candidate reference for `evidence-review v0.1.0-candidate`.

Use only lenses that can materially change the evidence relation or its scope.

## Relevance / directness

Ask whether the evidence actually bears on the target claim, outcome, population, environment, timeframe, and causal/descriptive relation being asserted.

Indirect evidence can be useful; it must not silently license a direct claim.

## Acquisition completeness

Check whether missing, not-run, access-blocked, partial, excluded, or substituted plan items materially alter interpretation.

A valid `COMPLETE_ZERO` is an observation. A failed acquisition is not.

## Internal validity / bias / contamination

Consider only applicable risks:
- confounding;
- selection bias;
- contamination/leakage;
- evaluator dependence;
- self-report/self-certification;
- intervention implementation differences;
- missing negative/failure cases;
- uncontrolled environment differences.

Do not cargo-cult experimental terminology into simple source verification.

## Measurement validity / uncertainty

Ask:
- does the metric/oracle measure the target property?
- is measurement resolution sufficient?
- could the proxy be improved without improving the real property?
- can measurement error or model/parser uncertainty change the conclusion?

Use domain-specific uncertainty methods when required.

## Independence / provenance

Check whether purportedly corroborating items have shared upstream lineage or correlated failure modes.

Separate artifact count from independent information.

## Consistency / contradiction

Determine whether apparently conflicting evidence is actually comparable.

Differences may arise from:
- scope;
- environment;
- time;
- version;
- method;
- population;
- measurement semantics.

If the contradiction remains after those distinctions, preserve it as unresolved rather than selecting a convenient winner.

## Scope / external validity

Bound claims to what was tested/observed. A local run, narrow sample, single account/runtime, historical cohort, or selected case set does not automatically generalize.

## Counterevidence / unresolved alternatives

Surface evidence already in the controlling package that materially limits the claim. Identify plausible alternatives only when they follow from the evidence/plan strongly enough to affect inference.

Do not turn alternative-generation into speculative objection lists.

## Selective reporting / survivorship

Use when the acquisition process could hide failed, negative, inaccessible, or excluded cases.

Do not infer publication/selection bias merely because a result is positive.

## Temporal validity

For changing systems/products/markets/policies, check whether evidence age and known changes limit current claims.

Recency alone is not quality; temporal fit depends on the target property.

## Lens closure

For every lens used, connect it to a consequence for:
- support relation;
- assessment confidence;
- scope;
- or evidence gap.

Do not append unused caveats.
