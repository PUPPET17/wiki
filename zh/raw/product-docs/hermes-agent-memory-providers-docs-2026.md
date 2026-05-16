---
source_url: https://raw.githubusercontent.com/NousResearch/hermes-agent/main/website/docs/user-guide/features/memory-providers.md
retrieved: 2026-05-14
source_type: product-docs
reliability: high
raw_preservation: full_parsed_text
extraction_status: complete
capture_method: raw_github_markdown
content_sha256: fbe06fde298cb34fbc4aaedb9e77d7d014e4723860bd3201c1b4586f305c4cec
---

# Hermes 代理内存提供程序文档

## 源元数据

- source_url：https://raw.githubusercontent.com/NousResearch/hermes-agent/main/website/docs/user-guide/features/memory-providers.md
- 检索时间：2026-05-14
- 来源类型：产品文档
- 捕获方法：raw_github_markdown
- 提取注释：direct_raw_markdown_fetch
- content_sha256：`fbe06fde298cb34fbc4aaedb9e77d7d014e4723860bd3201c1b4586f305c4cec`

## 解析后的源文本

---
侧边栏位置：4
标题：“内存提供者”
描述：“外部内存提供程序插件 — Honcho、OpenViking、Mem0、Hindsight、Holographic、RetainDB、ByteRover、Supermemory”
---

# 内存提供者

Hermes Agent 附带 8 个外部内存提供程序插件，除了内置 MEMORY.md 和 USER.md 之外，还为代理提供持久的跨会话知识。一次只能有**一个**外部提供程序处于活动状态 - 内置内存始终与其一起处于活动状态。

## 快速入门

```bash
hermes memory setup      # interactive picker + configuration
hermes memory status     # check what's active
hermes memory off        # disable external provider
```

您还可以通过 `hermes plugins` → Provider Plugins → Memory Provider 选择活动内存提供程序。

或者在`~/.hermes/config.yaml`中手动设置：

```yaml
memory:
  provider: openviking   # or honcho, mem0, hindsight, holographic, retaindb, byterover, supermemory
```

## 它是如何工作的

当内存提供者处于活动状态时，Hermes 会自动：

1. **将提供者上下文**注入系统提示符（提供者知道的内容）
2. **每轮前预取相关内存**（后台，非阻塞）
3. 每次响应后，**将对话同步到**提供者
4. **在会话结束时提取记忆**（对于支持它的提供商）
5. **将内置内存写入**镜像到外部提供者
6. **添加特定于提供商的工具**，以便代理可以搜索、存储和管理记忆

内置内存（MEMORY.md / USER.md）继续像以前一样工作。外部提供者是附加的。

## 可用的提供商

### 本町

具有辩证推理、会话范围上下文注入、语义搜索和持久结论的人工智能原生跨会话用户建模。基础上下文现在包括会话摘要以及用户代表和对等卡，使代理了解已经讨论的内容。

