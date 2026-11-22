# Loom-foo Onboarding — skill changelog

## 0.3.0 — candidate (2026-11-22)

- **ADDED** `ALREADY_INSTALLED_TRYOUT`: first-use testing for users with an installed plugin, without a reinstall or settings mutations.
- **ADDED** explicit `RESUME_TASK`, `FIRST_USE`, and `SETUP_CHECK` paths, with existing concrete task precedence.
- **ADDED** clear behavior for a live demo versus offering starter choices; one self-contained illustrative exercise is allowed only when a demo was explicitly requested.
- **IMPROVED** concrete, outcome-specific starter prompts and strict handoff to the actual skill owner.
- **CLARIFIED** observed catalog, explicit specialist loading, resulting artifact, and automatic host routing are distinct evidence layers.
- **PRESERVED** no global router, no mandatory Core dependency, no setup side effects, no assumption of automatic invocation, and no interception of routine tasks.
- **UNCHANGED** `agents/openai.yaml` interface metadata from GitHub base 0.2.0.

**Source base:** `ejct/loom-foo`, `main`, `skills/loom-foo-onboarding/SKILL.md`, Git blob SHA `7e74544957936ad8bb6ffe1d32c0d971e8a25458`, version `0.2.0`; installed skill also reports `0.2.0`.

**Status:** Local candidate. No repository mutation, host installation, fresh-context routing observation, marketplace release, or user-field benefit verified.
