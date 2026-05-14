---
source_url: https://simonwillison.net/2023/Oct/23/embeddings/
fetched_url: https://simonwillison.net/2023/Oct/23/embeddings/
source_type: blog
author: Simon Willison
source_date: 2023-10-23
ingested: 2026-05-14
sha256: 3ecb398ff085a095f913cf1b2a4bbeecb6ffa4c437c28ac012f40bdaa35b8d75
raw_preservation: tool_parsed_or_summarized_text
---

# Simon Willison Embeddings 2023

## Source Metadata

- Source URL: https://simonwillison.net/2023/Oct/23/embeddings/
- Fetched URL: https://simonwillison.net/2023/Oct/23/embeddings/
- Source type: blog
- Author: Simon Willison
- Source date: 2023-10-23
- Ingested: 2026-05-14
- Reliability: high
- Raw preservation status: tool_parsed_or_summarized_text
- Extraction note: Parsed source text is preserved below where accessible. If extraction tooling returned a summary/truncated representation, this is explicitly marked and should be replaced by fuller text in a later pass.

## Parsed Source Text

# Embeddings: What they are and why they matter — Simon Willison

**Source:** <https://simonwillison.net/2023/Oct/23/embeddings/>  
**Author:** Simon Willison  
**Posted:** 23 October 2023  
**Context:** Expanded article version of Simon’s PyBay 2023 talk on embeddings, with practical demos using SQLite, Datasette, OpenAI, local embedding models, CLIP, RAG, and his `llm` tooling.

---

## Core idea

Embeddings convert content into a **fixed-length array of floating-point numbers**. That array represents a point in a high-dimensional vector space.

> Embeddings are based around one trick: take a piece of content—in this case a blog entry—and turn that piece of content into an array of floating point numbers.

Important properties:

- The vector length is fixed by the model:
  - e.g. **300**, **1,000**, **1,536**, **512** dimensions.
- Content of any length can be mapped to the same-size vector.
- Nearby vectors tend to represent semantically similar content.
- Individual numbers are not directly interpretable.

> Nobody fully understands what those individual numbers mean, but we know that their locations can be used to find out useful things about the content.

A useful mental model: embeddings are **coordinates in a strange multi-dimensional semantic space**.

---

## Why embeddings matter

Embeddings enable:

- Related-content recommendations
- Semantic search / “vibes-based search”
- Code search
- Image search
- Multimodal search across text and images
- Clustering
- Classification-like scoring
- 2D/3D visualization of semantic spaces
- Retrieval-Augmented Generation, or **RAG**

Simon emphasizes embeddings as a practical “toolbox” technology: once content can be embedded, it can be stored, compared, searched, clustered, and combined with other systems.

---

# Related content using embeddings

Simon’s first major use case was a **related articles** feature for his TIL site.

## Setup

- Site: <https://til.simonwillison.net/>
- Model used: OpenAI `text-embedding-ada-002`
- Number of articles: **472**
- Embedding size: **1,536 dimensions**
- Storage: SQLite database
- Comparison: cosine similarity
- Goal: show related articles at the bottom of each page

For a given article:

1. Calculate its embedding.
2. Compare it to every other article embedding.
3. Sort by cosine similarity.
4. Return the closest matches.

Example top related articles for a geospatial SQLite article:

- Geopoly in SQLite
- Viewing GeoPackage data with SpatiaLite and Datasette
- Using SQL with GDAL
- KNN queries with SpatiaLite
- GUnion to combine geometries in SpatiaLite

## Cosine similarity function

```python
def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))
    magnitude_a = sum(x * x for x in a) ** 0.5
    magnitude_b = sum(x * x for x in b) ** 0.5
    return dot_product / (magnitude_a * magnitude_b)
```

## SQLite storage and inspection

Embeddings are stored as binary values in SQLite.

View as hexadecimal:

```sql
select id, hex(embedding) from embeddings
```

Decode into JSON arrays using a custom SQL function:

```sql
select id, llm_embed_decode(embedding) from embeddings limit 10
```

## Similarity query in SQLite

Using the `llm_embed_cosine(vector1, vector2)` SQL function from Simon’s `datasette-llm-embed` plugin:

```sql
select
  id,
  llm_embed_cosine(
    embedding,
    (
      select
        embedding
      from
        embeddings
      where
        id = 'sqlite_sqlite-tg.md'
    )
  ) as score
from
  embeddings
order by
  score desc
limit 5
```

Example results:

| id | score |
| --- | --- |
| sqlite_sqlite-tg.md | 1.0 |
| sqlite_geopoly.md | 0.8817322855676049 |
| spatialite_viewing-geopackage-data-with-spatialite-and-datasette.md | 0.8813094978399854 |
| gis_gdal-sql.md | 0.8799581261326747 |
| spatialite_knn.md | 0.8692992294266506 |

The article itself scores **1.0**, as expected.

## Performance and precomputation

- Querying all embeddings took around **400ms**.
- Simon precomputes the top 10 similarities for every article.
- Results are stored in a separate `similarities` table with:
  - `id`
  - `other_id`
  - `score`

## Cost of OpenAI embeddings

For Simon’s TIL site:

- Embedded around **402,500 tokens**
- Price: **$0.0001 / 1,000 tokens**
- Total cost: **$0.04**

> It’s really easy to use: you POST it some text along with your API key, it gives you back that JSON array of floating point numbers.

## Caution: proprietary model dependency

OpenAI deprecated older embedding models, forcing users to potentially re-embed content.

Simon notes OpenAI promised to:

> “cover the financial cost of users re-embedding content with these new models.”

But he still warns this is a reason to be cautious about relying on proprietary models.

Openly licensed local models avoid shutdown/deprecation risk.

---

# Word2Vec: how embeddings became influential

Google Research’s **Word2Vec** was an early influential embedding model.

- Paper: *Efficient Estimation of Word Representations in Vect

[... summary truncated for context management ...]
