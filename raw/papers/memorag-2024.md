---
source_url: https://arxiv.org/abs/2409.05591
fetched_url: https://arxiv.org/abs/2409.05591
source_type: paper
author: Hongjin Qian et al.
source_date: 2024-09-09
ingested: 2026-05-14
sha256: 9079f9af4d8ca6076fa91e1d5795d2a4daef242819ba24479b53092c0a1abc06
raw_preservation: tool_parsed_or_summarized_text
---

# Memorag 2024

## Source Metadata

- Source URL: https://arxiv.org/abs/2409.05591
- Fetched URL: https://arxiv.org/abs/2409.05591
- Source type: paper
- Author: Hongjin Qian et al.
- Source date: 2024-09-09
- Ingested: 2026-05-14
- Reliability: high
- Raw preservation status: tool_parsed_or_summarized_text
- Extraction note: Parsed source text is preserved below where accessible. If extraction tooling returned a summary/truncated representation, this is explicitly marked and should be replaced by fuller text in a later pass.

## Parsed Source Text

# MemoRAG: Boosting Long Context Processing with Global Memory-Enhanced Retrieval Augmentation

## Paper Metadata

- **arXiv ID:** [arXiv:2409.05591](https://arxiv.org/abs/2409.05591)
- **Title:** *MemoRAG: Boosting Long Context Processing with Global Memory-Enhanced Retrieval Augmentation*
- **Primary Subject:** Computation and Language (`cs.CL`)
- **Additional Subject:** Artificial Intelligence (`cs.AI`)
- **Venue/Comments:** *theWebConf 2025*
- **Submitted:** 9 Sep 2024
- **Latest Revision:** 9 Apr 2025 — version 3
- **DOI:** [https://doi.org/10.48550/arXiv.2409.05591](https://doi.org/10.48550/arXiv.2409.05591)
- **Code & Models:** [GitHub repository](https://github.com/qhjqhj00/MemoRAG)

## Authors

- [Hongjin Qian](https://arxiv.org/search/cs?searchtype=author&query=Qian,+H)
- [Zheng Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+Z)
- [Peitian Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+P)
- [Kelong Mao](https://arxiv.org/search/cs?searchtype=author&query=Mao,+K)
- [Defu Lian](https://arxiv.org/search/cs?searchtype=author&query=Lian,+D)
- [Zhicheng Dou](https://arxiv.org/search/cs?searchtype=author&query=Dou,+Z)
- [Tiejun Huang](https://arxiv.org/search/cs?searchtype=author&query=Huang,+T)

---

## Key Excerpt: Abstract

> Processing long contexts presents a significant challenge for large language models (LLMs). While recent advancements allow LLMs to handle much longer contexts than before (e.g., 32K or 128K tokens), it is computationally expensive and can still be insufficient for many applications. Retrieval-Augmented Generation (RAG) is considered a promising strategy to address this problem. However, conventional RAG methods face inherent limitations because of two underlying requirements: 1) explicitly stated queries, and 2) well-structured knowledge. These conditions, however, do not hold in general long-context processing tasks.

> In this work, we propose MemoRAG, a novel RAG framework empowered by global memory-augmented retrieval. MemoRAG features a dual-system architecture. First, it employs a light but long-range system to create a global memory of the long context. Once a task is presented, it generates draft answers, providing useful clues for the retrieval tools to locate relevant information within the long context. Second, it leverages an expensive but expressive system, which generates the final answer based on the retrieved information. Building upon this fundamental framework, we realize the memory module in the form of KV compression, and reinforce its memorization and cluing capacity from the Generation quality's Feedback (a.k.a. RLGF). In our experiments, MemoRAG achieves superior performances across a variety of long-context evaluation tasks, not only complex scenarios where traditional RAG methods struggle, but also simpler ones where RAG is typically applied.

---

## Core Problem

Long-context processing remains difficult for LLMs even as context windows expand to **32K** or **128K tokens**.

### Key limitations of simply using longer context windows

- **High computational cost**
- **Still insufficient** for many real-world applications requiring very long or complex context understanding
- Performance may degrade when relevant information is buried in large amounts of text

### Limitations of conventional RAG

The paper identifies two assumptions behind traditional Retrieval-Augmented Generation that often fail in general long-context tasks:

1. **Explicitly stated queries**
   - Traditional RAG works best when the user query clearly specifies what information to retrieve.
2. **Well-structured knowledge**
   - RAG assumes information is chunked, indexed, and semantically retrievable in a structured or clean way.

In many long-context tasks, these conditions do **not** hold. Queries may be vague, implicit, or require global reasoning, and relevant evidence may be scattered throughout unstructured text.

---

## Proposed Method: MemoRAG

**MemoRAG** is a retrieval-augmented generation framework designed to improve long-context processing through **global memory-enhanced retrieval augmentation**.

### Main idea

MemoRAG introduces a **dual-system architecture**:

1. A lightweight long-range memory system
2. A more expensive expressive generation system

Together, these systems improve retrieval and final answer quality for long-context tasks.

---

## MemoRAG Architecture

### 1. Light but Long-Range Memory System

MemoRAG first uses a lightweight system capable of processing long contexts to build a **global memory** of the input.

This memory system:

- Reads or compresses the long context
- Maintains global information across the entire document or context
- Generates **draft answers**
- Produces useful retrieval clues

These draft answers are not necessarily final outputs. Instead, they guide retrieval by helping identify where relevant evidence may exist in the long context.

### 2. Retrieval Using Memory-Generated Clues

Once a task

[... summary truncated for context management ...]
