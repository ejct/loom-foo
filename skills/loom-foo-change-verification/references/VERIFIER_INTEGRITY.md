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

## P4 — real permissions and acceptance-oracle integrity

Distinguish a role contract (`INSTRUCTION_ONLY`), observed `HOST_ENFORCED_READ_ONLY`, and `NOT_CONFIRMED`. A prompt, role label, fresh context or omitted Write/Edit API does **not** prove shell and other mutation paths are blocked. Use actual sandbox/permission controls where available and authorized; a negative write probe must use safe scratch fixtures, never mutate a protected production artifact.

When candidate and test/golden/evaluator changes coexist, compare relevant verdict-producing files and commands with the **pre-change oracle baseline**. Classify an unchanged oracle, an independently justified **authorized oracle update**, or unexplained/unapproved tampering separately. A green suite after weakening an acceptance assertion is insufficient. Hash/readback/diff detects change; it does not enforce immutability. If enforcement or integrity is unobserved, qualify the verdict; do not claim protected tests merely because a synthetic example detects tampering.

A synthetic mutation regression proves only its own detector. Actual host-enforced read-only needs separate runtime-native observation, and a reviewer that can inspect independently is not automatically permission-sandboxed.
