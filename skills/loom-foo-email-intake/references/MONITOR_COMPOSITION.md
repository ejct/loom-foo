# Email Intake as evidence stage of a recurring monitor (v0.9.0)

## Trigger and ownership

Only use when a caller such as an existing scheduled email monitor explicitly requests the email evidence phase within its authorized scope. Load the root SKILL.md on each supported run; read this reference for the parent contract. This skill is **not** the scheduler, policy engine, alert generator or canonical state writer. Parent workflow owns its source windows, authorization, previous fingerprints, checkpoint validation, notification rules, output and write approvals. Skill instructions never override a direct user's current monitor restrictions.

A parent may request **always-load, selective deep work**: the root governs ordinary scoped metadata/ID evidence, while `EPISODE`, `DELTA`, `SECURITY_INSPECTION` and deeper references are selected only when material. Keep lightweight repetitive messages cheap. Prevent redundant provider calls: if a parent already enumerated verified message IDs, reconcile and reuse, but do not incorrectly claim the parent checked all IDs when it did not.

## Minimum handoff: Email Evidence Packet v1

Provide conceptually structured fields (not necessarily a JSON code block):

- `contract`: `email-evidence-packet/v1`; `intake_skill_version`; `as_of` and authorized account/scope (avoid unnecessary identifiers).
- `coverage`: for each surface (normal, spam, sent or scoped query), exact time bounds and expression, `pages_complete`, authoritative ID membership count, material body-read status, thread/attachment gaps, `READ_COMPLETE_WITHIN_SCOPE | PARTIAL | METADATA_ONLY | SOURCE_UNAVAILABLE`.
- `candidates`: provider-native message IDs, received/sent timestamps, relevant episode keys, source locators, source labels, reason for reading; *no raw bodies*.
- `episodes`: supported chronology, actors as needed, event types, state/delta assertions, provenance and `SOURCE_ASSERTED | CORROBORATED | OBSERVED | UNKNOWN`; contradictory statuses are kept distinct.
- `security`: when warranted, mechanism, provenance, `ATTEMPT | NO_OBSERVED_EFFECT | OBSERVED_EFFECT | EXTERNAL_STATE_UNKNOWN`, external-content coverage and observed real harm if any.
- `gaps`: exact failed pages/reads/access and whether a checkpoint is unsafe to advance.
- `result`: `EVIDENCE_READY | PARTIAL_INTAKE | SOURCE_UNAVAILABLE | NEED_AUTHORITY`.

The packet contains evidence, **not** `SILENT/DAILY/INTERRUPT` or a directive to alert. Results of authoritative ID enumeration cannot be inferred from metadata summaries. Significant outcomes without action are retained for the parent's materiality gate.

## Failure and fallback

- If skill loading is unavailable in the scheduled host, parent must record `SKILL_NOT_LOADED` internally, follow its minimal safe Gmail-ID enumeration/reading contract and preserve alert state. It must not claim activation or erase known episodes, or notify merely because the skill is unavailable.
- If source enumeration or required material reads are incomplete, report surface `PARTIAL`, preserve existing source findings, do **not** certify the checkpoint. Parent may independently notify only on truly evidenced new material consequences.
- If the monitor's persistent state is stale, malformed, inaccessible or the guarded write fails, do not reconstruct state by guessing. Email Intake can provide source facts; parent owns state repair, replay/dedup and writes.
- User-visible strict silence suppresses any intake footer or diagnostics in the scheduled output; it does not suppress an independently warranted alert.

## Linked-consumer update contract

When changing this skill's `Email Evidence Packet` schema, acquisition semantics or critical composition behavior, identify any *authorized, explicitly linked* recurring consumer before release. Check its interface/prompt compatibility, update that consumer in the same approved release sequence when necessary, and verify saved instructions and real host loading independently. A new plugin release is **not** proof that an already-running scheduled task loads it; a static routing fixture is not actual host telemetry. Do not automatically alter unknown users' scheduled tasks or embed private user IDs or mail in this portable package.

Compatibility: additive fields in v1 are allowed; removing/renaming required fields requires explicit consumer migration. Always preserve the caller's rule that scheduling, persistent state, cross-run dedup and attention policy are external to Email Intake.
