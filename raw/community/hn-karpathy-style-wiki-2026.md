---
source_url: https://news.ycombinator.com/item?id=47899844
fetched_url: https://news.ycombinator.com/item?id=47899844
source_type: hn
author: HN / WUPHF submitter
source_date: 2026
ingested: 2026-05-14
sha256: d367bcb97213dc9bacf3980f41f93fa2fd084d3521e39d9dc7e85035ad605625
raw_preservation: tool_parsed_or_summarized_text
---

# Hn Karpathy Style Wiki 2026

## Source Metadata

- Source URL: https://news.ycombinator.com/item?id=47899844
- Fetched URL: https://news.ycombinator.com/item?id=47899844
- Source type: hn
- Author: HN / WUPHF submitter
- Source date: 2026
- Ingested: 2026-05-14
- Reliability: medium
- Raw preservation status: tool_parsed_or_summarized_text
- Extraction note: Parsed source text is preserved below where accessible. If extraction tooling returned a summary/truncated representation, this is explicitly marked and should be replaced by fuller text in a later pass.

## Parsed Source Text

# Hacker News Summary: **Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and Git)**

**Source:** Hacker News item [47899844](https://news.ycombinator.com/item?id=47899844)  
**Project:** [github.com/nex-crm/wuphf](https://github.com/nex-crm/wuphf)  
**Score / discussion:** 260 points, 115 comments

---

## Key excerpts

> I shipped a wiki layer for AI agents that uses markdown + git as the source of truth, with a bleve (BM25) + SQLite index on top. No vector or graph db yet.

> It runs locally in `~/.wuphf/wiki/` and you can git clone it out if you want to take your knowledge with you.

> The shape is the one Karpathy has been circling for a while: an LLM-native knowledge substrate that agents both read from and write into, so context compounds across sessions rather than getting re-pasted every morning.

> What it does:
> - Each agent gets a private notebook at `agents/{slug}/notebook/.md`, plus access to a shared team wiki at `team/.`
> - Draft-to-wiki promotion flow.
> - Per-entity fact log: append-only JSONL at `team/entities/{kind}-{slug}.facts.jsonl`.
> - `[[Wikilinks]]` with broken-link detection rendered in red.
> - Daily lint cron for contradictions, stale entries, and broken wikilinks.
> - `/lookup` slash command plus an MCP tool for cited retrieval.

> Markdown for durability. The wiki outlives the runtime, and a user can walk away with every byte.

> The current benchmark (500 artifacts, 50 queries) clears **85% recall@20** on BM25 alone, which is the internal ship gate.

> Known limits:
> - Recall tuning is ongoing. 85% on the benchmark is not a universal guarantee.
> - Synthesis quality is bounded by agent observation quality. Garbage facts in, garbage briefs out.
> - Single-office scope today. No cross-office federation.

> Demo. 5-minute terminal walkthrough that records five facts, fires synthesis, shells out to the user's LLM CLI, and commits the result under Pam's identity:  
> https://asciinema.org/a/vUvjJsB5vtUQQ4Eb

> Install: `npx wuphf@latest`

> The wiki ships as part of WUPHF, an open source collaborative office for AI agents like Claude Code, Codex, OpenClaw, and local LLMs via OpenCode. MIT, self-hosted, bring-your-own keys.

---

## Main project summary

The post introduces **WUPHF**, an open-source, self-hosted collaboration system for AI agents, with the wiki as one component. The wiki is designed as an **LLM-native knowledge base** built on:

- **Markdown**
- **Git**
- **Bleve / BM25 search**
- **SQLite metadata**

The author explicitly avoids heavier infrastructure for now:

- **No vector DB**
- **No graph DB**
- **No Postgres / Kafka / dashboard stack**

The design goal is durability and portability: the wiki lives in a local directory, can be cloned, and remains readable outside the runtime.

---

## How it works

### Core structure
- **Private agent notebooks** at `agents/{slug}/notebook/.md`
- **Shared team wiki** at `team/`
- **Promotion flow** from draft notebook entries into canonical wiki pages
- **Append-only entity fact logs** in JSONL:
  - `team/entities/{kind}-{slug}.facts.jsonl`
- A synthesis worker rebuilds entity briefs every N facts
- Git commits are attributed to a distinct identity: **“Pam the Archivist”**

### Retrieval and indexing
- **Bleve** for BM25 full-text search
- **SQLite** for structured metadata:
  - facts
  - entities
  - edges
  - redirects
  - supersedes
- `/lookup` command plus **MCP tool** for cited retrieval
- A heuristic classifier routes:
  - short lookups → **BM25**
  - narrative queries → **cited-answer loop**

### Integrity features
- `[[Wikilinks]]`
- Broken links shown in red
- Daily lint cron checks:
  - contradictions
  - stale entries
  - broken links
- Canonical IDs are stable and deterministic
- Redirect stubs preserve renamed entities
- Rebuilds are “logically identical, not byte-identical”

---

## Design rationale

The author argues that **markdown + git** are enough to create a durable knowledge substrate before adding heavier systems.

### Why markdown?
- Durable
- Human-readable
- Portable
- Long-lived beyond the runtime
- Easy to carry away or self-host

### Why BM25 first?
- The current benchmark is acceptable enough to ship
- BM25 alone achieves **85% recall@20** on the internal benchmark
- A more expensive fallback exists if needed:
  - `sqlite-vec`

### Why deterministic canonical IDs?
- Avoid rename drift
- Preserve identity across rebuilds
- Support stable redirects and provenance

---

## Known limitations

The author is explicit about current constraints:

- **Recall tuning is ongoing**
- Benchmark results are not universal guarantees
- Output quality depends on input quality:
  - “Garbage facts in, garbage briefs out.”
- The lint pass helps, but does **not** act as a judgment engine
- The system is currently limited to a **single office**
- No cross-office federation yet

---

## Context: WUPHF

The wiki is part of **WUPHF**, described as:

- an open-source collaborative office for AI agents
- 

[... summary truncated for context management ...]
