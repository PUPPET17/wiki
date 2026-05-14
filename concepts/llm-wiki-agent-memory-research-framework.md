---
title: LLM Wiki / Agent Memory Research Framework
created: 2026-05-14
updated: 2026-05-15
type: concept
tags: [llm-wiki, agent-memory, rag, context-engineering, knowledge-integration, personal-ai-os, memory-architecture, retrieval, compression, indexing, tradeoff, failure-case, opportunity]
sources: [raw/articles/karpathy-llm-wiki-gist-2026.md, raw/papers/memgpt-2023.md, raw/papers/generative-agents-2023.md, raw/papers/coala-2023.md, raw/papers/rag-survey-2023.md, raw/articles/anthropic-effective-agents-2024.md, raw/articles/anthropic-multi-agent-research-2025.md, raw/articles/langchain-context-engineering-2025.md, raw/articles/harrison-chase-sequoia-context-engineering-2025.md, raw/articles/simon-willison-embeddings-2023.md, raw/articles/microsoft-vector-search-not-enough-2024.md, raw/community/hn-karpathy-style-wiki-2026.md, raw/community/hn-memgpt-2023.md, raw/community/hn-letta-code-2025.md, raw/product-docs/openai-chatgpt-memory-2024-2025.md, raw/product-docs/letta-memory-2026.md, raw/papers/raptor-2024.md, raw/papers/self-rag-2023.md, raw/papers/memorag-2024.md, raw/community/reddit-memory-systems-2026.md, raw/github/mem0-issue-4573-memory-audit-junk.md, raw/github/letta-issue-652-per-conversation-context-scoping.md, raw/github/mem0-repo-readme.md, raw/github/letta-code-repo-readme.md, raw/github/wuphf-repo-readme.md, raw/github/llm-wiki-compiler-repo-readme.md, raw/github/langchain-context-engineering-repo-readme.md, raw/github/langchain-how-to-fix-your-context-readme.md]
confidence: medium
contested: true
---

# Executive Summary

This document is the first stable research synthesis for a continuously evolving LLM Wiki / Agent Memory / Context Compression / Knowledge Integration framework.

Core finding: Karpathy's LLM Wiki pattern is best understood as a durable, editable, agent-maintained intermediate representation between raw sources and transient model context. It is not merely RAG with markdown output. Its key difference is compilation: claims, entities, conflicts, summaries, and cross-links are incrementally integrated once, then reused and revised. Source: Andrej Karpathy's own gist and X thread, 2026, type: gist/tweet, claim status: fact about his proposal; feasibility remains partly speculative. [raw/articles/karpathy-llm-wiki-gist-2026.md]

The most practical architecture today is local-first markdown+git as source of truth, plus explicit source provenance, BM25/full-text search, metadata, optional embeddings, and periodic lint/reflection. This is supported by Karpathy's proposal, WUPHF's HN-described implementation, Letta's MemFS docs, Simon Willison's small-scale embedding practice, and Microsoft's hybrid-search argument. Claim status: engineering inference, not universal proof. [raw/articles/karpathy-llm-wiki-gist-2026.md] [raw/community/hn-karpathy-style-wiki-2026.md] [raw/product-docs/letta-memory-2026.md] [raw/articles/simon-willison-embeddings-2023.md] [raw/articles/microsoft-vector-search-not-enough-2024.md]

The strongest technical lens is context engineering: write context outside the window, select relevant context, compress high-volume context, and isolate work across agents/files/subcontexts. This maps exactly onto LLM Wiki operations: ingest/write, query/select, summarize/compress, subagent/layer/isolate. Source: LangChain 2025 context engineering blog and Harrison Chase interview. Claim status: community/engineering framing. [raw/articles/langchain-context-engineering-2025.md] [raw/articles/harrison-chase-sequoia-context-engineering-2025.md]

The main bottleneck is not storage. It is memory quality: what gets saved, when it is retrieved, how contradictions are represented, and how stale or hallucinated summaries are prevented from hardening into accepted knowledge. OpenAI's ChatGPT memory controls and HN discussion around Letta show that users need transparency, deletion, and auditability. Claim status: cross-validated product/community concern. [raw/product-docs/openai-chatgpt-memory-2024-2025.md] [raw/community/hn-letta-code-2025.md]

Reddit evidence is currently insufficient. Search results found relevant LocalLLaMA threads, but direct extraction was blocked. They are listed in Source Map as low reliability and must not anchor core conclusions until retrieved through a reliable API/archive/manual review. [raw/community/reddit-memory-systems-2026.md]

