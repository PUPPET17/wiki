---
source_url: https://www.anthropic.com/research/building-effective-agents
fetched_url: https://www.anthropic.com/research/building-effective-agents
source_type: blog
author: Anthropic
source_date: 2024-12-19
ingested: 2026-05-14
sha256: fb9d01e03848f47c39a318fbd662f3974df7a2722031bf6daa9ddfff77384743
raw_preservation: tool_parsed_or_summarized_text
---

# Anthropic Effective Agents 2024

## Source Metadata

- Source URL: https://www.anthropic.com/research/building-effective-agents
- Fetched URL: https://www.anthropic.com/research/building-effective-agents
- Source type: blog
- Author: Anthropic
- Source date: 2024-12-19
- Ingested: 2026-05-14
- Reliability: high
- Raw preservation status: tool_parsed_or_summarized_text
- Extraction note: Parsed source text is preserved below where accessible. If extraction tooling returned a summary/truncated representation, this is explicitly marked and should be replaced by fuller text in a later pass.

## Parsed Source Text

# Building Effective AI Agents — Anthropic Summary

**Source:** Anthropic Engineering / Research  
**Published:** Dec 19, 2024  
**Core thesis:** The most successful LLM agent implementations are usually **simple, composable systems**, not complex frameworks.

> “Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns.”

---

## 1. Core Definitions: Workflows vs. Agents

Anthropic uses the umbrella term **agentic systems** for both structured workflows and autonomous agents, but makes an important architectural distinction:

> - **Workflows** are systems where LLMs and tools are orchestrated through predefined code paths.
> - **Agents**, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

### Practical distinction

| Type | Control flow | Best for |
|---|---|---|
| **Workflow** | Predefined by code | Predictable, well-defined tasks |
| **Agent** | Dynamically controlled by the LLM | Open-ended tasks requiring flexible decision-making |

---

## 2. When — and When Not — to Use Agents

Anthropic recommends starting with the **simplest possible solution**.

> “When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed.”

### Key guidance

- Do **not** default to agentic systems.
- Agentic systems often trade:
  - **Higher latency**
  - **Higher cost**
  - for **better task performance**
- Many applications can be solved with:
  - A single LLM call
  - Retrieval
  - In-context examples
  - Prompt optimization

### When complexity is warranted

- Use **workflows** when the task is well-defined and predictability matters.
- Use **agents** when the task requires flexibility, tool use, and model-driven decisions at scale.

---

## 3. Frameworks: Useful, But Be Careful

Anthropic lists several frameworks that help build agentic systems:

- [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview)
- [Strands Agents SDK by AWS](https://strandsagents.com/latest/)
- [Rivet](https://rivet.ironcladapp.com/) — drag-and-drop GUI LLM workflow builder
- [Vellum](https://www.vellum.ai/) — GUI tool for building and testing complex workflows

### Benefits of frameworks

They simplify common low-level tasks:

- Calling LLMs
- Defining tools
- Parsing tool calls
- Chaining LLM calls together

### Risks of frameworks

Frameworks can introduce abstraction layers that:

- Obscure prompts and responses
- Make debugging harder
- Encourage unnecessary complexity
- Lead to incorrect assumptions about what is happening under the hood

> “We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code.”

**Recommendation:** If using a framework, make sure you understand the underlying code.

---

# 4. Core Building Block: The Augmented LLM

The foundational component of agentic systems is an **LLM augmented with capabilities** such as:

- Retrieval
- Tools
- Memory

Modern models can actively use these capabilities by:

- Generating search queries
- Selecting appropriate tools
- Deciding what information to retain

### Implementation advice

Focus on:

1. **Tailoring capabilities to the use case**
2. **Providing an easy, well-documented interface for the LLM**

Anthropic highlights the [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) as one way to integrate tools through a standardized interface.

---

# 5. Workflow Patterns

Anthropic describes several common production patterns, increasing in complexity from simple workflows to autonomous agents.

---

## 5.1 Prompt Chaining

**Prompt chaining** breaks a task into a sequence of steps, where each LLM call processes the previous call’s output.

Programmatic checks or “gates” can be added between steps to verify quality or ensure the process remains on track.

### When to use

Use prompt chaining when:

- The task can be cleanly decomposed into fixed subtasks
- You want higher accuracy
- You can tolerate increased latency
- Each LLM call can be made simpler and more focused

### Examples

- Generate marketing copy, then translate it into another language.
- Write a document outline, check whether it meets criteria, then write the full document.

---

## 5.2 Routing

**Routing** classifies an input and sends it to a specialized downstream task, prompt, model, or tool.

This allows separation of concerns and helps avoid one prompt being forced to handle many unrelated cases.

### When to use

Routing works well when:

- Inputs fall into distinct categories
- Each category benefits from specialized handling
- Classification can be done accurately by an LLM, classifier, or algorithm

### Examples

- Route customer service queries into:
  - General questions
  - Refund requests
  - Technical support
- Route simple 

[... summary truncated for context management ...]
