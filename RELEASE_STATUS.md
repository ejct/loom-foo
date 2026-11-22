# loom-foo — release status

**PUBLIC_SOURCE · PUBLICATION_BLOCKED · DISTRIBUTION_NOT_RELEASED**

As of 22 November 2026, `ejct/loom-foo` is publicly accessible. This is a **source preview**, not a vetted tagged distribution or a marketplace release.

## Current state

- `main`: source candidate **0.44.0**, 41 independently versioned Agent Skills and five native host manifests.
- Email Intake 0.8.0 adds read-only correspondence reconstruction, with Link Intake 0.8.0 native email-link handoff; only source, not an installed plugin.
- P1–P4 execution reliability source changes are integrated: routing-observation comparison, source-signed context slices, semantic delivery readback, and host-permission/oracle integrity guidance. Static and synthetic checks do not prove host routing or enforcement.
- Owner-private ChatGPT plugin releases are managed independently and can advance ahead of this generic source. Owner-specific profiles and assets are excluded from this repository; matching version labels do not establish byte parity. A private plugin installation is not a public distribution.
- GitHub Issues is available for non-sensitive support; no confidential reporting channel has been verified.
- There are **no published GitHub Releases** as of this status check.

## Outstanding gates

1. **Confidentiality and Git history — accepted known exposure.** A targeted review confirmed personal contact metadata and private development identifiers in historical commits. On 22 November 2026 the maintainer chose to retain the existing public history and accept those known disclosures without rewriting history. This is **not** an assertion of full history clearance or absence of credentials in every Git object. Reopen remediation if a real secret or materially different sensitive exposure is later found.
2. **Exact release source.** Confirm intended candidate bytes, version and file hashes; obtain an actual owner approval before generating or labeling a public distribution.
3. **Attribution and rights.** The maintainer confirmed that the prior product name refers to the same project, so the rename/notice wording alone is not a third-party rights blocker. Review any independently sourced code, assets or contributions before including them in a release.
4. **Support and privacy.** Verify a private vulnerability-reporting route and a confidential privacy-request channel. Public Issues are inappropriate for sensitive disclosures.
5. **Directory artwork.** Approved logo/composer assets are still deferred and may be required by native directory submissions.
6. **Host validation.** Test installation and routing in relevant runtimes before claiming automatic selection or cross-host parity. Passing static CI is not runtime evidence.

**Public repository visibility does not imply publication clearance, a tagged release, marketplace listing, updated plugin installation or changed consumer pins.**
