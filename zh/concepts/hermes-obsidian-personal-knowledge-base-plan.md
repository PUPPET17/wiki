---
title: Hermes Obsidian Personal Knowledge Base Plan
created: 2026-05-14
updated: 2026-05-16
type: concept
tags: [agent-memory, llm-wiki, obsidian, hermes, knowledge-integration, local-first, memory-architecture, retrieval, indexing, mvp, personal-ai-os]
sources: [concepts/llm-wiki-agent-memory-research-framework.md, raw/articles/karpathy-llm-wiki-gist-2026.md, raw/github/llm-wiki-compiler-repo-readme.md, raw/github/wuphf-repo-readme.md, raw/github/mem0-issue-4573-memory-audit-junk.md, raw/github/letta-issue-652-per-conversation-context-scoping.md, raw/github/langchain-context-engineering-repo-readme.md, raw/github/langchain-how-to-fix-your-context-readme.md, raw/product-docs/openai-chatgpt-memory-2024-2025.md, raw/product-docs/letta-memory-2026.md, raw/product-docs/obsidian-uri-2026.md, raw/product-docs/obsidian-bases-2026.md, raw/product-docs/obsidian-web-clipper-2026.md, raw/product-docs/obsidian-properties-2026.md, raw/product-docs/hermes-agent-memory-docs-2026.md, raw/product-docs/hermes-agent-memory-providers-docs-2026.md, raw/github/obsidian-local-rest-api-readme.md, raw/github/obsidian-mcp-server-readme.md, raw/github/obsidian-dataview-docs-overview.md]
confidence: medium
contested: true
---

# 爱马仕+黑曜石个人知识库计划

> **对于 Hermes：** 在设计被接受后，使用子代理驱动的开发技能逐项实施该计划。使用黑曜石技能进行保管库文件操作。在更改 Hermes 配置、MCP、内存提供程序、cron、网关或工具集之前，请使用 hermes-agent 技能。

**目标：** 建立一个本地优先的个人知识库，其中 Obsidian 是面向人类的工作空间，Hermes 是代理研究、摄取、检索、合成、lint 和自动化层。

**架构：** 保持 markdown + git 作为规范存储。使用 Obsidian 进行编辑、审阅、反向链接、属性、基础/数据视图视图和手动剪辑。使用 Hermes 获取源代码、维护模式/索引/日志、检索上下文、生成引用的综合、运行质量门以及可选地自动执行后台审查作业。派生索引（例如 SQLite FTS/BM25、嵌入、图形视图和 MCP/REST 集成）是可选的，并且必须可从 markdown 重建。

**技术堆栈：** ObsidianVault、markdown/YAML 属性、git、Hermes 文件/搜索/会话/内存/cron/MCP 工具、可选的 Obsidian 本地 REST API 或 Obsidian MCP 服务器、可选的 Dataview/Bases、可选的 Docsify/GitHub Pages 发布、可选的 SQLite FTS5/BM25 和 sqlite-vec 版本。

---

＃ 执行摘要

近期最好的实施方案是不要用 Hermes 内存取代 Obsidian，也不要将所有对话都转储到 Obsidian。将 Hermes 内置内存视为小型工作内存，将 Obsidian 视为持久的个人知识基底。

Hermes 内存应该只保留紧凑的、高价值的事实，以减少未来的转向：用户偏好、稳定的环境约定和程序教训。 Obsidian 应该拥有更大的语料库：来源、注释、项目决策、文献、个人研究、会议摘要和不断发展的综合。这符合现有的 wiki 结论，即持久代理内存应该是可检查、可编辑、集成​​和可操作的。 [概念/llm-wiki-agent-memory-research-framework.md]

核心实践是三层体系：

1. 捕获层：Obsidian Web Clipper、手动注释、粘贴源、Hermes Web 提取、PDF、会议记录和会话导出。
2. 知识层：带有 frontmatter 的 Markdown 注释、源图、Obsidian 链接、仅附加日志和 git 历史记录。
3. 代理层：用于摄取、查询、合成、lint、审查和计划维护的 Hermes 工作流程。

不要从矢量 DB 开始。从 markdown+git、Obsidian 搜索、Hermes search_files 和可选的 SQLite FTS/BM25 开始。仅在小型评估集显示词法搜索遗漏了重要问题后才添加嵌入。这遵循研究综合：仅向量检索无法精确字符串，而本地优先 markdown+git 提供可检查性和可审查性。 [概念/llm-wiki-agent-memory-research-framework.md]

# 设计原则

## 1. Obsidian 是规范，Hermes 是算子

黑曜石金库文件是真相的来源。 Hermes 可以创建、编辑、lint 和查询它们，但每个重要的编辑都应该作为 markdown diff 可见并提交给 git。

原因：现有研究强调白盒内存、用户控制、可审计性和 git-native 审查。黑匣子内存变得难以检查并且会积累垃圾。 [raw/github/mem0-issue-4573-memory-audit-junk.md] [raw/product-docs/openai-chatgpt-memory-2024-2025.md]

## 2. 单独的内存类别

对于不同的内存类型使用不同的文件夹和架构：

|班级 |目的|规范位置 |爱马仕待遇|
|---|---|---|---|
|用户简介 |持久的偏好和个人事实| `00-system/user-profile.md` 加上 Hermes USER.md 的小子集 |重大变更前询问或确认 |
|项目记忆|项目惯例、决定、状态 | `20-项目/<项目>/` |仅在范围为项目时检索 |
|研究知识|来源、主张、综合 | `30-research/<主题>/` |需要引用的编辑 |
|程序|可重复使用的工作流程 |爱马仕技能+`40程序/` |促进技能稳定程序|
|会议记录|聊天/任务记录和摘要 | `50 个会话/YYYY-MM-DD-*.md` |总结一下，不要自动存储所有详细信息 |
|原材料来源|不可变的源文本/捕获 | `90-sources/` 或主题本地 `raw/` |保留源文本+元数据 |
|私人/敏感 |秘密相关数据或个人数据 | `99-私人/` |默认从自动化/索引中排除 |

这可以防止代理全局内存文件污染不相关的对话并产生隐私/令牌成本问题的 Letta 式问题。 [raw/github/letta-issue-652-per-conversation-context-scoping.md]

## 3. 优先选择编译的 wiki 页面而不是重复的查询时重建

每个有用的研究答案都应该有资格成为持久页面，而不仅仅是聊天响应。这遵循 Karpathy 的 LLM Wiki 模式：原始来源 -> wiki -> 模式，带有摄取/查询/lint 操作。 [原始/文章/karpathy-llm-wiki-gist-2026.md]

## 4. 有用时，按声明粒度使用出处

概念/计划/研究笔记中的每项重要主张都应引用原始笔记或源 URL。对于个人注释，请在适当的情况下引用会话/日期或直接用户断言。

最低引用形式：

```markdown
Claim text. [source-note.md]
```

对于更高面值的纸币：

```markdown
| Claim | Source | Evidence | Confidence | Status |
|---|---|---|---|---|
```

## 5. 将检索到的记忆视为上下文，而不是新证据

当 Hermes 检索一条笔记并随后写入摘要时，它不得像用户重复说过一样重新存储检索到的内容。这直接解决了 mem0 审计中描述的反馈循环放大问题。 [raw/github/mem0-issue-4573-memory-audit-junk.md]

## 6. 默认拒绝高熵瞬态

负内存过滤应包括默认拒绝瞬态的熵过滤器。这里的“熵”并不意味着香农熵。它意味着信息密度对于未来的检索来说价值较低：寿命短、重用性低、依赖于上下文、以后难以解释、令牌昂贵并且可能会污染检索。

