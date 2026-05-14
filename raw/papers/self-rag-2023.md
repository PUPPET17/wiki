---
source_url: https://arxiv.org/abs/2310.11511
fetched_url: https://arxiv.org/abs/2310.11511
source_type: paper
author: Akari Asai et al.
source_date: 2023-10-17
ingested: 2026-05-14
sha256: e8a9441076e67707c3b3161b4ac204ed87af99b5f97d0557a2dc8c2d8ec3a1ec
raw_preservation: tool_parsed_or_summarized_text
---

# Self Rag 2023

## Source Metadata

- Source URL: https://arxiv.org/abs/2310.11511
- Fetched URL: https://arxiv.org/abs/2310.11511
- Source type: paper
- Author: Akari Asai et al.
- Source date: 2023-10-17
- Ingested: 2026-05-14
- Reliability: high
- Raw preservation status: tool_parsed_or_summarized_text
- Extraction note: Parsed source text is preserved below where accessible. If extraction tooling returned a summary/truncated representation, this is explicitly marked and should be replaced by fuller text in a later pass.

## Parsed Source Text

# Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection — Summary

## Paper Metadata

- **Title:** *Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection*
- **arXiv ID:** [arXiv:2310.11511](https://arxiv.org/abs/2310.11511)
- **DOI:** [https://doi.org/10.48550/arXiv.2310.11511](https://doi.org/10.48550/arXiv.2310.11511)
- **Submitted:** 17 Oct 2023
- **Version:** v1  
  - Submitted: Tue, 17 Oct 2023 18:18:32 UTC
  - Size: 896 KB
- **Length:** 30 pages
- **Figures/Tables:** 2 figures, 12 tables
- **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/)
- **Primary Subject:** Computation and Language — `cs.CL`
- **Other Subjects:** Artificial Intelligence — `cs.AI`; Machine Learning — `cs.LG`

## Authors

- [Akari Asai](https://arxiv.org/search/cs?searchtype=author&query=Asai,+A)
- [Zeqiu Wu](https://arxiv.org/search/cs?searchtype=author&query=Wu,+Z)
- [Yizhong Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+Y)
- [Avirup Sil](https://arxiv.org/search/cs?searchtype=author&query=Sil,+A)
- [Hannaneh Hajishirzi](https://arxiv.org/search/cs?searchtype=author&query=Hajishirzi,+H)

## Access Links

- [View PDF](https://arxiv.org/pdf/2310.11511)
- [TeX Source](https://arxiv.org/src/2310.11511)
- [arXiv Abstract Page](https://arxiv.org/abs/2310.11511)

## Key Abstract Excerpt

> Despite their remarkable capabilities, large language models (LLMs) often produce responses containing factual inaccuracies due to their sole reliance on the parametric knowledge they encapsulate.

> Retrieval-Augmented Generation (RAG), an ad hoc approach that augments LMs with retrieval of relevant knowledge, decreases such issues. However, indiscriminately retrieving and incorporating a fixed number of retrieved passages, regardless of whether retrieval is necessary, or passages are relevant, diminishes LM versatility or can lead to unhelpful response generation.

> We introduce a new framework called Self-Reflective Retrieval-Augmented Generation (Self-RAG) that enhances an LM's quality and factuality through retrieval and self-reflection.

> Our framework trains a single arbitrary LM that adaptively retrieves passages on-demand, and generates and reflects on retrieved passages and its own generations using special tokens, called reflection tokens.

> Generating reflection tokens makes the LM controllable during the inference phase, enabling it to tailor its behavior to diverse task requirements.

> Experiments show that Self-RAG (7B and 13B parameters) significantly outperforms state-of-the-art LLMs and retrieval-augmented models on a diverse set of tasks.

> Specifically, Self-RAG outperforms ChatGPT and retrieval-augmented Llama2-chat on Open-domain QA, reasoning and fact verification tasks, and it shows significant gains in improving factuality and citation accuracy for long-form generations relative to these models.

## Core Idea

**Self-RAG** is a retrieval-augmented language modeling framework designed to improve **factuality**, **response quality**, and **controllability**.

Unlike standard RAG systems that retrieve a fixed number of passages regardless of whether retrieval is actually needed, Self-RAG teaches the language model to:

1. **Decide when retrieval is necessary**
2. **Retrieve passages on demand**
3. **Generate responses using retrieved evidence**
4. **Critique retrieved passages**
5. **Reflect on its own generations**
6. **Use special “reflection tokens” to guide inference-time behavior**

## Problem Addressed

Large language models often rely solely on internal, parametric knowledge. This can cause:

- Factual inaccuracies
- Hallucinated claims
- Unsupported answers
- Poor citation behavior
- Difficulty adapting responses to tasks with different factuality or evidence requirements

Traditional Retrieval-Augmented Generation helps by adding external knowledge, but the paper argues that common RAG approaches are limited because they often retrieve passages indiscriminately.

### Limitation of Standard RAG

Standard RAG methods may:

- Retrieve a fixed number of passages even when retrieval is unnecessary
- Incorporate irrelevant passages
- Reduce language model versatility
- Produce unhelpful or noisy responses when retrieved context is poor

## Proposed Solution: Self-Reflective Retrieval-Augmented Generation

Self-RAG introduces a framework where a single language model learns to perform retrieval and self-critique through special tokens.

### Key Mechanism: Reflection Tokens

Self-RAG uses **reflection tokens** that allow the model to explicitly control and evaluate its behavior.

These tokens help the model decide:

- Whether retrieval is needed
- Whether retrieved passages are relevant
- Whether generated content is supported
- Whether the response satisfies the task requirements

This makes the model more **controllable during inference**, allowing it to adapt to different tasks and quality requirements.

## Model

[... summary truncated for context management ...]
