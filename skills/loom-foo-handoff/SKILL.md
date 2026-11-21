---
name: loom-foo-handoff
description: "Prepare or restore a bounded operational handoff across agent sessions or contexts. Not normal task continuation or project-state mutation."
compatibility: Agent Skills-compatible clients. Connected project sources and write-capable systems are optional; missing capabilities must be represented rather than invented.
metadata:
  family: "planning"
  project: "loom-foo"
  version: "0.9.0"
---

<!-- loom-foo Answer Receipt v0.3: compact standalone projection -->
**Answer Receipt.** Finish user-facing prose with one compact receipt naming only actually consulted/applied skills and versions, `SKILL.md` model-visible delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered L2 coverage, sources, checks, actions and limits. `FULL` requires complete contiguous exact text to EOF; a successful tool fetch alone is insufficient. Use ordered **Process Trail** for actual material review/repair/recheck stages, with artifact identity and honest `SAME_CONTEXT` versus observed separate actors. Never invent independent reviews, tests, host routing, publication or external effects. Omit the footer only for strict machine/code-only output contracts.

# Handoff

## Critical contract — read first

- **Goal fidelity:** Preserve the owner's real result, required actors, source identity, constraints and scope. Do not treat an intermediate result as completion unless it is the exact outcome the user requested and meets its acceptance criteria.
- **Authority and verification:** Tool access cannot grant new action authority. Keep evidence proportional to the actual claim and honor the scope, refusal, resource and acceptance boundaries detailed below. Load conditional references when their trigger applies.

Compile the smallest high-signal checkpoint sufficient for correct continuation.

This skill implements the accepted handoff model:
- handoff is a compiler output, not a chronological transcript;
- project state and handoff are different artifacts;
- handoff creates no authority;
- source authority is dimension-specific;
- observed and prescribed state remain distinct;
- retrieval stops at material sufficiency;
- producer handoff and receiver Context Receipt remain separate;
- transport framing is transport-specific.

The historical OCHP v3.4.2 is evidence for the Chat/Text transport profile, not universal handoff semantics.

## L1 — ordinary execution and L2 selection

First identify producer-initiated versus receiver-initiated transfer and actual transport. Reconstruct the minimum current accepted state, distinct from historical claims; emit a recoverable checkpoint or restore the receiver without silently mutating project canon. Normal ongoing execution is not a handoff.

**Conditional method index (read the selected file before its detailed method is needed):**

- **The receiver lacks current state, conflicting sources exist, or a durable checkpoint must be constructed from multiple records** → `references/PD_HANDOFF_RECONCILIATION.md` (source H2 sections 5,7,10).
- **A consequential transfer requires quality gates, restoration fidelity, context receipts or explicit unknown/blocked states** → `references/PD_HANDOFF_FIDELITY.md` (source H2 sections 11,12,13,14).
- **Structured or specialized transport requires nonstandard emission rules or metadata** → `references/PD_HANDOFF_TRANSPORT.md` (source H2 sections 15).

**No-trigger:** a short, resolved ordinary case does not require all detailed references merely because this skill was selected. Existing specialist references linked inside these materials remain conditional on their original situations. A moved section does not grant new permissions or replace the owning L1 safeguards.

## 0. Determine transfer direction and ownership

First decide whether this is an operational continuation request rather than ordinary recall or knowledge transfer.

Use this skill when the user wants enough working state from another execution context to continue correctly, even if the user does not say “handoff”. Examples include “continue this here from the other chat”, “bring all necessary context from chat X into this one”, or “restore that work here”.

Do **not** use the full handoff workflow when the user only asks to remember, summarize, or find a fact from another conversation. Do not replace `loom-foo-cross-context-transfer` when the task is to transfer lessons, mechanisms, or knowledge between projects rather than continue the same operational workstream.

When the user asks what skills, sources or checks were actually used, prefer the independent `loom-foo-execution-inspector` skill. Only when that skill is genuinely unavailable use the legacy `EXECUTION_INSPECT` fallback and read `references/EXECUTION_INSPECTOR.md`; label the fallback and its evidence limits. Neither path creates a continuation handoff, runs fresh checks merely to fill a receipt, nor authorizes persistence or external action.

Choose one direction:

### `PRODUCER_INITIATED`
The current context is the source. Compile a handoff for another destination using the existing workflow.

### `RECEIVER_INITIATED`
The current context is the destination and the material work state lives in another chat, agent, or source context. Before restoration, classify source quality:

