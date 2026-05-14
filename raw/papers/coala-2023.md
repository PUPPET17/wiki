---
source_url: https://arxiv.org/abs/2309.02427
fetched_url: https://arxiv.org/abs/2309.02427
source_type: paper
author: Theodore R. Sumers et al.
source_date: 2023-09-05
ingested: 2026-05-14
sha256: 7fbdd5864409d6ab7a2bc7b30261eec90cb9df4952c8aac12522ccaefb92244f
raw_preservation: tool_parsed_or_summarized_text
---

# Coala 2023

## Source Metadata

- Source URL: https://arxiv.org/abs/2309.02427
- Fetched URL: https://arxiv.org/abs/2309.02427
- Source type: paper
- Author: Theodore R. Sumers et al.
- Source date: 2023-09-05
- Ingested: 2026-05-14
- Reliability: high
- Raw preservation status: tool_parsed_or_summarized_text
- Extraction note: Parsed source text is preserved below where accessible. If extraction tooling returned a summary/truncated representation, this is explicitly marked and should be replaced by fuller text in a later pass.

## Parsed Source Text

# Cognitive Architectures for Language Agents — arXiv Summary

## Paper Information

- **Title:** *Cognitive Architectures for Language Agents*
- **arXiv ID:** [arXiv:2309.02427](https://arxiv.org/abs/2309.02427)
- **Primary Category:** Computer Science > Artificial Intelligence (`cs.AI`)
- **Additional Subjects:**
  - Computation and Language (`cs.CL`)
  - Machine Learning (`cs.LG`)
  - Symbolic Computation (`cs.SC`)
- **Authors:**
  - [Theodore R. Sumers](https://arxiv.org/search/cs?searchtype=author&query=Sumers,+T+R)
  - [Shunyu Yao](https://arxiv.org/search/cs?searchtype=author&query=Yao,+S)
  - [Karthik Narasimhan](https://arxiv.org/search/cs?searchtype=author&query=Narasimhan,+K)
  - [Thomas L. Griffiths](https://arxiv.org/search/cs?searchtype=author&query=Griffiths,+T+L)
- **Submitted:** 5 Sep 2023
- **Latest Revision:** 15 Mar 2024 — **version v3**
- **DOI:** [https://doi.org/10.48550/arXiv.2309.02427](https://doi.org/10.48550/arXiv.2309.02427)
- **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/)

---

## Key Excerpt — Abstract

> Recent efforts have augmented large language models (LLMs) with external resources (e.g., the Internet) or internal control flows (e.g., prompt chaining) for tasks requiring grounding or reasoning, leading to a new class of language agents. While these agents have achieved substantial empirical success, we lack a systematic framework to organize existing agents and plan future developments. In this paper, we draw on the rich history of cognitive science and symbolic artificial intelligence to propose Cognitive Architectures for Language Agents (CoALA). CoALA describes a language agent with modular memory components, a structured action space to interact with internal memory and external environments, and a generalized decision-making process to choose actions. We use CoALA to retrospectively survey and organize a large body of recent work, and prospectively identify actionable directions towards more capable agents. Taken together, CoALA contextualizes today's language agents within the broader history of AI and outlines a path towards language-based general intelligence.

---

## Core Contribution

The paper proposes **Cognitive Architectures for Language Agents**, abbreviated **CoALA**, as a systematic framework for understanding and designing language agents built on large language models.

CoALA aims to organize recent work on LLM-based agents by drawing from:

- **Cognitive science**
- **Symbolic artificial intelligence**
- Research on **cognitive architectures**
- Recent empirical advances in **LLM agents**

The framework characterizes language agents through three central components:

1. **Modular memory components**
2. **A structured action space**
3. **A generalized decision-making process**

---

## Main Ideas

### 1. Language Agents Extend LLMs

The paper frames recent systems as a new class of **language agents**: LLM-based systems augmented with mechanisms beyond plain text generation.

These augmentations include:

- **External resources**, such as:
  - The Internet
  - Tools
  - APIs
  - External environments

- **Internal control flows**, such as:
  - Prompt chaining
  - Reasoning loops
  - Planning procedures
  - Memory access and updates

These additions help agents handle tasks requiring:

- **Grounding**
- **Reasoning**
- **Planning**
- **Interaction with environments**
- **Longer-term memory or context management**

---

### 2. Need for a Systematic Framework

The authors argue that while language agents have shown strong empirical results, the field lacks a clear framework to:

- Organize existing systems
- Compare agent designs
- Identify reusable architectural patterns
- Plan future developments
- Connect modern LLM agents to prior AI research

CoALA is proposed to fill that gap.

---

### 3. CoALA Framework

The **CoALA** framework describes a language agent as having:

#### Modular Memory Components

The agent’s memory is divided into modules rather than treated as a single undifferentiated context window.

This supports reasoning about how agents store, retrieve, and update information across tasks.

#### Structured Action Space

The agent can choose actions that interact with:

- **Internal memory**
- **External environments**
- External tools or resources

This action-centric view helps unify different agent capabilities under a common structure.

#### Generalized Decision-Making Process

The agent uses a decision-making process to determine which actions to take.

This generalizes many existing LLM-agent workflows, including:

- Tool use
- Planning
- Reflection
- Retrieval
- Prompt chaining
- Interaction loops

---

## Purpose and Scope of the Paper

The paper uses CoALA in two directions:

### Retrospective Use

CoALA is used to **survey and organize** a large body of recent work on language agents.

This helps situate current approaches within a broader architecture-level taxonomy.

### Prospective 

[... summary truncated for context management ...]
