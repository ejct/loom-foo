# loom-foo-skill-engineering — detailed instructions (PD_SKILL_RECOVERY)

> Conditional reference for `../SKILL.md` (progressive disclosure migration based on private loom-foo 0.27.0). The source sections below preserve their original normative content; Markdown `references/` links are rebased to sibling files. Read for the trigger named in the current root; do not silently treat all references as always loaded.

## 8. Handle failures and self-application

When a real failure is reported, first preserve/recover the user's active work. Diagnose whether the cause is `SEMANTICS`, `ROUTING`, `COMPOSITION`, `PACKAGE`, `DELIVERY`, `RUNTIME/TOOL`, `EVIDENCE/ORACLE`, or `UNKNOWN`. Check credible rivals. Apply the smallest correct repair, then run affected regressions and a nearby negative case. Avoid a new layer of governance for a local issue.

**Self-application** is permitted as diagnostic dogfooding. Treat the frozen input version as the subject and this skill's actual outcome (a corrected, usable version or justified no-change decision) as the test. Apply this sequence without unnecessary review loops:

1. Record exact input/version/hash and what the user wants. Check necessity and nearest competing owners before assuming this skill should be revised.
2. Select materially relevant specialists using the owner map; distinguish guidance actually loaded from independent specialist execution. Record one concrete scenario where each selected method changed or confirmed a decision.
3. Try to falsify the current contract with realistic activation, owner-overlap, change-safety and deployment scenarios. Distinguish *observed* defects from hypotheses and unexecuted model fixtures.
4. Make the smallest justified change, preserving the original version; run direct integrity checks and only risk-relevant positive/negative regressions. Use mutation checks when a test oracle might otherwise silently pass a defect, not as a universal release prerequisite.
5. Return the exact artifact and a concise self-use receipt: baseline, observed defects, changes, checks actually run, test gaps, and installation state. Keep the audit report outside the installed skill package.

Self-evaluation cannot independently establish effectiveness, host routing, broad generalization, canonical authority or release readiness. If those claims matter, use a separate evaluator and/or actual runtime use under a frozen contract.

## 9. Close at the real user outcome

Return the output actually requested: decision, skill artifact/patch, failure diagnosis or exact runtime receipt. A complete authorized engineering run identifies version, changed files, successful checks, checks not run, source/installed version differences and any genuine external blocker. For material prior-art research, mention competing surfaces examined, evidence gaps, and the exact design delta adopted/rejected; never claim exhaustive ecosystem coverage. Do not confuse a recommendation with an owner decision or a green test with a working deployment.

Finish when the skill can be used for the owner's intended work, and its installation/discovery limits are reported accurately, **without disproportionate new process**. When the user has already authorized installation, complete it in the same episode instead of delivering a local ZIP and requesting a second push. A saved release and a runtime-cached skill are distinct; a stale in-session loader does not erase successful release readback.
