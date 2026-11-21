> **Compatibility note (Answer Receipt v0.2, 2026-11-17).** The independent `loom-foo-execution-inspector` skill owns new execution-inspection requests when available. This legacy reference is a fallback for stale or constrained runtimes. Preserve its evidence boundaries; do not claim current activation of the independent skill without a read.

# Execution Inspector

Use this mode when the user asks what skills, sources, actions, or checks were actually used in the current task or an explicitly accessible conversation.

## Evidence boundary

Inspect only visible messages, runtime skill context, tool results, source records, and execution receipts available here. Do not infer hidden activation, tool calls, or verification from the final answer alone. A starter prompt, available skill, or mention of a source is not proof of loading, use, or reading.

Use these distinctions:

- **Available:** present in the exact runtime/package catalog inspected; this does not prove it was loaded.
- **Loaded:** confirmed only by active runtime context or a direct read/load of the exact skill instructions in this execution. Hidden activation timing is not recoverable without telemetry.
- **Applied:** name the concrete action supported by the visible evidence. If there is no evidence, report `NOT EVIDENCED`.
- **Sources:** list only sources actually opened or returned by a tool and used in the task. Include a title plus URL, file ID, release, commit, or other identity when visible. A user-supplied claim is not an independently checked source.
- **Verification:** use `PASS`, `FAIL`, `UNVERIFIED`, or `NOT RUN`. Preserve the scope and exact check. A successful command is not a PASS unless it covers the stated property. If an underlying report uses a narrower status such as `INCONCLUSIVE` or `NOT COVERED`, preserve it in the note.
- **Limitations:** state missing transcript ranges, inaccessible sources, partial history, runtime uncertainty, or unsupported checks that affect the receipt.

If the requested work is in another conversation, use it only when the full source conversation or a valid execution receipt is accessible. Search snippets or memory summaries support only a partial receipt and must be labeled accordingly.

Do not run new checks or collect new evidence merely to fill the receipt. If the user asks for fresh verification, route that work to the applicable verification owner and report it separately.

## Execution Receipt v0.1 — optional, evidence-bound

Use `ON_DEMAND` by default. Produce a compact text receipt unless the user/downstream consumer explicitly needs structured data. This is an **inspector output**, not a new always-on recording system, a mandatory task artifact, or proof of hidden runtime activation. Never silently save, transmit, or publish it.

Select evidence mode by actual provenance:
- `ON_DEMAND`: reconstruct from current accessible messages, tool results and sources; annotate gaps.
- `EVIDENCE_BACKED`: primary command output, tool responses, test logs or versioned artifacts are actually accessible.
- `TRACE_BACKED`: a genuine runtime-provided structured event stream is accessible, with identifiable run and coverage. A user-authored example JSONL or a self-report is not runtime telemetry.
- `PARTIAL`: use as a **coverage qualifier**, not a fourth source of authority. Any mode may have partial coverage.

The smallest useful structured representation (only when needed) is:

```json
{
  "receipt_version": "0.1",
  "subject": "exact candidate or bounded task identity",
  "evidence_mode": "ON_DEMAND",
  "coverage": "PARTIAL",
  "skills": [
    {"skill": "skill-id", "source_identity": "version or UNKNOWN", "available": "AVAILABLE", "loaded": "NOT_CONFIRMED", "applied": "NOT_EVIDENCED", "evidence_refs": []}
  ],
  "checks": [
    {"claim": "bounded property", "subject": "exact checked artifact", "status": "UNVERIFIED", "claimed_result": "PASS", "evidence_class": "REPORTED", "evidence_refs": ["report-id"]}
  ],
  "evidence": [
    {"ref": "report-id", "kind": "REPORT", "locator": "verifiable source path or URI", "scope": "what the source can actually prove"}
  ],
  "limitations": ["missing primary execution log"]
}
```

`evidence_refs` must resolve to an **actually observed** accessible source or explicitly identified inaccessible source; never invent locators. If a field cannot be grounded, use `UNKNOWN`, `NOT_CONFIRMED`, `NOT_EVIDENCED`, `UNVERIFIED`, or omit that optional field. Keep `claimed_result` separate from verified `status`.

### Evidence and status rules

- `available`: `AVAILABLE | UNAVAILABLE | UNKNOWN` for the exact inspected runtime/version.
- `loaded`: `CONFIRMED | NOT_CONFIRMED`. Direct tool read of exact skill instructions confirms a read; source files merely packaged or edited do **not** prove agent activation. Keep uncertainty about hidden automatic activation explicit.
- `applied`: `EVIDENCED | NOT_EVIDENCED`. Describe the concrete action/decision and its source; a plausible influence from a skill cannot establish causality.
- `evidence_class`: `OBSERVED | REPORTED | INFERRED | UNVERIFIED`. A report stating tests passed is `REPORTED`, not an observed test run.
- `status`: `PASS | FAIL | INCONCLUSIVE | NOT_COVERED | NOT_RUN | UNVERIFIED`. Use `PASS` only for a directly observed check that actually establishes the property for the **exact** subject. `NOT_RUN` requires evidence it was not run, not simply an absent log. Without primary evidence, keep a reported PASS as `claimed_result: PASS`, `status: UNVERIFIED`. An accessible, authenticated artifact report alone does not make its underlying test claims `OBSERVED`.
- Version/readback demonstrates release **installation**, not runtime skill discovery/routing; event traces show events they actually cover, not hidden motivations or skill causality.
- Missing source files or spans limit coverage. A complete local JSONL log cannot establish the completeness of host-internal tracing unless the host explicitly guarantees it. If a run is only a local subprocess, label it `LOCAL_SUBPROCESS_TRACE` and **never** call it Codex telemetry.

### Minimal capture when producing a high-stakes result

The **owning workflow**, when it already produces a consequential claim, should preserve references to the original tool result, exact checked subject, test outcome and limits where native logs exist. The inspector consumes these references; it does not become a required observer of every skill or request broad always-on tracing. If evidence was not captured, report the gap instead of reconstructing nonexistent tool calls. Use existing project-native logging and storage; no separate database or network sink.

### Privacy and authority

Store locators or narrowly scoped summaries, not raw credentials, private document bodies, attachment contents or sensitive tool arguments. Do not copy user-private artifacts into a distributable skill or test fixture. When source access is restricted, preserve that restriction; don't expand permissions or disclose values to complete a receipt. Inspection is read-only by default and confers no execution, upload or publication permission.

### Conditional integration

Keep `EXECUTION_INSPECT` owned by `loom-foo-handoff`. If requested to freshly verify properties, defer that work to `loom-foo-change-verification` or other appropriate owner. `loom-foo-skill-engineering` already has release/verification evidence duties; do not create a new skill, central telemetry service or universal return schema. Test this contract on a prior release receipt and one observed structured local run before adding any cross-skill requirements.

## Receipt format

Keep the result proportional. A small task can use the compact form below:

```text
Execution Inspector — <scope>
Evidence basis: <current conversation / exact receipt / partial history>

| Skill | Availability | Loaded | Applied |
|---|---|---|---|
| <name and version if verified> | <AVAILABLE / UNAVAILABLE / UNKNOWN> | <CONFIRMED / NOT CONFIRMED / UNVERIFIED> | <evidenced action or NOT EVIDENCED> |

Sources: <actual sources and identities, or NONE>
Verification: <PASS / FAIL / UNVERIFIED / NOT RUN, with scope>
Limitations: <material limits, or NONE OBSERVED>
```

Do not present this response as a persistent audit log or complete runtime trace. Without telemetry, the receipt is a bounded account of available evidence, not a reconstruction of every internal activation.
