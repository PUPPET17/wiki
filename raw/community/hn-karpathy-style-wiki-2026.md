---
source_url: https://news.ycombinator.com/item?id=47899844
ingested: 2026-05-14
sha256: 74671a36b1f99b24b70891169e5e4e3002ba096f2637a19cb438f906dfb5cf28
---

# HN: Karpathy-style LLM wiki your agents maintain

Source URL: https://news.ycombinator.com/item?id=47899844
Author: HN submitter najmuzzaman; project WUPHF
Date: 2026 (as captured)
Type: Hacker News / GitHub project discussion
Reliability: medium; direct project claims but community thread.

Engagement: 260 points, 115 comments.

Key extracted claims:
- WUPHF uses markdown+git source of truth, Bleve BM25 and SQLite indexing; no vector/graph DB yet.
- Private agent notebooks and shared team wiki.
- Draft-to-wiki promotion flow with review, provenance, expiry/archive.
- Per-entity append-only JSONL facts; synthesis worker rebuilds briefs.
- Daily lint checks contradictions, stale entries, broken wikilinks.
- Author reports benchmark: 500 artifacts, 50 queries, 85% recall@20 with BM25 alone; not universal.
- Relevance: practical validation of markdown+git+BM25 MVP pattern.