# Core Thesis

A useful agent memory system should not be a bag of retrieved chunks. It should be an editable knowledge substrate with four properties:

1. Durable: survives sessions, model changes, and application runtimes.
2. Inspectable: humans and agents can read, diff, cite, and edit it.
3. Integrated: new evidence updates existing pages/facts instead of creating duplicate fragments.
4. Operational: it has ingestion, retrieval, editing, summarization, linting, decay, and conflict-resolution workflows.

Karpathy's key move is replacing repeated query-time re-derivation with cumulative compilation. RAG answers: what chunks are relevant right now? LLM Wiki asks: what should the long-lived knowledge base now believe, and how should it change? Source: Karpathy gist. Claim status: interpretation grounded in primary source. [raw/articles/karpathy-llm-wiki-gist-2026.md]

# Key Concepts

- Raw sources: immutable source documents. Fact: Karpathy explicitly separates raw sources from the LLM-maintained wiki. [raw/articles/karpathy-llm-wiki-gist-2026.md]
- Wiki layer: LLM-generated markdown pages for entities, concepts, summaries, comparisons, contradictions, and queries. Fact about proposal. [raw/articles/karpathy-llm-wiki-gist-2026.md]
- Schema: the operating manual for the agent maintainer. Fact about proposal; practical necessity inferred. [raw/articles/karpathy-llm-wiki-gist-2026.md]
- Memory tiers: active context, pinned memory, searchable memory, raw archive. Fact in MemGPT/Letta-like systems; architecture inference for LLM Wiki. [raw/papers/memgpt-2023.md] [raw/product-docs/letta-memory-2026.md]
- Context engineering: deciding what is written, selected, compressed, or isolated for a model step. Source: LangChain blog / Harrison Chase interview. [raw/articles/langchain-context-engineering-2025.md] [raw/articles/harrison-chase-sequoia-context-engineering-2025.md]
- Reflection/consolidation: generating higher-level summaries or memory edits from experience streams. Paper-backed in Generative Agents; product-backed in Letta sleep-time reflection docs. [raw/papers/generative-agents-2023.md] [raw/product-docs/letta-memory-2026.md]
- Hybrid retrieval: vector + full-text + merge + rerank. Engineering-backed by Microsoft blog; not proven universal. [raw/articles/microsoft-vector-search-not-enough-2024.md]

# Karpathy Gist Analysis

Karpathy's gist defines three layers: raw sources, wiki, and schema. It defines three operations: ingest, query, lint. It also emphasizes index.md and log.md as navigation and chronology. These are primary-source facts. [raw/articles/karpathy-llm-wiki-gist-2026.md]

Most important insight: a question result can itself become a durable page. This converts exploration into persistent knowledge, which is often missing from RAG chatbots and file-upload products. Fact about proposal; practical value is an engineering hypothesis. [raw/articles/karpathy-llm-wiki-gist-2026.md]

The gist is intentionally abstract. It does not specify evaluation methodology, source quality scoring, provenance schema, concurrency model, access control, conflict resolution algorithms, or scaling thresholds beyond rough guidance. These are gaps, not criticisms. Claim status: direct reading/inference. [raw/articles/karpathy-llm-wiki-gist-2026.md]

The gist's moderate-scale claim, about index-first navigation working around ~100 sources / hundreds of pages, should be treated as anecdotal. WUPHF's HN project claim of 85% recall@20 on 500 artifacts with BM25 is encouraging but still project-specific and not a universal benchmark. [raw/articles/karpathy-llm-wiki-gist-2026.md] [raw/community/hn-karpathy-style-wiki-2026.md]

# Architecture Patterns

## Pattern A: Markdown+Git canonical memory

Use markdown files as canonical human/agent-readable memory; use git for diff, provenance, rollback, branches, and review. This is Karpathy's implied stack, WUPHF's explicit stack, and Letta MemFS's documented stack. Claim status: validated as an emerging engineering pattern, not formally benchmarked. [raw/articles/karpathy-llm-wiki-gist-2026.md] [raw/community/hn-karpathy-style-wiki-2026.md] [raw/product-docs/letta-memory-2026.md]

Tradeoff: excellent inspectability and portability; weaker for high-volume low-latency retrieval unless indexed.

## Pattern B: Append-only facts + synthesized pages

Store atomic facts/events as append-only JSONL or records, then rebuild human-readable entity briefs/summaries. WUPHF claims per-entity JSONL facts and synthesis workers. Generative Agents stores experience streams and synthesizes reflections. [raw/community/hn-karpathy-style-wiki-2026.md] [raw/papers/generative-agents-2023.md]

