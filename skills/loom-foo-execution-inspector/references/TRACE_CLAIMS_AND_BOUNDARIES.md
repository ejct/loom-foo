# Trace claims and evidence boundaries — conditional method

Read only for disputed multi-agent execution, artifact ancestry, incomplete source-range delivery, or materially conflicting run traces. This reference adds detail to the root and does not replace its activation/authority conditions.

## Compact evidence ledger

For each material claim record:

| Field | Purpose |
| --- | --- |
| Claimed event | Exact bounded assertion, agent/context, time or stage if available |
| Subject identity | Skill version/blob, file/hash, test name/run, message or action target |
| Observed evidence | Tool/host event ID, file version, explicit output, or provided trace with origin label |
| Coverage | Complete/partial/unknown, gaps and access limitations |
| Disposition | PASS, FAIL, UNVERIFIED, NOT_RUN, NOT_COVERED, INCONCLUSIVE, NOT_CONFIRMED as applicable |
| Consequence | Material correction or minimum extra evidence that would settle it |

These are analytical fields, not a required rigid JSON contract or persistent registry. Keep the output short for simple inspections.

## Source delivery reconstruction

1. Establish exact root `SKILL.md` identity/version or mark it unknown.
2. Identify actual delivered source ranges and whether the forwarding channel was model-visible; metadata/catalog is not source body.
3. For FULL, ranges must cover every byte/span of that exact root through EOF with no gap. Do not assume overlapping or out-of-order chunks concatenate correctly without evidence; a tool fetching all bytes but forwarding a truncated summary supports at most PARTIAL when truncation is observed.
4. Evaluate each conditionally necessary L2 reference separately. A complete L1 does not automatically prove L2 read or use.
5. `FULL` means delivery only, not agent comprehension, selection, application or correctness.

## Trace/actor reconstruction

- A named sub-agent, persona or role does not prove a separate executor. Require actual spawn/session/context evidence and corresponding inputs/access for any claimed independent actor.
- Verify stage sequence from observed events, not a neatly formatted final Process Trail. For repeat reviews, distinguish REVIEW1 from REVIEW2 using artifact/check identities.
- Compare the inspected candidate to the exact version on which a test ran; a passing log from an older SHA is not a PASS for new bytes.
- An API returning a success flag for a draft or file write cannot be stretched into a sent message or installed runtime.
- User-provided logs may accurately describe a run, but without provenance authentication report them as provided evidence rather than host-observed facts.
- If only some stages are recorded, report which ones are supported, which are merely claimed, and which were outside the accessible horizon.

## Counterexample discipline

A report should distinguish: confirmed false assertion; plausible but unconfirmed claim; evidence gap; and a clean result (`NO_MATERIAL_MISMATCH_FOUND`). The absence of a tool call proves no action only under a sufficiently complete, reliable scope. Do not invent future audits/tests or use write tools in a read-only inspection.
