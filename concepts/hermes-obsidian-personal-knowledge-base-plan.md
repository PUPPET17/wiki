---
title: Hermes Obsidian Personal Knowledge Base Plan
created: 2026-05-14
updated: 2026-05-14
type: concept
tags: [agent-memory, llm-wiki, obsidian, hermes, knowledge-integration, local-first, memory-architecture, retrieval, indexing, mvp, personal-ai-os]
sources: [concepts/llm-wiki-agent-memory-research-framework.md, raw/articles/karpathy-llm-wiki-gist-2026.md, raw/github/llm-wiki-compiler-repo-readme.md, raw/github/wuphf-repo-readme.md, raw/github/mem0-issue-4573-memory-audit-junk.md, raw/github/letta-issue-652-per-conversation-context-scoping.md, raw/github/langchain-context-engineering-repo-readme.md, raw/github/langchain-how-to-fix-your-context-readme.md, raw/product-docs/openai-chatgpt-memory-2024-2025.md, raw/product-docs/letta-memory-2026.md, raw/product-docs/obsidian-uri-2026.md, raw/product-docs/obsidian-bases-2026.md, raw/product-docs/obsidian-web-clipper-2026.md, raw/product-docs/obsidian-properties-2026.md, raw/product-docs/hermes-agent-memory-docs-2026.md, raw/product-docs/hermes-agent-memory-providers-docs-2026.md, raw/github/obsidian-local-rest-api-readme.md, raw/github/obsidian-mcp-server-readme.md, raw/github/obsidian-dataview-docs-overview.md]
confidence: medium
contested: true
---

# Hermes + Obsidian Personal Knowledge Base Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task after the design is accepted. Use Obsidian skill for vault file operations. Use hermes-agent skill before changing Hermes configuration, MCP, memory providers, cron, gateway, or toolsets.

**Goal:** Build a local-first personal knowledge base where Obsidian is the human-facing workspace and Hermes is the agentic research, ingestion, retrieval, synthesis, lint, and automation layer.

**Architecture:** Keep markdown + git as the canonical store. Use Obsidian for editing, review, backlinks, properties, Bases/Dataview views, and manual clipping. Use Hermes to ingest sources, maintain schema/index/log, retrieve context, produce cited syntheses, run quality gates, and optionally automate background review jobs. Derived indexes such as SQLite FTS/BM25, embeddings, graph views, and MCP/REST integrations are optional and must be rebuildable from markdown.

**Tech Stack:** Obsidian vault, markdown/YAML properties, git, Hermes file/search/session/memory/cron/MCP tools, optional Obsidian Local REST API or Obsidian MCP server, optional Dataview/Bases, optional Docsify/GitHub Pages publication, optional SQLite FTS5/BM25 and sqlite-vec later.

---

# Executive Summary

The best near-term implementation is not to replace Obsidian with Hermes memory, nor to dump every conversation into Obsidian. Treat Hermes built-in memory as small working memory and Obsidian as the durable personal knowledge substrate.

Hermes memory should keep only compact, high-value facts that reduce future steering: user preferences, stable environment conventions, and procedural lessons. Obsidian should hold the larger corpus: sources, notes, project decisions, literature, personal research, meeting summaries, and evolving syntheses. This matches the existing wiki conclusion that durable agent memory should be inspectable, editable, integrated, and operational. [concepts/llm-wiki-agent-memory-research-framework.md]

The core practice is a three-layer system:

1. Capture layer: Obsidian Web Clipper, manual notes, pasted sources, Hermes web extraction, PDFs, meeting transcripts, and session exports.
2. Knowledge layer: markdown notes with frontmatter, source maps, Obsidian links, append-only logs, and git history.
3. Agent layer: Hermes workflows for ingest, query, synthesize, lint, review, and scheduled maintenance.

Do not start with a vector DB. Start with markdown+git, Obsidian search, Hermes search_files, and optionally SQLite FTS/BM25. Add embeddings only after a small evaluation set shows lexical search misses important questions. This follows the research synthesis: vector-only retrieval fails exact strings, while local-first markdown+git provides inspectability and reviewability. [concepts/llm-wiki-agent-memory-research-framework.md]

# Design Principles

## 1. Obsidian is canonical, Hermes is an operator

Obsidian vault files are the source of truth. Hermes can create, edit, lint, and query them, but every non-trivial edit should be visible as a markdown diff and committed to git.