Tradeoff: better provenance and regeneration; more complex than just editing pages.

## Pattern C: Hierarchical summaries

Use page summaries, topic maps, and recursive abstraction. RAPTOR provides paper evidence that tree-organized summaries can improve retrieval over chunk-only retrieval on some tasks. A wiki is a human-editable variant of this hierarchy. [raw/papers/raptor-2024.md]

Tradeoff: summaries lose detail and can hallucinate; must retain links to raw evidence.

## Pattern D: Virtual context / memory paging

MemGPT frames long-term interaction as moving information between memory tiers, inspired by OS virtual memory. Letta operationalizes memory blocks and MemFS. [raw/papers/memgpt-2023.md] [raw/product-docs/letta-memory-2026.md]

Tradeoff: powerful abstraction; community pushes back when OS metaphors overclaim. [raw/community/hn-memgpt-2023.md]

## Pattern E: Hybrid search and reranking

Use BM25/full-text for exact names, IDs, strings, numbers; embeddings for semantic recall; reranking for top-k quality. Microsoft argues vector search alone fails exact-match queries. Simon Willison shows embeddings are cheap/useful at small scale but opaque and model-dependent. [raw/articles/microsoft-vector-search-not-enough-2024.md] [raw/articles/simon-willison-embeddings-2023.md]

Tradeoff: more moving parts than plain markdown; much better retrieval robustness.

# Existing Projects

- Karpathy LLM Wiki idea file: primary conceptual seed; no fixed implementation. [raw/articles/karpathy-llm-wiki-gist-2026.md]
- MemGPT / Letta: OS-inspired virtual context and memory-first agents. [raw/papers/memgpt-2023.md] [raw/product-docs/letta-memory-2026.md]
- Letta Code / MemFS: long-lived coding agents with portable memory across models; `/init`, `/remember`, `/clear`, and skill learning. The repo frames the difference from Claude Code/Codex/Gemini CLI as agent-based persistence vs independent sessions. [raw/product-docs/letta-memory-2026.md] [raw/github/letta-code-repo-readme.md]
- LettaBot context-scoping issue: a concrete design discussion showing that agent-level memory blocks and MemFS files become privacy, attention, and token-cost problems when reused identically across conversations. Proposed solution: conversation-level context include/exclude or per-file frontmatter scoping. [raw/github/letta-issue-652-per-conversation-context-scoping.md]
- WUPHF: independently inspected repo README confirms a local/self-hosted “collaborative office” with per-agent notebook + shared workspace wiki, git-native markdown memory, fresh sessions, per-agent scoped tools, and claimed flat-token/caching economics. [raw/community/hn-karpathy-style-wiki-2026.md] [raw/github/wuphf-repo-readme.md]
- llm-wiki-compiler: direct Karpathy-pattern implementation with `ingest`, `compile`, `query`, `query --save`, `lint`, `watch`, `serve` MCP, review queue, claim-level provenance markers, page metadata, and line-range citations. It explicitly notes limitations: early software, best for small high-signal corpora, index-based routing, and honest truncation metadata. [raw/github/llm-wiki-compiler-repo-readme.md]
- Mem0: universal memory layer project with production-oriented claims: single-pass ADD-only extraction, entity linking, multi-signal retrieval, temporal reasoning, and open evaluation framework. However, the GitHub issue audit below provides a severe counterexample for memory quality. [raw/github/mem0-repo-readme.md] [raw/github/mem0-issue-4573-memory-audit-junk.md]
- LangChain context-engineering repos: runnable notebooks implementing write/select/compress/isolate, plus “How to Fix Your Context” examples for RAG, tool loadout, context quarantine, context pruning, context summarization, and context offloading. [raw/github/langchain-context-engineering-repo-readme.md] [raw/github/langchain-how-to-fix-your-context-readme.md]
- LangMem: SDK framing semantic, episodic, procedural memory and namespaces. [raw/articles/langchain-context-engineering-2025.md]
- OpenAI ChatGPT Memory: productized saved memories and chat-history personalization with controls. [raw/product-docs/openai-chatgpt-memory-2024-2025.md]

# Community Consensus

Evidence-backed consensus:

1. Memory must be transparent and editable. HN Letta thread contrasts white-box memory with ChatGPT-style black-box memory that can accumulate bad facts. OpenAI's own docs emphasize controls. [raw/community/hn-letta-code-2025.md] [raw/product-docs/openai-chatgpt-memory-2024-2025.md]

