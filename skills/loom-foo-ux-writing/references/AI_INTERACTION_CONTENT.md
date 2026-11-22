# AI/agent interaction content: truth, progress and user control

Read for agentic UX, generated responses, automated tasks, background operations, tool actions, approval gates, partial outcomes or confidence statements. This reference governs **user-visible content**, not system prompt engineering or actual tool permissions.

## Align message with operational state

| Actual event | Safe content direction | Unsupported assertion to avoid |
| --- | --- | --- |
| Request accepted, not started | “Request received” / “Queued” | “Working on it” when nothing is running |
| Work started | “Processing…” or name observed current step | Percentage or ETA without measurement |
| A draft or suggestion exists | “Draft ready for review” | “Sent”, “published” or “applied” |
| User approval requested | Name proposed action, audience, scope and consequences | Treating a preview as authorization |
| Action attempted, outcome unknown | “Couldn’t confirm whether the action completed” | “Completed” or “Failed” without evidence |
| Partial completion | Identify completed and pending/failed units | Blanket “Everything is done” |
| Explicitly verified completion | Name the verified outcome | Broader success claim than the evidence |
| Action refused / unavailable | Name constraint and real next option, if available | Pretending to have found a workaround |

If the system doesn't expose reliable stages, content design cannot invent them. Recommend a more observable state model as a **dependency**, not as an assumed product feature. Distinguish model-generated suggestions, fetched data, verified facts, human-approved actions and confirmed external side effects.

## Quality rules

- Do not anthropomorphize the agent as having feelings or independent intentions; describe observable capabilities and actions.
- Use calibrated uncertainty where needed; avoid absolute truth, completion or reliability promises.
- Preserve approval boundaries. A conversational “yes” may be ambiguous if exact payload or audience is missing; the copy must not silently enlarge authorization.
- For background processing or streaming, distinguish still-running, blocked, interrupted, resumed and completed states when those states actually exist.
- If generated content could be mistaken for verified third-party content, label the relevant provenance or uncertainty in a task-useful way rather than adding generic boilerplate.
- If retry may duplicate a charge, email or other external effect, don't recommend retry until duplicate-safety is known; surface this to the workflow owner.

## Example

Given only `report_generated=true`, `email_delivery_state=unknown`, prefer “Report ready. Email delivery hasn’t been confirmed.” over “Report sent.” If the UX spec requires delivery confirmation, identify the missing backend event separately.

Sources informing patterns: https://fluent2.microsoft.design/content-engineering ; https://developer.apple.com/design/human-interface-guidelines/writing

## Explain capabilities and limitations when the decision needs them

From Google People + AI guidance, adapt three separate content obligations: (a) establish a realistic mental model of what AI can and cannot do, (b) disclose relevant input/data-source context so output provenance is not surprising, and (c) return control after model uncertainty or failure. Use only actual available provenance and observed capabilities; do not fabricate explanations of model internals, certainty percentages or specific training-data claims.

- **Generated suggestion:** label as generated or proposed when readers might confuse it with verified external information. Preserve a review/correction path where the product provides one.
- **Model uncertainty:** prefer specific evidence bounds (“Could not verify the invoice total”) over generic disclaimers, false precision or confident alternatives that the system did not calculate.
- **Action provenance:** distinguish LLM reasoning/output, tool-returned data, user-provided claims, reviewer-approved payload and externally confirmed effects. Use a compact status only when people need the distinction.
- **Feedback:** say whether feedback is stored, used for this session, sent to a team or used for model improvement only when the actual product policy supports that consequence. Never imply a thumb-up automatically trains a model.
- **Multiple assistants or tools:** identify which actor is responsible for a request or result when confusion changes user control; avoid inventing global orchestration guarantees.
- **Failure categories:** distinguish input mismatch, insufficient data, generated answer error, operational tool failure, authorization refusal and unknown external-effect status. Do not force them into a single generic “Something went wrong”.

## Action confirmation copy contract

For irreversible or sensitive external effects (send, publish, purchase, permission, delete), the user's approval should be tied to the *specific* operation, target/audience, payload and salient consequences. Present missing details as a blocking prerequisite when needed. UX Writing can describe this contract but cannot grant permission, implement approvals or assert host enforcement.

Additional sources: https://pair.withgoogle.com/guidebook-v2/chapter/mental-models/ ; https://pair.withgoogle.com/guidebook-v2/chapter/explainability-trust/ ; https://pair.withgoogle.com/guidebook-v2/chapter/errors-failing/ ; https://pair.withgoogle.com/chapter/feedback-controls/
