---
name: loom-foo-onboarding
description: "Guide explicit Loom-foo setup or first-use task selection. Not routine specialist work, a global router or account-settings changes."
metadata:
  family: "engineering"
  version: "0.2.0"
  project: "loom-foo"
compatibility: Agent Skills-compatible clients; plugin install, inventory and runtime activation may not all be observable.
---

# Loom-foo Onboarding

## Goal and authority

Help the user successfully start **one real task** with Loom-foo by identifying relevant available specialists and handing the task to its proper owner. Setup is optional, and does not configure global host routing or modify the user's account or project files.

**Positive triggers:** first-run/Setup invoked by the plugin, "get started with Loom-foo", "introduce Loom-foo", or explicit onboarding/first-task selection.

**Non-triggers:** an ordinary work request in design, research, engineering, planning, writing or agent execution; a request already naming a specialist; skill portfolio diagnosis or revision (owned by `loom-foo-skill-engineering`); a request to create a Task Brief (owned by `loom-foo-agent-task-design`). Do not compete for generic tasks merely because Loom-foo is installed.

## Path

1. **Preserve the task.** If installation or Setup interrupted an existing concrete request, resume that exact request through the appropriate specialist; skip the welcome and do not ask the user to restate known inputs.
2. **Check availability.** Use runtime-visible installed skill names/descriptions or the actual plugin catalog. State the exact bundle version only if current metadata was read. Do not infer that a packaged, listed or named skill was selected or executed.
3. **Offer a concise entry.** If no task is known, explain what Loom-foo does and offer a few concrete first tasks using the available specialist descriptions (e.g. design critique, research, task brief, failure diagnosis). Invite a custom task. Do not show a full directory unless requested.
4. **Choose and hand off.** Match the user's specific goal to the most relevant specialist's current `description`, preserving the original request and constraints. Load its `SKILL.md` completely and only its conditionally required references, using actual tool availability. Do not add onboarding steps to the specialist's work or force a global parent/router.
5. **Finish with evidence.** After actual use, state the outcome, which skills and supporting instructions were genuinely read/applied, actual checks, and material limitations. If no task has been chosen, finish with a useful first-task invitation; do not claim activation or setup completion.

## Restrictions and fallback

- Never write to ChatGPT settings, memory, plugins, permissions, connected services or source repositories as part of onboarding without distinct authorized action. No installation hook or silent account mutation.
- Respect user instruction and skill authority boundaries. Reading a skill does not grant access, approval or publication rights.
- Do not assume Setup runs automatically on installation, or that the host guarantees implicit invocation. If the host cannot expose installed skills or a selected skill is unavailable, explain the limitation and offer an ordinary answer with available capabilities.
- An irrelevant question should proceed without this skill. The user can skip Setup at any time.
- Loading only this onboarding skill is not evidence that a separate specialist ran or that automatic routing was tested.
