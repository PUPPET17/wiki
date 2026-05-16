---
title: Hermes Obsidian Personal Knowledge Base Plan
created: 2026-05-14
updated: 2026-05-16
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

# Single Source of Truth Boundary

The knowledge base is meant to let an agent quickly enter the vault, locate evidence, and answer "what is true here?" without guessing. Therefore the system must distinguish canonical source documents, agent-authored knowledge, and rebuildable indexes.

## Canonical layers

| Layer | Canonical? | Mutable? | Purpose | Examples |
|---|---:|---:|---|---|
| Raw sources | Yes | No, except metadata correction | Evidence substrate. Every non-trivial claim must be traceable here. | Original article markdown, PDF file, screenshot, image, transcript, GitHub issue export, or a note pointing to an exact local storage path. |
| Wiki notes | Yes, but derived from raw sources | Yes, reviewed edits | Agent/human-authored concepts, decisions, comparisons, queries, syntheses. | `concepts/*.md`, `comparisons/*.md`, `queries/*.md`, project decision notes. |
| Logs | Yes | Append-only | Chronology of knowledge-base actions and source changes. | `log.md`, project logs, ingestion logs. |
| User/project profile notes | Yes within their scope | Yes, stricter review | Durable user/project facts, preferences, conventions. | `00-system/user-profile.md`, `20-projects/*/project-memory.md`. |
| Hermes built-in memory | No for corpus truth | Yes, tiny steering cache | Compact pointer/steering memory only. | Vault path, stable preferences, repeated corrections. |
| Derived indexes | No | Rebuild-only | Retrieval acceleration. Must never be the only copy of knowledge. | SQLite FTS, BM25 index, vector store, graph projection. |
| Published site | No | Generated | Read-only presentation surface. | VitePress/GitHub Pages output. |

## Raw sources are immutable evidence

Raw sources must be maintained separately from wiki/concept notes, following Karpathy's LLM Wiki pattern. Raw sources are not summaries. They are evidence records. A raw source may be:

1. A preserved original or near-original text extraction, such as article markdown, paper text, transcript text, GitHub issue JSON/markdown, or official docs markdown.
2. A binary/original artifact stored in the vault or repo, such as PDF, image, screenshot, audio, or downloaded HTML.
3. A pointer note that records an exact local path, content hash, source URL, retrieval date, and access instructions when the artifact is too large or cannot be copied into the vault.

A raw source may include `## Extraction Notes`, but those notes are commentary. They are not the raw source itself and must not replace preserved source content or artifact path.

Allowed edits to raw source files:
- Add or correct metadata.
- Add missing artifact paths, hashes, retrieval timestamps, or extraction status.
- Mark extraction as partial/blocked/truncated.
- Add an erratum note that the capture was defective.

Disallowed edits to raw source files:
- Rewriting original source wording for clarity.
- Deleting inconvenient source text.
- Collapsing full source content into a summary while still marking it as raw.
- Mixing synthesis claims into raw text without a clearly labeled analysis section.

## Truth lookup order for agents

When asked for a fact, Hermes should resolve truth in this order:

1. Identify the active scope: topic, project, user, time range, and privacy boundary.
2. Read the relevant index or topic map to locate candidate wiki notes.
3. Read the wiki note for current synthesis, confidence, contested status, and source links.
4. Follow source links to raw sources for verification of non-trivial claims.
5. If the wiki and raw source conflict, raw source wins as evidence, but the wiki may contain later synthesis explaining the conflict.
6. If no raw source supports a claim, answer with `insufficient evidence` or mark the claim as inference/speculation.
7. If retrieved memories or previous assistant outputs contain a claim but no raw/user-confirmed source, do not treat it as truth.

## One-writer rules by artifact type

| Artifact | Who may write directly | Review requirement |
|---|---|---|
| Raw source artifact | Capture tooling or explicit user instruction | Metadata-only corrections may be direct; content replacement requires review. |
| Concept/comparison/query note | Hermes or human | Direct patch allowed if source-backed; contested/high-impact changes need review note. |
| User profile note | Human or Hermes with explicit confirmation | Must show diff; no silent update of sensitive personal facts. |
| Project memory note | Hermes or human within active project scope | Direct patch allowed for stable conventions/decisions; ephemeral task state rejected. |
| Procedures/playbooks | Hermes or human | Promote to Hermes skill only when reusable and verified. |
| Derived index | Script/automation only | Rebuild from canonical markdown; never hand-edit. |
| Published site | GitHub Actions only | Generated from repo state. |

## Source identifiers