高熵内存候选者包括：

1. Shell/工具输出和命令日志。不要存储“Ran: npm install”以及原始输出。当存在持久解决方案时，仅存储持久解决方案，例如“解决方案：包锁损坏导致安装失败；删除锁定文件修复了它。
2.代理思维链或探索性推理痕迹。不要存储“首先我想到了 X，然后可能是 Y”。存储最终的推理、持久的结论以及选择性拒绝的假设（当它们对将来的调试有用时）。
3.反复检索摘录。不要重新存储从检索到的笔记或原始来源复制的段落。这会产生递归放大，未来的检索会发现检索工件而不是原始证据。
4. 对话支架。避免保存“用户询问”、“助理建议”、“然后探索”叙述，除非对话结构本身就是持久的事实。压缩决策，例如“决策：使用文件系统优先集成”。
5. 临时运行状态。不要存储“需要稍后检查”、“也许调查”或“可以进行基准测试”，除非该项目被提升到 TODO 系统、问题跟踪器或审查队列中。

过滤器的默认策略是reject-unless-durable。仅当候选记忆是稳定的用户偏好、持久的事实、已接受的决策、可重用的过程、未解决但已跟踪的开放问题或有源支持的综合时，才应通过。否则它属于短暂的会话上下文，而不是长期记忆。

# 单一真相来源边界

知识库的目的是让特工快速进入金库，找到证据，并回答“这里什么是真的？”无需猜测。因此，系统必须区分规范源文档、代理创作的知识和可重建索引。

## 规范层

|层 |典范？ |可变的？ |目的|示例 |
|---|---:|---:|---|---|
|原材料来源|是的 |否，元数据修正除外 |证据基质。每一个重要的主张都必须在这里可追溯。 |原始文章 Markdown、PDF 文件、屏幕截图、图像、文字记录、GitHub 问题导出或指向确切本地存储路径的注释。 |
|维基注释|是的，但源自原始来源 |是的，已审核编辑 |代理/人类创作的概念、决策、比较、查询、综合。 | `concepts/*.md`、`comparisons/*.md`、`queries/*.md`、项目决策说明。 |
|日志 |是的 |仅附加|知识库操作和源更改的时间顺序。 | `log.md`，项目日志，摄取日志。 |
|用户/项目简介注释|是的，在他们的范围内|是的，更严格的审查|持久的用户/项目事实、偏好、约定。 | `00-system/user-profile.md`、`20-projects/*/project-memory.md`。 |
| Hermes内置内存|语料库真相不存在 |是的，微小的转向缓存|仅紧凑型指针/转向存储器。 |跳马路径，稳定偏好，反复修正。 |
|派生索引|没有 |仅限重建 |检索加速。决不能是知识的唯一副本。 | SQLite FTS、BM25 索引、向量存储、图形投影。 |
|发布网站 |没有 |生成 |只读演示表面。 | VitePress/GitHub 页面输出。 |

## 原始来源是不可变的证据

原始来源必须与 wiki/概念注释分开维护，遵循 Karpathy 的 LLM Wiki 模式。原始来源不是摘要。它们是证据记录。原始来源可能是：

1. 保留的原始或接近原始文本提取，例如文章 Markdown、论文文本、抄本文本、GitHub 问题 JSON/Markdown 或官方文档 Markdown。
2. 存储在保管库或存储库中的二进制/原始工件，例如 PDF、图像、屏幕截图、音频或下载的 HTML。
3. 指针注释，记录准确的本地路径、内容哈希、源 URL、检索日期以及工件太大或无法复制到保管库中时的访问说明。

原始来源可能包括“##提取注释”，但这些注释是评论。它们不是原始源本身，并且不得替换保留的源内容或工件路径。

允许编辑原始源文件：
- 添加或更正元数据。
- 添加缺失的工件路径、哈希值、检索时间戳或提取状态。
- 将提取标记为部分/阻止/截断。
- 添加勘误表，指出捕获有缺陷。

禁止对原始源文件进行编辑：
- 为了清晰起见，重写原始来源措辞。
- 删除不方便的源文本。
- 将完整源内容折叠成摘要，同时仍将其标记为原始内容。
- 将综合声明混合到原始文本中，而没有明确标记的分析部分。

## 代理的真相查找顺序

当被问及事实时，赫尔墨斯应该按以下顺序解决事实：

1. 识别活动范围：主题、项目、用户、时间范围、隐私边界。
2. 阅读相关索引或主题图以找到候选 wiki 注释。
3. 阅读 wiki 注释，了解当前的综合、置信度、争议状态和源链接。
4. 按照原始来源的来源链接来验证重要的声明。
5. 如果 wiki 和原始来源发生冲突，则原始来源作为证据获胜，但 wiki 可能包含解释冲突的后续综合。
6. 如果没有原始来源支持某个主张，请回答“证据不足”或将该主张标记为推论/推测。
7. 如果检索到的记忆或之前的辅助输出包含声明但没有原始/用户确认的来源，请不要将其视为事实。

## 按工件类型划分的单作者规则

|神器|谁可以直接写|审核要求|
|---|---|---|
|原始源码神器|捕获工具或明确的用户指令 |仅元数据修正可能是直接的；内容替换需要审核。 |
|概念/比较/查询注释 |赫尔墨斯还是人类|如果有源代码支持，则允许直接修补；有争议/高影响力的变更需要审查说明。 |
|用户资料备注 |具有明确确认的人类或 Hermes |必须显示差异；不会悄悄更新敏感的个人事实。 |
|项目记忆笔记| Hermes 或活跃项目范围内的人类 |直接补丁允许稳定的约定/决定；临时任务状态被拒绝。 |
|程序/手册 |赫尔墨斯还是人类|仅当可重复使用并经过验证时才能升级为 Hermes 技能。 |
|派生索引 |仅脚本/自动化 |从规范的降价重建；切勿手动编辑。 |
|发布网站 |仅限 GitHub 操作 |从回购状态生成。 |

## 源标识符

每个原始源都应该有一个稳定的“source_id”，这样即使文件名发生变化，维基注释也可以引用源。

格式：

```text
src:<type>:<slug>:<year-or-date>
```

示例：

```text
src:article:karpathy-llm-wiki-gist:2026
src:paper:memgpt:2023
src:github:mem0-issue-4573-memory-audit-junk:2026-05-14
src:clip:obsidian-web-clipper:2026-05-14
```

Wiki 注释可能会引用“source_id”和路径。 Path用于代理导航； ID 仅供持久参考。

# 推荐的 Vault 布局

使用一个黑曜石库作为个人知识库，最好是由 git 支持且本地优先。

```text
Obsidian Vault/
  00-system/
    SCHEMA.md
    AGENT-RULES.md
    user-profile.md
    memory-policy.md
    review-queue.md
    dashboards/
      research.base
      projects.base
      memory-audit.base
  10-inbox/
    clips/
    notes/
    transcripts/
  20-projects/
    hermes-agent/
      index.md
      decisions/
      tasks/
      sources/
  30-research/
    agent-memory/
      index.md
      concepts/
      comparisons/
      queries/
      raw/
      log.md
  40-procedures/
    skills-candidates/
    playbooks/
  50-sessions/
    active/
    archive/
  60-people/
  70-entities/
  80-attachments/
  90-sources/
    web/
    pdf/
    github/
  99-private/
    .agentignore
```

对于当前的“/Users/a17/wiki”，存在两个实用选项：

1. 将其保留为项目/研究仓库，并直接作为黑曜石金库打开。
2. 将其移动或镜像到“30-research/agent-memory/”下更大的黑曜石保险库中。

