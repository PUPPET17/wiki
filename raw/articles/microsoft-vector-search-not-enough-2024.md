---
source_url: https://techcommunity.microsoft.com/blog/azuredevcommunityblog/doing-rag-vector-search-is-not-enough/4161073
fetched_url: https://techcommunity.microsoft.com/blog/azuredevcommunityblog/doing-rag-vector-search-is-not-enough/4161073
source_type: blog
author: Pamela Fox / Microsoft
source_date: 2024-06-06
ingested: 2026-05-14
sha256: 5fb137e54b765bf1d6d8eb0866e599d5ca0018a35e20761f6958962f3f809568
raw_preservation: tool_parsed_or_summarized_text
---

# Microsoft Vector Search Not Enough 2024

## Source Metadata

- Source URL: https://techcommunity.microsoft.com/blog/azuredevcommunityblog/doing-rag-vector-search-is-not-enough/4161073
- Fetched URL: https://techcommunity.microsoft.com/blog/azuredevcommunityblog/doing-rag-vector-search-is-not-enough/4161073
- Source type: blog
- Author: Pamela Fox / Microsoft
- Source date: 2024-06-06
- Ingested: 2026-05-14
- Reliability: high
- Raw preservation status: tool_parsed_or_summarized_text
- Extraction note: Parsed source text is preserved below where accessible. If extraction tooling returned a summary/truncated representation, this is explicitly marked and should be replaced by fuller text in a later pass.

## Parsed Source Text

# Doing RAG? Vector search is *not* enough — Markdown Summary

**Source:** Microsoft Developer Community Blog  
**Author:** Pamela Fox (Microsoft)  
**Published:** Jun 06, 2024  
**Read time:** 9 min  
**Main thesis:** For RAG retrieval, **vector search alone is insufficient**. A robust retriever should use **full hybrid search**: vector search + full-text search + result merging + semantic re-ranking.

---

## Core Argument

> “Yes, your retriever for a RAG flow should definitely support vector search, since that will let you find documents with similar semantics to a user's query, but vector search is not enough.”

The author argues that RAG systems need more than semantic similarity. They must also handle **exact-match retrieval** for things like:

- Proper names
- IDs
- Numbers
- Prices
- Function names
- Domain-specific terminology

A proper retriever should support **full hybrid search**, meaning it can:

1. Perform vector search
2. Perform full-text search
3. Merge results
4. Re-rank results against the original query

This allows RAG systems to retrieve both:

- Semantically similar concepts
- Exact textual matches

---

## Full Hybrid Search: Four Steps

Azure AI Search provides a full hybrid search stack:

1. **Vector search**  
   Uses a distance metric, typically **cosine similarity** or **dot product**.

2. **Full-text search**  
   Uses the **BM25 scoring algorithm**.

3. **Result merging**  
   Uses **Reciprocal Rank Fusion (RRF)**.

4. **Semantic re-ranking**  
   Uses a Bing-derived machine learning model that compares each result to the original user query and assigns a score from **0–4**.

> “Unsurprisingly, they found that the best results came from using the full stack…”

This full-stack approach is the default configuration in Microsoft’s **AI Search RAG starter app**.

---

## Why Hybrid Search Is Needed

The article demonstrates hybrid search using sample documents from the **AI Search RAG starter app**, which contains fictional company internal policy documents such as healthcare and benefits information.

### Example: Exact Price Query

Query:

```python
search_query = "what plan costs $45.00"
search_vector = get_embedding(search_query)
r = search_client.search(None, top=3, vector_queries=[
  VectorizedQuery(search_vector, k_nearest_neighbors=50, fields="embedding")])
```

With **pure vector search**, the results contained related costs, such as:

> “The copayment for primary care visits is typically around $20, while specialist visits have a copayment of around $50.”

But none of the results contained the exact value **$45.00**.

### Full-text Search Handles Exact Matches

```python
r = search_client.search(search_query, top=3)
```

With **pure full-text search**, the top result contained a table of health insurance plan costs with a row containing **$45.00**.

### Hybrid Search Gets the Best of Both

```python
r = search_client.search(search_query, top=15, vector_queries=[
  VectorizedQuery(search_vector, k_nearest_neighbors=10, fields="embedding")])
```

With **hybrid search**, the top result was again the table containing the exact string **$45.00**.

### Key Insight

> “Users *will* make queries that are better answered by full-text search, and that's why we need hybrid search solutions.”

Common exact-search behaviors include:

- Searching email for a person’s name
- Searching code docs for a function name
- Searching records for an ID
- Searching policy documents for prices or numeric values

---

## Another Reason Vector Search Alone Falls Short

Generic embedding models, such as OpenAI embedding models, are usually **not perfectly aligned to your domain**.

> “Their understanding of certain terms aren't going to be the same as a model that was trained entirely on your domain's data.”

Hybrid search helps compensate for domain mismatch by combining semantic search with lexical/full-text matching.

---

## Why Re-ranking Is Needed

Hybrid search is important, but the author also emphasizes the importance of the final **semantic re-ranking** step.

### Example: “Underwater Activities”

Hybrid search query:

```python
search_query = "learning about underwater activities"
search_vector = get_embedding(search_query)
r = search_client.search(search_query, top=5, vector_queries=[
  VectorizedQuery(search_vector, k_nearest_neighbors=10, fields="embedding")])
```

The most relevant result appeared as the **third result**. It was a benefits document mentioning:

- Surfing lessons
- Scuba diving lessons

Notably, the word **“underwater”** did not appear in the documents, so this result came from the vector search component.

### Adding Semantic Ranker

```python
search_query = "learning about underwater activities"
search_vector = get_embedding(search_query)
r = search_client.search(search_query, top=5, vector_queries=[
  VectorizedQuery(search_vector, k_nearest_neighbors=50, fields="embedding")],
  query_type="semantic", semantic_configuration_name="default")
```

With semantic ranki

[... summary truncated for context management ...]
