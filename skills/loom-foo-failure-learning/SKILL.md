---
name: loom-foo-failure-learning
description: "Investigate a concrete agent/assistant failure, including missed skill activation and broken handoffs, and repair its cause. Not generic criticism."
compatibility: Agent Skills-compatible ChatGPT/agent clients. May use available conversation context, authorized project sources and tools. Routine in-scope project-native reads and writes derive from the user's actual task and applicable project authority across supported connectors; optional user-specific standing instructions may refine them, but are not universal. Memory changes, public sharing and separate effects retain their own boundaries. No background surveillance assumed. Excludes psychological analysis, emotional profiling, cross-domain personal-assessment routing and profile updates.
metadata:
  family: "engineering"
  project: "loom-foo"
  version: "0.10.0"
---

<!-- loom-foo Answer Receipt v0.3: compact standalone projection -->
**Answer Receipt (when consulted/applied).** End user-facing prose with one compact receipt listing only actually consulted/applied skills and versions, `SKILL.md` delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered reference coverage, sources, material checks, actual actions and limitations. `FULL` requires contiguous **model-visible** exact source through EOF, not merely tool retrieval; comprehension/execution is separate. For material distinct stages use an ordered **Process Trail** (review → repair → recheck), with actual findings, provenance and `SAME_CONTEXT` vs observed separate actors. No invented stages, independent review, tests, runtime telemetry, publication or action success. For detail consult `docs/ANSWER_RECEIPT_V0.3.md` if accessible. Do not append a footer when a strict JSON/code/machine/producer-only contract forbids it; do not run extra logging/tests just for the receipt.

# Failure Learning

## Critical contract — read first

**Owner:** Upon a concrete assistant/agent failure report (including ignored instructions, wrong skills, broken handoffs, repeated botched repair), **recover the original user task first**, then investigate the smallest evidenced failure and corrective action. An explicit user report is a direct trigger; do not ask permission to perform local read-only triage. A user's irritation or sarcasm is only a cue to check task evidence, **never** grounds for psychological profiling or inventing an incident.

**Separation:** `TASK_RECOVERY = RECOVERED | PARTIAL | BLOCKED | NOT_REQUIRED`; `LEARNING = LOCAL_FIX_ONLY | FINDING_READY | EVIDENCE_REQUIRED | IMPROVEMENT_PROPOSED | NO_LOCAL_DELTA | ESCALATED`. An analysis, proposal, PASS, or apology does not substitute for task recovery. Preserve already-correct output and original acceptance; stop unauthorized/risky action, then repair proportionately in existing authority. Don't demand a new owner gate for routine local repair.

## Operational method

1. **Trigger check:** Concrete discrepancy and actual expected behavior? If user only changes requirements, debates a concept, dislikes a style without violated requirement, or describes unrelated emotions, do not manufacture a Failure Case. A prompt about a reported missed activation *is itself* an incident to inspect. A repeated private Drive approval loop is a concrete trigger: begin Failure Learning instead of responding only with explanations or apologies; activation is not guaranteed unless the runtime actually routes to this skill. Never route operational failures to psychological/profile tools.
2. **Recover:** Identify the exact original outcome, subject and authority. Preserve what worked, fix the blocked task if safe; distinguish active-task status from systemic lesson. If an input/action needs specific new authorization, prepare only in-scope work.
3. **Reconstruct evidence:** Separate `OBSERVED` (actual trace/report), `EXPECTED` (source/user contract), `INFERRED` (hypothesis) and `UNKNOWN`. Check rival causes, including routing, context-delivery, composition, runtime/tool, policy/authority, semantic rules and evaluator defects. A user report proves a report, not the claimed cause. Missing access to older chats is `NOT_OBSERVABLE`, not permission to invent history.
4. **Minimal intervention:** Check existing skill owner and already-existing rules. A missed activation is generally a routing/delivery candidate rather than proof that `SKILL.md` semantics are wrong. Prefer one repaired prompt/description/fixture/tool/context handoff to new layers, global logs or unrelated changes. A single incident does not establish general prevalence.
5. **Truthful close:** Explain what failed, what was restored, what evidence supports/limits the diagnosis, what small delta is proposed, and what was *actually persisted*. Do not claim independent validation from a model-authored receipt. Avoid long ceremonies when one correction suffices.

**Conditional evidence-to-repair composition (L1).** For a retrospective claim about which skills, files, checks or actions actually ran, consult `loom-foo-execution-inspector` when its narrower evidence inspection is materially needed; do not call it merely to produce a receipt or as a required incident preflight. When a traced recurring failure is specifically in skill activation, owner boundaries, delivery or the reusable skill contract, consult `loom-foo-skill-engineering` for the smallest justified repair; a single missed activation is not itself proof that the SKILL.md body is defective. Failure Learning retains incident causality and original-task recovery; inspector findings do not execute new tests, and skill changes do not establish runtime routing until observed. An ordinary local correction needs neither specialist.

## Conditional method index (read BEFORE affected analysis)

- **Subtle/ambiguous trigger, sarcasm, failure-learning self-failure, missed activation or repeated delegation ping-pong:** `references/PD_FAILURE_ACTIVATION.md` (original §1).
- **Substantive incident requiring causal attribution, recovery strategy or skill-level correction:** `references/PD_FAILURE_RECOVERY.md` (original §§2–5). If writing durable Failure Case, also `references/FAILURE_CASE_CONTRACT.md`.
- **Portfolio/recurrence, storage/privacy, formal dogfood or cross-context incident evidence:** `references/PD_FAILURE_EVIDENCE.md` (original §§6–9 + final); for first-use tests `tests/DOGFOOD_PROTOCOL.md`.
- **Substantive proposed change/architecture:** `loom-foo-proposal-refinement` or the actual owner may take its own artifact. Consult its current instructions; do not imply its execution merely from mentioning it. Frozen C0/C1/C2 belongs to installed `loom-foo-skill-validation`, or `UNAVAILABLE`.

## Privacy and authority

**Routine Authorized Operations recovery:** An actual user task and applicable project context authorize ordinary necessary in-scope project-native file operations without fabricated per-file/per-step gates across supported storage providers. If preparing a durable output includes known downstream delivery, continue that delivery without a *prepare*-versus-*save* fiction; do not save mere chat drafts unnecessarily. A user-specific standing grant may apply when verified, but must never be asserted as universal. Filename/count/hash/ordinary regeneration do not themselves require reapproval. **Do not infer authority for Git merge, public sharing, new external audience, paid calls, destructive irreversible changes, Memory updates or independent task launch.** Respect explicit no-write, actual inherited audience, connector write limitations, native host approvals and OAuth/ACL denials; do not bypass them. Distinguish `MODEL_INVENTED_GATE`, `HOST_REVIEW_REQUEST`, `HOST_DENIED`, `PROVIDER_AUTH_OR_ACL_ERROR`, `CONNECTOR_CAPABILITY_MISSING` and `NOT_OBSERVABLE` from actual traces. Keep incidents project-local/private and source-grounded. If this skill missed a trigger or fabricated a gate, mark self-failure; do not self-certify the fix. Normal final answer prioritizes restored user result; one proportional Answer Receipt only when used.