2. Vector DB alone is not enough for reliable knowledge systems. Microsoft gives concrete exact-match failure examples; WUPHF reports BM25-first performance; Simon Willison presents embeddings as useful but not magical. [raw/articles/microsoft-vector-search-not-enough-2024.md] [raw/community/hn-karpathy-style-wiki-2026.md] [raw/articles/simon-willison-embeddings-2023.md]

3. Agent systems should start simple. Anthropic explicitly advises simple composable patterns and adding complexity only when outcomes improve. [raw/articles/anthropic-effective-agents-2024.md]

4. Long-horizon agents need traces/context observability. Harrison Chase argues traces reveal what context entered each step. [raw/articles/harrison-chase-sequoia-context-engineering-2025.md]

5. Indiscriminate memory storage is worse than no memory for some production settings. A mem0 production audit reported 10,134 entries over 32 days with only 224 survivors after audit, and argued that the bottleneck was extraction/storage policy rather than model capability alone. Treat as a single-user production case study, not universal statistics. [raw/github/mem0-issue-4573-memory-audit-junk.md]

6. Context scoping is not optional for multi-conversation agents. LettaBot issue #652 describes privacy leaks, attention pollution, and token waste when agent-level memory is pinned identically into unrelated conversations. [raw/github/letta-issue-652-per-conversation-context-scoping.md]

Reddit consensus: unknown. Relevant threads exist, but evidence is insufficient because extraction failed. [raw/community/reddit-memory-systems-2026.md]

# Major Debates

## Debate 1: Wiki vs RAG

Position A: Wiki beats RAG because knowledge compounds and contradictions are pre-integrated. Source: Karpathy gist. [raw/articles/karpathy-llm-wiki-gist-2026.md]

Position B: RAG remains necessary because raw evidence retrieval is still required for verification and long-tail detail. Source: RAG survey, Microsoft hybrid search. [raw/papers/rag-survey-2023.md] [raw/articles/microsoft-vector-search-not-enough-2024.md]

Synthesis: LLM Wiki should not replace RAG; it should sit above it. The wiki is the compiled layer, while RAG/search retrieves raw evidence and page details.

## Debate 2: Graph memory vs vector memory vs symbolic memory

Graph memory: explicit entities/edges support inspection, conflict resolution, and user control. But graph extraction is brittle and schema-heavy.

Vector memory: cheap semantic recall and fuzzy matching. But embeddings are opaque, weak for exact strings, and model-dependent. [raw/articles/simon-willison-embeddings-2023.md] [raw/articles/microsoft-vector-search-not-enough-2024.md]

Symbolic/markdown memory: most inspectable and editable. But retrieval and consistency require discipline and tooling.

Synthesis: start symbolic+BM25; add vector and graph indices as derived indexes, not source of truth.

## Debate 3: Personal AI OS

MemGPT's OS metaphor is technically useful for memory tiers, interrupts, read/write operations. But HN criticism shows the phrase invites hype if interpreted literally. [raw/papers/memgpt-2023.md] [raw/community/hn-memgpt-2023.md]

Synthesis: call the MVP a personal knowledge substrate or memory filesystem. Reserve personal AI operating system for later when it coordinates apps, permissions, identity, tools, and memory across workflows.

# Failure Cases

1. Context poisoning: hallucinated or incorrect content enters memory and is later trusted. Source: LangChain context failure taxonomy. [raw/articles/langchain-context-engineering-2025.md]

2. Memory garbage accumulation: community concern in HN Letta thread about ChatGPT memory filling with useless or incorrect statements. [raw/community/hn-letta-code-2025.md]

3. Production memory junk at scale: mem0 issue #4573 reports a 32-day production audit where 97.8% of 10,134 entries were judged junk, including boot-file restating, heartbeat/cron noise, system architecture dumps, transient task state, hallucinated user profiles, identity confusion, and sensitive operational leakage. Reliability: medium because it is a single GitHub issue/case study, but it is detailed and includes comments with proposed mitigations. [raw/github/mem0-issue-4573-memory-audit-junk.md]

4. Feedback-loop amplification: the same mem0 audit reports a hallucinated “User prefers Vim” memory being re-extracted repeatedly after appearing in recall context, producing hundreds of copies. This is a concrete example of memory poisoning becoming self-reinforcing when recalled memories are not marked separately from new user input. [raw/github/mem0-issue-4573-memory-audit-junk.md]

