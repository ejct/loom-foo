# project-integration — conditional method

> Preserved sections from private Loom-foo 0.35.1 SKILL.md. Referenced `references/...` paths are relative to the owning skill root. L1 activation and authority remain controlling.

## 4. Authorized installation and continuation

When the project is explicitly approved for Core setup:

1. Resolve the **exact, available** foo-loom source commit or immutable package and compatible installer. Do not point a new install at mutable branch HEAD, and do not change historical Core pins.
2. Preview proposed changes to `.foo-loom/`, `.agents/skills/foo-loom-bootstrap/` and the managed portion of `AGENTS.md` using available safe reads/diffs. If the actual installer has no native `--dry-run`, do **not** invent one; use a copy/snapshot or equivalent preflight before approved writes. Protect symlinks, changed managed blocks and unrelated instructions.
3. Apply only the explicitly approved project-local writes using the actual available installer, verify exact pin, installed files, managed block and preserved neighboring content. Any new Core policies remain **unadopted** until the project authority explicitly accepts them. Never silently upgrade.
4. Default to **one ordinary primary agent and no custom `.codex/agents/*.toml` profiles**. Native delegation remains on demand. Install optional specialized profiles only with separate specific authorization and host-supported runtime validation.
5. Continue the **original authorized task** after setup where the executor can do so. If setup is blocked, continue safe independent work; escalate only the blocked write/authority dependency. Do not close the original task with `SETUP_DONE`.
6. On subsequent sessions, use the existing project entrypoint/Bootstrap, not a repeated installation. Report actual skill discovery/load/use and task checks only when observed.

Read `references/PROJECT_SETUP_HANDOFF.md` when producing a Codex or other agent handoff that includes local inspection or setup.
