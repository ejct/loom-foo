# Email Intake v0.8.0 — Method lineage

This is the **first independently packaged** `loom-foo-email-intake` skill. Version 0.8.0 recognizes substantial predecessor engineering and the owner's explicit versioning decision. It does not imply earlier standalone v0.1.0–v0.7.0 releases.

## Adapted predecessor mechanisms

| Development phase | Reusable mechanism | Transfer boundary |
| --- | --- | --- |
| Semantic email triage research | Separate requests, commitments, decisions, outcomes and time-of-knowledge | Scenario coverage is not proven deployment quality |
| Multiple email-monitor iterations | Reconstruct real-world episodes across threads; identify meaningful deltas | Notification thresholds are not intake filters |
| Retrieval hardening | Enumerate provider pages, inspect source coverage, distinguish folder and thread gaps | No automatic hourly windows or account-wide crawls |
| State recovery | Keep optional persistence distinct from source truth and completion claims | Email Intake does not maintain monitor state |
| Trust inspection | Treat messages and quoted content as untrusted; distinguish attempted injection from observed effects | No LLM-only security guarantee |
| Skill handoff | Return a compact evidence packet with provenance and uncertainties | No implicit mail sending or knowledge-canon write |

## Version and release boundary

- `0.8.0` is the first standalone **source candidate** dated 2026-11-22, reflecting the maturity of predecessor methods, not a fabricated sequence of standalone releases.
- A predecessor email-monitor workflow was developed through multiple versions. That workflow and its private source history are separate from this skill's releases.
- Behavioral SemVer for subsequent changes is based on Email Intake's own activation, outputs and permissions; the containing loom-foo bundle has an independent version.
- Static fixtures and source checks do not establish host routing, live Gmail execution, human usefulness or cross-provider equivalence.

## Public-source privacy

No actual correspondence, private incident records, mailbox IDs, owner-specific exclusions, persistent state locators, private release IDs or credentials are included. Detailed source evidence remains private.
