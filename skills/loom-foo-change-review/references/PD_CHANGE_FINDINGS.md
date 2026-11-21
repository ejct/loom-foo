# change-review — detailed conditional method (PD_CHANGE_FINDINGS.md)

> Source: exact private Loom-foo 0.35.1 `SKILL.md`. L1 retains activation, goal and authority precedence. Below sections are preserved in full, in source order; `references/...` paths refer to the owning skill root. Read this file only when its explicit L1 trigger applies.

## 8. Findings

For each material finding preserve enough to act and later verify closure:
- stable id where useful;
- severity: CRITICAL | MAJOR | MODERATE | MINOR;
- confidence: HIGH | MEDIUM | LOW when useful;
- category/scope;
- claim;
- evidence;
- consequence / failure path;
- affected requirement/invariant/user scenario when known;
- resolution criterion;
- status: OPEN | RESOLVED | REJECTED | ACCEPTED_RISK.

Equivalent findings keep the same identity across remediation cycles.

Read `references/FINDINGS_AND_SEVERITY.md` for detailed guidance.
## 9. Record non-risks when material

Review quality is not finding count.

When a plausible concern is investigated and evidence shows it is not material, record a concise NON_RISK when this prevents repeated re-litigation or clarifies the boundary.
## 10. Findings are not redesign commands

State what property is wrong and what must become true.

A finding may include an illustrative correction when useful, but the review does not own the implementation.

If closure requires architecture redesign, route to `loom-foo-architecture-design`.
If it requires specification/product change, route to the relevant upstream owner.
If it is one bounded remediation task, route to `loom-foo-agent-task-design`.
If it requires several dependent units, route to `loom-foo-work-decomposition`.
## 13. Reviewer independence

A fresh/separate reviewer can improve adversarial value when proportionate, but independence is not universally required.

If the same context reviews its own change, call it self-review.
Do not call builder claims independent evidence.

When independence matters, give the reviewer the exact candidate, controlling authority, and necessary evidence while avoiding builder advocacy/reasoning that could bias first-pass inspection.
## 16. Output contract

Return the Change Review as the primary artifact. For consequential work include:
- subject/base/change intent;
- review scope/lenses actually used;
- findings;
- material non-risks;
- review limits;
- disposition;
- next owner for open findings when useful.

Do not append a verification PASS unless a separate verification owner performed that work.
## 17. Candidate validation requirements

Before retention/promotion test at least:
- small-diff fast path;
- unknown defect outside acceptance criteria;
- real regression;
- unintended side effect;
- maintainability/complexity issue;
- scope/authority violation;
- false positive resolved as non-risk;
- architecture-review negative routing;
- evidence-review negative routing;
- change-verification negative routing;
- specialist-review escalation;
- remediation handoff;
- same-context self-review vs separate reviewer labeling;
- trivial change ceremony control;
- C0 ordinary model review;
- fresh holdout.

Behavioral execution may remain deferred by portfolio policy. Static/package checks are not retention evidence.
## Final checks

Before returning verify that:
- exact subject/base are clear enough for the claims;
- actual delta was inspected rather than only summarized;
- stronger specialist owners were not displaced;
- review surface is proportionate to plausible impact;
- findings distinguish consequence from confidence;
- remediation criteria do not silently redesign the system;
- passing tests are not presented as exhaustive defect absence;
- review completion is not presented as verification or acceptance.
