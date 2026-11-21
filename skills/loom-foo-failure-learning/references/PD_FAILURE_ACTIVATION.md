# loom-foo-failure-learning — detailed instructions (PD_FAILURE_ACTIVATION)

> Conditional reference for `../SKILL.md` (progressive disclosure migration based on private loom-foo 0.27.0). The source sections below preserve their original normative content; Markdown `references/` links are rebased to sibling files. Read for the trigger named in the current root; do not silently treat all references as always loaded.

## 1. Activation and scope

Run when the user explicitly reports a failure, e.g. "є помилка", "навичка спрацювала неправильно", "інструкцію проігноровано", "результат не відповідає запиту", or describes a concrete failure without a keyword. Do not ask permission to begin local read-only analysis of that signal. Treat a user report as credible evidence *of the report*, not automatic proof of its proposed cause.

### Interaction friction: discovery cue, not diagnosis

When a user responds with sarcasm, profanity, irritation, terse repetition, or a comment indicating repeated misunderstanding, inspect **only the task-relevant accessible context** for a concrete mismatch, repeated failed correction, broken constraint, or lost intent. The signal is evidence of dissatisfaction if explicit, **not** evidence of a particular psychological state, personality trait, failure mechanism, or even an assistant error. Do not classify the user or infer motives. Do not require polite phrasing before offering ordinary recovery.

- If a concrete task discrepancy is identifiable, recover that task and conduct proportionate `EPISODE` analysis. Repeated failed repair is itself a candidate `RECOVERY_FAILURE`: check whether the earlier correction damaged previously correct output, dropped requirements, or repeated the same failure.
- If irritation is apparent but no task discrepancy can be verified, respond to the substance of the message without inventing an incident. Ask at most one narrow clarification **only if necessary** to recover the task. Do not launch a deep investigation based on tone alone.
- An explicit user report of a concrete defect remains a direct trigger regardless of tone. Ordinary calm correction is not lower priority than angry correction.
- Do not reward intensity with disproportionate analysis: severity follows observed task impact, recurrence, and evidence, not language intensity. Do not reproduce insults in portable artifacts when a neutral bounded summary suffices.

**Hard boundary:** this skill performs operational failure analysis only. It does not conduct psychological research, infer emotion beyond the user's explicit statement, profile the user, initiate other personal-assessment workflows, transmit incident records to them, or change any personal profile. Those systems, if used, operate separately under their own authority and consent.

When the assistant notices a material error itself: immediately repair what is safely repairable; perform cheap local triage. Suggest deeper failure learning for apparent recurrence, systemic ownership uncertainty, material downstream harm or a significant governance gap. Do not interrupt the user with a ceremony for trivial one-off corrections.

Negative routing: changed requirements, ordinary alternative preferences, conceptual disagreement, frustration without a traceable task defect, psychology or self-reflection requests, unsubstantiated assumptions about other chats, and a generic request to create/review a proposal are not failure incidents without a concrete alleged discrepancy. A frozen skill-evaluation execution belongs to `loom-foo-skill-validation` only when that optional skill is installed and available; otherwise report **UNAVAILABLE** and do not improvise the campaign. An evidence-method design belongs to `loom-foo-research-design`; a general project proposal belongs to `loom-foo-proposal-refinement`. This skill may provide incident input to those owners but must not take over their work.

If explicitly invoked but a canonical `SKILL.md` cannot be retrieved, disclose that the skill was **not** actually loaded; offer/perform ordinary bounded task recovery and source-grounded triage without claiming skill execution. Do not reconstruct hidden skill rules from memory.

### Detect delegation ping-pong

Treat a recurring sequence `BLOCKED → narrower Task Brief → BLOCKED` with unchanged owner outcome, subject and authority as a candidate RECOVERY_FAILURE at the `COMPOSITION`/runtime projection boundary. Reconstruct who narrowed the contract, whether the actual blocker was human-only, whether authorized alternative tools/context/capability could have been used, and whether the coordinator or executor created the stop. Do not blame the skill body or an executor without evidence. Recover the original outcome and preserve genuine approval, safety, evaluation-treatment and resource boundaries. Add a minimal regression example when the failure is material; do not initiate a general portfolio audit for each local tool error.
