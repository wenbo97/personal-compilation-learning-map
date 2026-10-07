# Multilanguage Compilation and Runtime Lab

## Required Initialization Before Every Task

**Before every distinct task, including resumed work, retrieve the initialization context and complete the read-only checks below before substantive work. Repeat this at task boundaries even when an earlier task in the session was already initialized.**

Initialization source: session `01a115cd-0061-71d1-9f9c-13d7b69b338e`, dated 2026-10-07. Locate its JSONL by session ID in the local Codex session or archived-session directories; the original filename is `rollout-2026-10-07T17-58-38-01a115cd-0061-71d1-9f9c-13d7b69b338e.jsonl`. Retrieve the relevant initial user messages, tool calls, and text results, skipping image payloads. If the archive is unavailable, state that limitation and perform the live checklist using this file.

1. **Resolve the project and instructions.** Confirm the actual project root and working directory rather than assuming the session starts in the project. Read applicable ancestor instructions, this root file, and any instructions governing the task's target directory. Apply the English-only file requirement.
2. **Reload learning context.** List and read all `.learn-contract/*.rules.md`, including newly added rules. Read the project skill relevant to the task. Retrieve available project-specific history and progress evidence without assuming earlier sessions are visible.
3. **Inspect the current project.** Review the top-level layout and a scoped file inventory, excluding dependency directories, caches, and build outputs. Inspect the relevant language directory, experiments, artifacts, and learning records. Distinguish prepared examples and plans from verified learner practice.
4. **Check repository capabilities.** Detect whether the project is a Git worktree and whether a `.codegraph/` index exists. Use CodeGraph before locating or understanding code when indexed; otherwise use normal file tools. Record absent capabilities without initializing Git or CodeGraph automatically.
5. **Retrieve the learning blueprints.** Check `pc-language-code-learning-map.pdf` and `Py-Learn-Map-With-Links.md.pdf`, then retrieve sections relevant to the task. The first PDF is the primary blueprint; the second supplies supplementary reference material. Use page rendering when text extraction loses structure. Treat blueprint mechanism summaries as topics to verify against implementations and experiments.
6. **Probe toolchain readiness.** Resolve current command paths and versions for Python / `py`, Node.js / npm / TypeScript, .NET SDKs, Java / `javac`, Go, Rust / Cargo, and available C / C++ compilers. Check `uv`, PDF extraction/rendering commands, and PDF Python modules. Mark tools missing from the current PATH as unverified availability outside that PATH; add dependencies only when the current task needs them.
7. **Verify runtime identity.** For Python, inspect `sys.executable`, `sys.version`, `sys.implementation`, OS/architecture, available interpreter alternatives, `ast` / `dis`, and actual GIL state when its inspection API exists. For JS / TS work, identify Node.js, V8, architecture, and TypeScript compiler versions separately. Use UTF-8 for Python inspection output; temporary PDF inspection may use `uv run --no-project` with task-required dependencies.
8. **Establish the next action.** Briefly report task-relevant verified state, missing evidence or prerequisites, and the current learning entry point when applicable. For learning tasks, use the progress skill and give one concrete operation under the stepwise guidance rules; for maintenance tasks, proceed with the authorized change after initialization.

Current project instructions and confirmed learner preferences take precedence over historical instructions. Historical tool versions, missing-tool findings, directory contents, and Git / CodeGraph state are provenance, not current facts. Recheck them live. Initialization checks performed by the guiding agent do not establish learner completion of an experiment.

## Project Goals and Scope

Use reproducible small experiments and real open-source projects to understand compilation, execution, and AST parsing across languages. Develop evidence-based comparisons and language-selection judgments. Connect syntax to type systems, compiled artifacts, memory models, or runtime behavior.

The [Multilanguage Internals and Architecture Learning Guide](pc-language-code-learning-map.pdf) defines the target languages: **C#, Java, Python, Go, Rust, C, C++, JavaScript, and TypeScript**. Use the guide to determine scope and topics; verify specific mechanisms against version-matched official documentation, compiler or runtime source, and experiments.