Why: the existing research emphasizes white-box memory, user control, auditability, and git-native review. Black-box memories become hard to inspect and can accumulate junk. [raw/github/mem0-issue-4573-memory-audit-junk.md] [raw/product-docs/openai-chatgpt-memory-2024-2025.md]

## 2. Separate memory classes

Use distinct folders and schemas for different memory types:

| Class | Purpose | Canonical location | Hermes treatment |
|---|---|---|---|
| User profile | Durable preferences and personal facts | `00-system/user-profile.md` plus Hermes USER.md for tiny subset | Ask or confirm before major changes |
| Project memory | Project conventions, decisions, status | `20-projects/<project>/` | Retrieve only when scoped to project |
| Research knowledge | Sources, claims, syntheses | `30-research/<topic>/` | Citation-required edits |
| Procedures | Reusable workflows | Hermes skills + `40-procedures/` | Promote stable procedures to skills |
| Session notes | Chat/task transcripts and summaries | `50-sessions/YYYY-MM-DD-*.md` | Summarize, do not auto-store all details |
| Raw sources | Immutable source text/captures | `90-sources/` or topic-local `raw/` | Preserve source text + metadata |
| Private/sensitive | Secrets-adjacent or personal data | `99-private/` | Default exclude from automation/indexing |

This prevents the Letta-style issue where agent-global memory files pollute unrelated conversations and create privacy/token-cost problems. [raw/github/letta-issue-652-per-conversation-context-scoping.md]

## 3. Prefer compiled wiki pages over repeated query-time reconstruction

Every useful research answer should be eligible to become a durable page, not just a chat response. This follows Karpathy's LLM Wiki pattern: raw sources -> wiki -> schema, with ingest/query/lint operations. [raw/articles/karpathy-llm-wiki-gist-2026.md]

## 4. Use provenance at claim granularity when useful

Every non-trivial claim in a concept/plan/research note should cite either a raw note or a source URL. For personal notes, cite session/date or direct user assertion where appropriate.

Minimum citation form:

```markdown
Claim text. [source-note.md]
```

For higher-value notes:

```markdown
| Claim | Source | Evidence | Confidence | Status |
|---|---|---|---|---|
```

## 5. Treat retrieved memory as context, not new evidence

When Hermes retrieves a note and later writes a summary, it must not re-store the retrieved content as if the user said it again. This directly addresses feedback-loop amplification described in the mem0 audit. [raw/github/mem0-issue-4573-memory-audit-junk.md]

# Recommended Vault Layout

Use one Obsidian vault for the personal knowledge base, ideally git-backed and local-first.

```text
Obsidian Vault/
  00-system/
    SCHEMA.md
    AGENT-RULES.md
    user-profile.md
    memory-policy.md
    review-queue.md
    dashboards/
      research.base
      projects.base
      memory-audit.base
  10-inbox/
    clips/
    notes/
    transcripts/
  20-projects/
    hermes-agent/
      index.md
      decisions/
      tasks/
      sources/
  30-research/
    agent-memory/
      index.md
      concepts/
      comparisons/
      queries/
      raw/
      log.md
  40-procedures/
    skills-candidates/
    playbooks/
  50-sessions/
    2026/
  60-people/
  70-entities/
  80-attachments/
  90-sources/
    web/
    pdf/
    github/
  99-private/
    .agentignore
```

For the current `/Users/a17/wiki`, two practical options exist:

1. Keep it as a project/research repo and open it directly as an Obsidian vault.
2. Move or mirror it into the larger Obsidian vault under `30-research/agent-memory/`.

Recommendation: keep `/Users/a17/wiki` as the research repo for this topic, and optionally add it as a separate Obsidian vault. This avoids mixing publication/Docsify files with the user's entire personal vault before the workflow stabilizes.

# Note Schemas

## Research concept note

```yaml
---
title: Human Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept
tags: [agent-memory, obsidian, hermes]
project: hermes-personal-kb
status: draft | active | archived
confidence: low | medium | high
contested: true | false
sources:
  - 90-sources/web/source-note.md
scope:
  users: [a17]
  projects: [hermes-agent]
  channels: []
review:
  last_reviewed: YYYY-MM-DD
  next_review: YYYY-MM-DD
---
```

## Raw source note

