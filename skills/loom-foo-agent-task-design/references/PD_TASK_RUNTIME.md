# loom-foo-agent-task-design — detailed instructions (PD_TASK_RUNTIME)

> Conditional reference for `../SKILL.md` (progressive disclosure migration based on private loom-foo 0.27.0). The source sections below preserve their original normative content; Markdown `references/` links are rebased to sibling files. Read for the trigger named in the current root; do not silently treat all references as always loaded.

## 9. Context budget and provenance

Persistent project/repository knowledge belongs in durable project sources or runtime-native instruction files when available.

The task prompt should act as a map to those sources, not a stale copy of them.

Inline source content only when at least one is true:

- the runtime cannot reliably access the source;
- a small exact excerpt is required for correctness;
- the content is task-local and has no durable owner;
- freezing exact bytes/text is itself part of the task contract.

Do not claim full-source review from snippets, summaries, or partial retrieval.

### Source reachability

A stable pointer is useful only when the target execution runtime can actually resolve it.

During runtime projection classify controlling sources as:

- `SOURCE_RETRIEVABLE` — the runtime can read the controlling source reliably;
- `SOURCE_CRITICAL_SLICE_INLINE` — direct source access is unreliable, but a small exact decision-critical slice is sufficient and can be provided with provenance;
- `SOURCE_REQUIRED_UNAVAILABLE` — correctness depends on source content that cannot be reliably retrieved or safely reduced to a bounded exact slice.

For `SOURCE_REQUIRED_UNAVAILABLE`, return `NEED_CONTEXT` or `BLOCKED` rather than inviting semantic reconstruction.

Do not assume that because the task compiler can access Drive, Notion, a private repository, or another connector, the target runtime has equivalent access. Preserve source reachability as part of projection fidelity.

### Input delivery and output materialization

When a Task Brief relies on cross-runtime retrieval, staging or publication, read [input/output delivery](INPUT_AND_OUTPUT_DELIVERY.md). Do not assume the executor inherits coordinator access.

## 10. Verification proportionality

Every required verification step must answer a concrete property or risk question.

For ordinary bounded changes, task-specific tests plus relevant repository gates and scope/diff inspection may be enough.

For high-assurance, security-, schema-, evidence-, migration-, or release-critical work, add only the stronger checks that establish distinct properties: negative/adversarial cases, clean reproduction, mutation/property tests, independent review, exact-head verification, or artifact integrity as applicable.

For a scarce, single-use, or irreversible production operation, define the first meaningful attempt-consumption boundary and include one proportional non-production rehearsal of the *actual integration route* before crossing it, when feasible. Bind the rehearsal to the exact subject and controlling guard: entrypoint → branch selection → real host validator/method chain → simulated effect. Mock external OS/production effects as necessary, but not the dispatcher or validator whose correctness is at issue. If that route cannot be rehearsed at adequate fidelity, mark the coverage gap explicitly and defer to the existing authority/risk gate; do not claim source PASS proves activation safety, invent a new approval ritual, or spend a real attempt merely to discover routing mistakes.

Do not repeat identical checks unless code, bytes, environment, or the property under test changed, or determinism itself is the property.

A verification ritual is not evidence merely because it is long.

## 11. Reviewer / audit profile

For review assignments, read [review/audit guidance](TASK_PROFILES_AND_ASSURANCE.md#11-reviewer--audit-profile).

## 12. Repair / remediation profile

For repair assignments, read [remediation guidance](TASK_PROFILES_AND_ASSURANCE.md#12-repair--remediation-profile).

## 13. Runtime projection

### Skill entry and completion envelope (runtime-specific)

When the executor has access to Agent Skills, compile the following proportional requirements:

1. Before substantive task actions, identify task-relevant installed skills by their activation descriptions and owner boundaries. Load exact current SKILL.md sources and any conditionally required references; do not invoke every available skill or create a new planning gate for ordinary authorized execution.
2. Verify that the whole source reached the active executor before saying a skill was fully read. A source reader returning the complete string is insufficient if the outer orchestration channel emits only an excerpt. If output is clipped or a range is missing, emit/re-read missing ranges within the actual output budget. Never silently truncate via slice(0,N), summarize an unread tail, or claim FULL from length metadata alone. Preserve exact source/version identity across ranges where possible.
3. Before claiming completion, bind material verification output to the exact candidate or runtime state. Distinguish performed, verified, partial, unverified and blocked. Earlier logs and worker self-reports do not establish fresh success.
4. When a runtime lacks a guaranteed startup hook, state the scope as a task-local executor instruction, not that every ChatGPT session automatically activated loom-foo.

Keep this envelope compact in actual Task Briefs; it grants no new authority or extra user-approval gate.


Render the same Task Brief through the runtime's native context model without weakening semantics.

Examples:

- Codex: immediate task + repository/project `AGENTS.md` or equivalent persistent instructions;
- Claude Code: immediate task + `CLAUDE.md`;
- GitHub Copilot coding agent: issue/task + repository instructions;
- Gemini CLI: immediate task + `GEMINI.md` / relevant skills;
- other agents: equivalent persistent context + task-local instruction.

### Projection invariant

A runtime rendering may change syntax, placement, and references. It must not silently change:

- outcome;
- subject identity;
- authority;
- protected boundaries;
- acceptance criteria;
- verification claims;
- stop boundary.

If a runtime cannot represent a material boundary faithfully, report the limitation rather than silently weakening it.

Input delivery is part of projection fidelity when external material is required. The rendering should make the chosen retrieval/staging path executable without silently shifting transport work to the user. Do not assume that child workers inherit the coordinator's connectors, permissions, or source visibility.

Next-step readiness is part of projection fidelity: preserve the consumer's legitimate next action, material return payload, evidence/limitations and retrievable identity in the runtime-rendered brief. A natural-language promise to report success is not an executable return contract when another actor needs an artifact, data or decision input.

Output materialization is also part of projection fidelity when the result has a downstream consumer outside the producing runtime. The rendering must not claim a continuation-bearing artifact is fully deliverable when it is represented only by an inaccessible local path. Preserve publication authority and choose the project-native durable owner rather than forcing one provider-specific surface.
