# Prompt Library

A collection of structured prompts for AI-assisted workflows, built on [Emotional Intelligence Prompting (EIP)](https://github.com/OuterSpacee/claude-emotion-prompting) principles.

## Software Development Prompts

Four prompts covering the full software development lifecycle. Each is self-contained but designed to hand off context between phases via session summaries.

| File | Phase | Purpose |
|---|---|---|
| `00-swdev-project-customizer.md` | 0 | Meta-prompt that interviews you about your project and generates domain-specific versions of all three phase prompts |
| `01-swdev-requirement-gathering.md` | 1 | Requirements analysis, key design decisions, contribution structure mapping |
| `02-swdev-architecture-design.md` | 2 | Layered architecture design, observability planning, contribution-aligned organization |
| `03-swdev-development-testing-debugging.md` | 3 | Incremental development, testing, debug instrumentation, KPI observability |

### Getting Started

**Generic use:** Load any phase prompt directly as a system prompt or paste it at the start of a conversation.

**Project-specific use:** Start with `00-swdev-project-customizer.md` to generate prompts tailored to your tech stack, team structure, and domain constraints.

### Workflow

Phases are designed for non-linear use. Start with Phase 1, move to Phase 2, then Phase 3 — but freely return to earlier phases as the project evolves. Each phase produces a **session summary** that serves as the handoff artifact when switching.

```
Phase 1 (Requirements) --> Phase 2 (Architecture) --> Phase 3 (Development)
         ^                        ^                          |
         |                        |                          |
         +--- update reqs --------+------ design changed ----+
```

### Key Features

- **Contribution-aware:** Prompts capture who contributes what (end-to-end ownership, module-specific work, human validation, artifact correction, eval data) and organize code/artifacts accordingly
- **Debug instrumentation:** Phase 3 builds structured error codes, diagnostic modes, and layered logging into the code from the start
- **Observability:** KPI collection (accuracy, resource usage, throughput, response times) stored in persistent DB for optimization decisions
- **Remote collaboration:** When the LLM can't directly access runtime data, the meta-prompt generates augmented prompts with diagnostic CLI, structural fingerprints, and compact reporting formats

## EIP Foundation

These prompts apply seven principles from the [Emotional Intelligence Prompting](https://github.com/OuterSpacee/claude-emotion-prompting) framework, based on Anthropic's research into emotion vectors in LLMs:

1. **Grant Permission to Fail** — reduces fabrication under pressure
2. **Decompose Into Checkpoints** — interrupts failure cascades
3. **Frame With Curiosity** — activates genuine engagement
4. **Invite Transparency** — surfaces honest reasoning
5. **Collaborate, Don't Command** — reduces sycophancy
6. **Acknowledge Difficulty** — normalizes struggle on hard problems
7. **Counteract Brooding Baseline** — balances post-training pessimism

## License

MIT
