---
name: review-learning-progress
description: "Retrieve progress in this project's multilanguage compilation and runtime learning against the PDF blueprint. Use when the learner asks where they left off, resumes learning, reviews coverage, or checks alignment with the final goal. Do not use for software-development status reports or generating an entire course."
---

# Review Learning Progress

Locate progress against the learner's final goal: **experience compilation across programming languages through hands-on practice, understand principles and differences, and make scenario-based language-selection judgments**. Return an evidence-based current position and one actionable next operation.

## Read Project Context

This skill lives at `.agents/skills/review-learning-progress/`. Locate the project root three levels above the skill directory, independently of the current working directory and without hardcoding a machine-specific absolute path.

1. Read root [AGENTS.md](../../../AGENTS.md), list and read every `*.rules.md` in [.learn-contract/](../../../.learn-contract/), and apply the current learning track and guidance preferences.
2. Use [pc-language-code-learning-map.pdf](../../../pc-language-code-learning-map.pdf) as the blueprint. The [blueprint index](references/blueprint-map.md) only locates pages and topics. If the original PDF has not been read in this session, read its relevant pages first; read all five pages for a complete review. The original PDF takes precedence when it changes.
3. The blueprint defines scope and topics. Verify its mechanism summaries against the relevant implementation, version, official sources, or experiments. Progress retrieval normally needs local evidence; verify new mechanism explanations according to project requirements.

## Retrieve Actual Progress

Inspect the project file inventory and follow its existing structure. Read language-specific `experiments/`, experiment documentation, concise artifacts, and existing learning records as needed. Follow root CodeGraph conventions when locating or understanding source. Include learner-provided code, actual output, explanations, and explicit progress statements from the current conversation.

Limit retrieval to this project, the current conversation, and historical materials explicitly supplied by the learner. Treat unavailable or unrecorded history as an evidence gap; ask about the latest operation and result when necessary. Identify which conclusions come from files, current output, or learner reports.

| Available information | Supported judgment |
|---|---|
| Learning rules, course plans, the PDF, installed tools | Learning arrangements or environment preparation; experiment completion is unverified |
| Example source exists without execution results | The example is prepared; actual execution is unverified |
| Learner supplies commands, environment, and actual artifacts | The corresponding operation was practiced; state implementation and version |
| The guiding agent runs the example alone | The example can run; learner hands-on practice remains unverified |
| Learner explains artifacts or tests a prediction by modifying the example | Evidence of understanding the corresponding mechanism; identify its support |
| Comparable artifacts and explanations for the same question across languages | The corresponding cross-language comparison has been conducted |
| A selection judgment with scenario constraints, comparison evidence, and reasons | A scenario-specific selection analysis exists; state its limits |

Use prior language experience as teaching context. Judge completion of an internals topic by evidence for that topic. An intentional compilation failure counts as practice when the actual error matches its verification objective.

## Assess Against the Blueprint

Map evidence to shared dimensions: compilation and execution, AST / IR, types and abstractions, memory and resources, concurrency and system interaction, debugging and language selection. Cover C#, Java, Python, Go, Rust, C, C++, JavaScript, and TypeScript, relating topics to the blueprint's three routes and project entry points.

Assess **practice, mechanism understanding, cross-language comparison, and scenario-based selection** separately. Use verified, in progress, awaiting verification, or no available record according to evidence. No available record means evidence is missing; label a topic not started only when the learner confirms that state. Surface conflicting evidence and distinguish old records from current confirmation.

Prefer the rules' Python main track and JS / TS comparison track. The three routes frame topic selection; order learning according to confirmed preferences and current foundations. Express progress as topic coverage when no complete task list and completion criteria exist.

## Return Results and the Next Step

Use the learner's preferred conversation language. Start with the learning position that can be confirmed, then provide a concise topic table covering topic / language, blueprint location, practice evidence, understanding and comparison status, and evidence gaps. Group languages with no available records when useful while retaining overall scope.

Explain how the current activity serves the final goal and which evidence is still missing. End with **one concrete next operation**, its purpose, working directory, and expected observation. Follow stepwise guidance and wait for learner output before proceeding. Ask only for missing information that affects the starting point.

Return retrieval results in conversation by default. Save or update progress only when explicitly requested, following an existing record location or `learning-records/` if no structure exists. Write saved records entirely in English under root `AGENTS.md`, including dates, topics, environment, operations and actual results, evidence locations, unresolved verification, and the next step. Preserve other requested record content. `.learn-contract` is reserved for learning rules.
