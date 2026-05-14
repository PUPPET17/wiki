---
source_url: https://www.anthropic.com/engineering/built-multi-agent-research-system
fetched_url: https://www.anthropic.com/engineering/built-multi-agent-research-system
source_type: blog
author: Anthropic
source_date: 2025-06-13
ingested: 2026-05-14
sha256: 687e40047227018541a9b2d9225ba9f5ac2deb90fbe1a33bd95ebca3c160626d
raw_preservation: tool_parsed_or_summarized_text
---

# Anthropic Multi Agent Research 2025

## Source Metadata

- Source URL: https://www.anthropic.com/engineering/built-multi-agent-research-system
- Fetched URL: https://www.anthropic.com/engineering/built-multi-agent-research-system
- Source type: blog
- Author: Anthropic
- Source date: 2025-06-13
- Ingested: 2026-05-14
- Reliability: high
- Raw preservation status: tool_parsed_or_summarized_text
- Extraction note: Parsed source text is preserved below where accessible. If extraction tooling returned a summary/truncated representation, this is explicitly marked and should be replaced by fuller text in a later pass.

## Parsed Source Text

# How Anthropic Built Its Multi-Agent Research System

**Source:** Anthropic Engineering  
**Published:** Jun 13, 2025  
**Topic:** Architecture, prompting, evaluation, and production lessons from building Claude’s multi-agent Research feature.

---

## Core Idea

Anthropic’s **Research** feature uses a **multi-agent system**: multiple Claude agents autonomously use tools in loops and collaborate to investigate complex topics.

The system is designed for open-ended research tasks where the path cannot be hardcoded in advance. A **lead agent** plans the research process and delegates parallel work to **subagents**, which search across the web, Google Workspace, and integrations.

> “A multi-agent system consists of multiple agents (LLMs autonomously using tools in a loop) working together.”

> “Our Research feature involves an agent that plans a research process based on user queries, and then uses tools to create parallel agents that search for information simultaneously.”

---

## Why Multi-Agent Systems Help with Research

Research is dynamic, path-dependent, and often impossible to solve with a fixed pipeline. Good research requires following leads, changing strategies, and exploring tangential connections.

### Key Benefits

- **Parallel exploration:** Subagents investigate different aspects simultaneously.
- **Context-window scaling:** Each subagent has its own context window.
- **Compression:** Subagents search through large information spaces and return condensed findings.
- **Separation of concerns:** Different agents can use distinct tools, prompts, and investigation strategies.
- **Reduced path dependency:** Independent investigations avoid overcommitting to one search trajectory.
- **Better breadth-first search:** Especially useful for queries with many independent directions.

> “The essence of search is compression: distilling insights from a vast corpus.”

> “Subagents facilitate compression by operating in parallel with their own context windows, exploring different aspects of the question simultaneously before condensing the most important tokens for the lead research agent.”

---

## Performance Findings

Anthropic reports major gains from multi-agent research compared with single-agent research.

### Internal Eval Result

> “We found that a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval.”

Example task:

- Query: identify all board members of companies in the Information Technology S&P 500.
- Multi-agent system succeeded by decomposing the task across subagents.
- Single-agent system failed due to slow sequential searches.

### BrowseComp Analysis

Anthropic analyzed performance on **BrowseComp**, an evaluation for browsing agents locating hard-to-find information.

They found that three factors explained **95% of performance variance**:

1. **Token usage** — alone explained **80%** of variance.
2. **Number of tool calls**
3. **Model choice**

> “Multi-agent systems work mainly because they help spend enough tokens to solve the problem.”

> “Multi-agent architectures effectively scale token usage for tasks that exceed the limits of single agents.”

### Model Efficiency

Upgrading the model can outperform simply increasing token budget:

> “Upgrading to Claude Sonnet 4 is a larger performance gain than doubling the token budget on Claude Sonnet 3.7.”

---

## Cost and Fit Tradeoffs

Multi-agent systems are powerful but expensive.

### Token Costs

> “In our data, agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats.”

### Best Fit

Multi-agent systems are best for tasks with:

- High task value
- Heavy parallelization
- Information exceeding a single context window
- Many complex tools or data sources
- Breadth-first investigation needs

### Poor Fit

They are less suitable when:

- All agents must share the same context.
- Tasks have many dependencies between agents.
- Work is not easily parallelizable.

Example:

> “Most coding tasks involve fewer truly parallelizable tasks than research, and LLM agents are not yet great at coordinating and delegating to other agents in real time.”

---

## Architecture Overview

Anthropic uses an **orchestrator-worker pattern**.

### Main Components

- **User query**
- **LeadResearcher / lead agent**
  - Analyzes query
  - Plans strategy
  - Saves plan to memory
  - Spawns subagents
  - Synthesizes findings
  - Decides whether more research is needed
- **Subagents**
  - Receive specialized research tasks
  - Search independently
  - Use tools and interleaved thinking
  - Return findings to lead agent
- **CitationAgent**
  - Processes documents and research report
  - Identifies source locations for citations
  - Ensures claims are attributed

### Workflow

1. User submits query.
2. Lead agent analyzes task and creates a research plan.
3. Plan is saved to memory to s

[... summary truncated for context management ...]