| | |
|---|---|
| **最适合** |具有跨会话上下文、用户代理对齐的多代理系统
| **需要** | `pip install honcho-ai` + [API 密钥](https://app.honcho.dev) 或自托管实例 |
| **数据存储** | Honcho Cloud 或自托管 |
| **成本** | Honcho 定价（云）/免费（自托管）|

**工具 (5)：** `honcho_profile`（读取/更新对等卡）、`honcho_search`（语义搜索）、`honcho_context`（会话上下文 - 摘要、表示、卡片、消息）、`honcho_reasoning`（LLM 合成）、`honcho_conclude`（创建/删除结论）

**架构：**两层上下文注入——基础层（会话摘要+表示+对等卡，在“contextCadence”上刷新）加上辩证补充（LLM推理，在“dialecticCadence”上刷新）。 Dialectic 根据基本上下文是否存在自动选择冷启动提示（一般用户事实）与热提示（会话范围上下文）。

**三个正交配置旋钮**独立控制成本和深度：

- `contextCadence` — 基础层刷新的频率（API 调用频率）
- `dialecticCadence` — dialectic LLM 触发的频率（LLM 调用频率）
- `dialecticDepth` — 每个辩证调用传递多少个 `.chat()`（1-3，推理深度）

**设置向导：**
```bash
hermes memory setup        # select "honcho" — runs the Honcho-specific post-setup
```

旧的“hermes honcho setup”命令仍然有效（它现在重定向到“hermes memory setup”），但仅在选择 Honcho 作为活动内存提供程序后才注册。

**Config:** `$HERMES_HOME/honcho.json` (profile-local) or `~/.honcho/config.json` (global). Resolution order: `$HERMES_HOME/honcho.json` > `~/.hermes/honcho.json` > `~/.honcho/config.json`. See the [config reference](https://github.com/hermes-ai/hermes-agent/blob/main/plugins/memory/honcho/README.md) and the [Honcho integration guide](https://docs.honcho.dev/v3/guides/integrations/hermes).

<详情>
<summary>完整配置参考</summary>

|关键|默认 |描述 |
|-----|---------|-------------|
| `apiKey` | --|来自 [app.honcho.dev](https://app.honcho.dev) 的 API 密钥 |
| `baseUrl` | --|自托管 Honcho 的基本 URL |
| `peerName` | --|用户对等身份 |
| `aiPeer` |主机密钥 | AI 对等身份（每个档案一个） |
| `工作区` |主机密钥 |共享工作区 ID |
| `contextTokens` | `null`（无上限）|每回合自动注入上下文的代币预算。在字边界处截断 |
| `contextCadence` | `1` | `context()` API 调用之间的最小轮次（基础层刷新） |
| `辩证节奏` | `2` | `peer.chat()` LLM 调用之间的最小轮次。推荐 1-5。仅适用于“混合”/“上下文”模式 |
| `辩证深度` | `1` |每个辩证调用的“.chat()”传递次数。夹紧 1-3。第0道：冷/暖提示，第1道：自审，第2道：对账|
| `辩证深度级别` | `空` |每次传递的可选推理级别数组，例如`[“最小”、“低”、“中”]`。覆盖比例默认值 |
| `辩证推理水平` | ''低'` |基本推理级别：`最小`、`低`、`中`、`高`、`最大` |
| `辩证动态` | `真实` |当为“true”时，模型可以通过工具参数覆盖每次调用的推理级别 |
| `dialecticMaxChars` | `600` |辩证结果注入系统提示符的最大字符数 |
| `recallMode` | ''混合'` | `hybrid`（自动注入+工具），`context`（仅注入），`tools`（仅工具）|
| `写入频率` | `'异步'` |何时刷新消息：“async”（后台线程）、“turn”（同步）、“session”（批量结束）或整数 N |
| `保存消息` | `真实` |是否将消息持久保存到 Honcho API |
| `观察模式` | ''定向'` | “定向”（全部开启）或“统一”（共享池）。用“观察”对象覆盖 |
| `messageMaxChars` | `25000` |每条消息的最大字符数（如果超过则分块）|
| `dialecticMaxInputChars` | `10000` | `peer.chat()` 辩证查询输入的最大字符数 |
| `会话策略` | `'每个目录'` | “每个目录”、“每个存储库”、“每个会话”、“全局” |

</详情>

<详情>
<summary>最小 honcho.json（云）</summary>

```json
{
  "apiKey": "your-key-from-app.honcho.dev",
  "hosts": {
    "hermes": {
      "enabled": true,
      "aiPeer": "hermes",
      "peerName": "your-name",
      "workspace": "hermes"
    }
  }
}
```

</详情>

<详情>
<summary>最小的honcho.json（自托管）</summary>

```json
{
  "baseUrl": "http://localhost:8000",
  "hosts": {
    "hermes": {
      "enabled": true,
      "aiPeer": "hermes",
      "peerName": "your-name",
      "workspace": "hermes"
    }
  }
}
```

</详情>

:::tip 从 `hermes honcho` 迁移
如果您以前使用过“hermes honcho setup”，您的配置和所有服务器端数据都完好无损。只需再次通过设置向导重新启用或手动设置“memory.provider：honcho”即可通过新系统重新激活。
:::

**多点设置：**

Honcho 将对话建模为点对点交换消息——每个 Hermes 配置文件中都有一个用户点加上一个 AI 点，所有这些都共享一个工作空间。工作空间是共享环境：用户对等点是跨配置文件的全局，每个 AI 对等点都有自己的身份。每个人工智能同行都会根据自己的观察构建独立的表示/卡片，因此“编码器”配置文件保持面向代码的状态，而“作家”配置文件则针对同一用户保持编辑性。

映射：

|概念 |它是什么 |
|--------|------------|
| **工作区** |共享环境。一个工作区下的所有 Hermes 配置文件都看到相同的用户身份。 |
| **用户对等点** (`peerName`) |人类。在工作区中的配置文件之间共享。 |
| **AI 对等** (`aiPeer`) |每个爱马仕资料一份。主机密钥 `hermes` → 默认；其他人的“hermes.<个人资料>”。 |
| **观察** |每个对等点切换控制 Honcho 根据谁的消息进行建模。 “定向”（默认，所有四个都打开）或“统一”（单观察者池）。 |

### 新的个人资料，新的 Honcho 同行

```bash
hermes profile create coder --clone
```

`--clone` 在 `honcho.json` 中使用 `aiPeer: "coder"`、共享的 `workspace`、继承的 `peerName`、`recallMode`、`writeFrequency`、`observation` 等创建一个 `hermes.coder` 主机块。AI 对等点是在 Honcho 中急切创建的，因此它存在于第一条消息之前。

### 现有配置文件，回填 Honcho 同行

```bash
hermes honcho sync
```

扫描每个 Hermes 配置文件，为任何没有配置文件的主机块创建主机块，继承默认“hermes”块的设置，并急切地创建新的 AI 对等点。幂等 — 跳过已经具有主机块的配置文件。

### 每个配置文件的观察

每个主机块都可以独立地覆盖观察配置。示例：以代码为中心的配置文件，其中 AI 同行观察用户但不进行自我建模：

```json
"hermes.coder": {
  "aiPeer": "coder",
  "observation": {
    "user": { "observeMe": true, "observeOthers": true },
    "ai":   { "observeMe": false, "observeOthers": true }
  }
}
```

**观察切换（每个同伴一组）：**

|切换|效果|
|--------|--------|
| `观察我` | Honcho 根据自己的消息构建该对等点的表示 |
| `观察其他人` |该对等点观察其他对等点的消息（提供跨对等推理）|

通过“observationMode”预设：

- **`"定向"`**（默认）- 所有四个标志均打开。充分相互观察；实现跨同行辩证法。
- **`"统一"`** — 用户 `observeMe: true`，AI `observeOthers: true`，其余为 false。单观察员池；人工智能对用户建模，但不对自身建模，用户同行仅对自我建模。

Server-side toggles set via the [Honcho dashboard](https://app.honcho.dev) win over local defaults — synced back at session init.

See the [Honcho page](./honcho.md#observation-directional-vs-unified) for the full observation reference.

<详情>
<summary>完整的 honcho.json 示例（多配置文件）</summary>

```json
{
  "apiKey": "your-key",
  "workspace": "hermes",
  "peerName": "eri",
  "hosts": {
    "hermes": {
      "enabled": true,
      "aiPeer": "hermes",
      "workspace": "hermes",
      "peerName": "eri",
      "recallMode": "hybrid",
      "writeFrequency": "async",
      "sessionStrategy": "per-directory",
      "observation": {
        "user": { "observeMe": true, "observeOthers": true },
        "ai": { "observeMe": true, "observeOthers": true }
      },
      "dialecticReasoningLevel": "low",
      "dialecticDynamic": true,
      "dialecticCadence": 2,
      "dialecticDepth": 1,
      "dialecticMaxChars": 600,
      "contextCadence": 1,
      "messageMaxChars": 25000,
      "saveMessages": true
    },
    "hermes.coder": {
      "enabled": true,
      "aiPeer": "coder",
      "workspace": "hermes",
      "peerName": "eri",
      "recallMode": "tools",
      "observation": {
        "user": { "observeMe": true, "observeOthers": false },
        "ai": { "observeMe": true, "observeOthers": true }
      }
    },
    "hermes.writer": {
      "enabled": true,
      "aiPeer": "writer",
      "workspace": "hermes",
      "peerName": "eri"
    }
  },
  "sessions": {
    "/home/user/myproject": "myproject-main"
  }
}
```

</详情>

See the [config reference](https://github.com/hermes-ai/hermes-agent/blob/main/plugins/memory/honcho/README.md) and [Honcho integration guide](https://docs.honcho.dev/v3/guides/integrations/hermes).


---

### 开放维京

Volcengine（字节跳动）的上下文数据库，具有文件系统式的知识层次结构、分层检索和自动内存提取到 6 个类别。

| | |
|---|---|
| **最适合** |具有结构化浏览功能的自托管知识管理 |
| **需要** | `pip install openviking` + 运行服务器 |
| **数据存储** |自托管（本地或云）|
| **成本** |免费（开源，AGPL-3.0）|

**工具：** `viking_search`（语义搜索）、`viking_read`（分层：摘要/概述/完整）、`viking_browse`（文件系统导航）、`viking_remember`（存储事实）、`viking_add_resource`（摄取 URL/文档）

**设置：**
```bash
# Start the OpenViking server first
pip install openviking
openviking-server

# Then configure Hermes
hermes memory setup    # select "openviking"
# Or manually:
hermes config set memory.provider openviking
echo "OPENVIKING_ENDPOINT=http://localhost:1933" >> ~/.hermes/.env
```

**主要特点：**
- 分层上下文加载：L0（~100 个令牌）→ L1（~2k）→ L2（完整）
- 会话提交时自动内存提取（配置文件、首选项、实体、事件、案例、模式）
- 用于分层知识浏览的“viking://” URI 方案

---

###内存0

服务器端 LLM 事实提取，具有语义搜索、重新排名和自动重复数据删除功能。

| | |
|---|---|
| **最适合** |无需干预的内存管理 — Mem0 自动处理提取 |
| **需要** | `pip install mem0ai` + API 密钥 |
| **数据存储** | Mem0 云 |
| **成本** | Mem0 定价 |

**工具：** `mem0_profile`（所有存储的记忆），`mem0_search`（语义搜索+重新排名），`mem0_conclude`（逐字存储事实）

**设置：**
```bash
hermes memory setup    # select "mem0"
# Or manually:
hermes config set memory.provider mem0
echo "MEM0_API_KEY=your-key" >> ~/.hermes/.env
```

**配置：** `$HERMES_HOME/mem0.json`

|关键|默认 |描述 |
|-----|---------|-------------|
| `用户 ID` | `hermes 用户` |用户标识符|
| `agent_id` | “爱马仕”|代理标识符|

---

### 事后诸葛亮

具有知识图、实体解析和多策略检索的长期记忆。 “hindsight_reflect”工具提供了其他提供商无法提供的跨内存综合功能。通过会话级文档跟踪自动保留完整的对话轮次（包括工具调用）。

| | |
|---|---|
| **最适合** |基于知识图谱的实体关系召回 |
| **需要** |云：来自 [ui.hindsight.vectorize.io](https://ui.hindsight.vectorize.io) 的 API 密钥。本地：LLM API 密钥（OpenAI、Groq、OpenRouter 等）|
| **数据存储** | Hindsight 云或本地嵌入式 PostgreSQL |
| **成本** |事后定价（云）或免费（本地）|

**工具：** `hindsight_retain`（实体提取存储）、`hindsight_recall`（多策略搜索）、`hindsight_reflect`（跨内存合成）

**设置：**
```bash
hermes memory setup    # select "hindsight"
# Or manually:
hermes config set memory.provider hindsight
echo "HINDSIGHT_API_KEY=your-key" >> ~/.hermes/.env
```

安装向导会自动安装依赖项，并且仅安装所选模式所需的内容（云的“hindsight-client”，本地的“hindsight-all”）。需要 `hindsight-client >= 0.4.22`（如果过时，则会在会话启动时自动升级）。

**本地模式 UI：** `hindsight-embed -p hermes ui start`

**配置：** `$HERMES_HOME/hindsight/config.json`

|关键|默认 |描述 |
|-----|---------|-------------|
| `模式` | `云` | “云”或“本地”|
| `银行_id` | “爱马仕”|内存库标识符|
| `recall_budget` | `中` |回忆彻底性：`低`/`中`/`高` |
| `内存模式` | `混合` | `hybrid`（上下文 + 工具）、`context`（仅自动注入）、`tools`（仅工具）|
| `自动保留` | `真实` |自动保留对话轮次 |
| `自动召回` | `真实` |每次转弯前自动回忆记忆 |
| `retain_async` | `真实` |在服务器上异步处理保留 |
| `retain_context` | `Hermes 代理与用户之间的对话` |保留记忆的上下文标签 |
| `retain_tags` | — |应用于保留记忆的默认标签；与每次调用工具标签合并 |
| `保留源` | — |附加到保留内存的可选“metadata.source” |
| `retain_user_prefix` | `用户` |用户提交自动保留的成绩单之前使用的标签 |
| `retain_assistant_prefix` | `助理` |助理提交自动保留的成绩单之前使用的标签 |
| `recall_tags` | — |召回时过滤的标签 |

See [plugin README](https://github.com/NousResearch/hermes-agent/blob/main/plugins/memory/hindsight/README.md) for the full configuration reference.

---

### 全息

本地 SQLite 事实存储，具有 FTS5 全文搜索、信任评分和用于组合代数查询的 HRR（全息简化表示）。

| | |
|---|---|
| **最适合** |仅本地内存，具有高级检索功能，无外部依赖性 |
| **需要** |什么都没有（SQLite 始终可用）。 NumPy 对于 HRR 代数是可选的。 |
| **数据存储** |本地 SQLite |
| **成本** |免费|

**工具：** `fact_store`（9 个操作：添加、搜索、探测、相关、推理、矛盾、更新、删除、列表）、`fact_feedback`（训练信任分数的有用/无用评级）

**设置：**
```bash
hermes memory setup    # select "holographic"
# Or manually:
hermes config set memory.provider holographic
```

**配置：** `plugins.hermes-memory-store`下的`config.yaml`

|关键|默认 |描述 |
|-----|---------|-------------|
| `db_path` | `$HERMES_HOME/memory_store.db` | SQLite 数据库路径 |
| `自动提取` | `假` |会话结束时自动提取事实 |
| `默认信任` | `0.5` |默认信任评分 (0.0–1.0) |

**独特的能力：**
- `probe` — 特定于实体的代数回忆（关于人/事物的所有事实）
- `reason` — 跨多个实体的组合 AND 查询
- `contradict` — 自动检测冲突事实
- 不对称反馈的信任评分（+0.05 有帮助/-0.10 无帮助）

---

### 保留数据库

具有混合搜索（Vector + BM25 + Reranking）、7 种内存类型和增量压缩的云内存 API。

| | |
|---|---|
| **最适合** |已经使用 RetainDB 基础设施的团队 |
| **需要** | RetainDB 帐户 + API 密钥 |
| **数据存储** | RetainDB 云 |
| **成本** | 20 美元/月 |

**工具：** `retaindb_profile`（用户配置文件）、`retaindb_search`（语义搜索）、`retaindb_context`（任务相关上下文）、`retaindb_remember`（存储类型+重要性）、`retaindb_forget`（删除内存）

**设置：**
```bash
hermes memory setup    # select "retaindb"
# Or manually:
hermes config set memory.provider retaindb
echo "RETAINDB_API_KEY=your-key" >> ~/.hermes/.env
```

---

### 字节漫游

通过“brv”CLI 实现持久内存 — 具有分层检索功能的分层知识树（模糊文本 → LLM 驱动的搜索）。本地优先，可选云同步。

| | |
|---|---|
| **最适合** |想要使用 CLI 实现便携式、本地优先内存的开发人员 |
| **需要** | ByteRover CLI (`npm install -g byteover-cli` 或 [安装脚本](https://byterover.dev)) |
| **数据存储** |本地（默认）或 ByteRover 云（可选同步）|
| **成本** |免费（本地）或 ByteRover 定价（云）|

**工具：** `brv_query`（搜索知识树），`brv_curate`（存储事实/决策/模式），`brv_status`（CLI版本+树统计）

**设置：**
```bash
# Install the CLI first
curl -fsSL https://byterover.dev/install.sh | sh

# Then configure Hermes
hermes memory setup    # select "byterover"
# Or manually:
hermes config set memory.provider byterover
```

**主要特点：**
- 自动预压缩提取（在上下文压缩丢弃见解之前保存见解）
- 知识树存储在“$HERMES_HOME/byterover/”（配置文件范围）
- SOC2 Type II 认证云同步（可选）

---

### 超强记忆力

语义长期记忆，包括配置文件回忆、语义搜索、显式记忆工具以及通过超级记忆图 API 进行的会话结束对话摄取。

| | |
|---|---|
| **最适合** |通过用户分析和会话级图表构建进行语义回忆 |
| **需要** | `pip install supermemory` + [API 密钥](https://supermemory.ai) |
| **数据存储** |超记忆云|
| **成本** |超级内存定价|

**工具：** `supermemory_store`（保存显式记忆）、`supermemory_search`（语义相似性搜索）、`supermemory_forget`（通过 ID 或最佳匹配查询忘记）、`supermemory_profile`（持久配置文件 + 最近上下文）

**设置：**
```bash
hermes memory setup    # select "supermemory"
# Or manually:
hermes config set memory.provider supermemory
echo 'SUPERMEMORY_API_KEY=***' >> ~/.hermes/.env
```

**配置：** `$HERMES_HOME/supermemory.json`

|关键|默认 |描述 |
|-----|---------|-------------|
| `容器标签` | “爱马仕”|用于搜索和写入的容器标签。支持配置文件范围标签的“{identity}”模板。 |
| `自动召回` | `真实` |在轮流之前注入相关的内存上下文 |
| `自动捕获` | `真实` |每次响应后存储已清理的用户助理轮次 |
| `max_recall_results` | `10` |最大回忆项目以格式化为上下文|
| `配置文件频率` | `50` |包括第一回合和每 N 回合的个人资料信息 |
| `捕获模式` | `全部` |默认情况下跳过微小或琐碎的转弯 |
| `搜索模式` | `混合` |搜索模式：“混合”、“回忆”或“文档” |
| `api_timeout` | `5.0` | SDK 和摄取请求超时 |

**环境变量：** `SUPERMEMORY_API_KEY`（必需），`SUPERMEMORY_CONTAINER_TAG`（覆盖配置）。

**主要特点：**
- 自动上下文围栏——从捕获的回合中剥离回忆，以防止递归内存污染
- 会话结束对话摄取，以构建更丰富的图形级知识
- 在第一回合并以可配置的时间间隔注入的配置文件事实
- 简单的消息过滤（跳过“好的”、“谢谢”等）
- **配置文件范围的容器** — 在 `container_tag` 中使用 `{identity}` （例如 `hermes-{identity}` → `hermes-coder`）来隔离每个 Hermes 配置文件的内存
- **多容器模式** — 使用“custom_containers”列表启用“enable_custom_container_tags”，让代理跨命名容器读取/写入。自动操作（同步、预取）保留在主容器上。

<详情>
<summary>多容器示例</summary>

```json
{
  "container_tag": "hermes",
  "enable_custom_container_tags": true,
  "custom_containers": ["project-alpha", "shared-knowledge"],
  "custom_container_instructions": "Use project-alpha for coding context."
}
```

</详情>

**Support:** [Discord](https://supermemory.link/discord) · [support@supermemory.com](mailto:support@supermemory.com)

---

## 提供商比较

|供应商|存储|成本|工具|依赖关系 |独特的功能|
|----------|---------|------|--------|-------------|----------------|
| **本町** |云|付费| 5 | `本町爱` |辩证的用户建模+会话范围的上下文|
| **开放维京** |自托管 |免费| 5 | `openviking` + 服务器 |文件系统层次结构+分层加载|
| **内存0** |云|付费| 3 | `mem0ai` |服务器端LLM提取|
| **事后诸葛亮** |云/本地 |免费/付费| 3 | `事后客户` |知识图谱+反映综合 |
| **全息** |本地|免费| 2 |无 | HRR 代数 + 信任评分 |
| **保留数据库** |云| $20/月 | 5 | `请求` | Delta 压缩 |
| **ByteRover** |本地/云端 |免费/付费| 3 | `brv` CLI |预压缩提取|
| **超级记忆力** |云|付费| 4 | `超级记忆` |上下文防护 + 会话图摄取 + 多容器 |

## 配置文件隔离

Each provider's data is isolated per [profile](/docs/user-guide/profiles):

- **本地存储提供商**（Holographic、ByteRover）使用每个配置文件不同的“$HERMES_HOME/”路径
- **配置文件提供程序**（Honcho、Mem0、Hindsight、Supermemory）将配置存储在“$HERMES_HOME/”中，因此每个配置文件都有自己的凭据
- **云提供商** (RetainDB) 自动派生配置文件范围的项目名称
- **环境变量提供程序** (OpenViking) 通过每个配置文件的 `.env` 文件进行配置

## 构建内存提供程序

See the [Developer Guide: Memory Provider Plugins](/docs/developer-guide/memory-provider-plugin) for how to create your own.

## 摘录笔记

- 保留获取的降价/文本，用作 Hermes + Obsidian 个人知识库计划中的实施证据。