建议：保留“/Users/a17/wiki”作为本主题的研究存储库，并可选择将其添加为单独的黑曜石保险库。这可以避免在工作流程稳定之前将出版物/Docsify 文件与用户的整个个人保管库混合。

# 注释模式

模式规则是 Obsidian（作为人类笔记应用程序）和 Hermes（作为代理知识运算符）之间的桥梁。该模式对于搜索、仪表板、lint 和自动化来说应该足够严格，但又不能复杂到人们停止写笔记的程度。

## 全局 frontmatter 字段

每个托管注释，除了“README.md”和简单的生成/发布文件之外，都应该使用 YAML frontmatter。

|领域 |必填|价值观 |意义|
|---|---:|---|---|
| `id` |是的 |稳定的蛞蝓状ID |持久引用与文件名无关。 |
| `标题` |是的 |字符串|人类可读的标题。 |
| `类型` |是的 | `raw_source`、`concept`、`comparison`、`query`、`decision`、`project_memory`、`user_profile`、`session_summary`、`procedure`、`dashboard`、`index` |笔记类。 |
| `创建` |是的 | `年-月-日` |创建日期。 |
| `已更新` |是的 | `年-月-日` |最后一次有意义的内容更新。 |
| `状态` |是的 | “草稿”、“有效”、“审查”、“有争议”、“被取代”、“已存档” |生命周期状态。 |
| `标签` |是的 |列表 |搜索/仪表板标签。 |
| `范围` |是的 |对象|用户/项目/主题/渠道边界。 |
| `可见性` |是的 | `私有`、`内部`、`公共` |出版和自动化边界。 |
| `代理读取` |是的 |布尔 |代理是否可以默认读取。 |
| `agent_write` |是的 | “从不”、“提议”、“直接” |代理是否可以直接写信。 |
| `来源` |有条件|源 ID 或路径列表 |对于有源代码支持的 wiki 注释是必需的。 |
| `信心` |有条件| ‘低’、‘中’、‘高’ |概念/比较/查询/决策所需。 |
| `有争议` |有条件|布尔 |概念/比较/查询/决策所需。 |

## 原始源注释模式

原始来源是不可变的证据记录。它们必须包含保留的源文本或指向 Hermes 可以使用适当的工具定位和读取的精确工件路径。

```yaml
---
id: src:article:example-source:2026-05-16
title: Example Source Title
type: raw_source
created: 2026-05-16
updated: 2026-05-16
status: active
tags: [raw-source, article]
scope:
  users: [a17]
  projects: []
  topics: [agent-memory]
  channels: []
visibility: public
agent_read: true
agent_write: propose
source:
  source_url: https://example.com/article
  original_artifact_path: raw/assets/example-source.html
  local_text_path: raw/articles/example-source.md
  media_paths: []
  captured_by: hermes-web | obsidian-clipper | manual | pdf-parser | screenshot | api
  captured_at: 2026-05-16T00:00:00Z
  content_sha256: sha256:...
  license: unknown
  access_notes: public web page
source_derivation:
  derived_from: []
  transformation: []
raw_preservation: full_text | full_binary | full_html | full_pdf_text | pointer_only | transformed_text | tool_parsed_or_summarized_text | extraction_blocked
extraction_status: complete | partial | blocked | needs_pdf_pass | needs_manual_review
reliability: high | medium | low
---
```

所需的身体部分：

```markdown
# Source Title

## Source Metadata

## Original Artifact / Storage Path

- original_artifact_path: raw/assets/example-source.html
- local_text_path: raw/articles/example-source.md
- media_paths: []

## Parsed Source Text

Preserved source text goes here. If source is binary-only, write where the binary lives and how an agent should read it.

## Extraction Notes

Only commentary about extraction quality, missing sections, blocked access, or parser limitations.
```

## 转换源的源推导

当源注释不是原始工件而是另一个原始源的转换表示时，请使用“source_derivation”。示例包括 OCR 输出、转录清理、解析的 PDF、翻译版本、规范化 HTML 提取和 Markdown 清理过程。

```yaml
source_derivation:
  derived_from:
    - src:pdf:memgpt-paper:2023
  transformation:
    - OCR
    - markdown_cleanup
```

规则：
- `衍生自` 必须指向上游原始/原始工件的源 ID 或路径。
- “转换”必须列出改变表示或措辞的每个有意义的处理步骤。
- 转化后的来源仍然是证据，但不是根本证据。当确切的措辞、布局、数字或法律/出处问题很重要时，代理应遵循“衍生自”。
- 翻译必须在“转换”或“摘录注释”中记录源语言和目标语言。
- 仅清理转换不得默默地删除不确定性、OCR 错误、演讲者标签、时间戳、页码或源行/页面引用。

## 概念笔记架构

概念笔记是代理/人类创作的综合页面。它们是可变的，但每一个事实主张都应该追溯到原始来源。

```yaml
---
id: concept:hermes-obsidian-personal-kb
title: Hermes Obsidian Personal Knowledge Base Plan
type: concept
created: 2026-05-14
updated: 2026-05-16
status: active
tags: [agent-memory, obsidian, hermes]
scope:
  users: [a17]
  projects: [wiki]
  topics: [agent-memory, personal-knowledge-base]
  channels: []
visibility: public
agent_read: true
agent_write: direct
sources:
  - src:article:karpathy-llm-wiki-gist:2026
  - raw/articles/karpathy-llm-wiki-gist-2026.md
confidence: medium
contested: true
review:
  last_reviewed: 2026-05-16
  next_review: 2026-06-16
---
```

所需的身体部分：

```markdown
# Title

# Executive Summary
# Claims
# Architecture / Analysis
# Open Questions
# Source Map
# Current Corrections / Evidence Gaps
```

## 决策记录模式

```yaml
---
id: decision:project:short-title:2026-05-16
title: Decision Title
type: decision
created: 2026-05-16
updated: 2026-05-16
status: accepted
scope:
  users: [a17]
  projects: [hermes-agent]
  topics: []
  channels: []
visibility: private
agent_read: true
agent_write: propose
sources: []
confidence: medium
contested: false
supersedes: []
superseded_by: null
---
```

所需的身体部分：

```markdown
# Decision
## Context
## Options Considered
## Decision
## Consequences
## Evidence / Sources
## Review Date
```

## 会话摘要架构

会话笔记不是原始内存转储。知识是压缩的状态转换，而不是交互历史。会话记录的目的不是重播记录、年表、工具日志或代理推理跟踪；它是从交互中提取与未来相关的状态转换。

内存管道：

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

不要为每个会话创建持久的会话记录。仅当交互超过下面的内存提取阈值时才创建一个。即便如此，会话摘要也不是永久权威的：会话是候选知识的临时容器和交互缓冲区，而不是长期知识。

## 内存类模型

保留时间由内存类别决定，而不是由文件夹决定。使用四个类：

|班级 |目的|生命周期 |默认检索 |
|---|---|---|---|
| `规范` |核心长期知识|永久|是的 |
| `语义` |长期经验提炼|长期|是的 |
| `运营` |项目运行时状态 |中期|仅限范围 |
| `情景式` |会话级流程记录 |短期|默认较弱|

会话笔记通常应该是“memory_class：episodic”。他们的工作是“交互缓冲区 -> 提取基质”，而不是永久的会话存档。

## 规范化规则

尽快将耐用项目从会议中剔除：

|会议内容 |目标位置|
|---|---|
|架构决策 | `决定/` |
|工作流程稳定 | `程序/` |
|耐久合成| `概念/` |
|可重复使用的调查| `研究/` |
|偏好稳定 | `用户配置文件.md` |
|经验证的操作规则 |项目记忆|

