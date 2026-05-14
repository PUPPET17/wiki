---
source_url: https://news.ycombinator.com/item?id=46294274
fetched_url: https://news.ycombinator.com/item?id=46294274
source_type: hn
author: Hacker News commenters + Letta author comments
source_date: 2025
ingested: 2026-05-14
sha256: 83094c7e2c7f28e2f75ce8072948fb837e8ba23f5ae3c1298162b1c0b1da2948
raw_preservation: tool_parsed_or_summarized_text
---

# Hn Letta Code 2025

## Source Metadata

- Source URL: https://news.ycombinator.com/item?id=46294274
- Fetched URL: https://news.ycombinator.com/item?id=46294274
- Source type: hn
- Author: Hacker News commenters + Letta author comments
- Source date: 2025
- Ingested: 2026-05-14
- Reliability: medium
- Raw preservation status: tool_parsed_or_summarized_text
- Extraction note: Parsed source text is preserved below where accessible. If extraction tooling returned a summary/truncated representation, this is explicitly marked and should be replaced by fuller text in a later pass.

## Parsed Source Text

# Letta Code | Hacker News

**Source:** https://news.ycombinator.com/item?id=46294274  
**HN stats:** 83 points, 37 comments

## What the post is about
**Letta Code** is an open-source, **memory-first coding harness** for CLI-based coding agents. It is positioned as:

- **#1 model-agnostic OSS on Terminal-Bench**
- **#4 overall** on Terminal-Bench
- Designed for using the **same coding agent continuously**, so it can build long-term learned context about:
  - you
  - your codebase
  - your organization

It is also described as being able to run **completely locally** when paired with the Letta Docker image.

---

## Key excerpts

> “It's specifically designed to be ‘memory-first’ - the idea is that you use the same coding agents perpetually, and have them build learned context (memory) about you / your codebase / your org over time.”

> “There are some built-in memory tools like `/init` and `/remember` to help guide this along (if your agent does something stupid, you can 'whack it' with /remember). There's also a `/clear` command, which resets the message buffer, but keeps the learned context / memory inside the context window.”

> “We built this for ourselves - Letta Code co-authors the majority of PRs on the letta-code GitHub repo.”

> “The entire thing is OSS and designed to be super hackable, and can run completely locally when combined with the Letta docker image.”

---

## Important commands / links

### Commands
```bash
/npm install -g @letta-ai/letta-code
```

```bash
letta -p "Do something dangerous (it's just a sandbox, after all)" --yolo
```

### Built-in memory tools
```text
/init
/remember
/clear
```

### Links mentioned
- Permissions docs: https://docs.letta.com/letta-code/permissions
- Skill learning article: https://www.letta.com/blog/skill-learning
- MemGPT reference: https://research.memgpt.ai/

---

## Main discussion themes

### 1. Memory in coding agents: useful or overhyped?
Several commenters questioned whether long-term memory is actually helpful for coding work.

**Skeptical view:**
- Project docs, feature specs, and style guides already capture most needed context.
- Maintaining memory can become a burden.
- There is a risk of **context poisoning** or storing bad/irrelevant habits.
- Some argued ChatGPT-style memory often fills with garbage or stale preferences.

**Supportive view:**
- Memory helps agents avoid repeating mistakes.
- It can capture **tribal knowledge** that is hard to encode in docs.
- It may be better for **learned preferences** than for strict procedural knowledge.
- Unlike black-box memory systems, Letta’s memory is described as **transparent and controllable**.

---

### 2. White-box memory vs black-box memory
A key distinction raised in the thread:

- **ChatGPT-style memory** was criticized as opaque and hard to manage.
- Letta’s memory was described as **text/file-based and inspectable**.
- One commenter emphasized that you can see:
  - every raw LLM request
  - exactly how memory affects the final prompt payload

This transparency was presented as a major advantage because users can modify or debug memory directly.

---

### 3. How Letta’s memory is structured
Responding to questions, Letta Code’s memory was described as:

- Based on the **MemGPT reference architecture**
- A small set of **memory blocks**
- Stored as system-prompt context
- Modifiable through tools
- Similar to a **“living CLAUDE.md”** that follows the agent around

When starting Letta Code and running `/init`, it can:

- scan for `AGENTS.md` / `CLAUDE.md`
- ingest those files into memory blocks

This makes it interoperable with existing repo-based instructions.

---

### 4. Comparison with CLAUDE.md / AGENTS.md / project docs
There was a strong comparison between Letta memory and conventional repo instructions:

- Some users prefer a local `llm.md` / `CLAUDE.md` / `AGENTS.md`
- Others argued Letta memory is effectively a more dynamic version of that
- One commenter said their own workflow involves:
  - a custom tool that merges code into one prompt
  - a project-specific `llm.md`
  - explicit instructions for LLM behavior
  - examples of good/bad notes
  - editable notes on project quirks

The discussion suggested Letta is most useful when memory is treated as an explicit, controllable artifact rather than invisible state.

---

### 5. Benchmarking and Cursor comparisons
A thread branch asked why **Cursor** wasn’t on Terminal-Bench.

Letta’s representative replied:

- Cursor CLI likely isn’t listed because Cursor focuses mainly on its **IDE agent**, not CLI
- Terminal-Bench is specifically for **CLI agents**
- If you want a quantitative proxy for “how good is this harness+agent combo at coding,” **Terminal-Bench** was suggested as the best current benchmark
- They noted **SWE-Bench** used to be the preferred proxy, but T-Bench is now better for this purpose

They also said Letta Code’s results are already public and reproducible.

---

### 6. Real-world workflow and model recommendations
Le

[... summary truncated for context management ...]
