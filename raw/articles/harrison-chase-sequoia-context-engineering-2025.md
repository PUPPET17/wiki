---
source_url: https://sequoiacap.com/podcast/context-engineering-our-way-to-long-horizon-agents-langchains-harrison-chase/
fetched_url: https://sequoiacap.com/podcast/context-engineering-our-way-to-long-horizon-agents-langchains-harrison-chase/
source_type: interview
author: Harrison Chase / Sequoia
source_date: 2025
ingested: 2026-05-14
sha256: 905c15b7eac70827a6b7d7cb2e2a58d71aa59b4355a6bc8331cfd3bb4f1fa90c
raw_preservation: tool_parsed_or_summarized_text
---

# Harrison Chase Sequoia Context Engineering 2025

## Source Metadata

- Source URL: https://sequoiacap.com/podcast/context-engineering-our-way-to-long-horizon-agents-langchains-harrison-chase/
- Fetched URL: https://sequoiacap.com/podcast/context-engineering-our-way-to-long-horizon-agents-langchains-harrison-chase/
- Source type: interview
- Author: Harrison Chase / Sequoia
- Source date: 2025
- Ingested: 2026-05-14
- Reliability: medium-high
- Raw preservation status: tool_parsed_or_summarized_text
- Extraction note: Parsed source text is preserved below where accessible. If extraction tooling returned a summary/truncated representation, this is explicitly marked and should be replaced by fuller text in a later pass.

## Parsed Source Text

# LangChain’s Harrison Chase: Context Engineering Our Way to Long-Horizon Agents — Summary

**Source:** Sequoia Capital / *Training Data* podcast  
**Title:** “Context Engineering Our Way to Long-Horizon Agents: LangChain’s Harrison Chase”  
**Guest:** Harrison Chase, cofounder of LangChain  
**Hosts:** Sonya Huang and Pat Grady  
**Core topic:** Why long-horizon AI agents are beginning to work, how agent harnesses and context engineering matter as much as model quality, and how agent development differs from traditional software development.

---

## Executive Summary

Harrison Chase argues that **long-horizon agents**—LLMs running in loops over extended periods, autonomously choosing actions and using tools—are finally becoming practically useful. The core agent idea existed in early systems like AutoGPT, but models and surrounding infrastructure were not good enough. Today, improved reasoning models plus more sophisticated **agent harnesses** have made agents effective in domains such as **coding, SRE, research, finance, and customer support**.

A major theme is that progress is not just about better models. The surrounding architecture—the **harness**—has become critical. Harnesses include opinionated scaffolding such as planning tools, compaction strategies, file-system access, subagents, MCP integrations, prompts, and context-management techniques. Chase describes this broader discipline as **context engineering**, saying it captures much of what LangChain has been building.

Agent development differs fundamentally from traditional software because much of the behavior lives not in code but in the model, prompts, tools, and evolving context. As a result, **traces** become a core artifact and partial “source of truth.” Developers cannot fully understand agent behavior by reading code; they need to inspect what context the agent had at each step and what decisions it made.

Looking forward, Chase sees **memory**, **file systems**, **async/sync agent management**, and **self-improving agents** as key areas. He expects agents to increasingly learn from traces, update their own instructions, and improve over time, though usually with humans reviewing first drafts or changes.

---

## Key Excerpts

### On why traces matter more for agents than ordinary LLM apps

> **Harrison Chase:** _People use traces from the start to just tell what’s going on under the hood. And it’s way more impactful in agents than in single LLM applications. Because in single LLM applications you get some bad response from the LLM, you know exactly what your prompt is, you know exactly what the context that goes in is because that’s determined by code, and then you get something out. In agents, they’re running and repeating. And so you don’t actually know what the context at step 14 will be, because there’s 13 steps before that that could pull arbitrary things in. So, like, what exactly is—everything’s context engineering. Context engineering is such a good term. I wish I came up with that term. Like, it actually really describes everything we’ve done at LangChain without knowing that that term existed. But, like, traces just like tell you what’s in your context. And that’s so important._

---

### On long-horizon agents finally working

> **Harrison Chase:** I mean, I agree that they’re starting to finally work. I think, like, the idea of running an LLM in a loop and just having it go was always the idea of agents from the start—AutoGPT was basically this. Then this is why it took off and captured so many people’s imagination, because it was just an LLM running in a loop, completely deciding what to do. The issue is the models weren’t really good enough, and the scaffolding and harnesses around them weren’t really good enough.

---

### On first-draft use cases as today’s killer applications

> **Harrison Chase:** And the issue with agents is they aren’t reliable to nine nines of reliability, but they can do a ton of work, and more and more work over longer time horizons. So if you can find these framings where they run for a long period of time but produce, like, a first draft of something, those to me are the killer applications of long-horizon agents right now.

---

### On models vs. frameworks vs. harnesses

> **Harrison Chase:** So a model is obviously the LLMs, tokens, messages in, messages out. The framework would be abstractions around that, so making it easy to switch between models, adding abstractions for other things like tools and vector stores, memory and things like that, but pretty unopinionated about what actually goes in there.  
>
> Harnesses are more like batteries included.

---

### On building agents vs. building software

> **Harrison Chase:** When you’re building software, all of the logic is in the code, in the software, and you can see it there. When you’re building an agent, the logic for how your application works is not all in the code. A large part of it comes from the model. And so what this means is 

[... summary truncated for context management ...]
