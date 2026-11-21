---
name: loom-foo-sanity-check
description: "Resolve a concrete agent judgment or evidence-boundary warning with the smallest decisive check. Not mandatory general review."
metadata:
  family: "engineering"
  version: "0.9.0"
  project: "loom-foo"
compatibility: Agent Skills-compatible clients. External sources and deterministic tools are optional; a skill cannot ensure its own activation or intercept arbitrary host actions.
---

<!-- loom-foo Answer Receipt v0.3: compact standalone projection -->
**Answer Receipt.** Finish user-facing prose with one compact receipt naming only actually consulted/applied skills and versions, `SKILL.md` model-visible delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered L2 coverage, sources, checks, actions and limits. `FULL` requires complete contiguous exact text to EOF; a successful tool fetch alone is insufficient. Use ordered **Process Trail** for actual material review/repair/recheck stages, with artifact identity and honest `SAME_CONTEXT` versus observed separate actors. Never invent independent reviews, tests, host routing, publication or external effects. Omit the footer only for strict machine/code-only output contracts.

# Sanity Check — decision-time reality check

## Critical contract

- **Original outcome first.** Restore the user's actual requested result; correcting one defect must not substitute an audit, study or new task for delivery.
- **Reality beats introspection.** Confidence, repetition, another pass over the same model-generated text, and unverified summaries are not independent evidence.
- **Exact claim, exact evidence.** A source snippet does not prove a whole source was read; local file existence does not prove remote upload, successful deployment, content correctness or plugin activation; a completed command does not prove an unrelated requirement.
- **Authority unchanged.** A user's actual task and established project rules may cover ordinary necessary in-scope project-native read/create/edit/organize/save across supported services; do not invent per-file or *prepare*-versus-*save* approval gates. Connector access or a claimed ownership label alone is not permission for unrelated actions. An optional verified user grant may refine scope. Verification does not grant permission to spend, publish, contact third parties, alter sharing, launch independent tasks or bypass real host/tool denials.
- **Zero ceremony when nothing is wrong.** A routine request should proceed directly; do not invent a mandatory report, score, second agent or review loop.

## Additional conditional detail

First identify the smallest decisive check and act locally; never turn this skill into a universal checkpoint. When an evidence-type-specific oracle is necessary, read `references/PD_EVIDENCE_ORACLES.md` before claiming a verdict.

**Trigger:** A concrete evidence type (source/tool/verifier/authority/runtime claim) calls for specialist falsification checks beyond the ordinary bounded procedure. Do not load this file for routine cases where that condition is absent.

## Responsibility

Input: an *identified* material doubt about a candidate claim, decision, approval requirement or next action, with the original user goal and observed evidence available.

Output: one disposition — `PROCEED`, `CORRECT`, `QUALIFY`, or `HOLD_ACTION` — and the corrected claim/next safe action. Usually keep diagnosis internal. Resume the original task wherever authorized.

This is a **triage** skill, not a universal fact checker, specialist review, release gate, evidence collector or runtime hook. It cannot detect its own missed invocation.

## Activation: event before review

Invoke explicitly when the user requests a sanity check, or by a standing instruction or host when any **material** event occurs:

1. **COMPLETION_CLAIM:** about to claim `read in full`, `sent`, `saved`, `installed`, `released`, `verified`, `tested`, or `finished` without a matching observed operation/result.
2. **SOURCE_COVERAGE:** retrieved content is truncated, sampled, partial, stale, inaccessible or its identity differs from the claim.
3. **CONTRADICTION:** a user constraint, authoritative source, tool return, error status or prior verified state conflicts with the proposed answer or action.
4. **RISKY_PRECONDITION:** a consequential or irreversible action relies on an unverified material assumption (check evidence **and** actual action authorization).
5. **GOAL_DRIFT:** the plan introduces an unrequested audit, escalation, repetitive loop or elaborate path when a directly authorized shorter route could satisfy the actual goal.
6. **CHECKABLE_FACT:** a consequential externally verifiable claim has no suitable source and would change the answer or decision.
7. **UNNECESSARY_AUTHORITY_GATE:** an agent plans to request permission, emit `DELIVERY_PENDING_AUTHORITY`, or stop an ordinary project-native operation despite a task and context that already authorize it. This includes Google Drive, Dropbox, OneDrive, Notion and local files where supported. *Prepare*, changed in-scope filename/count/hash or ordinary regeneration are not independent approval gates; neither do they force an upload of an in-chat draft. Identify a **specific material scope/audience/data/effect change** or actual native host/tool control before holding action. Distinguish invented model gates from real review, denial, OAuth/ACL error and a read-only connector; never bypass a genuine denial.

**Do not invoke** for low-stakes conjecture labeled as conjecture, ordinary creative work, writing edits, generic long tasks, user frustration alone, or because *any* claim could hypothetically be wrong. Prefer `loom-foo-change-verification`, `loom-foo-evidence-review`, `loom-foo-proposal-refinement` or other specialists when they own the primary requested review. If a specialist already handles the particular verification, do not run a parallel generic review.

## Procedure — bounded and falsifiable

1. **Preserve target:** record internally the original deliverable and single questionable claim, action or approval requirement. Do not change scope.
2. **Specify falsifier:** what observable fact contradicts it? For an approval gate, inspect the real owner dispatch, controlling delivery profile and intended effect; do not assume the gate is valid because another model or reviewer wrote it.
3. **Check the closest oracle:** choose the least expensive *decisive* observation: original source with location/coverage; authenticated operation result; deterministic test/API observation; current official docs; or independent check that adds information. A second model agreeing with the same context does not qualify.
4. **Resolve scope:** `PROCEED` for confirmed in-scope authority; `CORRECT` if the gate or claim is contradicted; `QUALIFY` if evidence is inconclusive while safe work continues; `HOLD_ACTION` only for a genuinely missing permission, safety, or material irreversible-action precondition. A model-authored Task Brief cannot remove owner-granted authority without a valid higher-priority source, nor grant missing authority.
5. **Resume:** correct the statement or immediate plan and continue the user's task. Do not recursively invoke checks, collect proof for its own sake or overwrite correct work.

If a claim cannot be checked in the current runtime, state specifically what is unknown; do not hallucinate a tool result. A failed check may restrict the *claim* without blocking unrelated permitted work.

## Stop rule and reporting

One decisive check is the default. Expand only if the first result exposes a material unresolved contradiction affecting the next action. Do not perform compulsory multi-pass review, independent benchmarking or new ceremony. Report changed conclusions, blocked effects or incomplete verification plainly; otherwise deliver the original result.

## Runtime and deployment boundaries

A skill is loaded selectively. For always-needed event cues, use host-supported standing instructions (see `AGENTS_SNIPPET.md`) and narrow deterministic controls in the execution path. Installing this package does **not** install that snippet or a hook, enforce its use in every chat, or prove improved behavior. No universal host interception, independently enforced verdict or fail-closed behavior is claimed.