一旦提升，会话的价值和检索优先级就会下降。会话应该只保留“规范化项目”指针列表。

## 最小会话前沿

避免过多的元数据和 YAML 膨胀。仅保留对操作有用的字段：

```yaml
---
id: session:2026-05-16-hermes-memory-design
title: Hermes Memory Design Session
type: session_summary

created: 2026-05-16
updated: 2026-05-16

memory_class: episodic

status: active

retention:
  mode: adaptive
  half_life_days: 30
  retrieval_weight: 1.0

memory_stats:
  retrieval_count: 0
  citation_count: 0
  promoted_items: 0

scope:
  projects:
    - wiki
  topics:
    - memory-architecture

contains:
  decisions: true
  procedures: true
  source_analysis: true
  transient_debugging: false

canonicalized: false
archive_candidate: false
---
```

所需的身体部分：

```markdown
# Session Summary
## Durable Outcomes
## Decisions
## Procedures Validated
## Sources Added
## Open Questions
## Canonicalized Items
## Rejected / Do Not Store
```

默认禁止的部分/内容：
- 成绩单转储/记录
- 按时间顺序重播
- 工具日志
- Shell输出垃圾邮件
- 思维链重播
- 重复检索/来源摘录

## 内存提取阈值

仅当至少发生了一次与未来相关的状态转换时，会话才应成为持久注释。

当满足以下任一条件时保存会话记录：
- 架构发生了变化。
- 发现持久偏好。
- 已验证可重复使用的程序。
- 添加了来源。
- 决定最终确定。
- 长期研究合成产生。
- 已确定未解决的问题并值得跟踪。

不要为以下目的保存持久会话记录：
- 一次性调试。
- 重试命令循环。
- 随意的头脑风暴，没有决定或可重复使用的输出。
- 失败的实验，没有可重复使用的结论。
- 简短的质量检查。
——临时规划。
- 通用操作帮助，例如“如何安装 X”，除非它产生可重用的过程或项目约定。

## 自适应保留和半衰期

会话半衰期并不意味着 30 天后删除笔记。这意味着动态降低检索优先级，同时保留可审计性。

保留阶段：

1. Active：新会话具有 `retrieval_weight: 1.0` 并且可以参与范围检索。
2. 衰减：在每个“half_life_days”之后，设置“retrieval_weight *= 0.5”。保留该文件，但不要主动将其放入上下文中，除非范围检索需要它。
3. 候选档案：当“retrieval_count == 0”、“itation_count == 0”、“canonicalized == true”且年龄超过 90 天时，设置“archive_candidate: true”。
4. 压缩：存档的会话应从情景记录压缩为语义结果。示例：`探索了 REST API；测试的文件系统写入；基准延迟；决定文件系统优先`变为“结果：为 MVP 稳定性选择文件系统优先集成”。
5. 删除：很少见，需要人工确认。仅在规范化、未引用、无入站链接、无项目依赖、长期检索计数为0、无审核值的情况下删除。

强化规则：会话记忆可以强化，也可以衰减。如果会话被检索或引用，则增加“retrieval_count”或“itation_count”，并向“retrieval_weight”添加一个小的强化奖励，以 1.0 为界。有价值的操作内存保持可发现性；噪音自然衰减。

## 会话内存的检索策略

情景会议不应高于规范知识。检索优先级应该是：

1. 规范概念
2. 决定
3. 程序
4. 项目记忆
5. 语义综合
6. 主动操作注意事项
7. 专题会议
8. 存档会议

这可以防止会话噪音污染长期的知识检索。

## 规范化管道

会话内存不应该永远直接用于检索。持久的知识应该通过：

```text
session
    ↓
extract durable items
    ↓
promote to canonical notes
    ↓
lower session importance
```

示例：记录“选择文件系统优先集成”的会话注释应生成“decisions/filesystem-first-architecture.md”。然后会话仅保留：

```markdown
## Canonicalized Items
- [[filesystem-first-architecture]]
```

运营目标是：

```text
session entropy
    ↓
semantic extraction
    ↓
canonical knowledge
```

不会永远存储更多会话。

## 自动化和指标

自动化可以更新“retrieval_count”、计算衰减、标记存档候选、起草压缩建议并建议规范提取。删除、修改规范知识、发布会话内容和更改用户个人资料事实需要人工确认。

仅跟踪最低限度的运营指标：

```yaml
memory_metrics:
  active_sessions:
  archived_sessions:
  avg_retrieval_count:
  canonicalization_rate:
  stale_session_ratio:
  orphan_session_ratio:
```

推荐的会话目录布局：

```text
50-sessions/
  active/
  archive/
```

不要按年份将会议划分得太深；会话不应该是主要导航层。长期导航属于“概念/”、“决策/”、“程序/”和“项目/”。

## 程序注释架构

```yaml
---
id: procedure:ingest-source
title: Ingest Source Procedure
type: procedure
created: 2026-05-16
updated: 2026-05-16
status: active
tags: [procedure, ingestion]
scope:
  users: [a17]
  projects: [wiki]
  topics: [agent-memory]
  channels: []
visibility: public
agent_read: true
agent_write: direct
sources: []
promote_to_skill: false
---
```

所需的身体部分：

```markdown
# Procedure
## Trigger
## Inputs
## Steps
## Validation
## Failure Modes
## Commit Message
```

# 爱马仕角色

## 1. 摄取算子

输入：URL、PDF、粘贴文本、GitHub 问题/存储库、会议记录或用户说明。

输出：
- 带有保留的解析文本的原始源注释
- 提取的声明/实体（如果有用）
- 更新了主题索引/日志
- 可选概念页面更新
- git 提交

护栏：
- 合成前保留原始文本。
- 明确标记阻塞/截断的提取。
- 不要创建许多小页面来传递提及。
- 在创建新笔记之前搜索现有笔记。

## 2. 检索/上下文运算符

输入：用户问题或任务。

输出：
- 结构化工作集：角色分离、令牌预算、语义压缩的执行上下文
- 带有引文的可选答案

检索顺序：
1.当前项目/主题索引
2. 文件名/标签/标题的精确搜索
3. 全文/BM25检索
4. 标签/frontmatter 的结构化过滤器
5.可选的语义搜索
6. 原始源回退

检索后，使用Working Set Assembly v1：检索只是候选生成，簇是含义单元，最终的工作集是运行时工件而不是存储的注释。

## 3.综合编辑器

输入：一组源/注释和一个目标注释。

输出：
- 建议对目标注释进行补丁
- 源地图更新
- 日志更新

护栏：
- 切勿默默地覆盖原始源。
- 保留冲突并标记有争议。
- 不要将低可信度的源代码片段变成高可信度的声明。

## 4. Lint/审计操作符

检查：
- 损坏的维基链接
- 缺少前题
- 没有来源的注释
- 没有解析源文本的原始文件
- 过时的 next_review 日期
- 孤儿笔记
- 重复的概念
- 概念说明中未引用的权利要求
- 公共页面意外引用私人文件夹

## 5. 反射/合并算子

定期或手动运行。它应该建议而不是自动应用主要的内存更改。

输入：
- 最近的会议总结
- 项目日志
- 收件箱笔记
- 审查队列

输出：
- 候选人对用户个人资料、项目记忆或概念页面的更新
- 候选赫尔墨斯技能更新
- 短暂事实的拒绝/禁止存储列表

# Hermes 内置内存与黑曜石

