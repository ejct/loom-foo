# Correspondence Episodes — semantic and temporal reconstruction

## Unit of analysis

A provider thread is a transport grouping. An **episode** is one real-world matter: a negotiation, request, purchase, application, support case, access event or sustained human conversation. It can span several threads/subjects/folders and can contain multiple related yet independent claims. Do not merge cases on lexical similarity alone. Require a defensible shared identifier, actor/recipient continuity, factual sequence or explicit cross-reference; retain identity ambiguity when unresolvable.

## Reconstruction sequence

1. Deduplicate exact provider message IDs; for forwarded/quoted material separately identify the original quote/forward and later author. Do not count quotes as separate confirmations.
2. Sort by observed received/sent timestamps. Record header date and provider receipt differences when consequential. `Message date` is not necessarily the date of the alleged external event.
3. Attribute who **stated** each fact; distinguish speaker assertion from independently established external state.
4. Determine event semantics: `ASSERTION`, `REQUEST`, `COMMITMENT`, `DECISION`, `OUTCOME`, `INFORMATION`, `SECURITY_SIGNAL`. Track `SOURCE_ASSERTED`, `CORROBORATED`, `OBSERVED`, `UNKNOWN` without implying absence.
5. Track `PROPOSED -> ACKNOWLEDGED -> ACCEPTED/REJECTED -> EXECUTED/UNKNOWN` only where supported. Do not invent required stages or infer completion from acknowledgment, last sender, a calendar RSVP or elapsed time.
6. Reconcile contradictions and supersession by source, time and authority. A later message may revise an earlier plan; a vendor update does not automatically supersede the user's own accepted terms.
7. Compare substantive episode fingerprints when user requests deltas: new owner/request, accepted commitment, decision, amount, deadline, external status, outcome or verified security effect. Mere subject/label/count changes and repeat reminders are not material deltas unless the question concerns those changes.

## Useful compact episode evidence

```
Episode: [descriptive identity; unresolved aliases noted]
Scope/as-of: [source window and retrieval time]
Timeline:
  - [timestamp, message locator, actor, evidence-supported action/statement]
Current known state: [supported; state as-of source time]
Outstanding: [exact ask, actor, explicit deadline if supplied]
Key claims: [claim -> source -> support level]
Contradictions: [claim A vs claim B; status unresolved/resolved]
Meaningful change: [from -> to, when asked]
Evidence gaps: [missing messages or attachments]
```

## Negative knowledge from the monitor

- Support acknowledgment or suggested procedure is not a payment decision or completed refund.
- A significant positive/negative outcome can matter even without an immediate user action.
- An old episode can remain relevant to historical reconstruction despite being muted by an attention monitor.
- A milestone need not close a longer process; separate related cases and outcome fingerprints.
- The last sender, absence of reply and an expired *inferred* deadline do not independently prove user obligation.
- A known stale checkpoint or corrupted JSON cannot be used as a validated basis for deduplication.

When there is insufficient evidence for a unique episode, give the supported messages and competing groupings instead of forcing a canonical ID. Project knowledge admission belongs to Knowledge Intake and its downstream owner, not this adapter.
