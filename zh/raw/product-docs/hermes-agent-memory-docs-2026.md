---
source_url: https://raw.githubusercontent.com/NousResearch/hermes-agent/main/website/docs/user-guide/features/memory.md
retrieved: 2026-05-14
source_type: product-docs
reliability: high
raw_preservation: full_parsed_text
extraction_status: complete
capture_method: raw_github_markdown
content_sha256: dfdacda05df6b3c52171aef0b2b403c5dce45498a085bd316c9929a5c626b498
---

# Hermes Agent 持久内存文档

## 源元数据

- source_url：https://raw.githubusercontent.com/NousResearch/hermes-agent/main/website/docs/user-guide/features/memory.md
- 检索时间：2026-05-14
- 来源类型：产品文档
- 捕获方法：raw_github_markdown
- 提取注释：direct_raw_markdown_fetch
- content_sha256：`dfdacda05df6b3c52171aef0b2b403c5dce45498a085bd316c9929a5c626b498`

## 解析后的源文本

---
侧边栏位置：3
书名：《持久记忆》
描述：“Hermes Agent 如何记住跨会话 - MEMORY.md、USER.md 和会话搜索”
---

# 持久内存

Hermes Agent 拥有跨会话持续存在的有界、精心策划的内存。这可以让它记住您的偏好、您的项目、您的环境以及它学到的东西。

## 它是如何工作的

两个文件组成了代理的内存：

|文件 |目的|字符限制 |
|------|---------|------------|
| **内存.md** |特工的个人笔记——环境事实、惯例、学到的东西| 2,200 个字符（约 800 个标记）|
| **用户.md** |用户个人资料 — 您的偏好、沟通方式、期望 | 1,375 个字符（约 500 个标记）|

两者都存储在“~/.hermes/memories/”中，并在会话开始时作为冻结快照注入系统提示符中。代理通过“内存”工具管理自己的内存——它可以添加、替换或删除条目。

:::信息
字符限制可以集中记忆。当内存已满时，代理会合并或替换条目以为新信息腾出空间。
:::

## 内存如何显示在系统提示符中

在每个会话开始时，内存条目都会从磁盘加载并作为冻结块呈现到系统提示符中：

```
══════════════════════════════════════════════
MEMORY (your personal notes) [67% — 1,474/2,200 chars]
══════════════════════════════════════════════
User's project is a Rust web service at ~/code/myapi using Axum + SQLx
§
This machine runs Ubuntu 22.04, has Docker and Podman installed
§
User prefers concise responses, dislikes verbose explanations
```

格式包括：
- 显示哪个存储的标题（内存或用户配置文件）
- 使用百分比和字符数，以便代理了解容量
- 由“§”（节号）分隔符分隔的各个条目
- 条目可以是多行的

**冻结快照模式：** 系统提示注入在会话开始时捕获一次，并且在会话中不会更改。这是有意为之的——它保留了 LLM 的前缀缓存以提高性能。当代理在会话期间添加/删除内存条目时，更改会立即保留到磁盘，但在下一个会话开始之前不会出现在系统提示中。工具响应始终显示实时状态。

## 记忆工具操作

代理使用“内存”工具执行以下操作：

- **添加** — 添加新的内存条目
- **替换** - 用更新的内容替换现有条目（通过“old_text”使用子字符串匹配）
- **remove** — 删除不再相关的条目（通过 `old_text` 使用子字符串匹配）

没有“读取”操作 - 内存内容会在会话启动时自动注入系统提示符中。智能体将其记忆视为对话上下文的一部分。

### 子串匹配

“替换”和“删除”操作使用简短的唯一子字符串匹配 - 您不需要完整的输入文本。 `old_text` 参数只需是一个唯一的子字符串，可以准确识别一个条目：

```python
# If memory contains "User prefers dark mode in all editors"
memory(action="replace", target="memory",
       old_text="dark mode",
       content="User prefers light mode in VS Code, dark mode in terminal")
```

如果子字符串与多个条目匹配，则会返回错误，要求更具体的匹配。

## 两个目标的解释

### `记忆` — 特工的个人笔记

有关代理需要记住的有关环境、工作流程和经验教训的信息：

- 环境事实（操作系统、工具、项目结构）
- 项目约定和配置
- 发现工具怪癖和解决方法
- 完成的任务日记条目
- 有效的技能和技巧

### `user` — 用户个人资料

有关用户身份、偏好和沟通方式的信息：

- 姓名、角色、时区
- 沟通偏好（简洁与详细、格式偏好）
- 讨厌的事情和要避免的事情
- 工作流程习惯
- 技术技能水平

## 保存什么与跳过什么

### 保存这些（主动）

代理会自动保存 - 您无需询问。当它学习到以下内容时，它会保存：

- **用户首选项：**“相比 JavaScript，我更喜欢 TypeScript”→ 保存到 `user`
- **环境事实：**“此服务器运行 Debian 12 和 PostgreSQL 16”→ 保存到 `内存`
- **更正：**“不要对 Docker 命令使用 `sudo`，用户位于 docker 组中”→ 保存到 `memory`
- **约定：**“项目使用制表符、120个字符的行宽、Google风格的文档字符串”→保存到`内存`
- **完成的工作：**“2026-01-15将数据库从MySQL迁移到PostgreSQL”→保存到`内存`
- **显式请求：**“请记住，我的 API 密钥每月轮换一次”→ 保存到“内存”

