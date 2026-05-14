---
source_url: https://docs.letta.com/letta-code/memory
fetched_url: https://docs.letta.com/letta-code/memory
source_type: product-docs
author: Letta
source_date: captured 2026-05-14
ingested: 2026-05-14
sha256: 1ea16ba70fe11c99bb68212aa62d0bae24068d59f764e3f2fc9a2f03d0e3fbdd
raw_preservation: tool_parsed_or_summarized_text
---

# Letta Memory 2026

## Source Metadata

- Source URL: https://docs.letta.com/letta-code/memory
- Fetched URL: https://docs.letta.com/letta-code/memory
- Source type: product-docs
- Author: Letta
- Source date: captured 2026-05-14
- Ingested: 2026-05-14
- Reliability: high
- Raw preservation status: tool_parsed_or_summarized_text
- Extraction note: Parsed source text is preserved below where accessible. If extraction tooling returned a summary/truncated representation, this is explicitly marked and should be replaced by fuller text in a later pass.

## Parsed Source Text

# Memory — Letta Docs Summary

Source: <https://docs.letta.com/letta-code/memory>

## Overview

Letta Code provides a **self-improving memory system** where you use the same agent indefinitely across sessions, days, or months. The agent can:

- Remember past interactions
- Learn user preferences
- Self-edit its own memory while working
- Improve over time
- Maintain personalized behavior and identity

Unlike Claude Code or Codex, where users generally interact with the same standardized agent behavior, Letta Code supports **deep personalization** of agents.

> With Letta Code, you use the same agent indefinitely - across sessions, days, or months - and have it get better over time.

> With Letta Code, you can deeply personalize your agents to be unique to _you_.

---

## Agents and Conversations

Letta Code has two core session concepts:

### Agent

An **agent** is an entity with:

- A name
- Memories
- A model configuration
- Messages
- Other persistent state

### Conversation

A **conversation** is a message thread or session with an agent.

Key details:

- A single agent can have many parallel conversations.
- Every agent has a **default conversation**, also called the **main chat**.
- Running the `letta` CLI command inside a project directory resumes the default conversation with the last used agent.
- In the desktop app, the left sidebar is sorted by agents, with conversations sorted by activity date.

### Starting Parallel CLI Sessions

To run multiple CLI sessions with the same agent in parallel, such as in separate terminal windows:

```bash
letta --new
```

In the desktop app, start a new conversation by pressing the **notepad icon**.

### Managing Agents

Letta Code includes a default pre-installed agent called **“Letta Code.”**

Useful commands and actions:

- Swap agents in the CLI:

```bash
/agents
```

- Favorite an agent in the CLI:

```bash
/pin
```

- Favorite an agent in the desktop app by clicking the favorites button.

---

## Initializing Your Agent’s Memory

Use `/init` to initialize or refresh the agent’s memory in the main conversation.

```bash
/init
```

During initialization, Letta Code performs an interactive process guided by **context constitution principles** for:

- Durable identity
- User preferences
- Project structure

Letta Code can also read from prior **Claude Code** and **OpenAI Codex** sessions to learn about:

- Your working style
- Past projects
- Ongoing projects

This is done using Letta Code [subagents](https://docs.letta.com/letta-code/subagents).

### When to Run `/init` Again

Run `/init` again when you want the agent to re-analyze your project, such as after:

- Major project changes
- Adding important documentation
- Introducing new information you want the agent to ingest

### Auditing Memory with `/doctor`

If the memory structure becomes messy or drifts over time, use:

```bash
/doctor
```

`/doctor` audits the current memory layout and refines it for:

- Proper memory placement
- Efficient token usage

---

## Manually Triggering Memory Updates

Letta Code agents can self-edit memory automatically based on conversation context. For example, the agent may store new information learned during a session.

You can also explicitly direct the agent to remember something using:

```bash
/remember
```

Example:

```text
> /remember not to make that mistake again
```

You can also run `/remember` without extra prompting. In that case, the agent infers your intent from the current conversation context and makes an appropriate memory edit.

---

## Configuring Dreaming / Reflection

Letta Code supports proactive memory creation and consolidation through periodic **sleep-time**, or **dream**, subagents.

These reflection subagents:

- Run in the background
- Review recent conversations and interactions
- Perform thorough memory editing
- May run for many steps because they are designed to be comprehensive

### Configure Reflection

In the CLI, use:

```bash
/sleeptime
```

In the desktop app, click the **sleeping alien icon** in the bottom-right corner.

### Dream Trigger Options

The **trigger** controls how often reflection subagents are automatically launched:

- `Off`: disables reflection subagents
- `Step count`: launches a reflection subagent every N user messages
- `Compaction event` **recommended, MemFS only**: launches a reflection subagent when the context window is compacted or summarized

When a dream trigger fires, Letta Code automatically launches the dream subagent in the background.

---

## How Letta Code’s Memory System Works

Letta Code stores agent memory in **MemFS**, short for **memory filesystem**.

MemFS is:

- A git-backed filesystem
- Also called a [context repository](https://www.letta.com/blog/context-repositories)
- Organized as a directory of markdown files
- Cloned locally to:

```text
~/.letta/agents/<your-agent-id>/memory
```

The agent edits memory files directly using bash tools, then commits and pushes changes to save them.

This 

[... summary truncated for context management ...]