```yaml
---
title: Source Title
created: YYYY-MM-DD
source_url: https://example.com
source_type: article | paper | docs | github | conversation | clip
captured_by: obsidian-clipper | hermes-web | manual | pdf-parser
raw_preservation: full_text | tool_parsed_or_summarized_text | extraction_blocked
extraction_status: complete | partial | blocked | needs_pdf_pass
hash: sha256:...
reliability: high | medium | low
---
```

Required sections:

```markdown
# Source Title

## Source Metadata

## Parsed Source Text

## Extraction Notes
```

## Project decision note

```yaml
---
title: Decision Title
type: decision
project: hermes-agent
created: YYYY-MM-DD
status: proposed | accepted | superseded
supersedes: []
sources: []
---
```

Required sections:

```markdown
# Decision
## Context
## Options
## Decision
## Consequences
## Review Date
```

# Hermes Roles

## 1. Ingest operator

Input: URL, PDF, pasted text, GitHub issue/repo, meeting transcript, or user instruction.

Output:
- raw source note with preserved parsed text
- extracted claims/entities if useful
- updated topic index/log
- optional concept page update
- git commit

Guardrails:
- Preserve raw text before synthesis.
- Mark blocked/truncated extraction explicitly.
- Do not create many tiny pages for passing mentions.
- Search existing notes before creating new notes.

## 2. Retrieval/context operator

Input: user question or task.

Output:
- concise context pack: relevant notes, source snippets, confidence, unresolved gaps
- optional answer with citations

Retrieval order:
1. Current project/topic index
2. Exact search over filenames/tags/headings
3. Full-text/BM25 search
4. Optional semantic search
5. Raw source fallback

## 3. Synthesis editor

Input: set of sources/notes and a target note.

Output:
- proposed patch to target note
- source map update
- log update

Guardrails:
- Never silently overwrite raw sources.
- Preserve conflicts and mark contested.
- Do not turn low-confidence source snippets into high-confidence claims.

## 4. Lint/audit operator

Checks:
- broken wikilinks
- missing frontmatter
- notes without sources
- raw files without Parsed Source Text
- stale next_review dates
- orphan notes
- duplicate concepts
- uncited claims in concept notes
- private folder accidentally referenced by public pages

## 5. Reflection/consolidation operator

Runs periodically or manually. It should propose, not automatically apply, major memory changes.

Inputs:
- recent session summaries
- project logs
- inbox notes
- review queue

Outputs:
- candidate updates to user profile, project memory, or concept pages
- candidate Hermes skill updates
- rejected/no-store list for ephemeral facts

# Hermes Built-in Memory vs Obsidian

Hermes built-in memory is intentionally bounded. Hermes documentation describes two core files, MEMORY.md and USER.md, injected at session start as a frozen snapshot with small character limits. That makes it useful for compact durable steering, not a full personal knowledge base.

Use Hermes memory for:
- Stable user preferences
- Stable environment facts
- Repeated corrections
- High-value conventions
- Pointers to canonical Obsidian vault/repo paths

Do not use Hermes memory for:
- Raw source text
- Research corpora
- Large project histories
- Completed task logs
- Temporary TODOs
- Detailed meeting notes

Use Obsidian for those larger artifacts.

# Obsidian Integration Options

## Option A: Filesystem-first integration, recommended first

Hermes reads/writes markdown files directly using file tools. This is already enough for local-first workflows.

Pros:
- Simple
- No plugin dependency
- Git-friendly
- Works when Obsidian is closed

Cons:
- Does not know active Obsidian pane
- Cannot trigger Obsidian commands
- Must be careful with concurrent edits

## Option B: Obsidian URI, light automation

Obsidian URI can open notes, create notes, open daily notes, search, and choose vaults via `obsidian://...`. Useful for generating local links from Hermes output or plan docs.

Use for:
- Open a note after Hermes writes it
- Link from dashboards to local Obsidian notes
- Create daily note from external automation

Avoid relying on URI as the main write API; filesystem edits are easier to diff and test.

## Option C: Obsidian Local REST API / built-in MCP, later

The Local REST API plugin provides authenticated HTTPS access to Obsidian and can read/create/update/delete notes, patch headings/frontmatter, search metadata/content, access the active file, manage periodic notes, query tags, and open files in Obsidian. Its README also says it exposes REST API and built-in MCP server interfaces.

Use when you need:
- Active note context
- Section/frontmatter patching through Obsidian
- Tag/metadata operations through plugin APIs
- MCP clients beyond Hermes file tools

