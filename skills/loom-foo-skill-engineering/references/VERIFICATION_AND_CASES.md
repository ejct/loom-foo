# Verification and exact claim semantics

Use proportionate checks tied to exact candidate/version and intended runtime. Do not convert one test into a broad performance claim.

## Evidence layers

1. STATIC: valid YAML and schema, version, files, references, executable scripts, distribution/privacy scan.
2. DISCOVERY: host sees exact skill identity and package version.
3. ROUTING: realistic fresh-context prompts select or reject the skill correctly relative to siblings.
4. EXECUTION: activated skill produces the correct artifact and preserves task/authority boundaries.
5. FIELD: usefulness of actual work and human correction burden.
6. COMPARATIVE: matched frozen conditions/oracle, uncontaminated C0 and C1, comparable runtime and explicit harm/cost handling; `loom-foo-skill-validation` owns frozen-plan execution only when installed in the current runtime. Otherwise report the optional owner unavailable; do not improvise a substitute campaign.

## Routing fixtures are not routing results

`tests/routing_cases.json` separates three **different things**:
- `expected_owner`: the skill that ought to activate, or `none`;
- `expected_mode`: the skill-engineering operation, only when expected owner is `loom-foo-skill-engineering`;
- `expected_decision`: an expected *post-activation recommendation* for explicit skill-necessity questions, never a routing label.

Do not make skill quality claims from the fact that an author filled these expectations. To evaluate automatic routing, run prompts in independent, representative fresh contexts with actual skill catalog, document raw selected owner/version and compare with the frozen oracle. Avoid exposing the oracle to the selecting executor. A same-context rehearsal is diagnostic and cannot validate its own claimed automatic routing.

## Change gates

- For a small metadata wording change: static constraints + one positive and negative routing case as feasible.
- For a logic change: complete impact contract checks, an edge/failure case, and nearby regression.
- For a portfolio boundary change: competing-owner cases, absence of accidental activation, and a representative multi-skill handoff scenario.
- For an installation claim: inspect actual installed location and runtime discovery; source or ZIP alone is insufficient.
- For causal-lift claims: freeze eval plan *before* observing outcomes; holdouts are not construction examples.

## Static checker

Local **self-package-only** helper: `python scripts/validate.py` (requires PyYAML) and `python -m unittest discover -s tests -v`. This checker is tailored to `loom-foo-skill-engineering` (including its test fixture schema and version metadata); **do not present it as a universal validator for newly created third-party skills**. For other skills use their own contract, the platform creator/official spec and applicable checks. It checks package/YAML/fixture integrity, **not** actual host selection. Use official `skills-ref validate` separately if it is available, but never claim it was run if missing. Static tests must fail closed when a dependency is absent.

Same-context self-review is valuable for finding a defect but never counts as independent acceptance evidence.

## Validator-of-validator regression

When changing version, run a deliberate invalid-version mutation and confirm the mutation **actually changed the candidate** before accepting a green negative test. Run a missing-reference mutation in a supplementary `references/` file, not only `SKILL.md`. This guards against vacuous tests that PASS merely because the original package is valid.
