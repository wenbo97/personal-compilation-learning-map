---
name: align-learning-guidance
description: "Align learner feedback on teaching style, pace, and practice approaches with this project's .learn-contract rules. Use when the learner finds guidance suitable or unsuitable, requests a future teaching preference, or asks to update learning rules. Do not use to change technical facts, assess learning progress, or infer lasting preferences from one experiment error."
---

# Align Learning Guidance

Convert explicitly stated preferences into executable guidance rules with appropriate scope. Follow the learner's intended approach while preserving the goal of learning compilation processes, principles, differences, and language selection.

## Locate Current Rules

This skill lives at `.agents/skills/align-learning-guidance/`. Locate the project root three levels above the skill directory, independently of the current working directory and without hardcoding a machine-specific absolute path.

Read root [AGENTS.md](../../../AGENTS.md), then list and read every `*.rules.md` in [.learn-contract/](../../../.learn-contract/). Locate the relevant topic using current feedback, previously confirmed preferences, and the specific guidance that prompted the feedback.

Treat [compilation-foundations.rules.md](../../../.learn-contract/compilation-foundations.rules.md) as a continuing agreement across all project languages and learning activities. Its conceptual scaffold connects compilation meaning and purpose to program representations, stage products, receiving components, and their uses. When aligning guidance, preserve that relationship across changes to pace, medium, entry point, or explanation depth; keep technical summaries subject to the project's implementation and evidence requirements.

## Understand Feedback and Scope

Extract three things: **the specific guidance approach, the desired alternative, and its scope**. For example, the learner may prefer running a minimal example before reading source, or starting from a real framework's call path. Establish whether the preference applies to this experiment or future sessions of a given kind.

- When the learner invokes this skill with a clear preference, explicitly requests rule updates, or specifies an approach for future guidance, update the corresponding rules directly. Continue changes covered by existing authorization.
- When feedback concerns only the current question, adjust current guidance first. Persist a lasting rule only with clear intent to do so.
- When the desired alternative is unclear, briefly restate the established disagreement and ask one concrete question that determines the next step. Continue independent work that does not depend on the answer.
- Retain language, topic, or phase restrictions stated by the learner. Update existing agreements from explicit feedback; avoid inferring personality, ability, or general preferences from a single setback.

## Update Independent Rule Files

Prefer editing the existing file for the same topic, preserving other valid agreements. For a new topic, add a clearly named `kebab-case.rules.md` file in `.learn-contract`, with each file maintaining an independent learning agreement.

Write all rules, headings, examples, and feedback summaries in English only, following root `AGENTS.md`. Paraphrase feedback received in another language into English while preserving its confirmed meaning.

Write positive, executable behavior with the necessary scope and trigger. After clarifying a complaint about abstraction, for example, record: "When introducing a compilation stage, show minimal source and an actual artifact excerpt first, then explain their relationship." Record only confirmed meaning.

Use the frontmatter requirements in root `AGENTS.md` for new and existing rules. Preserve an existing rule's creation date and update its modification date when editing. Use this concise structure for new rules; preserve an existing file's effective body structure:

```markdown
---
title: "Rule Topic"
date: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
scope: "Applicable language, topic, or learning phase"
tags:
  - guidance
---

# Rule Topic

Scope: language, topic, or learning phase.

- Under a specific condition, apply a concrete guidance behavior.
- State the observation or condition needed to continue.

Basis: explicit learner feedback on YYYY-MM-DD, briefly summarized.
```

Use the actual date and a concise preference summary. When the learner requests a one-session adjustment, adapt current guidance without creating a lasting rule.

Check other rule files for statements conflicting with the newly confirmed preference, and change only related content. Update the same rule when preferences change instead of stacking contradictory versions. Judge technical facts and experimental results by evidence; align explanation order, entry points, pace, or practice approaches.

When the learner asks to extend an agreement throughout learning, update its scope and applicability in the authoritative rule. Maintain the corresponding root `AGENTS.md` requirement or pointer when needed, and keep the detailed conceptual scaffold in that rule. Preserve explicit learner changes to the framework and distinguish them from routine adjustments to how it is taught.

Root `AGENTS.md` discovers rules dynamically. Reuse that mechanism after adding rules; update the entry point only if discovery is missing or its path is wrong. Keep progress, experiment code, and generated materials in their project-designated locations.

## Verify and Report

Read back affected files. Confirm executable behavior, correct scope, no duplicate or conflicting treatment of the topic, and independent rule files in `.learn-contract`.

For changes affecting the continuing compilation framework, check that root instructions, rule scope, and skill references agree on its applicability throughout learning. Confirm that the receiving component and its purpose remain part of the guidance, and that the framework is revisited as new topics arise.

Explain how feedback became concrete behavior, which files changed, and how the next session will be guided. Clearly requested rule updates need no extra confirmation step. When meaning remains uncertain, concentrate clarification on that unresolved point.
