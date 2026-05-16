---
title: Hermes + Obsidian 个人知识库方案
created: 2026-05-16
updated: 2026-05-16
type: concept
tags: [agent-memory, obsidian, hermes, knowledge-integration, local-first, memory-architecture]
sources: [../concepts/hermes-obsidian-personal-knowledge-base-plan.md]
confidence: medium
contested: true
---

# Hermes + Obsidian 个人知识库方案

这是英文方案文档的中文页面。英文原文仍保留在：

- [/concepts/hermes-obsidian-personal-knowledge-base-plan](/concepts/hermes-obsidian-personal-knowledge-base-plan)

## 总目标

构建一个 local-first 的个人知识库：Obsidian 是人类可见、可编辑、可审查的工作区；Hermes 是研究、摄取、检索、综合、lint、维护和自动化层。

## 核心架构

- markdown + git 是 canonical store。
- Obsidian 负责人工阅读、编辑、backlinks、properties、Bases/Dataview 和 review。
- Hermes 负责 ingest、query、synthesize、lint、working set assembly 和维护任务。
- SQLite FTS/BM25、embedding、graph view、MCP/REST 都是可重建的派生索引，不是唯一真相来源。

## 关键原则

1. Obsidian 是 canonical workspace，Hermes 是 operator。
2. Raw sources、concept notes、decision notes、procedures、session summaries 必须区分。
3. Raw sources 是证据层，不允许用摘要替代原始文本或可定位 artifact。
4. Hermes built-in memory 只保存小型稳定 steering facts。
5. Session 不是长期知识，而是候选知识的临时容器。

## Memory pipeline

```text
interaction
    ↓
working context
    ↓
temporary scratch
    ↓
candidate extraction
    ↓
entropy filter
    ↓
durable knowledge
    ↓
retrieval index
```

## Session half-life

Session half-life 不是 30 天后删除，而是动态降低 retrieval priority：

- Active：新 session 可参与 scoped retrieval。
- Decaying：超过 half-life 后 retrieval_weight 衰减。
- Archive candidate：已 canonicalized、长期未检索/引用、超过阈值后成为归档候选。
- Compression：把 episodic record 压缩成 semantic outcome。
- Deletion：极少发生，必须人工确认。

## Working Set Assembly v1

Working Set Assembly 是一个确定性 pipeline：把 scoped retrieval results 转换成 role-separated、token-budgeted、semantically compressed 的 LLM reasoning context。

核心步骤：

1. Retrieve：lexical search + structured filter + optional semantic search。
2. Rank：固定 scoring function。
3. Cluster：cluster 是 meaning unit。
4. Compress：保留结论、冲突和 source pointers。
5. Deduplicate：去除重复 note / repeated fact。
6. Isolate by Role：system/project/knowledge/evidence/task 分区。
7. Assemble：按 token budget 组装最小充分上下文。

## MVP 建议

- 先使用 `/Users/a17/wiki` 作为 standalone Obsidian/VitePress research vault。
- 不要一开始引入 vector DB。
- 使用 markdown+git、frontmatter、search_files、VitePress、Obsidian search 作为第一阶段。
- 所有 completed knowledge changes 本地 commit；只有用户明确要求时 push。