Security note: keep the API bound locally, protect the API key, and do not expose it over the network.

## Option D: Obsidian MCP server, optional

Community MCP servers can expose note read/write/search/frontmatter operations to MCP clients. Hermes has native MCP configuration support, so this can become a cleaner integration later.

Do not start here unless filesystem-first editing is insufficient.

## Option E: Dataview or Bases dashboards

Dataview is a live index/query engine over markdown metadata and can render tables/lists from frontmatter and inline fields. Obsidian Bases is a core plugin for database-like views of notes and their properties.

Use for human review dashboards:
- inbox items needing processing
- raw sources with `extraction_status != complete`
- concept notes with `contested: true`
- notes where `next_review <= today`
- project decision logs
- memory candidates awaiting approval

# Workflow Recipes

## Recipe 1: Capture a web source

1. User clips page with Obsidian Web Clipper into `10-inbox/clips/` or asks Hermes to ingest URL.
2. Hermes creates/moves a raw note with source frontmatter and `## Parsed Source Text`.
3. Hermes extracts claims/entities into a short `## Extraction Notes` section.
4. Hermes searches existing concept/project pages.
5. Hermes updates one target synthesis page or creates one if threshold is met.
6. Hermes updates index/log.
7. Hermes commits changes.

## Recipe 2: Ask Hermes a knowledge question

1. Hermes identifies active scope: user/project/topic/timeframe.
2. Hermes reads index notes and searches relevant folders.
3. Hermes assembles context pack with citations and confidence.
4. Hermes answers with source links.
5. If the answer is reusable, Hermes asks or infers whether to save it as a query/concept note.

## Recipe 3: Convert a session into durable knowledge

1. Export or summarize the session into `50-sessions/YYYY/YYYY-MM-DD-topic.md`.
2. Extract only durable facts, decisions, procedures, and open questions.
3. Reject ephemeral details and completed task logs.
4. Update project/concept notes if needed.
5. Promote stable procedures to Hermes skills when they are reusable.

## Recipe 4: Weekly memory audit

1. Find notes changed in the last 7 days.
2. Find memory candidates and user-profile changes.
3. Check for unprocessed inbox items.
4. Check raw sources with partial/blocked extraction.
5. Check contested or low-confidence notes.
6. Produce a review report and optional patch set.

# Retrieval Strategy

## Phase 1: lexical only

Use:
- Obsidian built-in search
- Hermes `search_files`
- git grep/ripgrep via safe wrappers where needed
- indexes/index.md files
- tags and frontmatter

This is enough for the first few hundred notes if filenames, tags, and indexes are disciplined.

## Phase 2: SQLite FTS/BM25

Add a small derived index:

```text
.hermes-kb/index.sqlite
  notes(path, title, type, tags, updated, hash)
  sources(path, source_url, reliability, extraction_status)
  links(src, dst)
  fts_notes(path, title, headings, body)
```

The index is derived and can be rebuilt from markdown.

## Phase 3: hybrid semantic retrieval

Add embeddings only after evaluation shows need. Store vectors outside markdown, keyed by file hash and heading/block IDs.

Use semantic retrieval for:
- fuzzy conceptual recall
- paraphrased questions
- cross-topic discovery

Use exact/BM25 for:
- names
- file paths
- commands
- dates
- IDs
- quotes
- prices/numbers

# Evaluation Plan

Create `00-system/evals/personal-kb-queries.yml` with 30-50 representative questions:

```yaml
- id: q001
  question: What is the recommended Hermes memory vs Obsidian split?
  expected_sources:
    - 30-research/agent-memory/concepts/hermes-obsidian-personal-knowledge-base-plan.md
  must_include:
    - Hermes memory is bounded
    - Obsidian stores larger corpus
```

Measure:
- retrieval recall@k
- citation correctness
- answer faithfulness
- stale/conflicting answer rate
- time to update knowledge after new evidence
- number of rejected junk memories

# Privacy and Safety Model

Default-deny automation for sensitive folders.

Recommended `.agentignore` semantics:

```text
99-private/**
**/.obsidian/workspace*.json
**/.trash/**
**/*secret*
**/*password*
```

Rules:
- Hermes may search private folders only when explicitly instructed.
- No secrets/API keys in Obsidian notes unless encrypted or intentionally stored in a password manager note excluded from automation.
- Personal facts require higher scrutiny than source facts.
- Memory edits about the user should be visible and reversible.
- Publication workflows must exclude private folders and session notes unless explicitly allowed.

