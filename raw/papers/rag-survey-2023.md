---
source_url: https://arxiv.org/abs/2312.10997
fetched_url: https://arxiv.org/abs/2312.10997
source_type: paper
author: Yunfan Gao et al.
source_date: 2023-12-18
ingested: 2026-05-14
sha256: 51965cd7862cb6a9efc0d713164a2afaa3d5c2cd6c80c2d0749c9a7d97ca9c2f
raw_preservation: tool_parsed_or_summarized_text
---

# Rag Survey 2023

## Source Metadata

- Source URL: https://arxiv.org/abs/2312.10997
- Fetched URL: https://arxiv.org/abs/2312.10997
- Source type: paper
- Author: Yunfan Gao et al.
- Source date: 2023-12-18
- Ingested: 2026-05-14
- Reliability: high
- Raw preservation status: tool_parsed_or_summarized_text
- Extraction note: Parsed source text is preserved below where accessible. If extraction tooling returned a summary/truncated representation, this is explicitly marked and should be replaced by fuller text in a later pass.

## Parsed Source Text

# Retrieval-Augmented Generation for Large Language Models: A Survey — Markdown Summary

## Paper Overview

- **Title:** *Retrieval-Augmented Generation for Large Language Models: A Survey*
- **arXiv ID:** [arXiv:2312.10997](https://arxiv.org/abs/2312.10997)
- **Version summarized:** v5
- **Initial submission:** 18 Dec 2023
- **Last revised:** 27 Mar 2024
- **Status / Comments:** Ongoing Work
- **Primary subject:** Computation and Language — `cs.CL`
- **Additional subject:** Artificial Intelligence — `cs.AI`
- **DOI:** [https://doi.org/10.48550/arXiv.2312.10997](https://doi.org/10.48550/arXiv.2312.10997)

## Authors

- Yunfan Gao
- Yun Xiong
- Xinyu Gao
- Kangxiang Jia
- Jinliu Pan
- Yuxi Bi
- Yi Dai
- Jiawei Sun
- Meng Wang
- Haofen Wang

## Access Links

- [View PDF](https://arxiv.org/pdf/2312.10997)
- [HTML — experimental](https://arxiv.org/html/2312.10997v5)
- [TeX Source](https://arxiv.org/src/2312.10997)
- [arXiv page](https://arxiv.org/abs/2312.10997)

## Key Excerpt: Abstract

> Large Language Models (LLMs) showcase impressive capabilities but encounter challenges like hallucination, outdated knowledge, and non-transparent, untraceable reasoning processes. Retrieval-Augmented Generation (RAG) has emerged as a promising solution by incorporating knowledge from external databases. This enhances the accuracy and credibility of the generation, particularly for knowledge-intensive tasks, and allows for continuous knowledge updates and integration of domain-specific information. RAG synergistically merges LLMs' intrinsic knowledge with the vast, dynamic repositories of external databases. This comprehensive review paper offers a detailed examination of the progression of RAG paradigms, encompassing the Naive RAG, the Advanced RAG, and the Modular RAG. It meticulously scrutinizes the tripartite foundation of RAG frameworks, which includes the retrieval, the generation and the augmentation techniques. The paper highlights the state-of-the-art technologies embedded in each of these critical components, providing a profound understanding of the advancements in RAG systems. Furthermore, this paper introduces up-to-date evaluation framework and benchmark. At the end, this article delineates the challenges currently faced and points out prospective avenues for research and development.

## Core Contributions and Themes

This survey examines **Retrieval-Augmented Generation**, or **RAG**, as a method for improving Large Language Models by connecting them to external knowledge sources.

### Problems RAG Addresses

The paper positions RAG as a response to major limitations of LLMs:

- **Hallucination**
- **Outdated knowledge**
- **Opaque or untraceable reasoning**
- Difficulty integrating **domain-specific information**
- Need for **continuous knowledge updates**

### Central Idea

RAG combines:

1. The **intrinsic knowledge** of LLMs
2. External, dynamic knowledge repositories such as databases, document collections, or other retrieval systems

This combination is intended to improve:

- Accuracy
- Credibility
- Factual grounding
- Transparency
- Performance on knowledge-intensive tasks

## RAG Paradigms Covered

The survey reviews the evolution of RAG through three major paradigms:

### 1. Naive RAG

A basic retrieval-then-generation pipeline where relevant documents or passages are retrieved and passed to the LLM to guide generation.

### 2. Advanced RAG

More sophisticated approaches that improve retrieval quality, context selection, integration, and generation reliability.

### 3. Modular RAG

A more flexible paradigm that decomposes RAG systems into interchangeable or customizable modules, allowing different retrieval, augmentation, and generation strategies to be combined.

## Main Framework Components

The paper analyzes RAG systems through a **tripartite foundation**:

### Retrieval

Focuses on finding relevant external knowledge from databases, corpora, or other knowledge sources.

### Generation

Covers how LLMs use retrieved knowledge to produce grounded responses.

### Augmentation

Includes techniques for improving how retrieved information is selected, structured, inserted, refined, or used during generation.

## Evaluation and Benchmarks

The survey introduces an **up-to-date evaluation framework and benchmark** for RAG systems.

Key evaluation concerns include likely assessment of:

- Retrieval quality
- Generation accuracy
- Factuality
- Credibility
- Knowledge grounding
- Domain-specific performance
- Robustness of RAG pipelines

## Research Outlook

The paper concludes by identifying:

- Current challenges faced by RAG systems
- Future directions for research and development
- Opportunities to improve RAG architectures, benchmarks, and real-world deployment

## Submission History

| Version | Date | File Size |
|---|---:|---:|
| v1 | Mon, 18 Dec 2023 07:47:33 UTC | 7,541 KB |
| v2 | Fri, 29 Dec 2023 18:25:00 UTC | 6,421 KB |
| v3 | Wed, 3 Jan 2024 17:04:40 UTC | 7,508 KB |
| v4 | Fri, 5 Jan 2024

[... summary truncated for context management ...]
