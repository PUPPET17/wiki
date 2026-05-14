---
source_url: https://simonwillison.net/2023/Oct/23/embeddings/
ingested: 2026-05-14
sha256: 9162eb09c11fc6052590830459bc7d21424ba1699adf1172df26181221b6cd11
---

# Simon Willison — Embeddings

Source URL: https://simonwillison.net/2023/Oct/23/embeddings/
Author: Simon Willison
Date: 2023-10-23
Type: engineering blog
Reliability: high for implementation experience.

Key extracted claims:
- Embeddings convert content to fixed-length vectors for semantic similarity.
- Individual vector dimensions are not human-interpretable.
- Simon used SQLite/Datasette to store embeddings and compute cosine similarity; related-article feature worked well at small scale.
- Proprietary embedding model dependency creates migration risk.
- Relevance: embeddings are useful but not sufficient as sole memory representation.
