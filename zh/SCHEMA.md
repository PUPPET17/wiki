# Wiki Schema / 维护规范

## Domain

LLM Wiki / Agent Memory / Context Compression / Knowledge Integration research and implementation framework.

## 中文国际化约定

- 英文文档保留在站点根目录，作为 canonical English content。
- 中文文档放在 `/zh/` 下，作为新增 locale 内容。
- 中文页面可以是翻译、摘要或中文维护入口；不得为了国际化而改写英文原文。
- 新增中文页面时，应保持与英文页面相同的相对路径，便于 VitePress locale 切换。

## 核心维护原则

- File names: lowercase, hyphens, no spaces.
- Raw sources are immutable evidence; corrections go into wiki pages.
- Raw sources must preserve parsed original/source text whenever accessible.
- Every update must append to `log.md`.
- Every completed file change should be committed locally; push only when explicitly requested.
- Non-trivial claims should cite source-backed notes or raw sources.
- Distinguish fact, inference, speculation, and community view.

## Tag Taxonomy

- topic: llm-wiki, agent-memory, rag, context-engineering, knowledge-integration, personal-ai-os
- architecture: memory-architecture, retrieval, compression, indexing, graph-memory, vector-memory, symbolic-memory
- evidence: paper, blog, github, hn, reddit, tweet, product-docs
- implementation: prototype, mvp, scalable-architecture, local-first, cloud-first
- analysis: tradeoff, failure-case, opportunity, debate

## Update Policy

When new evidence conflicts with existing content:

1. Keep the old view under a dated correction note.
2. Add the new evidence with source and date.
3. Mark contested: true if unresolved.
4. Update Source Map notes.