Hermes 内置内存是有意限制的。 Hermes 文档描述了两个核心文件 MEMORY.md 和 USER.md，它们在会话开始时作为具有小字符限制的冻结快照注入。这使得它对于紧凑耐用的转向非常有用，而不是完整的个人知识库。

会议摘要也不是完整的个人知识库。它们是短暂的候选知识容器。将持久内容提升为规范概念、决策、程序、项目记忆、源支持的综合或稳定的偏好；然后让会话半衰期机制降低检索优先级。

使用 Hermes 内存用于：
- 稳定的用户偏好
- 稳定的环境事实
- 反复修正
- 高价值的会议
- 指向规范黑曜石金库/回购路径的指针
- 持久的解决方案或程序可以防止未来重复调试

请勿将 Hermes 内存用于：
- 原始源文本
- 研究语料库
- 大型项目历史
- 完成的任务日志
- 临时待办事项
- 详细的会议记录
- Shell/工具输出或安装/构建日志
- 代理思维链或探索性推理痕迹
- 从检索到的笔记、搜索结果或原始来源中重复摘录
- 没有持久决定的对话式脚手架
- TODO 系统、问题跟踪器或审核队列中未跟踪的未来可能的操作状态

使用 Obsidian 处理较大的工件，并使用审核队列或问题跟踪器处理未解决的操作后续问题。如果候选人只解释了会话中发生的事情，但没有解释以后应该重复使用的内容，请从长期记忆中拒绝它。

# 黑曜石集成选项

## 选项A：文件系统优先集成，推荐首先

Hermes直接使用文件工具读取/写入Markdown文件。这对于本地优先的工作流程来说已经足够了。

优点：
- 简单
- 无插件依赖
- Git 友好
- 当黑曜石关闭时有效

缺点：
- 不知道活动的黑曜石窗格
- 无法触发黑曜石命令
- 必须小心并发编辑

## 选项 B：Obsidian URI，轻自动化

Obsidian URI 可以通过 `obsidian://...` 打开笔记、创建笔记、打开每日笔记、搜索和选择保管库。对于从 Hermes 输出或计划文档生成本地链接很有用。

用于：
- Hermes 写完后打开笔记
- 从仪表板链接到本地黑曜石笔记
- 从外部自动化创建每日笔记

避免依赖 URI 作为主要写入 API；文件系统编辑更容易区分和测试。

## 选项 C：Obsidian Local REST API / 内置 MCP，稍后

本地 REST API 插件提供对 Obsidian 的经过身份验证的 HTTPS 访问，可以读取/创建/更新/删除注释、补丁标题/frontmatter、搜索元数据/内容、访问活动文件、管理定期注释、查询标签以及在 Obsidian 中打开文件。它的自述文件还说它公开了 REST API 和内置的 MCP 服务器接口。

当你需要时使用：
- 活跃的笔记上下文
- 通过黑曜石修补部分/前题
- 通过插件 API 进行标签/元数据操作
- Hermes 文件工具之外的 MCP 客户端

安全注意事项：保持 API 本地绑定，保护 API 密钥，不要通过网络公开。

## 选项 D：Obsidian MCP 服务器，可选

社区 MCP 服务器可以向 MCP 客户端公开笔记读/写/搜索/frontmatter 操作。 Hermes 具有本机 MCP 配置支持，因此这可以在以后成为更清晰的集成。

除非文件系统优先编辑不够，否则不要从这里开始。

## 选项 E：Dataview 或 Bases 仪表板

Dataview 是基于 Markdown 元数据的实时索引/查询引擎，可以从 frontmatter 和内联字段渲染表/列表。 Obsidian Bases 是一个核心插件，用于笔记及其属性的类似数据库的视图。

用于人工审核仪表板：
- 需要处理的收件箱项目
- 带有“extraction_status！=完成”的原始来源
- 带有“有争议：真实”的概念注释
- 注释“next_review <= Today”
- 项目决策日志
- 内存候选人等待批准

# 工作流程食谱

## 方法 1：捕获网络源

1. 用户使用 Obsidian Web Clipper 将页面剪辑到 `10-inbox/clips/` 或要求 Hermes 提取 URL。
2. Hermes 创建/移动带有源 frontmatter 和 `## Parsed Source Text` 的原始注释。
3. Hermes 将声明/实体提取到一个简短的“## Extraction Notes”部分。
4. Hermes 搜索现有概念/项目页面。
5. Hermes 更新一个目标合成页面，或者如果满足阈值则创建一个目标合成页面。
6. Hermes更新索引/日志。
7. Hermes 做出改变。

## 秘诀2：问Hermes一个知识问题

1. Hermes 确定活动范围：用户/项目/主题/时间范围。
2. Hermes 通过词法搜索、结构化过滤器和可选的语义搜索来检索候选者。
3. Hermes 使用Working Set Assembly v1 对结果进行排名、聚类、压缩、去重和角色隔离。
4. Hermes 从带有源链接的结构化工作集中得到答案。
5. 如果答案可重复使用，Hermes 询问或推断是否将其保存为查询/概念注释；工作集本身仍然是一个运行时工件，而不是一个持久的注释。

## 秘诀 3：将会话转化为持久的知识

1. 在创建任何持久笔记之前检查内存提取阈值。仅当架构发生变化、发现持久偏好、验证可重用程序、添加源、最终确定决定、产生长期研究综合或确定有价值的未解决问题时才继续。
2. 将记忆管道视为：交互 -> 工作上下文 -> 临时暂存 -> 候选提取 -> 熵过滤器 -> 持久知识 -> 检索索引。
3. 提取与未来相关的状态转换，而不是交互历史。
4. 在写入任何持久内容之前运行熵过滤器：拒绝 shell/工具输出、思维链、重复检索摘录、会话脚手架、已完成的任务日志、重试循环和未来可能的操作状态。
5. 只保留持久的结果、决策、新知识、可重复使用的程序、悬而未决的问题和添加的证据。
6. 仅对值得审核的拒绝使用“## 拒绝/不存储”；否则完全省略蜉蝣。
7. 如果需要，更新项目/概念/程序说明。
8. 在可重用时，将稳定的程序推广到 Hermes 技能。

## 秘诀 4：每周内存审计

1. 查找最近 7 天内更改的笔记。
2. 查找候选内存和用户配置文件更改。
3. 检查收件箱中是否有未处理的项目。
4. 检查部分/阻塞提取的原始来源。
5. 检查有争议或低可信度的笔记。
6. 生成审核报告和可选补丁集。

# 检索策略

## 第 1 阶段：仅词汇

用途：
- 黑曜石内置搜索
- Hermes `搜索文件`
- git grep/ripgrep 在需要时通过安全包装器
- 索引/index.md 文件
- 标签和前言

如果文件名、标签和索引受到严格限制，这对于前几百个笔记来说就足够了。

## 第 2 阶段：SQLite FTS/BM25

添加一个小的派生索引：

```text
.hermes-kb/index.sqlite
  notes(path, title, type, tags, updated, hash)
  sources(path, source_url, reliability, extraction_status)
  links(src, dst)
  fts_notes(path, title, headings, body)
```

该索引是从 markdown 派生并可以重建的。

## 第三阶段：混合语义检索

仅在评估表明需要后才添加嵌入。将向量存储在 Markdown 之外，由文件哈希和标题/块 ID 键入。

使用语义检索：
- 模糊概念回忆
- 转述问题
- 跨主题发现

使用精确/BM25 用于：
- 名字
- 文件路径
- 命令
- 日期
- ID
- 引号
- 价格/数量

# 工作集装配标准 v1

工作集组装是一个确定性管道，它将作用域检索结果转换为角色分离、令牌预算、语义压缩的执行上下文，用于 LLM 推理。

