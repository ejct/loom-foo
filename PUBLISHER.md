# Publisher identity and contact — private release candidate

**Status:** proposed generic publisher metadata, not final authorization to publish.

## Source-facing identity

- **Publisher / maintainer handle:** [`ejct`](https://github.com/ejct) (the GitHub account that owns this repository).
- **Agent Plugins `author`:** `{"name":"ejct","url":"https://github.com/ejct"}`; email deliberately omitted.
- **OpenAI/Codex `developerName`:** `ejct`. The public directory may use the platform's separately verified developer identity instead of the manifest value.
- **Claude / Antigravity `author.name`:** `ejct` with the same GitHub URL.
- **Gemini manifest:** no author field is invented merely for cross-platform symmetry.

Using an account handle for attribution does **not** establish copyright ownership of every file or asset. The inherited MIT copyright line remains in `LICENSE`.

## Contacts and publication limits

- **Non-sensitive support:** [GitHub Issues](https://github.com/ejct/loom-foo/issues) *after* a public repository and issue access actually exist.
- **Security reports:** GitHub's private vulnerability reporting **only if enabled**. Enable and test that feature before stating that the channel is operational. If disabled, a minimal non-sensitive issue may request a private reporting route; never submit vulnerability details publicly.
- **Privacy requests:** the repository currently has **no verified dedicated private privacy-contact channel**. A user may request one through a minimal non-sensitive issue; a practical private channel must be confirmed before claiming that confidential requests can be received.
- **Public email:** **none committed to the generic candidate**. No personal mailbox should be copied from an installed private plugin without the owner's explicit choice.

**Public contact options:** GitHub Issues for support and bug reports; optional GitHub Discussions for questions and ideas if enabled; links from [the maintainer's GitHub profile](https://github.com/ejct) to outside social/professional networks for private outreach. Neither Issues nor Discussions is a private messaging channel. Private vulnerability reporting applies only to security flaws, after it has been activated. No general-purpose private messaging channel is currently verified.

**Release gate:** before publication, the owner confirms whether `ejct` is the desired public credit or whether a legal/brand name should replace it; confirms which private contact channels actually operate; and approves the exact future public source and audience. Do not make the existing private Git history public as-is.

References: [Agent Plugins spec](https://agent-plugins.org/specification), [OpenAI submission rules](https://developers.openai.com/plugins/deploy/submission-errors), [GitHub vulnerability reporting](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository).
