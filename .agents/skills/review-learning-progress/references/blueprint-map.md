# PDF Blueprint Topic Index

Source: root `pc-language-code-learning-map.pdf`. This index was prepared from its five pages read on 2026-10-07. Use it to locate learning topics and pages; the original PDF defines the blueprint, and technical conclusions require separate verification.

## Goals and Shared Dimensions

- Page 1: compilation principles, runtime models, and scenario suitability; observe compilation pipelines, type and memory models, concurrency scheduling, and debugging probes.
- Page 2: tools for syntax and ASTs, bytecode and intermediate artifacts, and operating-system and runtime probes.
- Pages 3-5: languages, open-source projects, and internals entry points.
- Page 5: three routes for cross-language experiments.

## Languages and Project Entry Points

| Language | Pages | Blueprint entry points | Related learning topics |
|---|---|---|---|
| C# | 1, 3, 5 | Dapper, ASP.NET Core | IL, JIT, dynamic code generation, generics, memory slices |
| Java | 3, 5 | Retrofit, Guava | JVM, dynamic proxies, generic erasure, comparison with C# |
| Python | 1, 3, 5 | FastAPI, pydantic-core | AST, bytecode, evaluation loop, attribute lookup, decorators, FFI |
| Go | 1, 4, 5 | Gin, Serf | Compilation and linking, deployment artifacts, GMP, network polling |
| Rust | 1, 4, 5 | ripgrep, hyper | Ownership, borrow checking, lifetimes, monomorphization |
| C | 1, 4, 5 | Redis | Manual memory layout, resource management, event loops, system calls |
| C++ | 1, 5 | llama.cpp, Dear ImGui | RAII, construction and destruction, SIMD, throughput control |
| JavaScript | 5 | Fastify, Express | V8 execution and optimization, Node.js event loop, microtasks |
| TypeScript | 5 | Fastify, Express | Type checking and code transformation, observed separately from JavaScript execution |

The layered TypeScript observation requirement comes from root `AGENTS.md`, refining the PDF's JS / TS entry. Personalized sequencing, including the Python main track, follows current `.learn-contract` rules.

## Three Routes

| Route | Comparison | Core questions |
|---|---|---|
| Managed VMs | C# / Java | Generics, dynamic code generation and proxies, JIT |
| Concurrency and scheduling | Go / Python | Coroutines, threads, event loops, runtime and system interaction |
| Memory and ownership | C / C++ / Rust | Manual allocation, RAII, ownership, borrow checking |

JS / TS add comparisons of type checking and transformation, V8 optimization, and the Node.js event loop.

## Practice Evidence Entry Points

Page 2 lists Tree-sitter, Semgrep, AST Explorer, Python `dis`, ILSpy, SharpLab, Compiler Explorer, ProcMon, and Process Explorer as observation tools. Retrieve tree nodes, instruction excerpts, errors, call paths, or system traces from corresponding experiments. Tool installation establishes environment readiness only.
