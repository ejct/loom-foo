# loom-foo-skill-engineering — detailed instructions (PD_SKILL_VERIFY_AND_RELEASE)

> Conditional reference for `../SKILL.md` (progressive disclosure migration based on private loom-foo 0.27.0). The source sections below preserve their original normative content; Markdown `references/` links are rebased to sibling files. Read for the trigger named in the current root; do not silently treat all references as always loaded.

## 6. Review and verify proportionately

**Claim Challenge (owner-local, conditional).** When a skill contract, routing decision, source interpretation, packaging claim or release assertion depends on a consequential checkable premise, ask what observable counterexample would materially weaken it. Prefer a direct source read, negative fixture, known failure case, or independent tool check that is cheap and permitted. Check that an apparent counterexample matches the exact subject/scope and that the verifier is trustworthy; reject speculative defect accusations. Report the narrowest support, contradiction or uncertainty and repair only the affected contract. Do not create a universal Challenge Record, falsification skill, extra review agent, or required evidence plan. A useful bounded challenge can end with no defect found.

**Use-first default.** For an authorized ordinary skill update, build the smallest workable version; perform package/syntax, reference, preservation and risk-specific checks as part of the same work episode; then install/update in the requested runtime and read back the saved source. Learn from real task use and fix specific observed failures. Do not postpone use for a separate benchmark, blind holdout, independent panel, comparative lift experiment, promotion ceremony, or invented approval step. Explicit performance claims, destructive migrations, safety-critical behavior and genuinely required gates may justify stronger tests. Frozen evaluation is opt-in; its separate owner must be installed and available before execution.


Inspect the actual delta from the exact base; verify the intended contract and absence of nearby routing/authority regressions. A material change can use the installed `loom-foo-change-review`, `loom-foo-architecture-review` or `loom-foo-change-verification` when those own the check. Choose based on the artifact and risk, never to populate a checklist. Read `references/VERIFICATION_AND_CASES.md` for tests and validity limits.

Base evaluative examples on actual user work and failure modes whenever available; a small, concrete set of positive, negative and sibling-owner prompts is usually more useful than an enormous synthetic fixture bank. **Use an agent/runtime execution** to observe invocation and results; static fixture integrity alone cannot measure it. For an explicit lift claim, freeze a comparable baseline and relevant acceptance tests before viewing outcomes; otherwise use bounded task dogfood without imposing a costly research campaign. Check for harm from stale instructions, extra context, excessive constraints and overwritten task intent.

Separate the following evidence layers:

1. **STATIC** — parsed metadata and source/package/reference correctness.
2. **DISCOVERY** — this exact version is listed/available in one runtime.
3. **ROUTING** — positive and negative automatic selection on real prompts.
4. **EXECUTION** — task output conforms to the skill contract.
5. **FIELD** — the user gets the intended result with acceptable overhead.
6. **COMPARATIVE** — matched controlled conditions support an actual lift/harm claim.

Never promote a lower-layer PASS to a higher-layer claim. Fixture authorship and same-context scenario rehearsal do not count as host routing execution. A self-review is not an independent audit. For frozen C0/C1 evaluations, use `loom-foo-skill-validation` only when it is available in the exact runtime; otherwise mark the owner **UNAVAILABLE**. Never change a frozen plan in response to results.

## 7. Deliver without inventing runtime state

**Behavioral Semantic Versioning.** Classify each changed skill and the containing plugin independently by *contract impact*, not file count or release frequency: `PATCH` for non-contract fixes/clarifications; `MINOR` for compatible added capabilities, changed normal behavior or new skills; `MAJOR` for breaking established activation, ownership, output or authority contracts after 1.0.0. During `0.x`, put materially breaking changes in the next `MINOR` with explicit `BREAKING` note; do not silently call them patches. The bundle gets **one bump at the highest impact of all its contained changes**, and unchanged skills keep their own versions even if new routing competition affects the bundle. Preserve past releases/pins; do not rewrite history. Read `references/PACKAGE_AND_DELIVERY.md` for classification examples and the lightweight release note.


Bind source version/hash, packaged bytes, target runtime and destination separately. A Google Drive Markdown file, Git tree, copied `.agents/skills` folder and ChatGPT plugin release are different states. Honor existing pins; never silently overwrite or upgrade consumers. Verify installation, runtime discovery and automatic routing individually if the necessary environment is accessible.

Creating a local package is not authorization to publish it, move private sources to a repository, install a ChatGPT plugin or change sharing. When an external change is authorized, apply it and read it back before claiming success. If access is missing, deliver the local artifact and a precise installation gap—not a fictional activation success.
