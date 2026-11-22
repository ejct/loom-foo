# Project Integration — Changelog

## 0.5.0 — 2026-11-22

- ADDED: `PARTIAL_SETUP` diagnostic outcome for interrupted or inconsistent foo-loom managed-file state.
- ADDED: `PROJECT_STATE_RECOVERY.md` with exact pin/lock/Bootstrap/AGENTS block preflight, safe repair and conflict handling.
- CHANGED: local agent handoff and authorized setup now inspect independently observed installed pieces and avoid an unconditional reinstall.
- PRESERVED: immutable source pins, opt-in Core, owner authority, original task priority, no persistent switches, no automatic policy adoption or runtime-activation claims.
- Version is a compatible MINOR change; host routing/use not implied by this candidate package.