Every raw source should have a stable `source_id` so wiki notes can cite sources even if filenames move.

Format:

```text
src:<type>:<slug>:<year-or-date>
```

Examples:

```text
src:article:karpathy-llm-wiki-gist:2026
src:paper:memgpt:2023
src:github:mem0-issue-4573-memory-audit-junk:2026-05-14
src:clip:obsidian-web-clipper:2026-05-14
```

Wiki notes may cite both `source_id` and path. Path is for agent navigation; ID is for durable reference.

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

Schema discipline is the bridge between Obsidian as a human note app and Hermes as an agentic knowledge operator. The schema should be strict enough for search, dashboards, lint, and automation, but not so complex that humans stop writing notes.

## Global frontmatter fields

Every managed note, except `README.md` and simple generated/publication files, should use YAML frontmatter.

| Field | Required | Values | Meaning |
|---|---:|---|---|
| `id` | Yes | stable slug-like ID | Durable reference independent of filename. |
| `title` | Yes | string | Human-readable title. |
| `type` | Yes | `raw_source`, `concept`, `comparison`, `query`, `decision`, `project_memory`, `user_profile`, `session_summary`, `procedure`, `dashboard`, `index` | Note class. |
| `created` | Yes | `YYYY-MM-DD` | Creation date. |
| `updated` | Yes | `YYYY-MM-DD` | Last meaningful content update. |
| `status` | Yes | `draft`, `active`, `review`, `contested`, `superseded`, `archived` | Lifecycle state. |
| `tags` | Yes | list | Search/dashboard tags. |
| `scope` | Yes | object | User/project/topic/channel boundary. |
| `visibility` | Yes | `private`, `internal`, `public` | Publication and automation boundary. |
| `agent_read` | Yes | boolean | Whether agents may read by default. |
| `agent_write` | Yes | `never`, `propose`, `direct` | Whether agents may write directly. |
| `sources` | Conditional | list of source IDs or paths | Required for source-backed wiki notes. |
| `confidence` | Conditional | `low`, `medium`, `high` | Required for concepts/comparisons/queries/decisions. |
| `contested` | Conditional | boolean | Required for concepts/comparisons/queries/decisions. |

## Raw source note schema

Raw sources are immutable evidence records. They must either contain preserved source text or point to an exact artifact path that Hermes can locate and read with appropriate tools.

```yaml
---
id: src:article:example-source:2026-05-16
title: Example Source Title
type: raw_source
created: 2026-05-16
updated: 2026-05-16
status: active
tags: [raw-source, article]
scope:
  users: [a17]
  projects: []
  topics: [agent-memory]
  channels: []
visibility: public
agent_read: true
agent_write: propose
source:
  source_url: https://example.com/article
  original_artifact_path: raw/assets/example-source.html
  local_text_path: raw/articles/example-source.md
  media_paths: []
  captured_by: hermes-web | obsidian-clipper | manual | pdf-parser | screenshot | api
  captured_at: 2026-05-16T00:00:00Z
  content_sha256: sha256:...
  license: unknown
  access_notes: public web page
source_derivation:
  derived_from: []
  transformation: []
raw_preservation: full_text | full_binary | full_html | full_pdf_text | pointer_only | transformed_text | tool_parsed_or_summarized_text | extraction_blocked
extraction_status: complete | partial | blocked | needs_pdf_pass | needs_manual_review
reliability: high | medium | low
---
```

Required body sections:

```markdown
# Source Title

## Source Metadata

## Original Artifact / Storage Path

- original_artifact_path: raw/assets/example-source.html
- local_text_path: raw/articles/example-source.md
- media_paths: []

## Parsed Source Text

Preserved source text goes here. If source is binary-only, write where the binary lives and how an agent should read it.

## Extraction Notes

Only commentary about extraction quality, missing sections, blocked access, or parser limitations.
```

## Source derivation for transformed sources

Use `source_derivation` when a source note is not the original artifact but a transformed representation of another raw source. Examples include OCR outputs, transcript cleanups, parsed PDFs, translated versions, normalized HTML extracts, and markdown cleanup passes.

```yaml
source_derivation:
  derived_from:
    - src:pdf:memgpt-paper:2023
  transformation:
    - OCR
    - markdown_cleanup
```

Rules:
- `derived_from` must point to source IDs or paths for the upstream raw/original artifact.
- `transformation` must list every meaningful processing step that changed representation or wording.
- A transformed source is still evidence, but it is not the root evidence. Agents should follow `derived_from` when exact wording, layout, figures, or legal/provenance questions matter.
- Translations must record source language and target language in `transformation` or `Extraction Notes`.
- Cleanup-only transformations must not silently remove uncertainty, OCR errors, speaker labels, timestamps, page numbers, or source line/page references.

