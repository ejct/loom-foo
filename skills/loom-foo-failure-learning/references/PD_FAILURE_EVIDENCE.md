# loom-foo-failure-learning — detailed instructions (PD_FAILURE_EVIDENCE)

> Conditional reference for `../SKILL.md` (progressive disclosure migration based on private loom-foo 0.27.0). The source sections below preserve their original normative content; Markdown `references/` links are rebased to sibling files. Read for the trigger named in the current root; do not silently treat all references as always loaded.

## 6. Recurrence and portfolio mode

`EPISODE` is the default. Use `PORTFOLIO` when the user asks to analyze multiple incidents, or when sufficient accessible, authorized incident records show possible recurrence.

In portfolio mode, group by a source-grounded shared mechanism or testable failure condition; record individual episodes, counterexamples, source coverage, version/context differences and alternative explanations. Similar wording is not recurrence proof. Never imply complete incidence rates from an opportunistic sample of user-reported failures. Where possible include comparable successful episodes and explicit retrieval/selection limitations.

Keep a stable link to the project-local primary owner and references to affected projects. Do not create a global registry, universal taxonomy or cross-project data export unless independently justified and authorized.

## 7. Persistence, privacy and authority

**Routine project-native persistence.** When a user task and established project conventions include ordinary private read/create/edit/organize/save of resulting project files, proceed without repeated per-file or *prepare*-versus-*save* approval across supported Google Drive, Dropbox, OneDrive, Notion, local or other storage. Do not invent a universal standing owner grant: a user-specific permission may apply when actually available, but no profile is required for task-based authorization. Check actual project destination, effective inherited audience, payload sensitivity, current task scope, real connector write ability and host confirmation/denial. Names, counts and hashes do not independently change an otherwise approved effect. Separate authorization is needed for new audience/sensitive disclosure, bulk irreversible destruction, spending, third-party contact, public sharing, merge/release, sibling launch or other material external transitions. A proposal draft/save does not imply its adoption or canonicalization. If a connector is read-only or a host denies access, offer a truthful accessible result; do not route around the denial. For failed approvals distinguish `MODEL_INVENTED_GATE`, `HOST_REVIEW_REQUEST`, `HOST_DENIED`, `PROVIDER_AUTH_OR_ACL_ERROR`, `CONNECTOR_CAPABILITY_MISSING` and `NOT_OBSERVABLE`, without inventing native enforcement evidence.

Project-local/private by default. Redact sensitive extracts in portable skill packages; store evidence locators where possible. Do not share private chat, memory, file or project content across project boundaries without explicit permission. If the storage surface is inaccessible or unauthorized, return a ready-to-save artifact and mark persistence pending; never claim it was saved.

Candidate improvement is `PROPOSED` until the owner explicitly accepts it. A successful local recovery, a passed regression case, a converged proposal and owner acceptance are different claims. Respect existing frozen subjects, development sets and reserved holdouts; do not contaminate evaluation by retroactively converting the incident used for candidate development into an independent holdout.

## 8. UX and truthful reporting

Normal incident answer should prioritize a useful restored task result. Add a short learning note stating: **what failed**, **what was fixed**, **what remains uncertain**, **what changes are proposed**, **whether anything was actually persisted**. Do not attach full procedural reports to routine conversation unless material or requested.

For substantive multi-stage work, follow any explicitly supplied project-specific receipt convention when accessible; it is not trace telemetry. Distinguish a user-reported symptom from an independently verified mechanism. Do not claim a skill loaded, a tool ran, a document changed, or a recurring pattern exists unless observed. If an exact skill version cannot be verified, write `version: unknown`.

If contextual friction led to a real failure finding, evaluate the repair against the original goal rather than merely appeasing the latest message. If the user says this skill should have activated but did not, log a **missed-activation** candidate with the actual trigger, accessible routing context and outcome. If this skill itself produced the wrong diagnosis, duplicate ceremony or unauthorized action, create a separate **self-failure** case. Avoid recursive self-invocation; an independent/fresh evaluator is required before authoritative claims about this skill's own lift, defects or promotion readiness.

### Goal-substitution regression fixture (synthetic case)

A synthetic regression case describes a plan that wrongly prioritized proving a tool's effectiveness over the requested functional development. Observable failure: mandatory comparative experiments and evidence gates displaced concrete functional improvement despite the hypothetical project contract prioritizing real-work use. Record the observed mismatch as `GOAL_SUBSTITUTION / EVIDENCE_GATE_PROLIFERATION`, with candidate locus `COMPOSITION/ROUTING`; direct causality from any individual skill remains unverified. Keep this operational incident separate from psychological analysis. Use the synthetic, non-authoritative regression fixture `references/GOAL_FIDELITY_REGRESSION.md` for the minimum positive and negative routing checks; do not expand this into a broad evaluation campaign or conflate engineering integrity verification with proof-of-value studies. The fixture does not establish any real-world acceptance, installation or behavioral lift.

### Integration-path regression (general rule)

A component-level `PASS` or synthetic regression suite does not establish that the real host dispatcher, validator and irreversible-action route use the verified component. For a high-impact activation, review the actual host dispatch → validation → promotion path; distinguish production routes from mocks and unit-test substitutes. When attempt consumption or irreversible effects matter, require a proportionate isolated end-to-end route rehearsal. Keep rollback/fail-closed protections; do not equate a safe rollback with completion or success. Ordinary reversible changes do not need this added gate.

Preserve exact source, reviewer, run, attempt and receipt identities in project-local evidence, not in this reusable skill. The synthetic case illustrates this boundary; it is not user-specific evidence or a mandate for portfolio-wide testing. Never claim skill-level causality from an unverified activation.

## 9. First-use dogfood and validation

This is an experimental candidate. First real user-reported incident is a development/dogfood case. Preserve exact skill/routing subject identity for each observed run; record actual activation, recovery, evidence fidelity, causal restraint, ceremony, persistence boundary and proposed delta utility. Include negative routing examples and failures of this skill itself. Compare with no-skill C0 only in properly isolated contexts under an external frozen evaluation contract; never simulate a clean C0 from a chat that already loaded this skill. Reserve genuinely fresh cases for post-freeze holdouts. Never mutate another campaign's frozen subjects or oracle.

Read `tests/DOGFOOD_PROTOCOL.md` when conducting the pilot or curating test cases. Use the new friction-negative fixtures to detect both missed activation and false psychological routing.

## Final check

Before closing, answer: Did we recover the task? Did we preserve the user's actual report? What is established versus conjectural? What is the minimum justified owner/delta? Is the output small enough for the situation? What was actually written or applied? What evidence would prove the fix? If there is no justified change, say so plainly.
