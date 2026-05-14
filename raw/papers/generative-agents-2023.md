---
source_url: https://arxiv.org/abs/2304.03442
fetched_url: https://arxiv.org/abs/2304.03442
source_type: paper
author: Joon Sung Park et al.
source_date: 2023-04-07
ingested: 2026-05-14
sha256: b120af7418fc043417daf2cf6e95f45a43040e39c49723a82cea85502a465d96
raw_preservation: tool_parsed_or_summarized_text
---

# Generative Agents 2023

## Source Metadata

- Source URL: https://arxiv.org/abs/2304.03442
- Fetched URL: https://arxiv.org/abs/2304.03442
- Source type: paper
- Author: Joon Sung Park et al.
- Source date: 2023-04-07
- Ingested: 2026-05-14
- Reliability: high
- Raw preservation status: tool_parsed_or_summarized_text
- Extraction note: Parsed source text is preserved below where accessible. If extraction tooling returned a summary/truncated representation, this is explicitly marked and should be replaced by fuller text in a later pass.

## Parsed Source Text

# Generative Agents: Interactive Simulacra of Human Behavior — Markdown Summary

## Paper Metadata

- **Title:** *Generative Agents: Interactive Simulacra of Human Behavior*
- **arXiv ID:** [arXiv:2304.03442](https://arxiv.org/abs/2304.03442)
- **Version:** v2
- **Submitted:** 7 Apr 2023
- **Last revised:** 6 Aug 2023
- **Primary category:** Computer Science > Human-Computer Interaction
- **Subjects:**
  - Human-Computer Interaction `cs.HC`
  - Artificial Intelligence `cs.AI`
  - Machine Learning `cs.LG`
- **DOI:** [https://doi.org/10.48550/arXiv.2304.03442](https://doi.org/10.48550/arXiv.2304.03442)
- **PDF:** [View PDF](https://arxiv.org/pdf/2304.03442)
- **TeX Source:** [Download Source](https://arxiv.org/src/2304.03442)
- **License:** [arXiv non-exclusive distribution license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/)

## Authors

- [Joon Sung Park](https://arxiv.org/search/cs?searchtype=author&query=Park,+J+S)
- [Joseph C. O'Brien](https://arxiv.org/search/cs?searchtype=author&query=O%27Brien,+J+C)
- [Carrie J. Cai](https://arxiv.org/search/cs?searchtype=author&query=Cai,+C+J)
- [Meredith Ringel Morris](https://arxiv.org/search/cs?searchtype=author&query=Morris,+M+R)
- [Percy Liang](https://arxiv.org/search/cs?searchtype=author&query=Liang,+P)
- [Michael S. Bernstein](https://arxiv.org/search/cs?searchtype=author&query=Bernstein,+M+S)

---

## Key Excerpt: Abstract

> Believable proxies of human behavior can empower interactive applications ranging from immersive environments to rehearsal spaces for interpersonal communication to prototyping tools. In this paper, we introduce generative agents--computational software agents that simulate believable human behavior. Generative agents wake up, cook breakfast, and head to work; artists paint, while authors write; they form opinions, notice each other, and initiate conversations; they remember and reflect on days past as they plan the next day. To enable generative agents, we describe an architecture that extends a large language model to store a complete record of the agent's experiences using natural language, synthesize those memories over time into higher-level reflections, and retrieve them dynamically to plan behavior. We instantiate generative agents to populate an interactive sandbox environment inspired by The Sims, where end users can interact with a small town of twenty five agents using natural language. In an evaluation, these generative agents produce believable individual and emergent social behaviors: for example, starting with only a single user-specified notion that one agent wants to throw a Valentine's Day party, the agents autonomously spread invitations to the party over the next two days, make new acquaintances, ask each other out on dates to the party, and coordinate to show up for the party together at the right time. We demonstrate through ablation that the components of our agent architecture--observation, planning, and reflection--each contribute critically to the believability of agent behavior. By fusing large language models with computational, interactive agents, this work introduces architectural and interaction patterns for enabling believable simulations of human behavior.

---

## Core Contribution

This paper introduces **generative agents**: computational software agents powered by large language models that simulate believable human-like behavior in an interactive environment.

The agents are designed to:

- Wake up and follow daily routines
- Cook, go to work, paint, write, and perform occupational tasks
- Notice and interact with other agents
- Form opinions
- Initiate conversations
- Remember past events
- Reflect on experiences
- Plan future behavior
- Produce emergent social coordination without explicit scripting

---

## Technical Architecture

The paper describes an architecture that extends a **large language model** with mechanisms for:

1. **Observation**
   - Agents perceive events and activities in their environment.
   - Observations are stored as natural-language memory records.

2. **Memory Storage**
   - Each agent maintains a complete record of its experiences.
   - Memories are represented in natural language.

3. **Reflection**
   - Agents synthesize accumulated memories into higher-level conclusions.
   - These reflections help create coherent longer-term behavior.

4. **Dynamic Retrieval**
   - Relevant memories and reflections are retrieved when planning or acting.
   - This enables agents to respond based on past experiences rather than isolated prompts.

5. **Planning**
   - Agents use retrieved memories and reflections to generate plans.
   - Planning supports believable daily schedules and socially coordinated behavior.

The abstract specifically emphasizes that **observation, planning, and reflection** are critical components validated through ablation studies.

---

## Simulation Environment

The authors instantiate the agents in an **interactive sandbox environment inspired by *

[... summary truncated for context management ...]