## Concept note schema

Concept notes are agent/human-authored synthesis pages. They are mutable, but every factual claim should trace to raw sources.

```yaml
---
id: concept:hermes-obsidian-personal-kb
title: Hermes Obsidian Personal Knowledge Base Plan
type: concept
created: 2026-05-14
updated: 2026-05-16
status: active
tags: [agent-memory, obsidian, hermes]
scope:
  users: [a17]
  projects: [wiki]
  topics: [agent-memory, personal-knowledge-base]
  channels: []
visibility: public
agent_read: true
agent_write: direct
sources:
  - src:article:karpathy-llm-wiki-gist:2026
  - raw/articles/karpathy-llm-wiki-gist-2026.md
confidence: medium
contested: true
review:
  last_reviewed: 2026-05-16
  next_review: 2026-06-16
---
```

Required body sections:

```markdown
# Title

# Executive Summary
# Claims
# Architecture / Analysis
# Open Questions
# Source Map
# Current Corrections / Evidence Gaps
```

## Decision note schema

```yaml
---
id: decision:project:short-title:2026-05-16
title: Decision Title
type: decision
created: 2026-05-16
updated: 2026-05-16
status: accepted
scope:
  users: [a17]
  projects: [hermes-agent]
  topics: []
  channels: []
visibility: private
agent_read: true
agent_write: propose
sources: []
confidence: medium
contested: false
supersedes: []
superseded_by: null
---
```

Required body sections:

```markdown
# Decision
## Context
## Options Considered
## Decision
## Consequences
## Evidence / Sources
## Review Date
```

## Session summary schema

Session notes are not raw memory dumps. They are filtered summaries of durable outcomes.

```yaml
---
id: session:2026-05-16-hermes-obsidian-kb
title: Hermes Obsidian KB Planning Session
type: session_summary
created: 2026-05-16
updated: 2026-05-16
status: active
tags: [session, hermes, obsidian]
scope:
  users: [a17]
  projects: [wiki]
  topics: [personal-knowledge-base]
  channels: [cli]
visibility: private
agent_read: true
agent_write: propose
sources: []
contains_personal_data: true
retention: keep | delete_after_30d | archive
---
```

Required body sections:

```markdown
# Session Summary
## Durable Outcomes
## Decisions
## Open Questions
## Rejected / Do Not Store
## Follow-up Actions
```

## Procedure note schema

```yaml
---
id: procedure:ingest-source
title: Ingest Source Procedure
type: procedure
created: 2026-05-16
updated: 2026-05-16
status: active
tags: [procedure, ingestion]
scope:
  users: [a17]
  projects: [wiki]
  topics: [agent-memory]
  channels: []
visibility: public
agent_read: true
agent_write: direct
sources: []
promote_to_skill: false
---
```

Required body sections:

