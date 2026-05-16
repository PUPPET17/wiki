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

## [2026-05-14] plan | Hermes + Obsidian personal knowledge base
- Continued research on Obsidian integration options: Obsidian URI, Web Clipper, Properties/Bases, Dataview, Local REST API, MCP-style integrations, and Hermes memory docs.
- Added 9 raw source files for Obsidian/Hermes integration evidence under raw/product-docs and raw/github.
- Created concepts/hermes-obsidian-personal-knowledge-base-plan.md.
- Plan recommendation: keep markdown+git as canonical memory, use Obsidian as the human review/editing workspace, and use Hermes as ingestion/retrieval/synthesis/lint automation. Keep Hermes built-in memory bounded to compact steering facts; store larger personal/research/project knowledge in Obsidian.

## [2026-05-16] refine | Hermes + Obsidian KB truth boundaries
- Expanded concepts/hermes-obsidian-personal-knowledge-base-plan.md with a single-source-of-truth model: immutable raw sources as evidence, mutable wiki notes as synthesis, append-only logs, bounded Hermes memory as steering cache, and derived indexes as rebuildable non-canonical artifacts.
- Strengthened raw source rules: raw resources must be original text/artifact records or exact local storage paths that an agent can locate and read; summaries cannot replace raw evidence.
- Added strict global and per-note schemas for raw_source, concept, decision, session_summary, and procedure notes.
- Added automation/permission boundaries, folder policies, human-confirmation triggers, and MVP ingest/truth-lookup/session-to-knowledge loops.

## [2026-05-14] upgrade | Raw source full-text pass
- Upgraded 7 arXiv paper raw sources to `raw_preservation: full_pdf_text` using arXiv PDFs + PyMuPDF page text extraction: MemGPT, Generative Agents, CoALA, RAG Survey, RAPTOR, Self-RAG, MemoRAG.
- Upgraded 8 web/blog/product sources to `raw_preservation: full_html_article_text_candidate` using readability-lxml + html2text. These are candidate full article text because site-rendered dynamic content may still omit hidden sections.
- Upgraded 3 Hacker News discussions to full comment-tree text: HN Karpathy-style wiki via Algolia API (115 comments), HN MemGPT via Firebase API (106 comments), HN Letta Code via Firebase API (37 comments).
- Remaining gap: Reddit LocalLLaMA memory thread remains `extraction_blocked`; full thread still needs browser/API/archive/manual export.

## [2026-05-14] update | Git synchronization requirement
- User requested that future changes be synchronized through the git repository.
- Updated SCHEMA.md to require checking git status, staging relevant files, committing with a clear message, and pushing when a remote is configured/available.

## [2026-05-15] ingest | GitHub issue/repo evidence for agent memory systems
- Added raw GitHub sources under raw/github/:
  - mem0 issue #4573 production memory audit: 10,134 entries, reported 97.8% junk, feedback-loop amplification, quality-gate recommendations.
  - LettaBot issue #652: per-conversation context scoping for MemFS/memory blocks.
  - README snapshots for mem0, Letta Code, WUPHF, llm-wiki-compiler, LangChain context_engineering, and LangChain how_to_fix_your_context.
- Updated concepts/llm-wiki-agent-memory-research-framework.md with new GitHub-backed evidence on memory failure modes, context scoping, existing projects, ingestion quality gates, and Source Map rows.
- Updated index.md summary.