5. Better extraction model does not automatically fix memory quality: the mem0 audit reports switching from a 2B local model to Claude Sonnet reduced some hallucinations but caused faithful over-extraction of system architecture and operational details because the prompt/pipeline remained permissive. Engineering implication: storage policy and quality gates matter as much as model quality. [raw/github/mem0-issue-4573-memory-audit-junk.md]

6. Vector-only retrieval misses exact facts: Microsoft example where vector search failed to retrieve exact price `$45.00`. [raw/articles/microsoft-vector-search-not-enough-2024.md]

7. Summary drift: repeated summarization can erase nuance or source caveats. Supported indirectly by need for raw source provenance; specific benchmark unknown. Status: plausible engineering risk, insufficient direct evidence.

8. Over-agentic complexity: Anthropic warns agents add cost, latency, complexity, and compounding errors. [raw/articles/anthropic-effective-agents-2024.md]

9. AI-slop knowledge base: HN discussion about an AI-generated Show HN post shows community skepticism when generated synthesis lacks structure, proofreading, or clear authorship. [raw/community/hn-karpathy-style-wiki-2026.md]

# Engineering Constraints

- Latency: multi-step ingestion, reflection, and linting are slower than plain indexing.
- Token cost: Anthropic reports agents use ~4x chat tokens and multi-agent systems ~15x chat tokens. [raw/articles/anthropic-multi-agent-research-2025.md]
- Retrieval quality: hybrid search and reranking are needed for production-like recall. [raw/articles/microsoft-vector-search-not-enough-2024.md]
- Source provenance: every synthesis must trace to raw source; otherwise memory becomes unverifiable.
- Concurrency: multiple agents editing markdown can conflict; git branches/PRs or locks are needed.
- Privacy: personal memory needs namespaces, deletion, temporary/no-memory mode, and audit. [raw/product-docs/openai-chatgpt-memory-2024-2025.md]
- Context scope: memory and tool context must be scoped by conversation, channel, user, project, or task. Agent-global pinned memory becomes privacy risk, attention pollution, and unnecessary token cost in multi-conversation systems. [raw/github/letta-issue-652-per-conversation-context-scoping.md]
- Extraction/storage quality gates: memory candidates need negative examples, reject actions, provenance awareness, role preservation, significance scoring, and feedback-loop prevention before storage. [raw/github/mem0-issue-4573-memory-audit-junk.md]
- Model dependency: frontier models still outperform local models for nuanced synthesis, contradiction detection, and careful writing. Local models can handle indexing, clustering, simple extraction, and draft summaries, but better models do not fix bad memory pipelines by themselves. [raw/github/mem0-issue-4573-memory-audit-junk.md]

# Practical Integration Blueprint

## System Architecture

Canonical store:
- raw/ immutable sources
- facts/ append-only JSONL records with IDs, source spans, timestamps, confidence
- wiki/ markdown pages for entities, concepts, comparisons, synthesis
- schema/ agent operating instructions
- index.md and log.md
- git repository for history and review

Derived indexes:
- SQLite metadata: pages, sources, facts, tags, timestamps, links, checksums
- BM25/full-text index for exact retrieval
- optional vector index for semantic search
- optional graph index generated from entities/edges, not canonical source

Agent services:
- Ingest agent
- Retrieval agent
- Editor/synthesis agent
- Lint/audit agent
- Citation verifier
- Optional background reflection/pruning agent

## Data Flow

1. Source capture: URL/PDF/paste/repo -> raw file with URL, date, hash.
2. Extraction: parse title, author, date, source type, claims, entities, quotes.
3. Fact logging: write atomic claims with source spans and confidence.
4. Integration: update existing pages; create new pages only past threshold.
5. Cross-linking: add wikilinks and backlinks.
6. Indexing: update SQLite, BM25, vector index.
7. Verification: run citation checks and broken-link checks.
8. Git commit/review: preserve diff and provenance.

## Memory Lifecycle

Observe -> capture raw -> extract facts -> integrate wiki -> retrieve for tasks -> produce new synthesis -> file useful synthesis -> lint -> decay/prune/archive -> re-ingest when sources drift.

## Ingestion Pipeline

Prototype:
- full raw capture / manual clipping -> raw markdown
- LLM summary -> one concept page
- update index/log manually

MVP:
- deterministic raw frontmatter and hashes
- extraction prompt for claims/entities
- negative examples for what NOT to store
- REJECT / DO_NOT_STORE action before persistence
- existing-page search before writing
- source map table updates
- citation verifier pass