```markdown
# Procedure
## Trigger
## Inputs
## Steps
## Validation
## Failure Modes
## Commit Message
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

# Automation and Permission Boundary

Automation must be explicit because the knowledge base is both a personal workspace and an agent-readable truth substrate.

## Permission levels

| Level | Meaning | Allowed examples |
|---|---|---|
| `read_public` | Agent may read public/research notes. | `README.md`, `concepts/`, public raw sources. |
| `read_scoped` | Agent may read only when current task scope matches note scope. | Project memory, session summaries. |
| `read_explicit` | Agent may read only after explicit user instruction. | `99-private/`, sensitive personal notes. |
| `write_direct` | Agent may patch directly and commit. | Index/log updates, non-sensitive source-backed concept edits. |
| `write_propose` | Agent may create a patch/proposal, but user must approve. | User profile, project decisions, contested claims. |
| `write_forbidden` | Agent must not write. | Raw artifact content, private secrets, generated indexes by hand. |

## Folder policy

| Folder | Read default | Write default | Publish default | Notes |
|---|---|---|---|---|
| `raw/` / `90-sources/` | allowed | propose for metadata, forbidden for source content rewrite | allowed only if visibility public | Immutable evidence. |
| `concepts/`, `comparisons/`, `queries/` | allowed | direct if source-backed | allowed if visibility public | Main wiki layer. |
| `20-projects/` | scoped | propose/direct depending on project | private by default | Avoid leaking active work. |
| `50-sessions/` | scoped | propose | private by default | Summaries only, not transcript dumps. |
| `00-system/user-profile.md` | scoped | propose only | never | Personal facts require confirmation. |
| `40-procedures/` | allowed | direct for non-sensitive procedures | allowed if visibility public | Promote stable procedures to skills. |
| `99-private/` | explicit only | forbidden unless explicit | never | Default-deny. |
| `.hermes-kb/`, vector stores, search indexes | tool/script only | rebuild-only | never | Derived artifacts. |

## Automation classes

Safe automation:
- Rebuild search indexes from markdown.
- Lint missing frontmatter, broken links, missing raw source fields.
- Generate read-only dashboards.
- Append log entries for agent actions.
- Draft review reports.

Needs review:
- Editing user profile or personal facts.
- Marking a contested claim as resolved.
- Changing confidence from low/medium to high.
- Deleting or archiving notes.
- Moving notes across visibility boundaries.
- Publishing any private/project/session content.

Forbidden without explicit instruction:
- Reading secrets or private folders.
- Writing API keys, tokens, passwords, or credentials into notes.
- Replacing raw source content with summaries.
- Re-extracting recalled memory as if it were new user input.
- Publishing `99-private/`, `.obsidian/workspace*.json`, `.hermes-kb/`, session transcripts, or secrets-adjacent notes.

## `.agentignore` / publication exclusion baseline

```text
99-private/**
50-sessions/**
20-projects/**/secrets/**
**/.obsidian/workspace*.json
**/.trash/**
**/*secret*
**/*password*
**/*token*
.hermes-kb/**
node_modules/**
.vitepress/cache/**
.vitepress/dist/**
```

## Human confirmation triggers

Hermes must ask for confirmation or produce a proposal-only patch when:

- The edit changes a personal preference, identity fact, relationship, medical/financial/legal fact, or other sensitive personal data.
- The edit changes the system's conclusion about a contested or high-impact claim.
- The edit deletes, archives, or supersedes a note.
- The edit changes raw source content rather than metadata.
- The edit makes private/scoped content public.
- The task scope does not match the note's `scope` field.

# MVP Operating Loop

The MVP should prove that an agent can enter the vault, find truth, update knowledge, and leave an auditable trail.

## MVP scope

Use `/Users/a17/wiki` as the first standalone Obsidian/VitePress research vault. Do not migrate the full personal vault yet.

MVP includes:
- Raw source capture under `raw/`.
- Concept synthesis under `concepts/`.
- `index.md` and `log.md` maintenance.
- Git commits for every completed knowledge change.
- VitePress publication only for public/research-safe notes.
- Manual review for private, personal, contested, or destructive edits.

MVP excludes:
- Vector DB.
- Graph DB.
- Automatic personal memory extraction.
- Automatic publication of project/session/private notes.
- Autonomous deletion/archive.
- Obsidian REST/MCP dependency unless filesystem-first editing fails.

## MVP ingest loop

1. User provides a source URL/file/path or places a clip in inbox.
2. Hermes creates a raw source note or artifact pointer with `type: raw_source`, `source_id`, storage path, hash, capture date, preservation status, and extraction status.
3. Hermes verifies that the raw source is readable from the recorded path.
4. Hermes extracts candidate claims, entities, and open questions into an analysis section or separate draft.
5. Hermes searches existing concepts before creating new pages.
6. Hermes patches the most relevant concept/query/decision note with source-backed claims.
7. Hermes updates `index.md` if a new durable page was created.
8. Hermes appends `log.md` with what changed and why.
9. Hermes runs lint/build checks.
10. Hermes commits and pushes.

## MVP truth lookup loop

1. Parse the user question into topic/project/scope.
2. Search `index.md`, filenames, headings, and tags.
3. Read candidate concept notes.
4. Follow cited raw source paths for important factual claims.
5. Answer with citations and confidence.
6. If evidence is missing, say `insufficient evidence` and optionally create a query note.

## MVP session-to-knowledge loop

1. Summarize the session only if it contains durable outcomes.
2. Extract decisions, stable preferences, reusable procedures, open research questions, and source additions.
3. Put rejected ephemera into `## Rejected / Do Not Store`.
4. Update project/concept/procedure notes only when the extracted item is durable.
5. Promote repeated procedures to Hermes skills when verified.

## MVP done criteria

- One new source can be ingested end-to-end with raw source preservation and a source-backed concept update.
- A fresh Hermes session can answer a question by reading the vault and following raw source links.
- Lint catches missing raw source metadata, missing frontmatter, and missing source links.
- VitePress build succeeds after the update.
- Git history clearly shows what changed.

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