目标：将检索结果转换为 LLM 推理所需的最小充足上下文。检索是探索，而不是消费。簇，而不是音符，是主要的意义单位。工作集是运行时工件，而不是存储结构。

输入：
- `查询`
- “范围”，例如项目、主题或用户
- `检索结果`

输出：
- 结构化的“工作集”

## 数据结构

所有中间工件都必须结构化以避免自由文本漂移。

### 候选人备注

```yaml
id: string
title: string
type: concept | decision | session | source | procedure
score: float
content: string
metadata:
  project: string
  tags: []
  updated: date
```

＃＃＃ 簇

```yaml
cluster_id: string
theme: string
notes: [CandidateNote]
cluster_score: float
```

### 工作集输出

```yaml
system_context: string
project_context: string
knowledge_context:
  clusters: []
evidence_context: []
task_context: string
token_budget:
  system: int
  project: int
  knowledge: int
  evidence: int
```

## 管道

### 第 1 步 — 检索考生笔记

输入：
- `查询`
- “范围”，例如项目、主题或用户
- 索引/搜索后端

规则：
- 使用三个回忆通道：词汇搜索（例如 BM25/grep）、结构化过滤器（例如标签/frontmatter）以及可选的语义搜索。
- 输出`candidate_notes[]`。
- `topK = 30..80`;不要使候选集太大。
- 每个候选人都必须包含元数据：“类型”、“项目”和“更新”。

### 第 2 步 — 固定评分排名

使用版本化评分函数：

```text
ranking_version: v1.0

score =
  0.35 * relevance(query, note)
+ 0.20 * project_scope_match
+ 0.15 * recency_decay(note.updated)
+ 0.15 * citation_frequency(note)
+ 0.10 * canonicality(note.type)
- 0.05 * redundancy_penalty
```

规范性权重顺序：

```text
decision > concept > procedure > source > session
```

输出排序后的候选列表并保留前 20..40 个。

### 步骤 3 — 聚类为意义单元

目标：将语义上相邻的注释合并到主题块中。

更喜欢使用以下规则聚类：
- 标签重叠
- 共享实体
- 共享项目
- 标题相似度

倒退：

```text
cluster_key = dominant_tag OR project OR embedding_similarity
```

限制条件：
- 簇数 <= 8
- 每个簇的注释 <= 10

### 步骤 4 — 压缩每个簇

将每个簇从笔记集合转换为语义摘要单元：

```markdown
Cluster: <theme>

Key Claims:
- ...

Key Decisions:
- ...

Key Evidence:
- source refs

Conflicts:
- if any
```

压缩规则：
- 删除重复的句子。
- 保留结论，而不是处理日志。
- 保留冲突；不要平均它们。
- 保留源指针。

### 步骤 5 — 重复数据删除

目标：避免重复内容造成上下文污染。

规则：
1.内容哈希去重和相似度去重：

```text
if similarity(note_a, note_b) > 0.85:
    keep higher canonicality
```

2.语义重复优先级：

```text
decision > concept > cluster summary > session > raw
```

3.跨集群去重：如果集群A和集群B表达相同的事实，则保留一次，并将另一个出现的事件变成引用指针。

### 步骤 6 — 按角色隔离

固定分区：

```yaml
system_context: rules, constraints, safety
project_context: current scoped project state
knowledge_context: compressed clusters
evidence_context: raw source snippets or quotes
task_context: user query
```

分区规则：
- `system_context` 不是来自检索；它是固定的提示/规则。
- `project_context` 仅来自范围注释；不允许跨项目污染。
- `knowledge_context` 仅包含集群压缩输出。
- `evidence_context` 包含最少的原始源代码片段或引用。

### 步骤 7 — 组装最终上下文包

固定代币预算：

```text
system:   10%
project:  20%
knowledge: 40%
evidence: 20%
task:     10%
```

组装规则：
1.顺序固定：系统->项目->知识->证据->任务。
2. 证据必须最少：只有必要的参考文献，没有全文转储，每项 <= 3..8 行。
3. 知识仅使用聚类摘要。不要连接原始笔记或转储会话。
4. 如果超出预算，请按以下顺序修剪：
   - 基于会话的内容
   - 低分集群
   - 冗余证据
   - 旧笔记

## 维护和可观察性

对每个阶段进行版本控制，以便管道保持可重复性：

```yaml
ranking_version: v1.0
clustering_version: v1.0
compression_version: v1.0
```

记录指标：

```yaml
metrics:
  retrieved_count:
  clustered_count:
  compressed_size:
  final_tokens:
  redundancy_rate:
  evidence_ratio:
```

调试模式必须支持 `--debug-working-set` 并输出：
- 每一步结果
- 分数明细
- 集群形成
- 压缩差异

## MVP 实现

最低可行实施：
1. BM25检索前30名。
2. 应用简单加权分数。
3. 使用基于标签的聚类。
4. 用 LLM 或确定性规则总结每个集群。
5. 通过哈希值和相似度阈值进行重复数据删除。
6.应用固定角色分区。
7. 按代币预算截断。

设计原则：
1.检索是探索，而不是消费。
2.簇是意义单位。
3. 工作集是运行时工件。

# 评估计划

创建包含 30-50 个代表性问题的 `00-system/evals/personal-kb-queries.yml`：

```yaml
- id: q001
  question: What is the recommended Hermes memory vs Obsidian split?
  expected_sources:
    - 30-research/agent-memory/concepts/hermes-obsidian-personal-knowledge-base-plan.md
  must_include:
    - Hermes memory is bounded
    - Obsidian stores larger corpus
```

测量：
- 检索召回@k
- 引用正确性
- 回答忠诚度
- 陈旧/冲突的答案率
- 新证据出现后更新知识的时间
- 被拒绝的垃圾记忆的数量

# 自动化和权限边界

自动化必须是明确的，因为知识库既是个人工作空间，又是代理可读的真相基础。

## 权限级别

|水平|意义|允许的示例 |
|---|---|---|
| `read_public` |代理人可以阅读公开/研究笔记。 | `README.md`、`concepts/`、公共原始源。 |
| `read_scoped` |仅当当前任务范围与注释范围匹配时，代理才可以读取。 |项目记忆、会议总结。 |
| `read_explicit` |代理只能在明确的用户指令后读取。 | `99-private/`，敏感的个人笔记。 |
| `write_direct` | Agent可以直接打补丁并提交。 |索引/日志更新、非敏感源支持的概念编辑。 |
| `写提议` |代理可以创建补丁/提案，但用户必须批准。 |用户概况、项目决策、有争议的主张。 |
| `write_forbidden` |代理人不得写信。 |原始工件内容、私人秘密、手动生成的索引。 |

## 文件夹策略

|文件夹|阅读默认 |写入默认|发布默认 |笔记|
|---|---|---|---|---|
| `raw/` / `90-sources/` |允许 |建议元数据，禁止源内容重写 |仅当可见性公开时才允许 |不可改变的证据。 |
| `概念/`、`比较/`、`查询/` |允许 |如果有源支持，则直接 |如果公开可见性则允许 |主要维基层。 |
| `20 个项目/` |范围 |根据项目建议/直接 |默认为私有 |避免泄漏主动工作。 |
| `50 个会话/` |范围 |提议|默认为私有 |仅摘要，不转录转储。 |
| `00-system/user-profile.md` |范围 |仅建议|从来没有|个人事实需要确认。 |
| `40 个程序/` |允许 |直接用于非敏感程序|如果公开可见性则允许 |促进技能的稳定程序。 |
| `99-私人/` |仅显式|除非明确禁止 |从来没有|默认拒绝。 |
| `.hermes-kb/`，矢量存储，搜索索引 |仅工具/脚本 |仅重建 |从来没有|衍生的文物。 |