Scalable:
- queue-based ingestion
- chunk/source span IDs
- role-preserving extraction context so user/system/assistant/tool/recalled-memory content are not flattened together
- explicit marking of recalled memories so they cannot be re-extracted as new facts
- candidate-memory quality gate with significance, confidence, privacy, and staleness scoring
- batch fact extraction
- human review UI for high-impact changes
- CI lint on PRs

## Retrieval Pipeline

Prototype:
- read index.md, search_files, read relevant pages

MVP:
- BM25 over wiki+raw
- metadata filters by source type/date/reliability
- optional embeddings for semantic recall
- reranker before context assembly
- citation-required answer generation

Scalable:
- query planner chooses exact/BM25/vector/graph
- adaptive retrieval following Self-RAG principle: retrieve only when needed and critique evidence [raw/papers/self-rag-2023.md]
- context packer with budget, diversity, recency, confidence

## Editing Pipeline

- Propose diff, never silently overwrite.
- If contradiction: preserve both claims with dates and sources.
- If low confidence: mark confidence low/medium.
- If page exceeds size threshold: split and link.
- Every edit updates index/log and source map.

## Summarization Pipeline

- Single-source summary: page-level source summary.
- Multi-source synthesis: topic/concept page with paragraph-level provenance.
- Hierarchical summary: topic map and recursive summaries, inspired by RAPTOR. [raw/papers/raptor-2024.md]
- Guardrail: summaries are derived artifacts; raw sources and atomic facts remain canonical.

## Conflict Resolution

1. Check source reliability and date.
2. Check whether claims differ in scope or definitions.
3. Keep both if unresolved.
4. Add contested: true and conflict note.
5. Ask human for review when conflict affects architecture recommendation.

## Memory Decay / Pruning

- Archive pages superseded by later synthesis.
- Demote stale low-confidence claims after N days without corroboration.
- Keep raw sources forever unless user deletes them.
- Keep fact logs append-only, but mark facts superseded rather than deleting.
- Run periodic lint for orphans, stale claims, broken links, low-confidence single-source claims.

## Personalization Strategy

- Separate user profile, project memory, source knowledge, and procedural memory.
- Require explicit user-visible memory changes for personal facts.
- Provide ask/forget/export controls similar to OpenAI's product controls. [raw/product-docs/openai-chatgpt-memory-2024-2025.md]
- Namespaces prevent leakage across users/projects, as LangMem recommends. [raw/articles/langchain-context-engineering-2025.md]
- Add conversation/channel/project scoping for pinned memory files and memory blocks; default-deny unrelated user profiles and project files. [raw/github/letta-issue-652-per-conversation-context-scoping.md]
- Treat assistant-generated facts, recalled memories, system prompts, and tool outputs differently from direct user assertions; do not store them with equal confidence unless confirmed. [raw/github/mem0-issue-4573-memory-audit-junk.md]

# MVP Plan

## Prototype: 1-2 days

- Markdown directory with SCHEMA.md, index.md, log.md, raw/, concepts/.
- Manual ingestion of 10-20 core sources.
- Agent follows strict source map table.
- Search via ripgrep/BM25 or file search.
- No vector DB.

Complexity: low.
Risk: duplicated pages, weak provenance.

## MVP: 2-4 weeks

- Git repo with automatic commits per ingest.
- SQLite metadata index.
- BM25 search.
- Optional sqlite-vec for semantic search.
- Fact JSONL with stable IDs and source spans.
- Lint command: broken links, orphan pages, source drift, low confidence, contested pages.
- Human review workflow for page edits.
- Evaluation set: 50 representative questions; measure recall@k, citation correctness, answer faithfulness, update latency.

Complexity: medium.
Risk: citation verifier and conflict detection may be brittle.

## Scalable Architecture: 2-6 months

- Event-driven ingestion queue.
- Multi-agent research workers for source discovery and synthesis.
- Reranker and context packer.
- Graph index derived from facts/entities.
- Web UI/Obsidian plugin for review.
- Memory permissions, namespaces, deletion/export.
- Scheduled re-ingest/source drift detection.

Complexity: high.
Risk: cost, latency, synchronization conflicts, hallucinated synthesis.

# Recommended Stack

Local-first MVP:
- Storage: markdown + git + SQLite
- Search: BM25 first; Tantivy/Bleve/SQLite FTS5; add sqlite-vec or LanceDB only when needed
- Notes UI: Obsidian or VS Code
- Agent: Claude Code/Codex/OpenCode/Hermes-style tool-using agent
- Parsing: web_extract, trafilatura/readability, pymupdf/marker for PDFs
- Provenance: raw hash, source URL, quote/span IDs
- Eval: small YAML/JSON query set; manual+LLM-judge citation checks

