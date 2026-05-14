---
source_url: https://arxiv.org/abs/2310.08560
fetched_url: https://arxiv.org/abs/2310.08560
source_type: paper
author: Charles Packer et al.
source_date: 2023-10-12
ingested: 2026-05-14
sha256: 3659324dc10035b370a7f8b378347bf878afd0b5b36fe927d0c5508f5fef52ea
raw_preservation: tool_parsed_or_summarized_text
---

# Memgpt 2023

## Source Metadata

- Source URL: https://arxiv.org/abs/2310.08560
- Fetched URL: https://arxiv.org/abs/2310.08560
- Source type: paper
- Author: Charles Packer et al.
- Source date: 2023-10-12
- Ingested: 2026-05-14
- Reliability: high
- Raw preservation status: tool_parsed_or_summarized_text
- Extraction note: Parsed source text is preserved below where accessible. If extraction tooling returned a summary/truncated representation, this is explicitly marked and should be replaced by fuller text in a later pass.

## Parsed Source Text

# MemGPT: Towards LLMs as Operating Systems — Markdown Summary

## Paper Metadata

- **Title:** *MemGPT: Towards LLMs as Operating Systems*
- **arXiv ID:** [arXiv:2310.08560](https://arxiv.org/abs/2310.08560)
- **Category:** Computer Science > Artificial Intelligence (`cs.AI`)
- **Submitted:** 12 Oct 2023
- **Last revised:** 12 Feb 2024 — version 2
- **DOI:** [https://doi.org/10.48550/arXiv.2310.08560](https://doi.org/10.48550/arXiv.2310.08560)
- **License:** [Creative Commons Attribution 4.0 International — CC BY 4.0](http://creativecommons.org/licenses/by/4.0/)
- **Code and data:** [https://research.memgpt.ai/](https://research.memgpt.ai/)
- **Project site mentioned in abstract:** [https://memgpt.ai/](https://memgpt.ai/)

## Authors

- [Charles Packer](https://arxiv.org/search/cs?searchtype=author&query=Packer,+C)
- [Sarah Wooders](https://arxiv.org/search/cs?searchtype=author&query=Wooders,+S)
- [Kevin Lin](https://arxiv.org/search/cs?searchtype=author&query=Lin,+K)
- [Vivian Fang](https://arxiv.org/search/cs?searchtype=author&query=Fang,+V)
- [Shishir G. Patil](https://arxiv.org/search/cs?searchtype=author&query=Patil,+S+G)
- [Ion Stoica](https://arxiv.org/search/cs?searchtype=author&query=Stoica,+I)
- [Joseph E. Gonzalez](https://arxiv.org/search/cs?searchtype=author&query=Gonzalez,+J+E)

## Access Links

- [View PDF](https://arxiv.org/pdf/2310.08560)
- [TeX Source](https://arxiv.org/src/2310.08560)
- [arXiv abstract page](https://arxiv.org/abs/2310.08560)
- [Version 2 page](https://arxiv.org/abs/2310.08560v2)

## Key Excerpt: Abstract

> Large language models (LLMs) have revolutionized AI, but are constrained by limited context windows, hindering their utility in tasks like extended conversations and document analysis. To enable using context beyond limited context windows, we propose virtual context management, a technique drawing inspiration from hierarchical memory systems in traditional operating systems that provide the appearance of large memory resources through data movement between fast and slow memory. Using this technique, we introduce MemGPT (Memory-GPT), a system that intelligently manages different memory tiers in order to effectively provide extended context within the LLM's limited context window, and utilizes interrupts to manage control flow between itself and the user. We evaluate our OS-inspired design in two domains where the limited context windows of modern LLMs severely handicaps their performance: document analysis, where MemGPT is able to analyze large documents that far exceed the underlying LLM's context window, and multi-session chat, where MemGPT can create conversational agents that remember, reflect, and evolve dynamically through long-term interactions with their users. We release MemGPT code and data for our experiments at [this https URL](https://memgpt.ai/).

## Core Idea

The paper introduces **MemGPT**, short for **Memory-GPT**, a system designed to overcome the **limited context window** of large language models.

The central concept is **virtual context management**, inspired by **hierarchical memory systems in operating systems**. Just as operating systems move data between fast and slow memory to create the illusion of large available memory, MemGPT manages different memory tiers to give an LLM access to a larger effective context than its fixed context window allows.

## Key Contributions

- Proposes **virtual context management** for LLMs.
- Frames LLM context management using an **operating-system-inspired architecture**.
- Introduces **MemGPT**, a system that:
  - Manages different memory tiers.
  - Extends usable context beyond the model’s native context window.
  - Uses **interrupts** to control the flow between the system and the user.
- Evaluates MemGPT in two domains where context-window limits are a major bottleneck:
  1. **Document analysis**
  2. **Multi-session chat**

## Evaluation Domains

### 1. Document Analysis

MemGPT is evaluated on document-analysis tasks where documents exceed the underlying LLM’s context window.

Key claim:

> MemGPT is able to analyze large documents that far exceed the underlying LLM's context window

### 2. Multi-Session Chat

MemGPT is also evaluated for long-running conversational agents.

Key claim:

> MemGPT can create conversational agents that remember, reflect, and evolve dynamically through long-term interactions with their users.

This targets the problem of maintaining useful memory across multiple sessions, not just within a single conversation.

## Important Concepts

### Limited Context Windows

Modern LLMs can only process a fixed amount of text at once. This limits their usefulness for:

- Long conversations
- Multi-session interactions
- Large-document analysis
- Tasks requiring persistent memory

### Virtual Context Management

A technique inspired by traditional operating systems.

It provides the **appearance of a larger context** by moving information between different memory tiers, similar to how 

[... summary truncated for context management ...]
