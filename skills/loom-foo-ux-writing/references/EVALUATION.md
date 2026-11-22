# Evaluation and acceptance for UX content

Read for a consequential interface-content review, content-system acceptance, test plan or explicit evidence requirement. Do not turn routine microcopy into a multi-role QA ritual.

## Review a real content decision

First check *correctness*: actual operation and state, scope of deletion/payment/publication, preserved facts, security/privacy, authorized language and product vocabulary. Then check *comprehension*: could the intended user predict the button outcome, identify an error, and recover using only available controls? Then check *implementation feasibility*: component anatomy, accessible names/status, string placeholders, locale and layout.

Use `blocking` for inaccurate/misleading or materially inaccessible UI content; `important` for avoidable user uncertainty; `polish` for optional style/tone improvements. Provide exact source span/component, problem, specific corrected wording or changed pattern, and the behavioral dependency if any. Don't invent defects to populate a checklist.

## Hypotheses versus observed evidence

- `HEURISTIC`: an expert judgment grounded in source constraints, not observed user behavior.
- `SOURCE_VERIFIED`: a claim about product behavior confirmed in the supplied spec/runtime.
- `USER_OBSERVED`: genuine user-study/interview/analytics evidence with stated method and sample.
- `UNVERIFIED`: a material assumption that needs product or audience evidence.

Do not claim higher conversion, reduced cognitive load or accessibility conformance from a self-review alone. Quantitative readability formulas for US English are optional signals for appropriate audiences, not universal quality thresholds or substitute user tests.

## Proportional evaluation examples

- **Single label**: Does the action make sense, and is consequence clear? Stop.
- **Multi-step onboarding or critical error**: Test task scenarios, out-of-order entry, interruption and recovery; review representative locale and assistive-technology behavior with real implementation if available.
- **Consequential copy change**: Recommend an actual comprehension probe (e.g., ask participants what they expect a control to do before pressing it); compare the incumbent and proposal with a defined outcome and practical guardrails such as error rates or unintended actions.
- **System-wide terminology migration**: Check a real string inventory, duplicates, near-synonyms, UI locations, translations, impact and rollback plan. Cross-component governance belongs to Design Systems.

Read test fixtures in `tests/task_cases.md` when setting up a first-use candidate check. Static fixtures cannot prove runtime routing or real-user improvement.

Sources: https://www.nngroup.com/articles/ux-writing-study-guide/ ; https://www.nngroup.com/articles/ux-writing-faqs/ ; https://developers.openai.com/blog/eval-skills

## Test understanding and action prediction, not copy aesthetics

When an evidence-backed outcome matters, choose the smallest **valid** test. A useful comprehension probe asks the representative user (without prompting the answer): “What do you expect will happen if you choose this action?” and, after a simulated failure, “What can you do now, and what might already have happened?”. Compare with actual system behavior and available controls.

For consequential multi-step content, prefer task-situated moderated studies with representative people; don't substitute a generic preference poll or a model critique for observed comprehension. NN/g cautions that participants' real motivations and context particularly matter when testing content. For low-risk text edits, a heuristic review and product-owner check may suffice.

Record: observed task success or failure, mispredicted outcomes, wrong recipient/amount expectations, avoidable support requests, recovery errors, false-success interpretations, assistive-technology findings, and localization failures. Choose a guardrail against harmful conversion improvements (for example unintended consent or irreversible action). Do not claim causality from unrandomized feedback, a single quote or a copy-only edit when the interaction changed too.

Source: https://www.nngroup.com/articles/testing-content-websites/ ; https://www.nngroup.com/articles/usability-data-in-analysis/ ; https://pair.withgoogle.com/guidebook-v2/chapter/errors-failing/