Why not start with vector DB: vector-only failure modes are well documented for exact match and domain terms. [raw/articles/microsoft-vector-search-not-enough-2024.md]

Why not start with graph DB: graph extraction is useful later, but it adds schema and entity-resolution burden before the wiki has enough stable concepts.

# Open Problems

- How to evaluate memory quality over months, not single QA tasks.
- How to prevent low-quality summaries from becoming durable false beliefs.
- How to cite generated synthesis at paragraph or claim granularity without excessive overhead.
- How to decide what not to remember.
- How to merge conflicting agent edits safely.
- How to support privacy-preserving personal memory across local/cloud agents.
- How to make memory useful without making the agent rigid or over-personalized.

# Research Questions

1. What retrieval mix gives best recall for wiki+raw corpora: BM25, vector, hybrid, graph, or learned reranking?
2. What is the smallest provenance schema that prevents hallucinated memory hardening?
3. How often should reflection/consolidation run, and what should trigger it: time, token count, compaction, new sources, failed tasks?
4. Can source-map discipline be automated without making writing too slow?
5. When do LLM-maintained wikis outperform standard RAG on longitudinal research tasks?
6. What memory decay policies preserve usefulness while reducing clutter?
7. Which memory edits require human approval?

# Personal Developer Opportunities

Why now:
- Frontier models can reliably edit multi-file markdown, synthesize sources, and use tools.
- Embeddings and local search are cheap.
- Git/markdown/SQLite provide durable primitives.
- Users increasingly feel pain from repeating context across chats.

Already feasible for individuals:
- Personal research wiki
- Coding-agent memory repo
- Literature review assistant
- Obsidian+agent ingestion pipeline
- Team decision log with source citations
- Memory lint/audit tools

Still needs frontier models:
- High-quality contradiction detection
- Nuanced cross-source synthesis
- Robust source quality assessment
- Long-horizon autonomous research
- Human-grade writing and editing

Big opportunities:
- Memory observability: traces, why-this-was-retrieved, memory diff.
- White-box personal memory systems.
- Source-grounded research wikis for domains with high context churn.
- Evaluation harnesses for memory quality.
- Agent-native knowledge IDEs.

Likely pseudo-needs:
- Generic vector DB wrappers marketed as memory.
- Black-box personalization without review/delete/export.
- Fully autonomous memory editing for high-stakes personal/company data.
- Graph DB-first products with no clear editing workflow.

Moats:
- Accumulated private source corpus and curated wiki.
- Workflow integration and review UX.
- Provenance/evaluation harness.
- Trust, privacy, and local-first sync.

Will be swallowed by foundation models:
- Basic chat memory.
- Simple summarization.
- Generic RAG over uploaded files.
- Shallow embedding search UI.

# Source Map

