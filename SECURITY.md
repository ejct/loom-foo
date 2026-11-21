# Security Policy — loom-foo

## Scope

Security reports concerning the generic `loom-foo` package, its Agent Skills, optional scripts, release artifacts, or associated `foo-loom` project-installation tooling are in scope.

The current development baseline is `loom-foo v0.40.1`. Older versions and independent third-party AI runtimes may have different security properties; disclose the exact affected package and host when reporting.

## Reporting vulnerabilities

Use the repository's **Security → Report a vulnerability** feature if private vulnerability reporting is enabled. Its availability has not been independently confirmed.

If private reporting is unavailable, open a **minimal, non-sensitive** [GitHub issue](https://github.com/ejct/loom-foo/issues) requesting a private reporting channel. **Do not publish proofs of concept, credentials, exploitation steps, private data, or unpublished project material in the issue.**

No response timeframe, bounty or coordinated disclosure deadline is promised. Public disclosure should be coordinated after an appropriate private contact channel exists.

## Security model

loom-foo is a collection of procedural agent instructions, not a sandbox or independent security boundary. AI hosts, models and external tools may fail to follow instructions. Users must enforce access permissions, manage secrets and approve consequential external actions in their own environment.

Relevant failure classes include prompt-injection or malicious retrieved content, unauthorized disclosure of private project sources, unintended external side effects, insecure tool execution, unsafe installer changes and misleading verification claims.

Please report issues with exact versions, reproduction conditions and the smallest non-sensitive evidence necessary for investigation.

See [Privacy Policy](PRIVACY.md) and [Support](SUPPORT.md).
