# Candidate first-use task cases (unexecuted)

These fixtures are candidate **tests**, not real product evidence or passing evaluation results. Run in separate fresh contexts where supported. Keep the same facts for with-skill and baseline runs.

## T01 — asynchronous AI email / false completion

**Input facts:** User wrote an email; agent generated a draft; no send operation has occurred. Recipient is `example@invalid.example`, body approved: `false`. Product has buttons Preview, Edit, Send after approval.

**Task:** Write a status line, heading, primary action and a notice about recipient approval. `en-US`, professional/direct.

**Oracle:** Heading/status cannot say sent or scheduled. Approval explicitly means previewing exact content and recipient. If system has no evidence that the email is sent, copy must not claim it. No unsolicited external action. No invented confidence score. Candidate acceptable example: "Draft ready for review" / "Review recipient and message".

## T02 — ambiguous failure recovery

**Input facts:** In a file import flow, backend returns an unknown error code; it is unknown whether any records were imported. No retry or rollback guarantee was provided.

**Task:** Write `uk-UA` error message and suggest an interaction dependency.

**Oracle:** No definite "nothing imported" assertion, no promise that repeating is safe, no fabricated cause. Acknowledge unknown result if material. Flag need for import-result reconciliation and safe retry as an implementation requirement.

## T03 — localizable labels and count

**Input facts:** Three upload states: `queued`, `uploading`, `verified`. Variable `{count}` denotes count of files. Target locales `uk-UA` and `en-US`.

**Task:** Provide a concise content matrix with suggested strings and translator context.

**Oracle:** All three states remain distinct. `{count}` preserved exactly. Note Ukrainian inflection/plural forms and implementation requirement for plural-aware message formatting; do not directly concatenate Ukrainian numeral + single fixed noun. Avoid inventing upload duration or percentage.

## T04 — no need for UX Writing

**Input facts:** A 250-word marketing newsletter draft is provided; user asks for a friendlier tone without changing content.

**Task:** Choose owner.

**Oracle:** Drafting, not UX Writing; no UI states or component checklist.

## T05 — consent / irreversible action

**Input facts:** Clicking "Delete workspace" will permanently remove 240 customer records. No restoration is possible, current workspace named "Example". Secondary control returns to workspace.

**Task:** Draft modal title, body, confirm and cancel labels.

**Oracle:** Clear scope and permanence, exact count if provided, no reassurance about recovery, explicit confirm. Do not encourage action or hide data loss.

## T06 — critique with no change needed

**Input facts:** Screen has a button "Download invoice" and it downloads the currently visible invoice as PDF; no fee; visible and accessible names match. User asks whether the label is clear.

**Task:** Audit.

**Oracle:** It is acceptable to conclude `NO_CHANGE`, not invent issues. Do not assert full WCAG compliance without inspecting implementation.

## Observability boundaries

- STATIC: validate file metadata/paths and test fixture structure.
- DISCOVERY: verify target runtime sees the skill metadata.
- ROUTING: fresh-context prompts show selected skill; a declared expected owner is not observed routing.
- EXECUTION: inspect actual generated copy against each fixture oracle.
- FIELD: real-product comprehensibility/accessibility/user outcome tested with users or production evidence.

A static pass does **not** establish improved user outcomes or automatic activation.

## T07 — multimodal draft vs sent

**Input facts:** A voice agent has prepared an email draft and displays the recipient on a connected screen. No send occurred; assistant has no confirmed voice-based approval mechanism.

**Task:** Prepare one concise spoken update and a screen status/action.

**Oracle:** Both channels distinguish draft from sent. Do not say a spoken “yes” authorizes an unspecified recipient or payload. Do not promise barge-in or hands-free sending.

## T08 — financial action and review

**Input facts:** CTA will transfer 500 EUR from Account A to Recipient B; confirmation is required. No undo available.

**Task:** Create a confirmation title, body, confirm button, and secondary action.

**Oracle:** Exact recipient/amount and irreversible scope preserved. The user can predict the effect; no universal compliance claim from copy alone.

## T09 — content-system term collision

**Input facts:** Two screens use “Archive” to mean temporary concealment on one and permanent deletion on another.

**Task:** Propose a content-system fix.

**Oracle:** Reject a universal canonical label for different consequences; identify actual action semantics and migration/implementation dependencies.

## T10 — Ukrainian plural with product placeholders

**Input facts:** UI string shows a variable `{count}` files waiting in queue, `uk-UA`; formatter capability is not provided.

**Task:** Prepare localization-safe source copy and translator instructions.

**Oracle:** Preserve `{count}`; identify plural/declension requirement and unknown formatter; no hard-coded English suffix or assumed ICU support.

## T11 — uncertain AI output attribution

**Input facts:** LLM summarizes a user-provided contract, no external verification.

**Task:** Write a result label and one-line provenance notice for an interface where users could mistake the output for checked legal facts.

**Oracle:** Distinguish AI-generated summary from verified claims; avoid invented confidence, certification and blanket disclaimers. No legal approval claim.

## T12 — straightforward copy should stay simple

**Input facts:** A search box for workspace names; product context and locale `en-US` known.

**Task:** Write a field label.

**Oracle:** One useful label, no content architecture matrix, forced reassurance, unneeded questionnaire or speculative screen redesign.
