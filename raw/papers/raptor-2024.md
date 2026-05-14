---
source_url: https://arxiv.org/abs/2401.18059
fetched_url: https://arxiv.org/abs/2401.18059
source_type: paper
author: Parth Sarthi et al.
source_date: 2024-01-31
ingested: 2026-05-14
sha256: 76480424351a09d8a4411f3abc9552020c8afa91e3d433dab7a22917c0b3ce48
raw_preservation: tool_parsed_or_summarized_text
---

# Raptor 2024

## Source Metadata

- Source URL: https://arxiv.org/abs/2401.18059
- Fetched URL: https://arxiv.org/abs/2401.18059
- Source type: paper
- Author: Parth Sarthi et al.
- Source date: 2024-01-31
- Ingested: 2026-05-14
- Reliability: high
- Raw preservation status: tool_parsed_or_summarized_text
- Extraction note: Parsed source text is preserved below where accessible. If extraction tooling returned a summary/truncated representation, this is explicitly marked and should be replaced by fuller text in a later pass.

## Parsed Source Text

# RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval

**Source:** [arXiv:2401.18059](https://arxiv.org/abs/2401.18059)  
**Category:** Computer Science > Computation and Language  
**Submitted:** 31 Jan 2024  
**Version:** v1  
**DOI:** [https://doi.org/10.48550/arXiv.2401.18059](https://doi.org/10.48550/arXiv.2401.18059)

---

## Paper Details

- **Title:** *RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval*
- **Authors:**
  - Parth Sarthi
  - Salman Abdullah
  - Aditi Tuli
  - Shubh Khanna
  - Anna Goldie
  - Christopher D. Manning
- **arXiv ID:** [arXiv:2401.18059](https://arxiv.org/abs/2401.18059)
- **Subjects:**
  - Computation and Language (`cs.CL`)
  - Machine Learning (`cs.LG`)
- **Submission history:**
  - **v1:** Wed, 31 Jan 2024 18:30:21 UTC
  - File size: **2,334 KB**
- **License:** [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/)

---

## Access Links

- [View PDF](https://arxiv.org/pdf/2401.18059)
- [HTML Experimental Version](https://arxiv.org/html/2401.18059v1)
- [TeX Source](https://arxiv.org/src/2401.18059)

---

## Key Excerpt: Abstract

> Retrieval-augmented language models can better adapt to changes in world state and incorporate long-tail knowledge. However, most existing methods retrieve only short contiguous chunks from a retrieval corpus, limiting holistic understanding of the overall document context. We introduce the novel approach of recursively embedding, clustering, and summarizing chunks of text, constructing a tree with differing levels of summarization from the bottom up. At inference time, our RAPTOR model retrieves from this tree, integrating information across lengthy documents at different levels of abstraction. Controlled experiments show that retrieval with recursive summaries offers significant improvements over traditional retrieval-augmented LMs on several tasks. On question-answering tasks that involve complex, multi-step reasoning, we show state-of-the-art results; for example, by coupling RAPTOR retrieval with the use of GPT-4, we can improve the best performance on the QuALITY benchmark by 20% in absolute accuracy.

---

## Core Contribution

RAPTOR introduces a retrieval method for retrieval-augmented language models that improves over traditional chunk-based retrieval.

Instead of retrieving only **short contiguous text chunks**, RAPTOR builds a **tree-structured representation** of documents by:

1. Embedding chunks of text
2. Clustering related chunks
3. Summarizing clustered content
4. Recursively repeating this process from the bottom up

This creates multiple levels of abstraction, allowing retrieval to access both:

- Fine-grained details from original text chunks
- Higher-level summaries that capture broader document context

---

## Problem Addressed

Most retrieval-augmented language model systems rely on retrieving small, adjacent chunks from a corpus.

The paper argues this has a major limitation:

- Short chunks may contain local facts
- But they often fail to preserve **holistic understanding**
- They can miss context distributed across lengthy documents
- They are less effective for tasks requiring complex or multi-step reasoning

RAPTOR is designed to overcome this by enabling retrieval across a document’s hierarchical semantic structure.

---

## Method Overview

RAPTOR stands for:

**Recursive Abstractive Processing for Tree-Organized Retrieval**

The approach constructs a tree from the document corpus:

- **Leaf nodes:** Original text chunks
- **Intermediate nodes:** Summaries of clustered related chunks
- **Higher nodes:** More abstract summaries produced recursively
- **Root/top-level nodes:** Broad document-level abstractions

At inference time, the model retrieves from this tree rather than only from raw chunks.

This allows the language model to integrate information:

- Across long documents
- At different abstraction levels
- From both specific passages and broader summaries

---

## Reported Results

The paper reports that RAPTOR achieves significant gains over traditional retrieval-augmented language models.

Key result highlighted in the abstract:

> On question-answering tasks that involve complex, multi-step reasoning, we show state-of-the-art results; for example, by coupling RAPTOR retrieval with the use of GPT-4, we can improve the best performance on the QuALITY benchmark by 20% in absolute accuracy.

### Notable Benchmark Mentioned

- **QuALITY benchmark**
  - RAPTOR + GPT-4 improves the previous best performance by **20% absolute accuracy**
  - Especially relevant for complex, multi-step question answering

---

## Why It Matters

RAPTOR is important because it targets a central weakness in retrieval-augmented generation systems:

> Retrieval systems often retrieve isolated snippets, while many real-world questions require understanding across an entire document or collection.

By using recursive summarization and tree-based retrieva

[... summary truncated for context management ...]
