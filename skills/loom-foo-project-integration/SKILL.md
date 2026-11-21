---
name: loom-foo-project-integration
description: "Evaluate and set up optional foo-loom project integration for long-lived agent work. Not ordinary one-off task design or install without authority."
compatibility: "Portable Agent Skills-compatible clients. Read-only assessment works without local project access; applying foo-loom Core requires access to the exact authorized workspace/source and a project-scoped write authorization."
metadata:
  family: "planning"
  project: "loom-foo"
  version: "0.4.0"
---

<!-- loom-foo Answer Receipt v0.3: compact standalone projection -->
**Answer Receipt.** Finish user-facing prose with one compact receipt naming only actually consulted/applied skills and versions, `SKILL.md` model-visible delivery (`FULL | PARTIAL | METADATA_ONLY | NOT_CONFIRMED | FAILED`), triggered L2 coverage, sources, checks, actions and limits. `FULL` requires complete contiguous exact text to EOF; a successful tool fetch alone is insufficient. Use ordered **Process Trail** for actual material review/repair/recheck stages, with artifact identity and honest `SAME_CONTEXT` versus observed separate actors. Never invent independent reviews, tests, host routing, publication or external effects. Omit the footer only for strict machine/code-only output contracts.

# Project Integration — optional foo-loom project readiness

## Critical contract

- **One user-facing product:** `loom-foo` is the entry to agent workflows. `foo-loom` supplies optional durable project infrastructure (Development Kernel, pinned Bootstrap, explicitly adopted policies). Do not require the user to understand this distinction before getting useful work done.
- **Platform-controlled availability:** This skill is independently discovered/selected by the host. Users enable or disable it using their platform's normal Skill controls where supported. **Do not implement an Auto/Off/On switch, persistent toggle, global registry, mandatory parent skill, or a fallback trigger inside another skill.** If this skill is unavailable, ordinary task authoring remains unaffected.
- **Original outcome first:** Evaluate project readiness only when it changes a real project/delegation decision. A successful setup is a prerequisite, never a replacement for the requested feature, fix or research result.
- **Authority:** Inspection and proposal do not authorize writes. Neither installing Core nor copying policy files automatically adopts those policies. Preserve the user's existing project instructions, historical pins, external action boundaries and privacy.
- **Evidence:** A prepared instruction is not an install; an install is not skill discovery; discovery is not loading; loading is not application; a staged agent profile is not a demonstrated runtime spawn. Report only the highest observed layer.

## Additional conditional detail

Do not install or configure a project merely from a recommendation or tool capability. For authorized setup, read `references/PD_AUTHORIZED_SETUP.md` first; respect exact project identity, permissions, local state and rollback.

**Trigger:** Actual foo-loom project installation, runtime configuration or long-lived handoff is now authorized and feasible. Do not load this file for routine cases where that condition is absent.

## Ownership and triggers

**Owns:** `durable-project work + known project state + authority -> project-readiness decision + bounded, executable setup/continuation handoff`.

Use for an explicit request to initialize/inspect/connect a project with foo-loom, or when preparing work on a *durable* agent-developed project with a material continuity, project authority, repeat-session or multi-workstream need. A user who merely asks for a Codex Task Brief has not necessarily triggered Project Integration. Do not infer need from project size, prompt length, tool availability or message count.

**Sibling boundaries:** `loom-foo-agent-task-design` owns Task Brief and target-runtime rendering; `loom-foo-project-planning` owns a project's roadmap; `foo-loom-bootstrap` resolves already-installed Core authority and selectively loads context; the exact `foo-loom` installer owns filesystem changes; the optional Role Setup manager owns custom Codex TOML profiles. This skill **does not** reimplement those mechanisms, silently invoke another specialist, or mandate that another Skill call it. When both this skill and task-design are independently applicable, give task-design a short readiness clause rather than redesigning the task.

## 1. Detect whether durable infrastructure is material

Quickly assess the actual work, project-native evidence and user's desired result:

- Work continues across independently started agent sessions, or uses recurring agents on the same repository.
- Accepted decisions, invariants and authority must survive handoffs without repeatedly pasting a large prompt.
- Multiple workstreams need consistent acceptance/integration semantics or exact candidate identity.
- Existing `AGENTS.md`, project Skills, policies or conventions may already cover the need. **Compare before proposing duplication.**

If no material gap exists, continue the user's original work with **NO_SETUP** and no Core ceremony. If the user explicitly asks to install foo-loom, inspect readiness even if the project is small.

## 2. Resolve local evidence, without inventing access

If a trusted project workspace is accessible, read only the material files: existing `AGENTS.md` or equivalent, `.foo-loom/foo-loom.lock`, historical `.loomloom/loomloom.lock`, project Skill entries, accepted project policies, and relevant project state. Do not read private files unrelated to the task. Establish the exact Core source/version **only** from a verified pin or separately supplied approved source; mutable `main` is not a safe substitute. Reuse existing accepted project rules; copied Core policy files have no authority by themselves.

If the target is local Codex and ChatGPT cannot inspect that workspace, record **LOCAL_INSPECTION_NEEDED** and include a minimal read-only preflight in the *same* agent work unit. Do not report a speculative current install state.

## 3. Decide and prepare the smallest result

Choose the applicable operational finding:

- **NO_SETUP:** One-off task or existing project-native setup is sufficient. Deliver no integration clause.
- **EXISTING_CORE:** Exact pin and adopted policies are identifiable. Preserve them; bootstrap using the existing project entrypoint, without reinstall/upgrade.
- **SETUP_PROPOSED:** A material gap exists but project-scoped write approval or approved exact source is absent. Summarize the concrete changes/permission needed; do not install.
- **SETUP_AUTHORIZED:** Source, workspace, intended managed files and scope of writes are already explicitly authorized. Prepare a safe, bounded setup + verify + continue sequence for the executor.
- **LOCAL_INSPECTION_NEEDED:** The target runtime must inspect its own workspace before selecting any of the above. Include a read-only preflight, not an unconditional install.

These are **diagnostic outcomes**, not selectable enable/disable modes, persistent settings or a UI. Do not create configuration files solely to store them.

## 5. Output and stop rule

Keep the integration note small: **finding**, supporting signal/current pin, required approved action or read-only preflight, and continuation/verification boundary. Reuse the normal Task Brief; do not create another mandatory project plan, registry, scoring system, or approval ritual. A recurring project-level authorization may cover a bounded set of future managed-file writes, but **must not** be inferred from general task consent, granted tool access, a prior unrelated approval or this skill's activation.

Complete when the user has a correct readiness disposition and, where authorized/possible, verified setup plus continuation. If host skill loading, local execution, runtime discovery or output delivery cannot be observed, label that specific layer **UNVERIFIED**. No plugin installation, code snippet or Skill invocation proves its own automatic future selection.
