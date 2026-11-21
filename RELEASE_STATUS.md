# loom-foo — release status

**PUBLIC_SOURCE · DISTRIBUTION_NOT_RELEASED**

As of 21 November 2026, `ejct/loom-foo` is publicly accessible. This is a **source preview**, not a vetted tagged distribution or a marketplace release.

## Current state

- `main`: candidate **0.42.0**, 40 independently versioned Agent Skills and five native host manifests.
- An independent **0.43.0 draft PR** exists. It has not been merged into `main` or distributed through this repository.
- An installed private plugin can report the same numeric version as the generic candidate while containing **different bytes**. Source and installed runtime must be reconciled before claiming parity.
- GitHub Issues is available for non-sensitive support; no confidential reporting channel has been verified.
- There are **no published GitHub Releases** as of this status check.

## Outstanding gates

1. **Confidentiality and Git history.** Earlier commits, branches and other refs may contain private development provenance. The repository is already public. Editing today's files does not erase history, forks or cached copies. Inspect exposure and prepare a separately approved clean-source release; respond to any actual credential exposure.
2. **Exact release source.** Confirm intended candidate bytes, version and file hashes; obtain an actual owner approval before generating or labeling a public distribution.
3. **Attribution and rights.** Resolve inherited copyright-notice questions and check any third-party material.
4. **Support and privacy.** Verify a private vulnerability-reporting route and a confidential privacy-request channel. Public Issues are inappropriate for sensitive disclosures.
5. **Directory artwork.** Approved logo/composer assets are still deferred and may be required by native directory submissions.
6. **Host validation.** Test installation and routing in relevant runtimes before claiming automatic selection or cross-host parity. Passing static CI is not runtime evidence.

**Public repository visibility does not imply publication clearance, a tagged release, marketplace listing, updated plugin installation or changed consumer pins.**