## 自动化类

安全自动化：
- 从 Markdown 重建搜索索引。
- Lint 缺少 frontmatter、损坏的链接、缺少原始源字段。
- 生成只读仪表板。
- 附加代理操作的日志条目。
- 起草审查报告。

需要审核：
- 编辑用户个人资料或个人事实。
- 将有争议的索赔标记为已解决。
- 将信心从低/中改为高。
- 删除或存档笔记。
- 跨越可见性边界移动笔记。
- 发布任何私人/项目/会话内容。

未经明确指示禁止：
- 读取秘密或私人文件夹。
- 将 API 密钥、令牌、密码或凭据写入笔记中。
- 用摘要替换原始源内容。
- 重新提取调用的内存，就好像它是新的用户输入一样。
- 发布“99-private/”、“.obsidian/workspace*.json”、“.hermes-kb/”、会话记录或与机密相关的注释。

## `.agentignore` / 发布排除基线

```text
99-private/**
50-sessions/**
20-projects/**/secrets/**
**/.obsidian/workspace*.json
**/.trash/**
**/*secret*
**/*password*
**/*token*
.hermes-kb/**
node_modules/**
.vitepress/cache/**
.vitepress/dist/**
```

## 人工确认触发器

在以下情况下，Hermes 必须要求确认或生成提案专用补丁：

- 编辑更改了个人偏好、身份事实、关系、医疗/财务/法律事实或其他敏感个人数据。
- 编辑更改了系统关于有争议或高影响力主张的结论。
- 编辑删除、存档或取代注释。
- 编辑更改原始源内容而不是元数据。
- 编辑使私有/范围内的内容公开。
- 任务范围与注释的“范围”字段不匹配。

# MVP 操作循环

MVP 应该证明智能体可以进入金库、找到真相、更新知识并留下可审计的踪迹。

## MVP 范围

使用“/Users/a17/wiki”作为第一个独立的 Obsidian/VitePress 研究库。请勿迁移完整的个人保管库。

MVP 包括：
- “raw/”下的原始源捕获。
- “概念/”下的概念综合。
- `index.md` 和 `log.md` 维护。
- Git 提交每一个已完成的知识变更。
- VitePress 出版物仅用于公共/研究安全笔记。
- 手动审查私人、个人、有争议或破坏性的编辑。

MVP 不包括：
- 矢量数据库。
- 图形数据库。
- 自动提取个人记忆。
- 自动发布项目/会议/私人笔记。
- 自主删除。
- 自主归档，无需审查“archive_candidate”提案。
- 黑曜石 REST/MCP 依赖性，除非文件系统优先编辑失败。

## MVP 摄取循环

1. 用户提供源 URL/文件/路径或将剪辑放入收件箱。
2. Hermes 使用“type: raw_source”、“source_id”、存储路径、散列、捕获日期、保存状态和提取状态创建原始源注释或工件指针。
3. Hermes 验证原始源是否可以从记录的路径中读取。
4. Hermes 将候选声明、实体和开放问题提取到分析部分或单独的草稿中。
5. Hermes 在创建新页面之前搜索现有概念。
6. Hermes 用源支持的声明修补最相关的概念/查询/决策说明。
7. 如果创建了新的持久页面，Hermes 会更新“index.md”。
8. Hermes 在 `log.md` 后面附加更改内容和原因。
9. Hermes 运行 lint/build 检查。
10.赫尔墨斯承诺并推动。

## MVP 真相查找循环

1. 将用户问题解析为主题/项目/范围。
2. 搜索 `index.md`、文件名、标题和标签。
3. 阅读候选人的概念说明。
4. 遵循重要事实主张所引用的原始来源路径。
5. 引用并自信地回答。
6. 如果证据缺失，请说“证据不足”，并可以选择创建查询注释。

## MVP 会话到知识循环

1. 首先应用内存提取阈值。不要仅仅因为发生了会话就生成持久的会话注释。
2. 如果超过阈值，则在“50-sessions/active/”下创建“episodic”会话摘要，其中包含自适应保留元数据和固定正文部分。
3. 提取状态转换：持久结果、决策、验证的程序、添加的来源、开放性问题和规范化项目。
4. 使用熵默认拒绝应用负内存过滤：不存储 shell/工具日志、思想链、重复检索摘录、对话支架、已完成的任务跟踪、重试命令或未跟踪的未来可能状态。
5. 请勿包含文字记录、按时间顺序重播、工具日志、shell 输出垃圾邮件或思想链部分。
6. 快速规范化持久项目：决策 -> `decisions/`、工作流程 -> `procedures/`、综合 -> `concepts/`、稳定偏好 -> `user-profile.md`、经过验证的操作规则 -> 项目内存。
7. 规范化后，更新`promoted_items`，设置或走向`canonicalized: true`，并通过半衰期机制降低会话检索优先级。
8.维护期间，每个半衰期后衰减`retrieval_weight`；仅在规范化、旧的、未使用的和未引用的情况下标记 `archive_candidate: true`；起草压缩建议而不是删除。
9. 验证后，将重复程序推广到 Hermes 技能。

## MVP 完成标准

- 可以通过原始源保存和源支持的概念更新来端到端地摄取一个新源。
- 新的 Hermes 会话可以通过阅读金库并遵循原始源链接来回答问题。
- Lint 捕获丢失的原始源元数据、丢失的 frontmatter 和丢失的源链接。
- 更新后VitePress构建成功。
- Git 历史记录清楚地显示发生了什么变化。

# 实施计划

## 阶段 0：决定Vault 拓扑

**目标：** 选择“/Users/a17/wiki”是保留独立的黑曜石保管库还是成为更大的个人保管库的子文件夹。

**文件：**
- 评论：`/Users/a17/wiki/SCHEMA.md`
- 如果独立的话稍后创建：`/Users/a17/wiki/.obsidian/` 通过 Obsidian UI，而不是 Hermes

**建议：** 使用“/Users/a17/wiki”作为代理内存研究主题的独立黑曜石保管库。稍后创建一个单独的私人个人保管库并链接/镜像选定的研究页面。

**验证：** 在 Obsidian 中打开 `/Users/a17/wiki` 作为保管库并确认链接呈现。

## 第一阶段：添加代理操作规则

**目标：** 使金库能够为赫尔墨斯和未来的特工进行自我描述。

**文件：**
- 创建：`AGENTS.md`
- 如果采用更大的布局，则创建：`memory-policy.md`或`00-system/memory-policy.md`

**AGENTS.md 草案：**

```markdown
# Agent Rules for this Obsidian Wiki

- Preserve raw source text before synthesis.
- Search existing pages before creating new pages.
- Update index.md and log.md for every knowledge change.
- Cite raw sources for non-trivial claims.
- Do not edit raw sources except to fix preservation/extraction metadata.
- Use git status before and after edits.
- Commit and push completed changes when remote is available.
- Do not read or modify private folders unless explicitly instructed.
```

**验证：**要求赫尔墨斯在新的会话中解释保管库规则；当 workdir 是存储库时，它应该自动加载 AGENTS.md 。

## 第 2 阶段：添加面向黑曜石的仪表板

**目标：** 使 Obsidian 中的审阅队列对人类可见。

**文件：**
- 创建：`dashboards/research-review.md`
- 创建可选：`dashboards/sources-needing-review.md`

**数据视图示例：**

```markdown
# Research Review

```dataview
TABLE type, confidence, contested, updated
FROM "concepts"
WHERE contested = true OR confidence = "low"
SORT updated DESC
```
```