- `VALID_HANDOFF_AVAILABLE` — a valid producer handoff is present; restore it normally.
- `SOURCE_CONTEXT_AVAILABLE` — sufficiently complete source conversation/checkpoint evidence is directly accessible with source identity/provenance; compile the same handoff semantics from that source, validate them, then restore into the current context. Keep producer transfer and receiver receipt logically distinct even if one runtime performs both steps.
- `PARTIAL_RETRIEVAL_ONLY` — only memory, summaries, snippets, search results, or other incomplete retrieval aids are available. They may locate or verify claims but must not silently substitute for a fidelity-preserving handoff. Obtain a source-side handoff when possible. Use degraded best-effort reconstruction only when the user explicitly accepts that trade-off, and mark material gaps `UNVERIFIED`.
- `SOURCE_UNAVAILABLE` — do not invent source state. Return the smallest actionable source-side handoff request or acquisition step needed to obtain a valid transfer.

These are entry-time evidence classifications, not new Kernel states or handoff terminal dispositions.

### Ordinary recovery is not handoff

Do not use a handoff as a mandatory relay after each ordinary failure, test, review finding or minor local remediation while the same executor can continue toward the same outcome inside its authority. A genuine change of context, agent, transport or material information boundary can justify a handoff; preserve the original outcome, exact subject, allowed authority and point of continuation. Avoid producing a fresh narrower task as a substitute for restoring the ongoing delegated execution.

## 1. Determine transport

Use the narrowest applicable transport mode.

### `CHAT_TEXT`
Default for ordinary ChatGPT/chat continuation. Read `references/CHAT_TEXT_TRANSPORT.md`.

### `STRUCTURED`
Use when the requested destination provides typed framing (for example a structured artifact, JSON/MCP-like channel, or repository-native checkpoint). Preserve generic handoff semantics but do not require the OCHP text envelope or its activation policy.

If transport is unspecified in an ordinary chat, use `CHAT_TEXT`.

## 2. Authority and side-effect boundary

A handoff request authorizes checkpoint reconstruction and handoff compilation.

It does not itself create:
- product/design/technical decisions;
- acceptance/review/merge/publication/deployment authority;
- permission to normalize conflicting external state;
- permission to implement pending work.

A missing durable effect may be performed only when that exact persistence transition was already authorized, unambiguous, repeat-safe, current state is checked, capability exists, and the result can be verified.

## 4. Project state vs handoff

Prefer current project-native continuity state such as `PROJECT_STATE.md` or established equivalents when available, then add only material verification needed for transfer.

Do not turn persistent project state into a transcript.

Do not make every handoff reproduce all observations/history.

## 6. Observed vs prescribed state

If authoritative prescribed state differs from directly observed state:
- preserve both;
- preserve the discrepancy;
- do not infer that mismatch is automatically a defect;
- do not destructively normalize without separate authority.

## 7. Materiality stop rule

Stop retrieval when more context cannot reasonably change:
- interpretation of current state;
- relevant constraints and semantic invariants;
- material scope/ownership boundaries;
- action authority;
- persistence obligations;
- resumption point and active reasoning frontier;
- correct execution after continuation.

Do not perform exhaustive project archaeology.

## 14. Output

For legacy `EXECUTION_INSPECT` fallback, emit only the requested execution receipt and indicate the independent Inspector is unavailable. Use exact visible evidence; mark partial source coverage. Do not append a second Answer Receipt if the requested output is itself a complete execution-inspection receipt.

For a `PRODUCER_INITIATED` normal Chat/Text handoff request, the final response must contain only the validated runtime handoff artifact.

For a structured producer handoff request, emit only the requested structured checkpoint artifact.

For `RECEIVER_INITIATED` requests:
- with a valid handoff, restore and emit the receiver-owned Context Receipt according to the transport profile;
- with directly accessible sufficient source context, compile/validate the transfer internally, restore it, and emit the receiver-owned receipt;
- with partial retrieval only, do not claim a full handoff occurred; obtain a producer handoff or explicitly label an authorized best-effort reconstruction as degraded;
- with unavailable source context, return the smallest actionable acquisition request rather than a fabricated checkpoint.

If the same user message also contains a substantive instruction to continue work after restoration, follow the transport activation rules after restoration and material verification.

Do not append explanatory commentary to a producer runtime handoff unless the user explicitly asks for protocol analysis rather than an operational handoff.
