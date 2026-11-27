# loom-foo · v0.57.0

**A little more know-how for your AI agents.**

**Language:** English · [Українська](README.uk.md)

45 specialized Agent Skills in one bundle, for design, research, writing, translation, planning, engineering and knowledge work.

Give your assistant a task as you normally would. Loom-foo gives it methods to choose from, combine when useful, and apply to the work at hand.

> **Source preview.** The source is available here; a tagged distribution or marketplace release is not available yet. See [release status](RELEASE_STATUS.md).

## How to use

Once Loom-foo is installed in a compatible AI client, work as usual. Your assistant can select the relevant skills for your request, depending on the client's discovery and routing support.

In ChatGPT, if Loom-foo is installed and selectable, you can explicitly invoke it with `@loom-foo` alongside your task. You do not need to learn skill names or assemble a workflow yourself.

## What it helps with

| Area | Typical work |
| --- | --- |
| Design | Product and UX concepts, interaction, visual identity, design systems, production handoff |
| Research | Research plans, evidence gathering, assessment and grounded conclusions |
| Writing and language | Drafting, editing, translation, translation analysis, terminology and UX writing |
| Planning | Problem framing, decisions, project planning and continuity |
| Engineering | Architecture, specifications, agent tasks, review and verification |
| Knowledge | Context retrieval, knowledge intake, evidence-linked project stewardship |

## How it works

Loom-foo follows the [Agent Skills format](https://agentskills.io/). Each skill provides instructions and, where useful, references or scripts. An assistant can select the relevant methods, load supporting material when needed and combine complementary skills.

The emphasis is on concrete outcomes, evidence, proportional effort, explicit uncertainty and verification. Instructions do not grant permissions. Actual discovery, routing and execution depend on the host.

There is no required paid API, publisher-operated backend or central orchestrator.

## Availability and setup

This repository contains the [portable skills](skills/) and manifests for ChatGPT, Claude, Codex, Antigravity and Gemini. For source inspection or development:

```sh
git clone https://github.com/ejct/loom-foo.git
```

A source checkout is not an installation. Native setup and automatic selection depend on the client. This candidate is **not cleared for publication** as an installable public distribution.

For advanced source-based use, give a compatible agent access to the skill collection. See the [Agent Skills format](https://agentskills.io/) and your client's documentation.

## Explore and contribute

[All skills and versions](SKILL_INVENTORY.json) · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md) · [Support](SUPPORT.md) · [Release status](RELEASE_STATUS.md)

Use [GitHub Issues](https://github.com/ejct/loom-foo/issues) for non-sensitive questions and bug reports. See [Security](SECURITY.md), [Privacy](PRIVACY.md) and [Terms](TERMS.md).

[MIT license](LICENSE) · Maintainer: [ejct](https://github.com/ejct).
