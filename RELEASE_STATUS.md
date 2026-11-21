# Release status

**PRIVATE_CANDIDATE — NOT PUBLIC-APPROVED**

- **Repository:** `ejct/loom-foo` (PRIVATE).
- **Imported source:** private `ejct/LoomDev@f2e0fe4e02e848ea06ce3e72028a7c58c5959f5b`.
- **Baseline:** bundle version 0.40.0, 40 Skills; native manifests for OpenAI/Codex, Claude, Antigravity and Gemini.
- **Source projection:** 254 exact text files from LoomDev plus this repository's own README and governance/CI/release files. Source import checks verify exact Git blob identities, not semantic public suitability.
- **Missing original binary assets:** `assets/loom-foo-mark-v2.png`, `assets/loom-foo-mark-v3.png` — `UNVERIFIED_BINARY_PARITY`. Current manifests reference v3; do not assert host-native build readiness while unresolved.
- **Privacy:** owner-private overlays, reconciliation history and legacy source folders intentionally excluded. Semantic review, publisher contact, license/dependency audit and link validation are still required.
- **Public release gate:** `scripts/build_public_release.py` requires an external owner-approved SHA-256 file index. No index with `approved_by_owner: true` is generated automatically. Build passing would not grant publication authority.
- **GitHub Actions:** static verification only; no artifact upload (GitHub Actions storage quota was previously exhausted), deploy or release workflow.

Before publication, complete semantic privacy review of the exact commit, confirm the legal/support/public URL surface, recover or approve replacement brand assets, enforce the approved-hash builder in the actual release job, and obtain a separate explicit decision to make the repository public or publish a release.
