# change-verification — detailed conditional method (PD_VERIFICATION_METHODS.md)

> Source: exact private Loom-foo 0.35.1 `SKILL.md`. L1 retains activation, goal and authority precedence. Below sections are preserved in full, in source order; `references/...` paths refer to the owning skill root. Read this file only when its explicit L1 trigger applies.

## 6. Choose proportional checks

When the property-to-check relation is straightforward, this skill may select ordinary verification methods such as:
- relevant existing tests;
- targeted regression/negative case;
- direct code/config/schema inspection;
- exact artifact/hash/output comparison;
- reproduction of specified behavior;
- build/type/lint/static gate when it establishes a real property;
- clean-checkout reproduction when claim strength requires it;
- browser/device/runtime exercise when environment matters.

Every check must establish a concrete property or reduce a concrete uncertainty.

Do not add ritual checks merely because they are available.
## 7. Escalate method design when necessary

Route to `loom-foo-research-design` or a specialist method owner when credible verification requires designing a materially new:
- experiment;
- sampling strategy;
- benchmark;
- statistical inference method;
- human-subject study;
- lab/security methodology;
- oracle whose validity is itself an unresolved research question.

A routine regression test does not require a research plan.
## 8. Evidence acquisition / review composition

Use generic evidence skills when their artifacts have independent value or the evidence work is substantial.

`loom-foo-evidence-acquisition` may collect a large/reusable evidence body under an explicit Evidence Plan.
`loom-foo-evidence-review` may assess that evidence body.

Do not require this full chain for ordinary candidate verification.

When used, consume their artifacts rather than reconstructing tool/chat history.
## 14. Environment and fidelity

A check establishes only what its environment/fidelity supports.

When material record:
- runtime/platform/device/browser;
- production vs fixture/mock/simulation;
- dependency versions/config;
- clean vs dirty checkout/state;
- unavailable capabilities.

Low-fidelity evidence licenses a lower-fidelity claim.
## 18. Proportional fast path

For a small candidate with two explicit criteria, a sufficient report may be:
- exact candidate/base;
- criteria;
- check/evidence per criterion;
- PASS/FAIL/INCONCLUSIVE/NOT_COVERED;
- one-line limits/disposition.

Do not manufacture elaborate matrices or clean-room runs without need.
