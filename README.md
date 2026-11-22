# loom-foo

**Language:** English · [Українська](README.uk.md)

**Focused Agent Skills for design, research, product development, writing, and agent workflows.**

Explore a product idea. Improve an interface. Investigate evidence. Plan a change. Brief a coding agent. Check what it actually delivered.

**loom-foo** brings together **41 portable Agent Skills**. Each skill defines when it is useful, how to approach its kind of problem, what to produce, and which boundaries to respect. Use one skill when one is enough, or combine complementary skills when a task requires it.

## Start with a real task

If loom-foo is installed in your AI client, simply describe what you need:

> Help me turn a rough product idea into a clear problem, a useful concept, and practical next steps.

Other starting points:

> Review this onboarding flow. Identify the most consequential usability problems and propose specific improvements.

> Investigate this product decision. Compare viable alternatives, separate evidence from assumptions, and explain what could change the conclusion.

> Turn these requirements into a bounded task for an AI coding agent, with scope, constraints, and acceptance checks.

> Review this implementation for defects, then verify it against the agreed criteria. Keep review findings and verification results separate.

You don't need to memorize skill names. A client with supported skill discovery **may** select the right skill from your request. Otherwise, choose one from the [skills directory](skills/) and ask your agent to read its `SKILL.md`.

## What can loom-foo help with?

| Area | Example skills | Typical results |
| --- | --- | --- |
| **Product & UX design** | [Design](skills/loom-foo-design/SKILL.md) · [Experience Design](skills/loom-foo-experience-design/SKILL.md) · [Design Review](skills/loom-foo-design-review/SKILL.md) | Concepts, interaction models, prioritized UX findings |
| **Research & evidence** | [Research Design](skills/loom-foo-research-design/SKILL.md) · [Evidence Acquisition](skills/loom-foo-evidence-acquisition/SKILL.md) · [Evidence Review](skills/loom-foo-evidence-review/SKILL.md) | Research plans, traceable evidence, qualified findings |
| **Decisions & planning** | [Problem Understanding](skills/loom-foo-problem-understanding/SKILL.md) · [Decision Reconciliation](skills/loom-foo-decision-reconciliation/SKILL.md) · [Project Planning](skills/loom-foo-project-planning/SKILL.md) | Clearer problems, reasoned decisions, actionable plans |
| **Engineering & agent work** | [Architecture Design](skills/loom-foo-architecture-design/SKILL.md) · [Agent Task Design](skills/loom-foo-agent-task-design/SKILL.md) · [Change Verification](skills/loom-foo-change-verification/SKILL.md) | Architecture options, agent task briefs, evidence-based verification |
| **Writing & communication** | [Drafting](skills/loom-foo-drafting/SKILL.md) · [Narrative Design](skills/loom-foo-narrative-design/SKILL.md) · [Editorial Review](skills/loom-foo-editorial-review/SKILL.md) | Useful drafts, stronger arguments, targeted revisions |
| **Knowledge & continuity** | [Knowledge Retrieval](skills/loom-foo-knowledge-retrieval/SKILL.md) · [Email Intake](skills/loom-foo-email-intake/SKILL.md) · [Handoff](skills/loom-foo-handoff/SKILL.md) · [Execution Inspector](skills/loom-foo-execution-inspector/SKILL.md) | Source-grounded context, durable handoffs, checks of claimed work |

Other skills cover creative reasoning, visual identity, icons, typography, design systems, cross-context transfer, failure learning, skill engineering, and more. Browse [all 41 skills](skills/) or their exact versions in [SKILL_INVENTORY.json](SKILL_INVENTORY.json).

## How the skills work

loom-foo follows the [Agent Skills format](https://agentskills.io/). Each skill has an entry point at `skills/<skill-id>/SKILL.md` and may include supporting references, examples, scripts, or assets.

The practical principles are:

- **Start with the task.** Choose the specialist for the outcome rather than force every problem through a universal workflow.
- **Load selectively.** Read deeper references when the task calls for them.
- **Ground claims.** Distinguish observations, assumptions, proposals, and verified results.
- **Respect authority.** Instructions do not grant access to private data or permission to publish, deploy, spend, or accept changes.
- **Keep process proportional.** Do enough to produce a useful, trustworthy outcome without unnecessary ceremony.

Skills can work together when their responsibilities complement each other. These links are optional methods, not a guarantee that your AI client will automatically invoke them.

## Getting started

You can explore the source here or clone the repository:

```sh
git clone https://github.com/ejct/loom-foo.git
```

Then use the approach supported by your client:

1. **Native skill/plugin installation:** follow your client's installation instructions and permissions. This repository contains manifests for OpenAI/ChatGPT and Codex, Claude, Google Antigravity, and Gemini; supported installation and discovery differ across hosts.
2. **Direct skill use:** give your agent access to a chosen `skills/<skill-id>/` directory and ask it to read `SKILL.md`.

For example:

> Read `skills/loom-foo-design-review/SKILL.md` and apply it to the interface I'm sharing. Load supporting references only when relevant. Separate observed problems from hypotheses.

A clone or plugin manifest alone does not prove automatic discovery, correct skill routing, or equivalent behavior across hosts.

### Requirements and cost

You need an AI client capable of reading and following the skills and any tools or source access required by your task. **The skills themselves do not require a publisher-operated backend, paid API, or centralized orchestrator.** Your AI client and connected tools may have separate fees, restrictions, and data policies.

## Repository guide

- [`skills/`](skills/) — skills and supporting materials
- [`SKILL_INVENTORY.json`](SKILL_INVENTORY.json) — exact skill IDs and versions
- [`plugin.json`](plugin.json) and platform manifests — distribution metadata
- [`CHANGELOG.md`](CHANGELOG.md) — source evolution
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — proposing and checking changes
- [`SUPPORT.md`](SUPPORT.md), [`SECURITY.md`](SECURITY.md), [`PRIVACY.md`](PRIVACY.md), [`TERMS.md`](TERMS.md) — support and project policies

Individual skills have their own versions, separate from the bundle version.

## Status and limitations

**Public source preview, bundle source candidate 0.46.0.** The repository is publicly readable, but no tagged public distribution or marketplace release has been published. Release preparation, Git-history confidentiality and host compatibility are documented in [Release Status](RELEASE_STATUS.md). The source checkout is not a validated plugin installation. The current candidate is **not cleared for publication** as a tagged or marketplace distribution; public source visibility does not constitute release approval.

Skills are methods for AI agents, not guarantees of correctness. Actual selection, tool use, and verification depend on your AI host and its permissions. A passing static test does not prove that a host selected or executed a skill.

For non-sensitive questions and bug reports, use [GitHub Issues](https://github.com/ejct/loom-foo/issues). Do not post secrets or private project material.

**License:** [MIT](LICENSE) · **Maintainer:** [ejct](https://github.com/ejct)