# Implementation Plan

## Phase 0: Decide vault topology

**Objective:** Choose whether `/Users/a17/wiki` remains a standalone Obsidian vault or becomes a subfolder of a larger personal vault.

**Files:**
- Review: `/Users/a17/wiki/SCHEMA.md`
- Create later if standalone: `/Users/a17/wiki/.obsidian/` through Obsidian UI, not Hermes

**Recommendation:** Use `/Users/a17/wiki` as a standalone Obsidian vault for the agent-memory research topic. Later create a separate private personal vault and link/mirror selected research pages.

**Verification:** Open `/Users/a17/wiki` in Obsidian as a vault and confirm links render.

## Phase 1: Add agent operating rules

**Objective:** Make the vault self-describing for Hermes and future agents.

**Files:**
- Create: `AGENTS.md`
- Create: `memory-policy.md` or `00-system/memory-policy.md` if adopting larger layout

**AGENTS.md draft:**

```markdown
# Agent Rules for this Obsidian Wiki

- Preserve raw source text before synthesis.
- Search existing pages before creating new pages.
- Update index.md and log.md for every knowledge change.
- Cite raw sources for non-trivial claims.
- Do not edit raw sources except to fix preservation/extraction metadata.
- Use git status before and after edits.
- Commit and push completed changes when remote is available.
- Do not read or modify private folders unless explicitly instructed.
```

**Verification:** Ask Hermes to explain the vault rules in a new session; it should load AGENTS.md automatically when workdir is the repo.

## Phase 2: Add Obsidian-facing dashboards

**Objective:** Make review queues visible to the human in Obsidian.

**Files:**
- Create: `dashboards/research-review.md`
- Create optional: `dashboards/sources-needing-review.md`

**Dataview example:**

```markdown
# Research Review

```dataview
TABLE type, confidence, contested, updated
FROM "concepts"
WHERE contested = true OR confidence = "low"
SORT updated DESC
```
```

**Bases alternative:** create a Base filtered by `type`, `confidence`, `contested`, `updated`, and `extraction_status`.

**Verification:** Open dashboard in Obsidian and confirm table/base lists notes.

## Phase 3: Add source ingestion command convention

**Objective:** Define a repeatable Hermes prompt/procedure for ingestion.

**Files:**
- Create: `40-procedures/ingest-source.md` or `procedures/ingest-source.md`

**Procedure:**

```markdown
# Ingest Source Procedure

Input: URL/PDF/text and target topic.
1. Capture raw source markdown under raw/<type>/.
2. Add source metadata and hash when possible.
3. Preserve parsed source text.
4. Extract claims/entities with confidence.
5. Search existing concept pages.
6. Patch the most relevant page or create a new one only if threshold is met.
7. Update index.md and log.md.
8. Commit with docs: ingest <source/topic>.
```

**Verification:** Run the procedure on one new source and inspect git diff.

## Phase 4: Add lint script

**Objective:** Catch structural drift before the vault becomes unreliable.

**Files:**
- Create: `scripts/wiki_lint.py`
- Modify: `.github/workflows/wiki-maintenance.yml` to call the script instead of inline Python

**Checks:**
- frontmatter required keys
- raw files include Parsed Source Text
- broken markdown links
- duplicated source_url
- missing log update for changed concept/raw files
- private folder excluded from docsify/publication

**Verification:** Run `python3 scripts/wiki_lint.py`; expected PASS.

## Phase 5: Add session-to-note workflow

**Objective:** Preserve useful Hermes sessions without polluting durable memory.

**Files:**
- Create: `procedures/session-to-note.md`
- Create folder: `sessions/` or `50-sessions/`

**Policy:**
- Store concise session summary, not raw transcript by default.
- Extract durable decisions/open questions/procedures.
- Do not store temporary command outputs unless needed for reproducibility.
- Promote reusable workflows to Hermes skills, not just Obsidian notes.

**Verification:** Convert one prior wiki session into a note and ensure no secrets/transient logs are included.

## Phase 6: Optional MCP/REST integration

**Objective:** Integrate Hermes with Obsidian's active file and plugin APIs only after filesystem-first workflows are stable.

**Steps:**
1. Install Obsidian Local REST API plugin.
2. Keep API local and store token in Hermes `.env`, not in notes.
3. Configure Hermes MCP if using an Obsidian MCP server:

