---
title: LLM Wiki / Agent Memory 研究框架
created: 2026-05-16
updated: 2026-05-16
type: concept
tags: [llm-wiki, agent-memory, context-engineering, knowledge-integration]
sources: [../concepts/llm-wiki-agent-memory-research-framework.md]
confidence: medium
contested: true
---

# LLM Wiki / Agent Memory 研究框架

这是英文核心研究框架的中文页面。英文原文仍保留在：

- [/concepts/llm-wiki-agent-memory-research-framework](/concepts/llm-wiki-agent-memory-research-framework)

## 核心观点

LLM Wiki / Agent Memory 的目标不是无限保存对话历史，而是把来源、证据、概念、决策和可复用流程整理成可审计、可维护、可检索的知识结构。

## 关键原则

- Raw sources 与 wiki/concept synthesis 必须分离。
- Raw sources 是不可变证据层；concept pages 是可变综合层。
- Agent memory 应该小而稳，只保存能减少未来 steering 的事实、偏好和约定。
- 大型研究知识应进入 markdown+git 知识库，而不是黑盒长期记忆。
- 检索不是消费；检索只是候选生成，最终应构造最小充分 working set。

## 相关中文页面

- [Hermes + Obsidian 个人知识库方案](hermes-obsidian-personal-knowledge-base-plan.md)
