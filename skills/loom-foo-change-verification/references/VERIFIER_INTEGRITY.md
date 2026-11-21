# Verifier Integrity

Use only when verifier mutation could materially change the verdict.

## Risk
A candidate may pass because tests/goldens/evaluator logic changed with it rather than because the protected property holds.

## Preserve enough provenance to distinguish
A. candidate passed stable/trusted verifier;
B. candidate changed/weakened/staled verifier and then passed.

Useful project-native evidence:
- verifier version/baseline/diff;
- changed tests/goldens/fixtures/evaluator configuration;
- authorization for verifier changes;
- negative/mutation/counterexample evidence;
- independently owned/frozen oracle where proportionate;
- golden update separated from normal verify;
- exact runtime/tool/environment.

## Non-goals
No universal verifier registry, mandatory hash, new evidence ontology, DSL, state machine, or Kernel primitive.

Verifier integrity is one evidence-quality concern inside verification, not a new owner.
