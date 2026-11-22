# Gmail — conditional provider adapter (read-only)

Applies only when an authorized Gmail connection or Gmail API read client is actually available. Tool schemas differ by runtime: inspect current operations before calling. Do not invent token scopes, broad API endpoints or capabilities.

## Read pattern for the connected Gmail tool family

1. **Search IDs first** for a completeness claim: `search_email_ids(query, max_results, next_page_token)`; continue until `next_page_token` is absent. `search_emails` is convenient metadata/snippet and attachment preview but must not be taken as an exhaustive membership list if IDs differ or pagination is incomplete. A historical monitor observed richer metadata search returning fewer messages than the ID path; this is an observed adapter failure mode, not a universal Gmail guarantee.
2. **Read messages/threads:** `read_email_thread(message_id or thread_id, max_messages)` or `batch_read_email_threads` when supported. Compare `total_messages` to returned count and inspect `truncated`. The default thread limit of a particular connector may hide older history. Use supported per-message reads to recover gaps or mark partial; do not claim full thread coverage solely because `read_email_thread` returned successfully.
3. **Scope relevant folders:** ordinary search should not assume `INBOX` or `UNREAD` covers all mail. Include Sent and archived mail for correspondence reconstruction; search Spam deliberately when expected replies may be misclassified. Trash only if explicitly relevant and permitted. Folder, label and unread state are metadata, not importance or authenticity.
4. **Reconstruct cross-thread episodes:** search case IDs, dates, sender/recipient aliases, known subject variations and sent replies. Messages in one thread need not all share labels or match the same message-scoped search query. Explicitly separate exact ID deduplication from semantic episode grouping.
5. **Attachments and original form:** metadata can indicate attachments, but bytes/inline media/MIME may require separate authorized tools; unsupported media is a coverage gap. If a security question requires headers or hidden HTML, use raw MIME only when a current read action supports it. Never fetch suspicious inline/remote resources by default.
6. **Link handling:** treat `https://mail.google.com/...` as a *private mailbox locator*, not an externally fetchable webpage. Extract the referent only via an authorized connector; do not send its tokenized URL to public search. IDs shown in URLs can differ from provider API message IDs. Verify the resolved message identity before claiming a match. If resolving by URL is unsupported, search with grounded subject/participants/dates, and report uncertainty.

## Query notes

Gmail search syntax includes `from:`, `to:`, `after:`, `before:`, `newer_than:`, `subject:`, `has:attachment`, `in:spam`, `in:sent` and `-in:trash`, subject to the tool's documented parser. Search result pagination is explicit. The Gmail UI and API do not have fully equivalent thread-wide search behavior; do not equate a search hit with whole-thread relevance.

The Gmail REST API has `includeSpamTrash` semantics, but a connected tool may expose only Gmail search queries/labels instead. Use **the connected tool's actual contract**, not an assumed REST parameter. No authorization to mark mail read, label it, archive, send, draft or change settings is implied by this adapter.

Primary documentation:
- https://developers.google.com/workspace/gmail/api/guides/list-messages
- https://developers.google.com/workspace/gmail/api/guides/filtering
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
