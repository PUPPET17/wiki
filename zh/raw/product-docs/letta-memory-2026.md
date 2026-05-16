---
source_url: https://docs.letta.com/letta-code/memory
fetched_url: https://docs.letta.com/letta-code/memory
source_type: product-docs
author: Letta
source_date: captured 2026-05-14
ingested: 2026-05-14
sha256: 5b9010a2cf6fb0732c428aff7680ca0130e53a28edea17643bc58627679c2970
raw_preservation: full_html_article_text_candidate
extraction_method: readability_lxml_html2text
html_bytes: 93833
parsed_chars: 5257
---

# 内存 |莱塔文档

## 源元数据

- 来源网址：https://docs.letta.com/letta-code/memory
- 获取的 URL：https://docs.letta.com/letta-code/memory
- 来源类型：产品文档
——作者：莱塔
- 来源日期：拍摄于 2026-05-14
- 摄入时间：2026-05-14
- 可靠性：高
- 原始保存状态：full_html_article_text_candidate
- 提取方法：readability_lxml_html2text

## 解析后的源文本

借助 Letta Code，您可以无限期地使用同一个代理（跨会话、数天或数月），并且随着时间的推移，它会变得更好。您的代理会记住过去的交互，了解您的偏好，并在工作时自我编辑其记忆。

Letta Code 还允许您自定义代理的个性。使用 Claude Code 或 Codex，每个用户都会获得行为相同的相同代理。借助 Letta Code，您可以深度个性化您的代理，使其独一无二。

在 Letta Code 中，有两个重要的会话概念：**代理**和**会话**。

* **代理**是一个具有名称、内存、模型配置、消息和其他状态的实体。
  * **对话** 是与代理的消息线程（或“会话”）。您可以与单个代理进行多个并行对话。每个代理还有一个“默认对话”或“主要聊天”。

当您在项目目录中运行“letta” CLI 命令时，Letta Code 将恢复与上次使用的代理的默认对话。在 Letta Code 桌面应用程序中，左侧边栏按代理排序，您可以看到按活动日期排序的对话。

如果您想使用单个代理并行运行多个 CLI 会话（例如在单独的终端窗口中），请使用 `letta --new` 开始新对话。在桌面应用程序中，只需按记事本图标即可开始新对话。

Letta Code 预装了一个默认代理（称为“Letta Code”）。要在 CLI 中交换代理，请使用“/agents”。您可以使用“/pin”在 CLI 中收藏代理，或单击桌面应用程序中的收藏按钮。

When you run `/init`, Letta Code performs an interactive initialization in the main conversation, guided by context constitution principles for durable identity, preferences, and project structure. Letta Code will read from prior Claude Code and OpenAI Codex sessions to learn about your working style and past + ongoing projects using [subagents](/letta-code/subagents).

每当您希望代理重新分析您的项目时，例如在重大更改或添加您希望代理摄取的文档之后，请再次运行“/init”。

如果您的内存结构随着时间的推移发生了漂移或变得混乱，请运行“/doctor”来审核当前的内存布局并对其进行优化，以实现正确的内存放置和有效的令牌使用。

您的 Letta Code 代理可以自行编辑自己的记忆，并将使用对话的上下文来决定何时编辑其记忆（例如，存储在会话中学到的新信息）。在某些情况下，您可能希望通过“/remember”命令主动指示代理记住某些内容。

例如，如果您发现您的代理犯了一个容易避免的错误，您可以提供直接指导：

> /记住不要再犯同样的错误

您还可以使用“/remember”命令，而无需任何额外的提示，代理将根据上下文推断您的意图以进行内存编辑。

如果您的代理不能始终记住重要信息，请要求代理更新其策略，以便将来更加勤奋，并传达您希望其存储哪些信息。例如，“主动存储有关我的偏好、决定以及我明确要求您记住的任何内容的信息。”

为了改善主动记忆创建和巩固，Letta Code 会定期启动睡眠时间（梦）子代理来反映您最近的对话和互动。这些代理在后台启动，并且通常运行许多步骤，因为子代理是彻底的内存编辑器。

您可以使用 CLI 中的“/sleeptime”命令来配置反射设置，或者单击应用程序右下角的沉睡外星人图标。

**触发器**决定反射子代理自动启动的频率：

* `Off`：选择禁用反射子代理
  * `Step count`：每 N 个用户消息启动一个反射子代理
  * `Compaction event`（推荐，仅限 MemFS）：当上下文窗口被压缩/汇总时启动反射子代理

当梦想触发器触发时，Letta Code 会自动在后台启动梦想子代理。

MemFS ([context repositories](https://www.letta.com/blog/context-repositories)) is available in Letta Code version 0.15 and later. All new agents have MemFS enabled by default.

要在较旧的代理上启用 MemFS，请运行“/memfs enable”。

Your agent’s memory is stored in a git-backed filesystem called **MemFS** (short for “memory filesystem”), also known as a [context repository](https://www.letta.com/blog/context-repositories). Memory is organized as a directory of markdown files, cloned locally to `~/.letta/agents/<your-agent-id>/memory`. Your agent edits these files directly using its bash tools, then commits and pushes to save changes — giving you a full version history of everything your agent has learned.

`system/` 目录中的文件始终完整加载到代理的系统提示符中。代理可以通过内存树（文件名和描述）看到“system/”之外的文件，但它们的内容不会自动加载——保持上下文窗口的精简。

For a full explanation of the MemFS file format, the `system/` hierarchy, git synchronization, and the `letta memory` CLI subcommands, see the [MemFS reference](/letta-code/memfs).
