---
source_url: https://www.langchain.com/blog/context-engineering-for-agents
fetched_url: https://www.langchain.com/blog/context-engineering-for-agents
source_type: blog
author: LangChain Team
source_date: 2025-07-02
ingested: 2026-05-14
sha256: 757f3ed5ac907b350a7f3685797bd339cd19248c9bc2ab34f77ebb34b798b68f
raw_preservation: tool_parsed_or_summarized_text
---

# Langchain Context Engineering 2025

## Source Metadata

- Source URL: https://www.langchain.com/blog/context-engineering-for-agents
- Fetched URL: https://www.langchain.com/blog/context-engineering-for-agents
- Source type: blog
- Author: LangChain Team
- Source date: 2025-07-02
- Ingested: 2026-05-14
- Reliability: medium-high
- Raw preservation status: tool_parsed_or_summarized_text
- Extraction note: Parsed source text is preserved below where accessible. If extraction tooling returned a summary/truncated representation, this is explicitly marked and should be replaced by fuller text in a later pass.

## Parsed Source Text

# Context Engineering — LangChain Blog Summary

**Source:** https://www.langchain.com/blog/context-engineering-for-agents  
**Author:** The LangChain Team  
**Date:** July 2, 2025  
**Read time:** 14 min  
**Topic areas:** Agents, LangGraph, LangSmith, context management

---

## TL;DR

Agents need carefully managed context to perform long-running tasks effectively. **Context engineering** is the practice of deciding what information should enter, remain outside, be compressed within, or be separated from an LLM’s context window at each step of an agent’s trajectory.

The article groups common context engineering strategies into four categories:

- **Write context** — save information outside the context window.
- **Select context** — retrieve relevant information into the context window.
- **Compress context** — reduce context to only the tokens needed.
- **Isolate context** — split context across agents, environments, or state fields.

LangGraph is presented as a framework designed to support these strategies, while LangSmith helps observe, evaluate, and iterate on context usage.

---

## Core Definition: Context Engineering

The article frames LLMs as similar to operating systems:

- The **LLM** is like a CPU.
- The **context window** is like RAM.
- Context engineering plays the role of deciding what fits into working memory.

Key quote from Andrej Karpathy:

> _\[Context engineering is the\] ”…delicate art and science of filling the context window with just the right information for the next step.”_

### Main Types of Context in LLM Applications

Context engineering applies across several kinds of information:

- **Instructions** — prompts, memories, few-shot examples, tool descriptions, etc.
- **Knowledge** — facts, memories, retrieved data, etc.
- **Tools** — feedback and outputs from tool calls.

---

## Why Context Engineering Matters for Agents

Agents increasingly rely on:

- Reasoning
- Tool calling
- Long-running workflows
- Iterative loops of LLM calls and tool calls

Agents often accumulate large amounts of tool feedback and conversation history over many steps. This creates several risks:

- Exceeding the model’s context window
- Increased cost
- Higher latency
- Degraded performance
- Confusing or contradictory behavior

### Failure Modes of Long Context

The article references Drew Breunig’s taxonomy of context failures:

- **Context Poisoning:** When a hallucination makes it into the context.
- **Context Distraction:** When the context overwhelms the training.
- **Context Confusion:** When superfluous context influences the response.
- **Context Clash:** When parts of the context disagree.

### Importance for Agent Builders

Cognition emphasized the centrality of this work:

> _“Context engineering” … is effectively the #1 job of engineers building AI agents._

Anthropic similarly noted:

> _Agents often engage in conversations spanning hundreds of turns, requiring careful context management strategies._

---

# The Four Main Context Engineering Strategies

---

## 1. Write Context

**Definition:**

> _Writing context means saving it outside the context window to help an agent perform a task._

Writing context allows an agent to persist useful information without keeping everything in the active prompt.

---

### Scratchpads

A **scratchpad** is a temporary place for an agent to store notes, plans, intermediate results, or useful facts during a task.

Anthropic’s multi-agent researcher uses this pattern:

> _The LeadResearcher begins by thinking through the approach and saving its plan to Memory to persist the context, since if the context window exceeds 200,000 tokens it will be truncated and it is important to retain the plan._

Scratchpads can be implemented as:

- A tool call that writes to a file
- A field in a runtime state object
- A persistent session/thread-level store

They help agents retain information across steps without overloading the active context window.

---

### Memories

Scratchpads usually help within a single session or thread. **Memories** help across many sessions.

Referenced memory-related systems and ideas:

- **Reflexion** — agents reflect after each turn and reuse self-generated memories.
- **Generative Agents** — synthesize memories periodically from past feedback.
- **ChatGPT Memory**
- **Cursor Memories**
- **Windsurf Memories**

These systems allow agents to generate and persist long-term memories based on user-agent interactions.

---

## 2. Select Context

**Definition:**

> _Selecting context means pulling it into the context window to help an agent perform a task._

Once information has been written or stored, the agent must decide what to retrieve and expose to the LLM.

---

### Selecting from Scratchpads

Selection depends on implementation:

- If the scratchpad is a **tool**, the agent can read it through a tool call.
- If the scratchpad is part of **runtime state**, the developer controls which fields are exposed at each step.

This gives develop

[... summary truncated for context management ...]