| Topic | Claim | Source | Type | Reliability | Notes |
|---|---|---|---|---|---|
| LLM Wiki | Wiki is persistent compounding artifact between raw docs and chat | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f | gist | high | Author primary source; feasibility partly speculative |
| LLM Wiki | X thread had large engagement and framed gist as idea file | https://x.com/karpathy/status/2040470801506541998 | tweet | medium | Extracted via web summary; engagement numbers should be rechecked if used publicly |
| RAG | RAG helps hallucination/outdated knowledge but has retrieval/generation challenges | https://arxiv.org/abs/2312.10997 | paper | high | Survey |
| Memory architecture | Virtual context management uses OS-like memory tiers | https://arxiv.org/abs/2310.08560 | paper | high | MemGPT |
| Memory architecture | Memory stream + reflection + retrieval supports agent behavior | https://arxiv.org/abs/2304.03442 | paper | high | Generative Agents |
| Agent architecture | Agents need modular memory/action/decision framework | https://arxiv.org/abs/2309.02427 | paper | high | CoALA |
| Agent simplicity | Start simple; add complexity only when outcomes improve | https://www.anthropic.com/research/building-effective-agents | blog | high | Anthropic engineering advice |
| Research agents | Search is compression; multi-agent research costs ~15x chat tokens | https://www.anthropic.com/engineering/built-multi-agent-research-system | blog | high | Anthropic internal system; numbers context-specific |
| Context engineering | Write/select/compress/isolate context | https://www.langchain.com/blog/context-engineering-for-agents | blog | medium-high | Framework vendor; useful taxonomy |
| Harness engineering | Traces show what context enters agent step N | https://sequoiacap.com/podcast/context-engineering-our-way-to-long-horizon-agents-langchains-harrison-chase/ | interview | medium-high | Harrison Chase viewpoint |
| Embeddings | Embeddings useful but opaque/model-dependent | https://simonwillison.net/2023/Oct/23/embeddings/ | blog | high | Engineering experience |
| Retrieval | Vector search alone misses exact strings; hybrid search needed | https://techcommunity.microsoft.com/blog/azuredevcommunityblog/doing-rag-vector-search-is-not-enough/4161073 | blog | high | Microsoft concrete examples |
| Practical implementation | WUPHF uses markdown+git, BM25, SQLite, append-only facts | https://news.ycombinator.com/item?id=47899844 | hn/github discussion | medium | Need repo inspection for full verification |
| Community debate | MemGPT OS title criticized as overbroad; author clarified memory hierarchy intent | https://news.ycombinator.com/item?id=37894403 | hn | medium | Includes author comments |
| Product memory | Letta memory-first coding agent uses memory blocks/MemFS and commands | https://docs.letta.com/letta-code/memory | product-docs | high | Product behavior; marketing unverified |
| Product memory | ChatGPT memory has saved memories/chat history and controls | https://openai.com/index/memory-and-new-controls-for-chatgpt/ | product-docs | high | Product docs |
| Hierarchical retrieval | Recursive summaries improve some retrieval tasks | https://arxiv.org/abs/2401.18059 | paper | high | RAPTOR |
| Adaptive retrieval | Fixed top-k retrieval can hurt; model should decide when to retrieve/critique | https://arxiv.org/abs/2310.11511 | paper | high | Self-RAG |
| Long context | Conventional RAG assumes explicit queries/well-structured knowledge; often false | https://arxiv.org/abs/2409.05591 | paper | high | MemoRAG |
| Reddit memory practice | Relevant LocalLLaMA memory thread exists but extraction blocked | https://www.reddit.com/r/LocalLLaMA/comments/1r21ojm/weve_built_memory_into_4_different_agent_systems/ | reddit | low | insufficient evidence; do not rely yet |
| Memory failure | Production mem0 audit reports 97.8% junk memories after 32 days and 10,134 entries | https://github.com/mem0ai/mem0/issues/4573 | github issue | medium | Single case study; detailed enough to inform failure modes and mitigations |
| Memory failure | Recalled memories must be marked so extraction does not re-store them as new facts | https://github.com/mem0ai/mem0/issues/4573 | github issue | medium | Explains feedback-loop amplification; cross-links to context poisoning |
| Memory design | Agent-global memory blocks create privacy, attention, and token-cost problems across conversations | https://github.com/letta-ai/lettabot/issues/652 | github issue | medium-high | Direct design issue from LettaBot; no comments but concrete proposal |
| LLM Wiki implementation | llm-wiki-compiler implements ingest/compile/query/lint/watch/MCP/review queue and claim-level provenance | https://github.com/atomicstrata/llm-wiki-compiler | github repo | medium-high | README; independently fetched; still needs code inspection for implementation quality |
| Agent memory product | Letta Code frames persisted agent memory as different from session-based coding CLIs | https://github.com/letta-ai/letta-code | github repo | high | README/product repo; pair with docs/HN for community view |
| Team agent memory | WUPHF uses per-agent notebook + shared workspace wiki and fresh sessions to avoid accumulating context | https://github.com/nex-crm/wuphf | github repo | medium-high | README; performance claims should be reproduced before treated as general |
| Context engineering implementation | LangChain context-engineering repos implement write/select/compress/isolate and six context-fix techniques | https://github.com/langchain-ai/context_engineering | github repo | medium-high | Runnable notebooks; useful implementation reference |

# Current Corrections / Evidence Gaps

- Reddit analysis requirement is not yet satisfied. Direct extraction was blocked; only search snippets are available. Status: insufficient evidence.
- Twitter/X analysis is partial. Karpathy's X summary was extracted, but broader X high-quality discussion remains to be collected.
- GitHub issue/repo discussion is improved but still incomplete. This pass added Mem0, LettaBot, Letta Code, WUPHF, llm-wiki-compiler, and LangChain context-engineering repos/issues. Next GitHub pass should inspect code paths and additional discussions, not just READMEs/issues.
- No independent benchmark has yet shown LLM Wiki superiority over RAG on longitudinal research workflows. This remains speculative.
