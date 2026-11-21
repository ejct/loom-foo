---
name: loom-foo-execution-inspector
description: "Audit claimed agent execution, skill reads, tools and checks against accessible evidence. Not running new tests or repairing artifacts."
compatibility: "Agent Skills-compatible; runtime telemetry and source history may be absent."
metadata:
  family: "engineering"
  version: "0.3.0"
  project: "loom-foo"
---

# Execution Inspector

## Critical contract — read first

- **Evidence only:** Reconstruct from observable current messages, tool returns, source read ranges, receipts and genuine provided runtime events; never infer unseen activation, completion, or verification.
- **Permission:** Inspection is read-only. Do not execute new tests or open unrelated private records solely to make a receipt look complete. A new verification request belongs to its proper specialist.
- **Scope:** This skill owns retrospective **Execution Inspection** for any workflow, not only handoffs. An ordinary answer-level **Answer Receipt** is produced by the responding workflow without activating Inspector.

<!-- loom-foo Answer Receipt v0.3: shared response provenance and Process Trail projection -->
**Answer Receipt.** When this skill is directly consulted or materially applied in preparing a user-facing answer, include a compact **Answer Receipt** as the final section. List only actually used/consulted skills (including external skills when evidenced), exact versions if known, `SKILL.md` delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered reference coverage, actual sources, checks, actions and material limitations. `FULL` requires model-visible contiguous delivery of the exact source through EOF, not a reader success flag. **Process Trail:** for substantive multi-stage work, including repeated proposal/task reviews, corrections, verifications or genuine cross-agent/artifact handoffs, show an ordered breadcrumb sequence such as `DRAFT1 → REVIEW1 → REVISE1 → REVIEW2 → READY`, with a brief result, exact artifact identity when established, and provenance for consequential stages. Preserve distinct repeated passes in their original order; do not invent unseen stages, file revisions, handoffs, independence or runtime events. Different consulted skills in the same agent context are not separate agent executions. An internally reconstructed review is `MODEL_REPORTED`, not independently verified. Keep one footer, not a second Processing Receipt. No new tests or logging merely for the footer. Follow `docs/ANSWER_RECEIPT_V0.3.md` when accessible; this clause works standalone. Preserve JSON-only, machine payload, code-only and strict producer handoff formats when a footer is forbidden.

## Trigger and sibling boundaries

Use for requests such as 'What skills did you actually load?', 'Was SKILL.md fully delivered?', 'Audit the Answer Receipt', 'Prove those tests ran', 'Which agent took which action?'. Do not use for ordinary final-answer reporting; handoff restoration belongs to `loom-foo-handoff`; artifact correctness checks belong to `loom-foo-change-verification`; evidence-package interpretation to `loom-foo-evidence-review`; a single questionable claim to `loom-foo-sanity-check` where available.

## Procedure

1. Identify the exact bounded run or answer and evidence horizon; record source and runtime version if exposed. Do not guess missing messages or logs.
2. Extract actual skill metadata, direct reads, exact source ranges and reference-file reads. Mark source delivery `FULL` only for contiguous model-visible coverage of the full exact version through EOF; if the forwarding channel is unknown use `NOT_CONFIRMED` even if the upstream read succeeded. Model reception is not comprehension.
3. Compare claimed actions, checks and publications with direct evidence. Distinguish `RUNTIME_OBSERVED`, `TOOL_OBSERVED`, `SOURCE_SUPPORTED`, `MODEL_REPORTED`, and `UNKNOWN`. Keep actual status (`PASS/FAIL/INCONCLUSIVE/UNVERIFIED/NOT_RUN/NOT_COVERED`) distinct from a claimed result. No evidence is not proof of NOT_RUN.
4. Review an Answer Receipt against available evidence and identify only material mismatches, omissions and unsupported FULL/PASS/sent/install assertions. Distinguish confirmed contradiction from missing evidence.
5. Return an **Execution Inspection**: subject; coverage and provenance; relevant skills/read coverage/references; sources/checks/external actions; findings; material unknowns. Show a compact summary by default, detail on request. Do not claim host-level telemetry when only local events or agent-written logs are available.

## Process Trail inspection

For a receipt that includes a Process Trail, check the **actual order, repeated-pass identities, artifact version/derivation, reviewer identity and claimed independence**, and whether evidence supports the stated stage outcomes. A skill label in a self-report is not proof another agent executed; a model-authored staged narrative is not runtime telemetry. When only the final response exists, qualify the historical trail as `MODEL_REPORTED` or `UNVERIFIED`, and never manufacture missing intermediate revisions.

## Privacy and boundaries

Link to evidence locations rather than copying raw private tool arguments, credentials, personal source bodies or hidden internal instructions. Runtime trace is only as complete as host guarantees. Do not assign numeric correctness/confidence scores. No network sink, global logger or mandatory audit loop.

## Related shared contract

Read `docs/ANSWER_RECEIPT_V0.2.md` when available in the plugin package; it defines the answer-level projection and does not delegate ordinary response rendering to Inspector. Inspector can consume the same records but has no right to rewrite the original answer or invent independent results.
