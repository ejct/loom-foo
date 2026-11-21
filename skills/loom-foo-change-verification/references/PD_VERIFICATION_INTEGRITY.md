# change-verification — detailed conditional method (PD_VERIFICATION_INTEGRITY.md)

> Source: exact private Loom-foo 0.35.1 `SKILL.md`. L1 retains activation, goal and authority precedence. Below sections are preserved in full, in source order; `references/...` paths refer to the owning skill root. Read this file only when its explicit L1 trigger applies.

## 11. Verifier / oracle integrity

Read `references/VERIFIER_INTEGRITY.md` when the candidate can modify tests, goldens, fixtures, evaluator logic, check configuration, or other verdict-producing machinery.

When material preserve enough provenance to distinguish:
- candidate passed stable/trusted verifier;
from
- candidate changed/weakened/staled the verifier and then passed.

Possible evidence:
- verifier baseline/version/diff;
- authorization for verifier changes;
- negative/mutation/counterexample evidence;
- independent/frozen oracle where proportionate;
- golden-update separation;
- exact environment/tool version.

Do not create a universal verifier registry/object.
## 12. Bounded regression

Verify:
- properties directly changed;
- protected properties plausibly affected by the change;
- mandatory shared gates relevant to the requested claim.

For consequential outbound actions, verify **approval drift** and **aggregate effect** only when material to this exact subject and its controlling authority. Read `references/EXTERNAL_EFFECT_REGRESSIONS.md` for paired negative/positive scenarios and evidence requirements. Preserve the distinction between a passing synthetic dispatcher test, an observed runtime-native permission check, and successful enforcement on the real tool-call path.

For one-use or otherwise consequential runtime transitions, map the material integration path from entrypoint through dispatch/variant selection and host methods to the first irreversible effect. Where an existing routing/validation branch determines safety, obtain direct evidence that the intended branch is actually selected on the exact candidate. Prefer one isolated, realistic end-to-end route probe using the real relevant methods with external effects mocked over additional component-only tests. A real `backup_exact()` test does not establish that `promote()` invokes the correct validator. If the integration path was exercised only through `FakeOps` or equivalent, report it as `NOT_COVERED` or fidelity-limited instead of claiming a production-lifecycle PASS. Never require a production attempt as the verification probe.

Broaden regression only when coupling, defect history, release contract, or claim scope justifies it.

Do not rerun the entire world for every candidate.

If a surface is not checked, mark it NOT_COVERED rather than implying global safety.
## 13. Negative and falsification checks

Where the risk/claim warrants it, prefer checks capable of failing for the targeted defect:
- boundary/outside cases;
- mutation or seeded negative variant;
- invalid input;
- degraded dependency;
- counterexample fixture;
- wrong-version/wrong-subject guard.

Do not require mutation testing universally.
## 15. Self vs independent verification

The same skill supports both.

Label topology honestly:
- builder/self verification;
- fresh-context evaluator;
- independent role/process where genuine;
- shared evidence/oracle limitations.

Do not call self-verification independent.

Independent verification may be required by a project/claim, but is not universally mandatory.
## 16. Builder claims are claims

### Exact-subject completion and evidence freshness

Before a positive completion, fix or PASS claim, tie it to an observed result for the exact subject. Check the command/observation actually ran, its output or exit status, relevant environment and revision, and whether it covers the stated property. A prior commit's green log, a different task, a mocked integration or an unverified subagent report cannot establish current success. If a negative/mutation test is material, check that the intended assertion failed instead of an earlier unrelated failure, and confirm the temporary mutation was removed before final green verification. Report INCONCLUSIVE or NOT_COVERED instead of implying a broader PASS. Do not impose duplicate verification when a trustworthy current result already covers the claim.


Existing builder test reports, screenshots, logs, or “all checks pass” statements are evidence inputs to inspect/challenge, not inherited verdicts.

For consequential verification, independently reproduce the material property when the contract requires independence or when builder-controlled verifier integrity is at risk.
## 21. Candidate validation requirements

Before retention/promotion test at least:
- two-criterion fast path;
- clear PASS;
- clear FAIL;
- INCONCLUSIVE due environment fidelity;
- NOT_COVERED vs PASS;
- missing criteria -> NEED_CRITERIA;
- builder suite green but one property unproven;
- candidate changes verifier/golden;
- negative/mutation evidence;
- bounded regression;
- stale/wrong candidate identity;
- ordinary check selection vs research-design escalation;
- self vs independent verification labeling;
- evidence-acquisition/review composition;
- change-review negative routing;
- architecture-review negative routing;
- PASS != ACCEPTED;
- C0 ordinary verification baseline;
- fresh holdout.

Behavioral execution may remain deferred by portfolio policy. Static/package checks are not retention evidence.
## Final checks

Before returning verify that:
- exact candidate and controlling criteria are resolved;
- criteria were not invented/relaxed;
- each material property has an honest result relation;
- checks actually establish the claimed properties;
- verifier changes are visible when material;
- regression scope matches plausible impact/claim;
- environment/fidelity limitations constrain claims;
- uncovered properties are not implied PASS;
- verification is not presented as exhaustive defect discovery;
- technical PASS is not presented as owner acceptance.