## Continuous Compilation and Artifact-Flow Framework

**Throughout learning in every language, connect each topic to the meaning and purpose of compilation, its products, the applicable stages, and the components that use those products.** Apply this framework during explanations, experiments, source reading, cross-language comparisons, and scenario-based language selection.

Use [compilation-foundations.rules.md](.learn-contract/compilation-foundations.rules.md) as the authoritative guidance and conceptual scaffold. Relate each applicable stage or runtime boundary through **input -> processing -> output -> receiving component -> purpose**. Revisit the relevant relationships as topics deepen, and connect local observations to the overall source-to-execution process. Keep the teaching model distinct from the selected implementation's verified behavior.

## English-Only Project Files

**All project file records and all content created or updated in project files must use English only. No other languages or bilingual content are allowed in authored project files.**

This requirement covers this file, learning rules, skill instructions and metadata, experiment documentation, code comments, authored output messages, learning records, and generated teaching materials. Paraphrase feedback in English when recording it in files. This is a file-content requirement; conversation language follows the learner's preference.

## Personalized Learning Rules: Required Before Guidance

Before planning learning, conducting training, explaining mechanisms, guiding experiments, reading source together, or comparing languages, **list and read every `*.rules.md` file in [.learn-contract/](.learn-contract/) and follow its personalized guidance**. These rules apply to every language directory. Each file maintains an independent learning agreement; include rules added later when reading the directory.

## Project Learning Skills

- Use [review-learning-progress](.agents/skills/review-learning-progress/SKILL.md) to retrieve progress, resume learning, or review coverage against the PDF blueprint. Locate the current state and next step using practice evidence.
- Use [align-learning-guidance](.agents/skills/align-learning-guidance/SKILL.md) to align teaching style, pace, or practice approaches, or to update rules from learner feedback. Maintain the relevant independent files in `.learn-contract`.

## Shared Observation Dimensions

- **Compilation and execution:** Observe the applicable stages of source processing, lexing, parsing, semantic analysis, type checking, lowering, IR, bytecode or IL, machine code, linking, and loading. Compare interpreted execution, AOT, JIT, and optimization behavior.
- **Syntax trees and intermediate representations:** Distinguish CSTs, ASTs, and compiler IR, and separate parsing tools from actual compilers. Retain tree nodes or instruction excerpts that explain observed behavior.
- **Types and abstractions:** Compare dynamic and static typing, generics and type erasure, monomorphization, reflection, dynamic dispatch, and runtime costs.
- **Memory and resources:** Observe object layout, stack and heap allocation, reference counting, GC, RAII, ownership, lifetimes, and FFI boundaries.
- **Concurrency and system interaction:** Compare OS threads, coroutines, event loops, task scheduling, synchronization, and I/O. Design CPU-bound and I/O-bound scenarios separately.
- **Debugging and language selection:** Establish evidence with breakpoints, tracing, disassembly, profiling, or system probes. Discuss suitability using latency, throughput, resource use, deployment, and ecosystem considerations.

## Experiment Workflow

1. Reduce the question to a testable hypothesis. Establish a minimal runnable example before tracing the same mechanism in an open-source project when needed.
2. Record the OS, architecture, compiler or runtime version, dependency versions, and settings affecting results, including optimization, debugging, JIT, and GC.
3. Provide commands reproducible in Windows PowerShell. State the working directory, prerequisites, and generated artifacts. Explain platform requirements when using tools for other platforms.
4. Run examples and preserve key evidence such as ASTs, bytecode, IL, IR, assembly, errors, or call traces. Separate expected results, actual observations, explanations, and hypotheses awaiting verification.
5. Keep questions, inputs, algorithms, and execution conditions comparable across languages. Record warm-up, repetitions, and statistics for performance experiments, and state the limits of conclusions.
6. Support conclusions with actual execution and evidence. State verification status when tools are missing or examples have not run. For intentional compilation failures, record the expected error and its mechanism.

