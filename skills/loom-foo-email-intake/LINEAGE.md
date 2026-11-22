# Email Intake v0.8.0 — method lineage

This is the **first independently packaged** `loom-foo-email-intake` skill. Version 0.8.0 recognizes substantial antecedent engineering and the owner's explicit versioning decision. It is **not** a claim that Email Intake v0.1.0–v0.7.0 shipped or that a separate monitor's SemVer sequence transfers automatically.

## Predecessor capabilities adapted to the new owner

| Development phase | Reusable mechanism | Transfer limit |
| --- | --- | --- |
| Semantic triage research | Distinguish user requests, stated obligations, commitments, outcomes and information; preserve as-of-time evidence | Evaluation scenarios are not proof of deployment quality |
| Repeated email-monitor iterations | Treat a real-world case as an episode across multiple threads; use semantic deltas rather than email counts | Monitoring alert thresholds do not filter historical intake |
| Mailbox retrieval hardening | Enumerate source ID pages, handle missing messages, separate mail folders, make scoped completeness claims | No fixed hourly windows or account-wide crawl |
| Source-state recovery | Keep optional persistent state separate from source facts; avoid silent corruption or false dedup checkpoints | Email Intake does not create or update monitor state |
| Injection and manipulation inspection | Treat all mail, quoted text and remote content as untrusted; distinguish attempts from independently observed effects | A model inspecting hostile content is not a sandbox |
| Cross-skill evidence handoff | Return compact source-grounded evidence with provenance, confidence and gaps | Knowledge admission and outgoing email are owned elsewhere |

## Version and validation boundary

- Skill ID: `loom-foo-email-intake`.
- First standalone **source candidate**: `0.8.0` (2026-11-22).
- Chosen development-series version reflects breadth of predecessor work; it is not an eighth published standalone release.
- Candidate tests check only source integrity and expected contracts, not actual automatic activation, live Gmail execution, delivered notifications or measured improvement.
- Future changes use Behavioral SemVer for **this skill's** contracts; the Loom-foo bundle version is independent.

## Confidentiality

The portable package contains no actual emails, user-specific episode identifiers, personal alert exclusions, monitor run logs, private storage IDs, private release IDs or authentication tokens. Detailed predecessor evidence belongs in authorized private project sources, not the public skill source.
