# loom-foo-agent-task-design — detailed instructions (PD_TASK_OUTPUT_AND_CONFIG)

> Conditional reference for `../SKILL.md` (progressive disclosure migration based on private loom-foo 0.27.0). The source sections below preserve their original normative content; Markdown `references/` links are rebased to sibling files. Read for the trigger named in the current root; do not silently treat all references as always loaded.

## 16. Output forms

### `TASK_READY`
Return the Task Brief, and when requested or useful, a runtime-specific rendered prompt. The Return Contract must be derived from the next authorized consumer or owner decision and tested for **Next-Step Readiness**, rather than defaulting to a generic completion summary. Before this status, check the **delegated result** against the owner's intended goal and governing accepted Work Unit; distinguish worker/experiment completion from root and parent success. `TASK_READY` means the *brief* is executable, not that the work was performed, that an engineering gain was observed, or that a parent product goal is achieved.

### `PLANNING_REQUIRED`
State why the request is not one coherent executable unit and identify the smallest visible decomposition boundary. Do not invent an execution-planning subsystem inside this skill.

### `NEED_CONTEXT`
Name the exact missing subject/authority/context dimension that materially prevents a correct task. Do not ask for information already available in current authoritative sources.

### `BLOCKED`
Use when a required authority/source/runtime property cannot be established and no honest bounded task can proceed.

## 17. Composition

- Proposal accepted/bounded -> this skill may compile the implementation/evaluation task.
- An already accepted multi-unit Work Plan + an authorized root execution request -> this skill may compile **one Root Execution Brief** with independent worker tasks, root-only orchestration and integrated closure evidence; Work Decomposition retains ownership of designing or changing the plan.
- Architecture ready -> this skill may compile a bounded implementation/probe task without redesigning architecture.
- Handoff continuation -> restore state first; if the next authorized work unit needs a new execution brief, apply this skill afterward.
- Cross-context transfer -> transfer findings may become context/input, but this skill owns only the final bounded execution task.
- Boundary-safety/runtime guardrails -> they may constrain execution; this skill must represent those constraints faithfully but does not replace runtime enforcement.

Avoid recursive ownership.

## 18. Skill maintenance and proportionate checks

This active skill has an ordinary semantic version and exact source identity. Do not make runtime use contingent on a separate `candidate` or promotion status. Frozen historical evaluation subjects remain historical and immutable; preserve evidence and exact versions without turning every local skill revision into a promotion campaign.

For consequential revisions check the failure modes implicated by the actual change, including single-task versus many-unit scope, delegated outcome fidelity, authority boundaries, runtime projection and premature-return regressions. Prefer one direct real-world routing/execution smoke check when available. Stronger validation belongs to consequential deployment or independent research decisions, not every routine skill edit. Installation/discovery and publication are separate transitions.

## 19. Workflow Configurator (opt-in)

Use this mode only when the user asks to configure loom-foo for a particular task, conversation session, or project. Produce a reviewable settings draft and a ready-to-use task instruction derived from it. Do not route ordinary requests through a setup dialogue or change the ordinary Task Brief contract.

This mode describes how a task should be handled; it does not change the actual runtime, load or install skills, install agent roles, launch agents, or modify every skill's behavior. State the difference between a requested target runtime and the runtime actually available. Never claim a draft was applied merely because it was produced.

### Resolve the requested settings

Use a clear value from the user's request when available. Otherwise use these defaults and label them as defaults:

| Setting | Default and allowed values |
| --- | --- |
| Runtime | Current observed runtime; a task instruction may target ChatGPT or Codex, but the draft cannot switch runtimes. |
| Task type | Infer Research, Design, Development, or Review from the task; ask only if the distinction would materially change the instruction. |
| Context | Current conversation, or the named project when the user identifies one. A project name alone does not grant access or write authority. |
| Verification | Proportional. Add deeper checks when stakes, uncertainty, explicit request, or acceptance criteria justify them; never disable verification. |
| Agent roles | Default; do not require or automatically start multiple agents. |
| Scope | One task. Session means a conversation preference, not durable storage. Project means a proposed project configuration only. |

`loom-foo-agent-role-setup` is an OPTIONAL standalone Codex project-skill export, with a Codex-only execution contract. A Codex task draft may name `minimal`, `review`, or `specialists` only when the exact Role Setup skill is available in that runtime and its current source confirms those presets. Otherwise mark role installation **UNAVAILABLE**. In ChatGPT, Codex role presets are **UNAVAILABLE**. This Configurator never installs or applies them; do not infer executable Codex setup from a saved export or invent capabilities.

If a selected setting is unsupported by the current runtime, retain it only as a requested target when useful and mark it **UNAVAILABLE** or **NOT APPLIED**. Do not render it as an active configuration. Interactive controls are optional; the complete flow must work through ordinary chat text.

### Return the draft

Use a compact table with each value marked as user-selected, inferred, or default. Include an availability/application status and a short limitation where needed. Distinguish what is supported by the current runtime from what is only represented in the generated instruction.

Then provide a task instruction that includes the accepted settings and preserves the user's actual task outcome, authority, relevant context, and acceptance checks. A user may revise the draft before using that instruction.

### Scope and authority limits

- **One task:** the setting applies only to the accompanying draft instruction. Do not start unrelated work or imply any setting persists.
- **Session:** only treat the accepted draft as a conversation-level preference for the remainder of this conversation. It is not durable storage and does not alter skill definitions or base runtime rules.
- **Project configuration:** always return **DRAFT / NOT WRITTEN** in this mode. Do not edit project, GitHub, Drive, or other files. A future write requires a separate explicit user request and a tool authorized for that exact project.
- Keep core safety, source verification, and authority rules active under every configuration. Never offer a setting that disables them.
- Keep Codex-only role presets unavailable in ChatGPT. A draft never grants permission to perform a project write, role installation, external action, or other state change.