### 跳过这些

- **琐碎/明显的信息：**“用户询问Python” - 太模糊而无用
- **容易重新发现的事实：**“Python 3.12 支持 f 字符串嵌套” - 可以在网络上搜索到这个
- **原始数据转储：** 大型代码块、日志文件、数据表 - 对于内存来说太大
- **特定于会话的蜉蝣：**临时文件路径，一次性调试上下文
- **上下文文件中已有信息：** SOUL.md 和 AGENTS.md 内容

## 容量管理

内存有严格的字符限制，以限制系统提示：

|商店 |限制|典型条目 |
|------|------|----------------|
|记忆 | 2,200 个字符 | 8-15 条目 |
|用户 | 1,375 个字符 | 5-10 个条目 |

### 内存已满时会发生什么

当您尝试添加超出限制的条目时，该工具会返回错误：

```json
{
  "success": false,
  "error": "Memory at 2,100/2,200 chars. Adding this entry (250 chars) would exceed the limit. Replace or remove existing entries first.",
  "current_entries": ["..."],
  "usage": "2,100/2,200"
}
```

然后代理人应该：
1. 读取当前条目（错误响应中显示）
2. 确定可以删除或合并的条目
3. 使用“replace”将相关条目合并为较短的版本
4. 然后“添加”新条目

**最佳实践：** 当内存超过 80% 容量时（在系统提示标题中可见），在添加新条目之前合并条目。例如，将三个单独的“项目使用 X”条目合并为一个综合项目描述条目。

### 良好记忆条目的实际例子

**紧凑、信息密集的条目效果最好：**

```
# Good: Packs multiple related facts
User runs macOS 14 Sonoma, uses Homebrew, has Docker Desktop and Podman. Shell: zsh with oh-my-zsh. Editor: VS Code with Vim keybindings.

# Good: Specific, actionable convention
Project ~/code/api uses Go 1.22, sqlc for DB queries, chi router. Run tests with 'make test'. CI via GitHub Actions.

# Good: Lesson learned with context
The staging server (10.0.1.50) needs SSH port 2222, not 22. Key is at ~/.ssh/staging_ed25519.

# Bad: Too vague
User has a project.

# Bad: Too verbose
On January 5th, 2026, the user asked me to look at their project which is
located at ~/code/api. I discovered it uses Go version 1.22 and...
```

## 防止重复

内存系统会自动拒绝完全相同的重复条目。如果您尝试添加已存在的内容，它将返回成功并显示“无重复添加”消息。

## 安全扫描

内存条目在被接受之前会被扫描以查找注入和渗漏模式，因为它们被注入到系统提示符中。与威胁模式（提示注入、凭据泄露、SSH 后门）匹配或包含不可见 Unicode 字符的内容将被阻止。

## 会话搜索

除了 MEMORY.md 和 USER.md 之外，代理还可以使用“session_search”工具搜索其过去的对话：

- 所有 CLI 和消息会话都存储在 SQLite (`~/.hermes/state.db`) 中，并具有 FTS5 全文搜索
- 搜索查询返回与 Gemini Flash 相关的过去对话摘要
- 代理可以找到几周前讨论过的事情，即使它们不在其活动内存中

```bash
hermes sessions list    # Browse past sessions
```

### session_search 与内存

|特色 |持久内存|会议搜索 |
|--------------------|--------------------------------|----------------|
| **容量** |总共约 1,300 个代币 |无限制（所有会话）|
| **速度** |即时（在系统提示符下）|需要搜索+LLM总结|
| **用例** |关键事实随时可用 |查找过去的特定对话 |
| **管理** |由代理手动策划|自动 — 存储所有会话 |
| **代币成本** |每个会话固定（约 1,300 个代币）|按需（需要时搜索）|

**记忆**用于存储应始终处于上下文中的关键事实。 **会话搜索**用于“我们上周讨论过 X 吗？”代理需要回忆过去对话中的细节的查询。

＃＃ 配置

```yaml
# In ~/.hermes/config.yaml
memory:
  memory_enabled: true
  user_profile_enabled: true
  memory_char_limit: 2200   # ~800 tokens
  user_char_limit: 1375     # ~500 tokens
```

## 外部内存提供商

为了获得超越 MEMORY.md 和 USER.md 的更深入、持久的内存，Hermes 附带了 8 个外部内存提供程序插件，包括 Honcho、OpenViking、Mem0、Hindsight、Holographic、RetainDB、ByteRover 和 Supermemory。

外部提供商与内置内存一起运行（从不替换它），并添加知识图、语义搜索、自动事实提取和跨会话用户建模等功能。

```bash
hermes memory setup      # pick a provider and configure it
hermes memory status     # check what's active
```

See the [Memory Providers](./memory-providers.md) guide for full details on each provider, setup instructions, and comparison.

## 摘录笔记

- 保留获取的降价/文本，用作 Hermes + Obsidian 个人知识库计划中的实施证据。
