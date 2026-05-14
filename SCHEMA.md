# Wiki Schema

## Domain
LLM Wiki / Agent Memory / Context Compression / Knowledge Integration research and implementation framework.

## Conventions
- File names: lowercase, hyphens, no spaces.
- Stable document structure is preserved across iterations.
- Every wiki page starts with YAML frontmatter.
- Use explicit source citations for every non-trivial claim.
- Distinguish: fact, inference, speculation, community view.
- Do not treat Twitter/X, Reddit, or Hacker News discussion as verified fact unless cross-validated by papers, docs, repos, or working implementations.
- If evidence is missing, write: unknown / insufficient evidence / speculative.
- Raw sources are immutable; corrections go into wiki pages.
- Every update must append to log.md.

## Required Research Document Sections
Executive Summary
Core Thesis
Key Concepts
Karpathy Gist Analysis
Architecture Patterns
Existing Projects
Community Consensus
Major Debates
Failure Cases
Engineering Constraints
Practical Integration Blueprint
MVP Plan
Recommended Stack
Open Problems
Research Questions
Personal Developer Opportunities
Source Map

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/...]
confidence: high | medium | low
contested: true | false
---
```

## Tag Taxonomy
- topic: llm-wiki, agent-memory, rag, context-engineering, knowledge-integration, personal-ai-os
- architecture: memory-architecture, retrieval, compression, indexing, graph-memory, vector-memory, symbolic-memory
- evidence: paper, blog, github, hn, reddit, tweet, product-docs
- implementation: prototype, mvp, scalable-architecture, local-first, cloud-first
- analysis: tradeoff, failure-case, opportunity, debate

## Page Thresholds
- Create or update a concept page when a claim affects architecture, engineering tradeoffs, or implementation direction.
- Avoid pages for passing mentions unless they are required by the stable research structure.
- Mark source quality and reliability explicitly.

## Reliability Scale
- high: primary source, paper, official docs, reproducible repo, or direct author statement.
- medium: engineering blog, HN thread with author participation, community discussion with technical detail.
- low: search-result snippet, secondary summary, inaccessible Reddit/Twitter content, marketing copy, unverified claims.

## Update Policy
When new evidence conflicts with existing content:
1. Keep the old view under a dated correction note.
2. Add the new evidence with source and date.
3. Mark contested: true if unresolved.
4. Update Source Map notes.
