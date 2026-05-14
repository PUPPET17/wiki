---
source_url: https://techcommunity.microsoft.com/blog/azuredevcommunityblog/doing-rag-vector-search-is-not-enough/4161073
ingested: 2026-05-14
sha256: 10e991f614005e8e4b042df3d340bfc60349b31e8506e6f6131e2b2c4d9a507d
---

# Doing RAG? Vector Search Is Not Enough

Source URL: https://techcommunity.microsoft.com/blog/azuredevcommunityblog/doing-rag-vector-search-is-not-enough/4161073
Author: Pamela Fox, Microsoft
Date: 2024-06-06
Type: engineering blog
Reliability: high.

Key extracted claims:
- Production RAG retrievers should support vector search, full-text search, result merging, and reranking.
- Vector search misses exact strings like prices, IDs, names, function names.
- Hybrid search plus semantic ranker performed best in Microsoft examples.
- Relevance: LLM Wiki search should start BM25+metadata and add vector rerank selectively.