Prefer built-in language tools and minimal dependencies. Introduce toolchains as experiments require them, check locally available versions first, and then add necessary dependencies.

## Organization and Records

- Maintain project and experiment conventions here, and maintain personalized learning rules by topic in `.learn-contract/*.rules.md`. Keep language-specific differences in the relevant sections of this file. Subdirectories follow this file and the rule directory.
- Begin every Markdown rule in `.learn-contract` with YAML frontmatter containing `title`, `date`, `updated`, `scope`, and `tags`. Use quoted ISO dates (`YYYY-MM-DD`): `date` records rule creation and remains unchanged; `updated` records the latest edit. Maintain the title, scope, and English tag list when the rule changes.
- Place new independent experiments in the relevant language directory under `experiments/<topic>/`, with source examples and an experiment `README.md` together. Prefer an established structure when one exists.
- Experiment documentation includes the question and hypothesis, environment and versions, commands, key artifacts or output, mechanism explanation, comparison conclusions, and references.
- Centralize cross-language summaries around shared questions and differences, linking to language-specific experiments. Keep local reproduction details in each language's documentation.
- Use separate output directories for intermediate artifacts and caches. Retain concise evidence that supports conclusions.
- After changing experiment code, execute the relevant example and necessary checks. Verify intentional failures against their expected errors.

## Learning Routes and Project Entry Points

Choose among the guide's three routes according to the current question:

1. **Managed VMs:** C# / Java; compare generics, dynamic code generation and proxies, and JIT. Entry projects: Dapper, ASP.NET Core, Retrofit, and Guava.
2. **Concurrency and scheduling:** Go / Python; compare goroutines, threads, event loops, and runtime limitations. Entry projects: Gin, Serf, FastAPI, and pydantic-core.
3. **Memory and ownership:** C / C++ / Rust; compare manual management, RAII, ownership, and borrow checking. Entry projects: Redis, llama.cpp, Dear ImGui, ripgrep, and hyper.

JavaScript / TypeScript add experiments on type checking and code transformation, V8 execution and optimization, and the Node.js event loop, compared with other scheduling models. Entry projects: Fastify and Express.

Choose tools by observation layer: native language AST or syntax APIs and Tree-sitter; bytecode and IR tools such as Python `dis`, ILSpy, SharpLab, and Compiler Explorer; system tools such as ProcMon and Process Explorer. Verify language, version, and platform support before use.

## Python Experiment Conventions

- Prefer standard-library minimal experiments: use `ast.parse` / `ast.dump` to observe syntax, and connect `compile`, code objects, and `dis` to compilation results and execution. Explore imports, `.pyc`, objects, GC, threads, processes, and `asyncio` next, entering the C API / PyO3 / FFI as needed.
- Identify the environment using `sys.version`, `sys.implementation`, and the actual interpreter path. State version and build configuration for conclusions about CPython internals, ASTs, bytecode, optimization, GC, and the GIL. Confirm actual runtime state when discussing free-threaded builds.
- Use the Python directory's virtual environment when third-party dependencies are needed, and record dependencies and commands.
- Relate local AST or bytecode evidence to the matching CPython implementation. Trace actual call paths when entering projects such as FastAPI or pydantic-core.
- Use explicitly controlled project examples for `exec` / `eval` experiments, and explain the source of executed code.

<!-- CODEGRAPH_START -->
## CodeGraph

In repositories indexed by CodeGraph (a `.codegraph/` directory exists at the repo root), reach for it BEFORE grep/find or reading files when you need to understand or locate code:

- **MCP tool** (when available): `codegraph_explore` answers most code questions in one call — the relevant symbols' verbatim source plus the call paths between them, including dynamic-dispatch hops grep can't follow. Name a file or symbol in the query to read its current line-numbered source. If it's listed but deferred, load it by name via tool search.
- **Shell** (always works): `codegraph explore "<symbol names or question>"` prints the same output.

If there is no `.codegraph/` directory, skip CodeGraph entirely — indexing is the user's decision.
<!-- CODEGRAPH_END -->
