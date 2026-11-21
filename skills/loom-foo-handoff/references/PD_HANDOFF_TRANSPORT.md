# handoff — detailed conditional method (PD_HANDOFF_TRANSPORT.md)

> Source: exact private Loom-foo 0.35.1 `SKILL.md`. L1 retains activation, goal and authority precedence. Below sections are preserved in full, in source order; `references/...` paths refer to the owning skill root. Read this file only when its explicit L1 trigger applies.

## 13. Transport-specific emission

### CHAT_TEXT
Use the collision-safe framing, fail-closed parsing, nested-handoff behavior, and activation boundary in `references/CHAT_TEXT_TRANSPORT.md`.

### STRUCTURED
Use the destination's typed framing. Do not add text-envelope ceremony merely to imitate Chat/Text.

The handoff itself creates no execution authority in either mode. Runtime continuation policy is resolved by the destination/runtime and existing authority; only Chat/Text uses the explicit external-activation rule defined by its profile.