```bash
hermes mcp add obsidian --command "npx -y obsidian-mcp-server"
hermes mcp test obsidian
hermes mcp configure obsidian
```

Exact command depends on selected MCP package; verify current package docs before running.

**Verification:** Use MCP/REST to read the active note and patch a test heading in a scratch note.

## Phase 7: Optional retrieval index

**Objective:** Improve recall once notes exceed what index.md + search_files handles well.

**Files:**
- Create: `scripts/build_index.py`
- Create derived: `.hermes-kb/index.sqlite`
- Add `.hermes-kb/` to `.gitignore` unless intentionally sharing index

**Verification:** Run benchmark queries and compare recall before/after.

# Acceptance Criteria

A working Hermes + Obsidian personal knowledge base should satisfy:

- Obsidian can browse/edit all notes normally.
- Hermes can ingest a new source with raw preservation, citation, index/log update, and git commit.
- Hermes can answer a research question with cited notes.
- Hermes can distinguish user profile, project memory, raw sources, and session notes.
- A dashboard shows notes needing review.
- A lint command catches missing frontmatter, missing Parsed Source Text, and broken links.
- Sensitive/private folders are excluded from automation and publication by default.
- The system has a documented retrieval/evaluation plan before adding embeddings.

# Open Questions

1. Should the user's main personal Obsidian vault be separate from public/publishable research vaults?
2. Should Hermes write directly to Obsidian via filesystem only, or should it use Local REST API for active-file awareness?
3. Which notes should be eligible for GitHub Pages / Docsify publication?
4. What is the minimum review UI: Obsidian Dataview/Bases, GitHub PRs, or both?
5. How should Hermes session summaries be exported: manual `/save`, session_search summaries, or scheduled cron jobs?
6. Should a future Hermes memory provider use Obsidian as a backend, or should Obsidian remain a separate canonical KB with retrieval tools?

# Source Map

| Claim | Source | Type | Reliability | Notes |
|---|---|---|---|---|
| Durable agent memory should be inspectable, editable, integrated, and operational | concepts/llm-wiki-agent-memory-research-framework.md | synthesis | medium | Existing wiki synthesis |
| Karpathy pattern separates raw sources, wiki, and schema with ingest/query/lint operations | raw/articles/karpathy-llm-wiki-gist-2026.md | primary/source | high | Conceptual seed |
| Markdown+git is an emerging canonical memory pattern | raw/github/wuphf-repo-readme.md; raw/github/llm-wiki-compiler-repo-readme.md | github/readme | medium-high | Implementation evidence, not universal benchmark |
| Context engineering maps to write/select/compress/isolate | raw/github/langchain-context-engineering-repo-readme.md; raw/github/langchain-how-to-fix-your-context-readme.md | github/readme | medium-high | Practical implementation references |
| Indiscriminate memory storage can create junk and feedback loops | raw/github/mem0-issue-4573-memory-audit-junk.md | github issue | medium | Single detailed production case study |
| Agent-global memory needs conversation/project scoping | raw/github/letta-issue-652-per-conversation-context-scoping.md | github issue | medium-high | Concrete design issue |
| Hermes built-in memory is bounded and best for compact durable steering | Hermes memory docs fetched 2026-05-14 | product docs | high | MEMORY.md/USER.md small prompt-injected stores |
| Obsidian Web Clipper saves web content locally to markdown files | Obsidian Web Clipper docs/README fetched 2026-05-14 | product docs/github | high | Useful capture layer |
| Obsidian Properties and Bases support structured metadata/database-like views over markdown | Obsidian Help fetched 2026-05-14 | product docs | high | Useful review dashboards |
| Dataview indexes markdown metadata and queries notes | Dataview docs fetched 2026-05-14 | plugin docs | medium-high | Community plugin, mature but not core |
| Obsidian Local REST API can expose read/write/search/patch/active-file operations and MCP | Local REST API README fetched 2026-05-14 | plugin docs/github | medium-high | Optional integration |

# Current Corrections / Evidence Gaps

- Obsidian official help is delivered through Obsidian Publish and was fetched via preloaded markdown URLs. Content should be rechecked if implementing exact plugin settings.
- The plan has not yet inspected the user's actual Obsidian vault path or installed plugins.
- MCP package commands vary by selected Obsidian MCP server; verify package docs before configuring Hermes MCP.
- No retrieval benchmark has been run on the user's real notes yet.
