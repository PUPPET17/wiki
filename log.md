# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`

## [2026-05-14] create | Wiki initialized
- Domain: LLM Wiki / Agent Memory / Context Compression / Knowledge Integration.
- Created SCHEMA.md, index.md, log.md, raw/, entities/, concepts/, comparisons/, queries/.

## [2026-05-14] ingest | Initial LLM Wiki / Agent Memory source batch
- Created 20 raw source files under raw/articles, raw/papers, raw/community, raw/product-docs.
- Created concepts/llm-wiki-agent-memory-research-framework.md.
- Sources include Karpathy gist, MemGPT, Generative Agents, CoALA, RAG survey, Anthropic agent posts, LangChain context engineering, Simon Willison embeddings, Microsoft hybrid search, HN discussions, OpenAI/Letta memory docs, RAPTOR, Self-RAG, MemoRAG.
- Reddit extraction blocked; marked low reliability / insufficient evidence.

## [2026-05-14] correction | Raw source preservation policy
- User corrected ingestion policy: raw sources should preserve parsed original/source text, not just source_url and key extracted claims.
- Updated SCHEMA.md to require parsed original/source text whenever accessible, with explicit raw_preservation / extraction_status marking when blocked, truncated, or summarized.
- Rewrote existing raw source files to include `## Parsed Source Text` sections from fetched/extracted markdown where accessible.
- Important caveat: web_extract often returns capped/summarized markdown for long sources; these files are now marked `tool_parsed_or_summarized_text` where appropriate and should be upgraded with full PDF/API/browser extraction in later passes.
