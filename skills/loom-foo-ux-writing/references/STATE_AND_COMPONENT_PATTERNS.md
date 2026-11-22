# State and component content patterns

Use when more than one meaningful UI state or a consequential component-specific message must be designed. These are **decision patterns**, not universal strings or mandatory fields.

## Pattern selection

| Situation | What copy must make clear | Important checks |
| --- | --- | --- |
| Control/CTA | Outcome or destination; key object when ambiguous | Don't say “Save” if action sends, publishes, charges or merely queues |
| Link | What destination or information follows | Accessible name should be distinguishable in context; avoid repeated vague links |
| Form label/hint | What data is wanted, constraints and format where needed | Visible label persists; placeholder is not the only label |
| Validation error | Which field is wrong and how to correct it | Specific true constraint; field association and summary if appropriate; no user blame |
| Failure of a system operation | What did not complete, user impact and real next option | Don't guess cause, suggest unsupported retry or imply data is safe |
| Empty first-use state | What belongs here and the actual next action | No marketing filler; consider no-next-action cases |
| Empty after filters/search | No matching results and what change can help | Don't say no data exists globally when it is only filtered |
| Loading/progress | What is happening and what remains uncertain | No arbitrary percent or ETA; prevent duplicate actions if relevant |
| Partial success | Completed objects/actions versus unresolved ones | Do not use a blanket “Done” for mixed outcomes |
| Success | What actually completed; significant downstream consequence | Queueing, saving and delivery are different states |
| Destructive confirmation | Scope, permanence/recovery and explicit confirm action | Preserve cancellation; don't promise undo unless supported |
| Permission request | Why needed, effect of allowing/denying, available alternative | Never misstate capabilities or hide a nonessential opt-out |
| Notification | Why it matters now and whether action is necessary | Interrupt only when value warrants it; don't claim urgency without evidence |
| Offline/interruption | Availability of local progress and real continuation path | Distinguish synced, pending and unknown; don't promise persistence |

## State-first content matrix

Use when a flow involves multiple meaningful states. Suggested columns: `object/action`, `trigger`, `system state`, `component`, `draft copy`, `action`, `consequence/accuracy basis`, `unresolved dependency`. Add localized strings or accessibility notes only when they materially matter.

Minimal example (illustrative, not a claim about any live app):

| State | Draft UI copy | Critical distinction |
| --- | --- | --- |
| Request accepted by local queue | “Report added to the queue” | Not yet processing or complete |
| Processing actually started | “Generating your report” | No fabricated ETA |
| Report generated, delivery not confirmed | “Report ready. Delivery is pending.” | Creation is not delivery |
| Generation failed; retry supported | “Couldn’t generate the report. Try again.” | Only when retry actually exists |

## Feedback and error method

Identify whether clearer interaction could prevent the error: labels, formats, selection constraints, confirmation, progressive help, or transaction design. If the cause is unknown, state the observable failure rather than guessing an internal mechanism. Prefer problem + meaningful resolution; don't force a three-sentence formula for a single field. Where financial/data consequences are involved, preserve those facts and ask for missing high-stakes operation details rather than inventing copy. Avoid habitual apology and defensive “we” language.

## Boundary examples

Copy cannot create a retry endpoint, undo stack, save guarantee, delivery confirmation, permission alternative or status event. Flag such needs as **interaction/implementation dependencies** for the owner of the behavior. If user requests redesign of the state graph, route primarily to Experience Design.

Sources informing patterns: https://design-system.service.gov.uk/patterns/validation/ ; https://shopify.dev/docs/apps/design/content ; https://polaris-react.shopify.com/content/error-messages ; https://atlassian.design/get-started/content-design ; https://www.w3.org/TR/WCAG22/

## Error and confirmation decision checks

Before writing a system-error message, classify **what is known** rather than inventing a cause: `VALIDATION_REJECTED` (no side effect), `OPERATION_FAILED_CONFIRMED`, `PARTIAL_SUCCESS`, `OUTCOME_UNKNOWN`, `ACCESS_DENIED`, or `TEMPORARILY_UNAVAILABLE`. These are local content-design distinctions, not required backend enum names. Only call a retry safe when idempotency/deduplication or post-failure reconciliation is known.

For forms, prefer error copy that identifies the same named field as its label and gives a correct fix. The interface may require an error summary linked to specific fields, focus behavior and live announcement. A content recommendation does not itself implement those conditions. Avoid premature validation that disrupts incomplete but valid input (for example date fields or complex formats) without research.

For deletion/payment/publication and other consequential transactions, spell out object, scope, amount/recipient, reversibility and pending/confirmed state as applicable. Avoid confirm button labels that conceal the actual operation. If the flow lacks review/undo or a safe return path, report that issue to the experience/engineering owner rather than writing copy that pretends it exists.

Sources: https://spectrum.adobe.com/page/writing-for-errors/ ; https://design-system.service.gov.uk/patterns/validation/ ; https://atlassian.design/foundations/content/designing-messages/warning-messages ; https://www.w3.org/WAI/WCAG22/Understanding/
