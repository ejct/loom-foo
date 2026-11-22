# Email Source Coverage — scoped retrieval and gaps

## Objective

Prevent silent false negatives. Always define the **search scope** before declaring completeness: account/source, subject or case, time range, relevant folders, search expressions, pagination, message-body retrieval and attachment inspection. Scope is task-specific; don't run a comprehensive inbox scan for a one-message lookup.

## Retrieval ladder

1. **Discovery:** run targeted search(es), note exact query and source. Search metadata/snippets identify *candidates*, not evidence of the full message's meaning. Use authoritative provider IDs.
2. **Enumeration:** follow all provider `next_page_token`/equivalent for the query whose result coverage you claim. A smaller page size or bounded retry may resolve transient errors; after unrecovered errors stop with PARTIAL. When search returns no IDs, do not infer that there are no relevant messages outside the declared query.
3. **Reading:** fetch full bodies for materially relevant candidates; follow thread references to related incoming and outgoing messages. If the reader returns last N messages with `truncated=true` or a larger total than fetched, explicitly recover the missing part or mark PARTIAL.
4. **Expansion:** for real-world episodes, consider aliases, participants, case/transaction IDs, subject shifts, Sent and Spam separately when relevant. If search is message-scoped (as Gmail API search can be), a thread match cannot prove all thread messages matched or were fetched.
5. **Attachments/links:** enumerate and characterize without blindly executing or contacting external hosts. For unsupported media record `UNSUPPORTED`; for uninspected content record `NOT_INSPECTED`; do not conflate either with `NO_ATTACHMENT`.
6. **Coverage result:** include query set/period/folders and whether pagination and material reads completed. One failed page prevents `READ_COMPLETE_WITHIN_SCOPE` for that surface. Findings from successfully read items remain usable despite other gaps.

## Incremental / repeat reads

Use overlap around a known checkpoint only for authorized incremental tasks. A state checkpoint is valid only for a fully enumerated/read/triaged **declared** surface. Stale/malformed/missing state must not be guessed or overwritten; continue from bounded source evidence and label dedup as unverified. Fingerprints relate to semantic changes in a real-world episode, not simply new subjects or counts.

The old hourly monitor used >=48 h for ordinary mail and >=7 days for Spam. **These were operational monitor windows, not general Email Intake defaults.** Instead scope to the actual question, expanding only with user intent and evidence.

## Coverage fields (use when material)

- `query_scope`: account/source; terms/filters; as-of/time range; folders.
- `enumeration`: COMPLETE | PARTIAL | NOT_ATTEMPTED; page count or gap when available.
- `body`: FULL_FOR_MATERIAL_SOURCES | PARTIAL | METADATA_ONLY | UNAVAILABLE.
- `thread`: COMPLETE_FOR_SELECTED_THREADS | TRUNCATED | NOT_REQUIRED | UNKNOWN.
- `attachments`: INSPECTED_FOR_REQUEST | PARTIAL | NOT_INSPECTED | UNSUPPORTED | NONE_VERIFIED.
- `overall`: READ_COMPLETE_WITHIN_SCOPE | PARTIAL | METADATA_ONLY | SOURCE_UNAVAILABLE.

Never claim read/delivery or source freshness based only on a scheduled task's `completed` status. A connector error means `UNKNOWN`, not “nothing happened”.
