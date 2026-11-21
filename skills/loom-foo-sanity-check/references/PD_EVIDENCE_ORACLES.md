# sanity-check — conditional method

> Preserved sections from private Loom-foo 0.35.1 SKILL.md. Referenced `references/...` paths are relative to the owning skill root. L1 activation and authority remain controlling.

## Checks by evidence type

### Source delivery and ownership boundary

For `SOURCE_COVERAGE` or `COMPLETION_CLAIM`, distinguish: (1) bytes the underlying tool retrieved, (2) contiguous text actually forwarded into the active agent's context by an outer tool/orchestrator, (3) behavior demonstrably applied. An inner reader's character count or successful call proves neither model-visible delivery nor compliance. Recover missing ranges by native paging/bounded output if material and accessible; otherwise label PARTIAL. Refer to `loom-foo-skill-engineering` for source delivery and to `loom-foo-change-verification` for exact PASS judgments. Sanity Check performs only the smallest triage and never duplicates the full specialist review. Never claim an always-on hook from this instruction alone.

- **Files/read coverage:** distinguish metadata, excerpt, retrieved pages, full bytes and rendered visual verification. Inspect remaining sections only if material and accessible. Do not claim the assistant read unreturned bytes.
- **Completion and external actions:** inspect actual tool return, stable record or readback. `DRAFT != SENT`, `LOCAL != REMOTE`, `PACKAGED != INSTALLED`, `INSTALLED != ROUTED`, `TEST PASS != ACCEPTED`.
- **Delegated authority:** `PREPARE != CODEX_TASK_LAUNCH`, but *preparing* an artifact does **not** prohibit its ordinary private Drive save; `IN_SCOPE_DELIVERY != PUBLIC_RELEASE`; `BOUNDED_OUTPUT_VARIATION != NEW_APPROVAL`. Standing owner-private Drive consent is known for this personal environment; verify the actual destination, effective audience, task, disclosure class and material effect, not a fabricated per-file permission dependency. Host reviewer decision and user authorization are different layers.
- **Technical correctness:** rely on exact test environment, return code, diff, target criteria and verifier integrity; route broad conformance to verification owner.
- **Current facts:** cite and inspect relevant primary/authoritative source with date and identity; preserve disputes or gaps.
- **Proportionate plans:** compare with a concrete simpler path, considering cost, reversibility, required authority and original goal. Prefer direct execution unless a real blocking risk exists.

For optional deterministic verification of local file existence/hash, use `scripts/check_local_artifact.py`; see `references/TRIGGERS_AND_ORACLES.md` for its narrow claims. It is never a remote-write/reading-completeness oracle.