**Bases alternative:** create a Base filtered by `type`, `confidence`, `contested`, `updated`, and `extraction_status`.

**Verification:** Open dashboard in Obsidian and confirm table/base lists notes.

## Phase 3: Add source ingestion command convention

**Objective:** Define a repeatable Hermes prompt/procedure for ingestion.

**Files:**
- Create: `40-procedures/ingest-source.md` or `procedures/ingest-source.md`

**Procedure:**

```markdown
# Ingest Source Procedure

Input: URL/PDF/text and target topic.
1. Capture raw source markdown under raw/<type>/.
2. Add source metadata and hash when possible.
3. Preserve parsed source text.
4. Extract claims/entities with confidence.
5. Search existing concept pages.
6. Patch the most relevant page or create a new one only if threshold is met.
7. Update index.md and log.md.
8. Commit with docs: ingest <source/topic>.
```

**验证：** 在一个新源上运行该过程并检查 git diff。

## 第 4 阶段：添加 lint 脚本

**目标：** 在拱顶变得不可靠之前捕获结构漂移。

**文件：**
- 创建：`scripts/wiki_lint.py`
- 修改：`.github/workflows/wiki-maintenance.yml`以调用脚本而不是内联Python

**检查：**
- frontmatter 所需的键
- 原始文件包括解析的源文本
- 损坏的降价链接
- 重复的source_url
- 缺少更改概念/原始文件的日志更新
- 私人文件夹从 docsify/publication 中排除

**验证：**运行 `python3 script/wiki_lint.py`；预期通过。

## 第 5 阶段：添加会话到笔记工作流程

**目标：** 保留有用的 Hermes 会话而不污染持久内存。

**文件：**
- 创建：`procedures/session-to-note.md`
- 创建文件夹：`sessions/` 或 `50-sessions/`

**政策：**
- 默认情况下存储简洁的会话摘要，而不是原始记录。
- 提取持久的决定/悬而未决的问题/程序。
- 除非需要重现性，否则不要存储临时命令输出。
- 将可重复使用的工作流程推广到 Hermes 技能，而不仅仅是黑曜石笔记。

**验证：** 将之前的 wiki 会话转换为注释，并确保不包含任何机密/临时日志。

## 第 6 阶段：可选的 MCP/REST 集成

**目标：** 仅在文件系统优先的工作流程稳定后，才能将 Hermes 与 Obsidian 的活动文件和插件 API 集成。

**步骤：**
1.安装Obsidian Local REST API插件。
2. 保持 API 本地化，并将 token 存储在 Hermes `.env` 中，而不是在注释中。
3. 如果使用 Obsidian MCP 服务器，请配置 Hermes MCP：

```bash
hermes mcp add obsidian --command "npx -y obsidian-mcp-server"
hermes mcp test obsidian
hermes mcp configure obsidian
```

确切的命令取决于所选的 MCP 封装；在运行之前验证当前的包文档。

**验证：** 使用 MCP/REST 读取活动笔记并修补草稿笔记中的测试标题。

## 第 7 阶段：可选检索索引

**目标：** 一旦笔记超出了 index.md + search_files 可以很好处理的范围，就可以提高召回率。

**文件：**
- 创建：`scripts/build_index.py`
- 创建派生：`.hermes-kb/index.sqlite`
- 将 `.hermes-kb/` 添加到 `.gitignore` 除非有意共享索引

**验证：** 运行基准查询并比较之前/之后的召回率。

# 验收标准

一个有效的 Hermes + Obsidian 个人知识库应该满足：

- Obsidian可以正常浏览/编辑所有笔记。
- Hermes 可以通过原始保存、引用、索引/日志更新和 git 提交来摄取新源。
- Hermes 可以通过引用的笔记回答研究问题。
- Hermes 可以区分用户配置文件、项目内存、原始来源和会话注释。
- 仪表板显示需要审阅的注释。
- lint 命令捕获丢失的前文、丢失的解析源文本和损坏的链接。
- 默认情况下，敏感/私人文件夹被排除在自动化和发布之外。
- 在添加嵌入之前，系统有一个记录的检索/评估计划。

# 开放式问题

1. 用户的主要个人黑曜石金库是否应该与公共/可发布的研究金库分开？
2. Hermes 应该仅通过文件系统直接写入 Obsidian，还是应该使用本地 REST API 来感知活动文件？
3. 哪些笔记应该有资格在 GitHub Pages / Docsify 发布？
4. 最低审核 UI 是多少：Obsidian Dataview/Base、GitHub PR，或两者？
5. Hermes 会话摘要应如何导出：手动 `/save`、session_search 摘要或计划的 cron 作业？
6. 未来的 Hermes 内存提供商应该使用 Obsidian 作为后端，还是应该将 Obsidian 保留为带有检索工具的独立规范知识库？

# 源图

|索赔 |来源 |类型 |可靠性 |笔记|
|---|---|---|---|---|
|持久的代理内存应该是可检查、可编辑、集成​​和可操作的 |概念/llm-wiki-agent-memory-research-framework.md |合成|中等|现有 wiki 综合 |
| Karpathy 模式通过摄取/查询/lint 操作将原始源、wiki 和模式分开 |原始/文章/karpathy-llm-wiki-gist-2026.md |主要/来源 |高|概念种子 |
| Markdown+git 是一种新兴的规范记忆模式 | raw/github/wuphf-repo-readme.md； raw/github/llm-wiki-compiler-repo-readme.md | github/自述文件 |中高 |实施证据，而非通用基准 |
|上下文工程映射到写入/选择/压缩/隔离| raw/github/langchain-context-engineering-repo-readme.md； raw/github/langchain-how-to-fix-your-context-readme.md | github/自述文件 |中高 |实际实施参考|
|不加区别的内存存储会产生垃圾和反馈循环raw/github/mem0-issue-4573-内存-audit-junk.md | github 问题 |中等|单个详细生产案例研究|
|代理全局记忆需要对话/项目范围界定| raw/github/letta-issue-652-per-conversation-context-scoping.md | github 问题 |中高 |具体设计问题|
| Hermes 内置内存有限，最适合紧凑耐用的转向 | Hermes 内存文档于 2026 年 5 月 14 日获取产品文档 |高| MEMORY.md/USER.md 小提示注入存储 |
| Obsidian Web Clipper 将网页内容本地保存到 Markdown 文件 | Obsidian Web Clipper 文档/自述文件于 2026 年 5 月 14 日获取 |产品文档/github |高|有用的捕获层|
| Obsidian Properties 和 Bases 支持 Markdown 上的结构化元数据/类似数据库的视图 |获取黑曜石帮助 2026-05-14 |产品文档 |高|有用的审查仪表板 |
| Dataview 索引 Markdown 元数据和查询注释 | Dataview 文档于 2026 年 5 月 14 日获取 |插件文档 |中高 |社区插件，成熟但不核心 |
| Obsidian Local REST API 可以公开读/写/搜索/补丁/活动文件操作和 MCP | 2026 年 5 月 14 日获取本地 REST API 自述文件 |插件文档/github |中高 |可选集成 |

# 当前的更正/证据差距

- Obsidian 官方帮助通过 Obsidian Publish 提供，并通过预加载的 Markdown URL 获取。如果实施精确的插件设置，则应重新检查内容。
- 该计划尚未检查用户的实际黑曜石金库路径或安装的插件。
- MCP 包命令因所选 Obsidian MCP 服务器而异；在配置 Hermes MCP 之前验证包文档。
- 尚未对用户的真实笔记运行检索基准。
