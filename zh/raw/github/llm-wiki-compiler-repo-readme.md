---
source_url: https://github.com/atomicstrata/llm-wiki-compiler
fetched_url: https://raw.githubusercontent.com/atomicstrata/llm-wiki-compiler/main/README.md
source_type: github repo
author: atomicstrata/llm-wiki-compiler maintainers
source_date: 2026-04-05
ingested: 2026-05-15
sha256: fff8b19b5c5307111de79a9e27f435f55fb0bf1f1ea3b080f4f1f4d5db50f601
raw_preservation: full_github_readme_text
extraction_method: github_repo_api_and_raw_readme
github_repo: atomicstrata/llm-wiki-compiler
stars: 1179
open_issues: 4
---

#GitHub存储库：atomicstrata/大语言模型维基编译器

##源元数据

-来源网址：https://github.com/atomicstrata/llm-wiki-compiler
-获取的URL：https://raw.githubusercontent.com/atomicstrata/llm-wiki-compiler/main/README.md
-来源类型：github repo
-作者：atomicstrata/大语言模型-维基-编译器维护者
-来源日期：2026-04-05
-摄入日期：2026-05-15
-可靠性：中-高
-原始保存状态：full_github_readme_text
-提取方式：github_repo_api_and_raw_readme

##解析的源文本

#存储库元数据：atomicstrata/大语言模型维基编译器

-GitHub网址：https://github.com/atomicstrata/llm-wiki-compiler
-描述：知识编译器。原始资料进来，链接维基出去。灵感来自Karpathy的大语言模型维基模式。
-星星：1179
-叉子：123
-未决问题：4
-创建时间：2026-04-05T19：53：06Z
-更新日期：2026-05-14T16：22:43 Z
-许可证：麻省理工学院

##README.md

#llmwiki

将原始资源编译成一个相互链接的降价维基。

Inspired by Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern: instead of re-discovering knowledge at query time, compile it once into a persistent, browsable artifact that compounds over time.

Image: llmwiki demo (docs/images/demo.gif)

##这是给谁的

-**AI研究人员和工程师**从论文、文档和笔记中构建持久的知识
-**技术作者**将分散的来源汇编成结构化的、相互关联的参考资料
-**任何有太多书签的人**想要一个维基而不是一个标签的墓地

##快速入门

```bash
npm install -g llm-wiki-compiler
export ANTHROPIC_API_KEY=sk-...
# Or use ANTHROPIC_AUTH_TOKEN if your Anthropic-compatible gateway expects it.
# Or use a different provider:
# export LLMWIKI_PROVIDER=openai
# export OPENAI_API_KEY=sk-...

llmwiki ingest https://some-article.com
llmwiki compile
llmwiki query "what is X?"
```

##配置

llmwiki通过环境变量配置提供者。默认提供程序是Anthropic。

人为值的配置优先级：

1.shell env/本地`.env`
2.Claude代码设置回退(`~/.claude/settings.json`→`env`块)
3.内置提供者默认值（如适用）

-`LLMWIKI_PROVIDER`：要使用的提供者(例如，anthropic、openai)。
-`LLMWIKI_MODEL`：覆盖提供者默认值的模型名称。

###Anthropic（默认）

-`ANTHROPIC_API_KEY`或`ANTHROPIC_AUTH_TOKEN`：必需。任何一个都可以满足人择认证。
-`ANTHROPIC_BASE_URL`：可选。代理的自定义端点。接受有效的HTTP(S)URL，包括克劳德风格的路径端点，如“https://api.kimi.com/coding/”。

使用Anthropic或cc-switch自定义代理的示例：

```bash
export LLMWIKI_PROVIDER=anthropic
export ANTHROPIC_API_KEY=sk-...
export ANTHROPIC_BASE_URL=https://proxy.example.com
```

如果这些值没有在shell env或`.env`中设置，llmwiki将尝试从`~/.claude/settings.json`（`env`块）中为：

-`ANTHROPIC_API_KEY`
-`ANTHROPIC_AUTH_TOKEN`
-`ANTHROPIC_BASE_URL`
-`ANTHROPIC_MODEL`

零导出示例（已配置Claude代码）：

```bash
llmwiki compile
```

###兼容OpenAI的本地服务器

将OpenAI提供程序用于本地OpenAI兼容服务器，例如
“美洲驼服务器”。`OPENAI_BASE_URL`用于聊天/工具调用，以及
“OPENAI_EMBEDDINGS_BASE_URL”是可选的。仅当嵌入为
从不同端点提供服务；未设置时，嵌入使用相同的客户端
以及作为聊天的基本URL。在自定义URL中包含`/v1`。

拆分端点示例：

```bash
export LLMWIKI_PROVIDER=openai
export LLMWIKI_MODEL=qwen3.6-35b
export LLMWIKI_EMBEDDING_MODEL=text-embedding-model
export OPENAI_API_KEY=sk-local
export OPENAI_BASE_URL=http://host_url:port/v1
export OPENAI_EMBEDDINGS_BASE_URL=http://host_url:port/v1
```

CLI和OpenAI SDK仍然需要“OPENAI_API_KEY”。对于本地
对于不检查身份验证的服务器，任何虚拟值都足够了。

##不要

Ollama使用其OpenAI兼容端点。设置“OLLAMA_HOST”进行聊天和
可选地，仅当嵌入从
不同的端点。未设置时，嵌入使用`OLLAMA_HOST`。将`/v1`包括在
自定义URL。

```bash
export LLMWIKI_PROVIDER=ollama
export LLMWIKI_MODEL=llama3.1
export LLMWIKI_EMBEDDING_MODEL=nomic-embed-text
export OLLAMA_HOST=http://ollama_host:11434/v1
export OLLAMA_EMBEDDINGS_HOST=http://ollama_host:11435/v1
```

###GitHub副驾驶

使用GitHub Copilot API(`https://api.githubcopilot.com`)，
Copilot订阅者可使用OpenAI兼容端点。需要一个GitHub
具有“副驾驶”作用域的OAuth令牌-**不支持经典Pat**。

首先，确保您的“gh”CLI令牌具有所需的范围：

```bash
gh auth refresh --scopes copilot
```

然后运行：

```bash
export LLMWIKI_PROVIDER=copilot
export GITHUB_TOKEN=$(gh auth token)  # OAuth token required; PATs will not work
export LLMWIKI_MODEL=gpt-4o           # optional; gpt-4o is the default
```

可用型号（名称使用点，而不是破折号）：`gpt-4o`、`gpt-4o-mini`、
`claude-sonnet-4.5`、`claude-sonnet-4.6`、`claude-opus-4.5`、`gemini-2.5-pro`、
和其他-可用性取决于您的副驾驶计划。

**嵌入：**GitHub Copilot API不公开嵌入端点。
语义搜索（由带有分块检索的“llmwiki查询”使用）将回落
没有嵌入的全索引选择。对于依赖于嵌入的工作流，
切换到“openai”提供程序并提供“OPENAI_API_KEY”。

###请求超时

OpenAI SDK默认为每个请求10分钟的超时，这可以在较慢的本地模型上切断长时间的编译完成。每个提供程序的覆盖：

-`LLMWIKI_REQUEST_TIMEOUT_MS`-与提供程序无关的超时，单位为毫秒。适用于“openai”和“ollama”后端。
-`OLLAMA_TIMEOUT_MS`-特定于OLLAMA的覆盖。当两者都设置时，将战胜“LLMWIKI_REQUEST_TIMEOUT_MS”。

默认值：“openai”10分钟，“ollama”30分钟（本地模型通常需要更多）。

###输出语言

生成的wiki内容默认为模型从源材料生成的任何语言——通常是英语。使用以下任一项覆盖：

-`LLMWIKI_OUTPUT_LANG`-例如`zh-CN`、`Chinese`、`ja`、`Japanese`。应用于编译和查询管道发出的每个提示。
-`--lang<code>`on`llmwiki compile`和`llmwiki query`-效果相同，作用域为一次调用。战胜环境变量。

Unset逐个字节地保留先前的行为。

###每个概念的即时预算

当许多源对同一个编译的概念做出贡献时，“compile”会对发送到大语言模型的组合源内容实施每个概念的字符上限，这样流行的共享概念就不会超出模型的上下文窗口。当截断生效时，每个贡献源都会得到公平的份额。

-`LLMWIKI_PROMPT_BUDGET_CHARS`-组合的每个概念提示的字符上限。默认为“200000”（约50k个令牌），适合具有净空的现代上下文窗口。对于较大的上下文模型，提高它，对于局部小上下文模型，降低它。

当cap触发时，截断警告会打印到stderr，这样您就知道哪个概念达到了预算。

##为什么不只是抹布？

RAG在查询时检索块。每个问题都从头开始重新发现相同的关系。什么都不会积累。

llmwiki**将你的资源编译成一个维基。概念有自己的页面。页面相互链接。当您用`--save'提问时，答案会变成一个新页面，未来的查询会将其用作上下文。你的探索化合物。

这是对RAG的补充，而不是替代。RAG非常适合大型语料库的特别检索。llmwiki为您提供了一个持久的、结构化的工件来检索。

```
RAG:     query → search chunks → answer → forget
llmwiki: sources → compile → wiki → query → save → richer wiki → better answers
```

##工作原理

```
sources/  →  SHA-256 hash check  →  LLM concept extraction  →  wiki page generation  →  [[wikilink]] resolution  →  index.md
```

**两阶段管道。**阶段1从所有来源提取所有概念。阶段2生成页面。这消除了顺序依赖性，在编写任何内容之前捕获失败，并将跨多个源共享的概念合并到单个页面中。

**增量。**只有经过更改的源才会通过大语言模型。其他一切都通过基于哈希的变化检测被跳过。

**复合查询。**`llmwiki query-save`将答案写入wiki页面并立即重建索引。保存的答案会在将来的查询中显示为上下文。

###它生产什么

像维基百科关于知识汇编的文章这样的原始来源变成了结构化的维基页面：

```yaml
---
title: Knowledge Compilation
summary: Techniques for converting knowledge representations into forms that support efficient reasoning.
kind: concept
sources:
  - knowledge-compilation.md
createdAt: "2026-04-05T12:00:00Z"
updatedAt: "2026-04-05T12:00:00Z"
---
```

```markdown
Knowledge compilation refers to a family of techniques for pre-processing
a knowledge base into a target language that supports efficient queries.

Related concepts: [[Propositional Logic]], [[Model Counting]]
```

页面在frontmatter中包含源属性。段落用“^【filename.md】”标记进行注释，指向贡献内容的源文件；特定权利要求可以使用诸如`^[filename.md：42-58]`或`^[filename.md#L42-L58]`的行范围。

##命令

|命令|它的作用|
|---------|-------------|
|`llmwiki摄取<url\|file>`|获取URL或将本地文件复制到`sources/`|
|`llmwiki ingest-session<path>`|将Claude/Codex/Cursor会话导出（单个文件或整个目录）导入到`sources/`|
|`llmwiki编译`|增量编译：提取概念，生成wiki页面|
|`llmwiki compile--review`|将候选页面写入`.llmwiki/candidates/`而不是`wiki/`，以便您可以在它们登陆之前进行审阅|
|`llmwiki compile-lang<code>`|以给定语言（例如`中文`、`ja`、`zh-CN`）生成wiki内容；也适用于“查询”|
|“llmwiki评论列表”|列出待定候选页面|
|`llmwiki评论显示<id>`|打印候选人的标题、摘要和正文|
|`llmwiki审查批准<id>`|将候选人提升到`wiki/`并刷新索引/MOC/embeddings|
|`llmwiki审查拒绝<id>`|在不接触`wiki/`的情况下存档候选人|
|`llmwiki schema init`|写一个starter`.llmwiki/schema.json`文件|
|`llmwiki架构显示`|打印当前项目的已解析架构|
|`llmwiki查询“问题”`|针对您编译的wiki提出问题|
|`llmwiki查询“问题”--保存`|回答并将结果保存为wiki页面|
|`llmwiki导出[--target<name>]`|将wiki导出为可移植格式-`llms.txt`、`大语言模型-full.txt`、JSON、JSON-LD、GraphML、Marp幻灯片|
|`llmwiki lint`|检查wiki质量（断开的链接、孤儿、空白页、低置信度、矛盾等）|
|“llmwiki watch”|当“sources/”更改时自动重新编译|
|`llmwiki serve[--root<dir>]`|启动向AI代理公开wiki工具的MCP服务器|

##输出

```
wiki/
  concepts/         one .md file per concept, with YAML frontmatter
  queries/          saved query answers, included in index and retrieval
  index.md          auto-generated table of contents
.llmwiki/
  schema.json       optional page-kind and cross-link policy
  candidates/       pending review candidates from `compile --review`
  candidates/archive/  rejected candidates kept for audit
```

黑曜石兼容。`[[wikilinks]]`解析为概念标题。

##审核队列

默认情况下，“compile”将页面直接写入“wiki/”。添加`-review`以将候选JSON记录写入`。llmwiki/candidates/`，这样您就可以在每个生成的页面登陆之前检查它。

```bash
llmwiki compile --review     # produces candidates, leaves wiki/ untouched
llmwiki review list          # see what's pending
llmwiki review show <id>     # inspect a single candidate
llmwiki review approve <id>  # write into wiki/ + refresh index/MOC/embeddings
llmwiki review reject <id>   # archive to .llmwiki/candidates/archive/
```

需要了解的几件事：

-**批准和拒绝获取`.llmwiki/lock`**，以便它们彼此之间以及任何并发`compile`干净地序列化。
-**源状态按每个源延迟。**当一个源产生多个候选时，在最后一个候选被批准之前，该源不会被标记为已编译——因此未解析的同级在下一次“编译——审查”时仍可重新检测。
-**删除簿记被推迟。**`编译——审查`不会孤立标记已删除的源；下一个非审查“编译”会这样做。“-review”帮助文本对此进行了宣传。
-MCP`wiki_status`公开`pendingCandidates`以便代理可以看到队列深度。

##页面元数据

编译后的页面可以在frontmatter中携带认知元数据，这样消费者就知道每个页面的可信度。所有字段都是可选的，没有它们的现有页面将继续工作。

```yaml
---
title: Knowledge Compilation
summary: Techniques for converting knowledge representations...
sources:
  - knowledge-compilation.md
confidence: 0.82           # 0–1, LLM-reported confidence in the synthesized page
provenanceState: merged    # extracted | merged | inferred | ambiguous
contradictedBy:
  - slug: probabilistic-reasoning
---
```

当多个源合并到一个slug中时，元数据会被协调：“min”置信度、“provenanceState=“merged”、“contradictedBy”的联合（由slug进行重复数据删除）。

“llmwiki lint”添加了三个显示此元数据的规则：

-“低置信度”-标记“置信度”低于阈值的页面
-`矛盾的页面`-标记具有非空`矛盾的页面
-`excess-inferred-paragraphs`-标记正文有太多未加注释的散文段落的页面（直接从呈现的文本中计算——正文是真实的唯一来源，不涉及frontmatter字段）

##索赔级别出处

段落引用继续使用原始来源标记形式：

```markdown
This paragraph is grounded in the source. ^[source.md]
```

对于需要更严格验证的声明，pages可以将语句固定到所摄取源中的行范围：

```markdown
The system uses a two-phase compile pipeline. ^[architecture-notes.md:42-58]
The same range can also use GitHub-style anchors. ^[architecture-notes.md#L42-L58]
```

“llmwiki lint”验证这两种表单。它报告丢失的源文件、格式错误的声明引用、不可能的范围，如行“0”或“8-3”，以及超出源文件末尾的范围。

##架构层

项目可以选择定义“。llmwiki/schema.json”来塑造维基，超越平面概念页面。现有项目不需要模式文件；缺失或无效的“种类”值会退回到“概念”。

```bash
llmwiki schema init
llmwiki schema show
```

架构支持四种页面类型：

-“概念”-独立的想法或模式
-“实体”-特定人员、产品、组织或命名工件
-“比较”-跨概念或实体的并排分析
-“概述”-连接域中多个概念的映射页面

模式规则可以设置每种类型的“minWikilinks”和可选的“seedPages”。编译可以实现种子页面，如概述，lint强制执行特定于页面类型的交叉链接最小值，并在批准之前审查候选表面模式违规。

##演示

在任何文章或文档上尝试：

```bash
mkdir my-wiki && cd my-wiki
llmwiki ingest https://en.wikipedia.org/wiki/Andrej_Karpathy
llmwiki compile
llmwiki query "What terms did Andrej coin?"
```

有关预生成的输出，请参见repo中的“examples/basic/”，您可以在没有API密钥的情况下浏览。

##MCP服务器

llmwiki附带了一个MCP（模型上下文协议）服务器，因此AI代理（Claude Desktop、Cursor、Claude Code等。）可以直接驱动整个管道：摄取源代码、编译、查询、搜索、lint和读取页面——而无需抓取CLI输出。

Where [llm-wiki-kit](https://github.com/iamsashank09/llm-wiki-kit) gives agents raw CRUD against wiki pages, llmwiki exposes the **automated pipelines**: agents get intelligent compilation, incremental change detection, and semantic query routing built in.

###设置

启动服务器（stdio传输，启动时不需要API密钥）：

```bash
llmwiki serve --root /path/to/your/wiki-project
```

###Claude桌面/游标配置

添加到客户端的MCP配置（例如`claude_desktop_config.json`）：

```json
{
  "mcpServers": {
    "llmwiki": {
      "command": "npx",
      "args": ["llm-wiki-compiler", "serve", "--root", "/path/to/wiki-project"],
      "env": {
        "ANTHROPIC_API_KEY": "sk-ant-..."
      }
    }
  }
}
```

需要大语言模型的工具（`compile_wiki`、`query_wiki`、`search_pages`）会在每次调用时检查已配置的提供程序。只读工具（`read_page`、`lint_wiki`、`wiki_status`）和`ingest_source'无需任何凭据即可工作。

##

|工具|它的作用|
|------|--------------|
|`ingest_source`|将URL或本地文件提取到`sources/`中。|
|`compile_wiki`|运行增量编译管道；返回计数、片段、错误。|
|`query_wiki`|带有可选`--save`的两步接地答案。|
|`search_pages`|返回与问题相关的页面的全部内容。|
|`read_page`|按slug（概念/然后查询/）读取单个页面。|
|`lint_wiki`|运行质量检查；返回结构化诊断。|
|`wiki_status`|页面计数、源计数、孤立项、挂起更改（只读）。|

###资源

URI返回
|-----|---------|
|`llmwiki：//index`|完整的`wiki/index.md`内容。|
|`llmwiki：//concept/{slug}`|单个概念页面（frontmatter+body）。|
|`llmwiki：//query/{slug}`|单个保存的查询页面。|
|`llmwiki：//sources`|包含元数据的摄取源文件列表。|
|`llmwiki：//state`|编译状态（每个源哈希，上次编译时间）。|

##限制

早期软件。最适合小型、高信号语料库（几十个来源）。查询路由是基于索引的。

**关于截断的诚实。**超过字符限制的源在摄取时会被截断，并记录在frontmatter中的原始字符数，因此下游消费者知道他们正在处理部分内容。

##Karpathy的大语言模型维基模式与此编译器

Karpathy描述了一种将原始数据转化为编译知识的抽象模式。以下是llmwiki如何映射到它：

|Karpathy的概念|llmwiki|状态|
|---|---|---|
|数据摄取|“llmwiki摄取”|已实现|
|编译wiki|“llmwiki compile”|已实现|
|问答|“llmwiki查询”|已实现|
|输出归档（保存答案）|`llmwiki查询--保存`|已实现|
|自动重新编译|“llmwiki watch”|已实现|
|Linting/健康检查通过|“llmwiki lint”|已实现|
|代理集成|“llmwiki serve”（MCP服务器）|已实现|
|映像支持|“llmwiki摄取<image>”|已实现|
|Marp幻灯片|“llmwiki导出——目标Marp”|已实现|
|微调|-|尚未实施|

##路线图

在0.6.0中发布：

-✅导出包（`llms.txt`、JSON、JSON-LD、GraphML、Marp幻灯片）
-✅会话历史适配器-用于Claude、Codex和Cursor导出的“llmwiki摄取-会话”
-✅可配置输出语言-`--lang<code>`和`LLMWIKI_OUTPUT_LANG`
-✅防御性的每个概念提示预算，因此流行的共享概念不会崩溃编译

在0.5.0中发布：

-✅多模式摄取（图像、PDF、抄本）
-✅具有重新排序和`--debug`输出的分块检索
-⚠️最小节点版本提高到24（以前是18）

在0.4.0中发布：

-✅具有来源范围的声明级出处
-✅具有类型化页面类型（“概念”、“实体”、“比较”、“概述”）的一级模式层

在0.3.0中发布：

-✅候选审核队列（在编写页面之前批准编译输出）
-✅编译页面上的置信度和矛盾元数据

在0.2.0中发布：

-✅更好的出处（段落级来源归属）
-✅wiki质量检查的林挺通行证
-✅多提供商支持（OpenAI、Ollama、MiniMax）
-✅大型语料库查询策略（语义搜索、嵌入）
-✅更深入的黑曜石集成（标签、别名、内容地图）
-✅用于代理集成的MCP服务器

下一个：

-**只读本地web UI**-在没有黑曜石的情况下浏览“wiki/”：侧边栏、降价渲染、维基链接、搜索和出处/引用面板。
-**图形/上下文层**-页面邻域工具、图形路径、间隙检测和代理的令牌预算上下文包。
-**评估工具**-针对严重检索基线的基准答案质量、引用准确性、更新漂移、检索召回率和规模曲线。
-**任务和决策分类账**-将会话摄取转化为持久的代理内存：目标、决策、开放问题、结果和下一个代理切换。
-**回滚、审核和源生命周期**-撤消/反向摄取、编译差异报告、陈旧声明检查、新鲜度报告和持久操作日志。
-**域模板**-用于研究、代码库文档、团队手册、决策日志和标准/法规的模式/提示包。

稍后/公开讨论：

-重复源刷新作业-按计划重新摄取URL，与之前的快照进行比较，仅重新编译已更改的内容
-MCP提示资源-策划代理提示，如“审查维基”、“提出新来源”和“起草比较页面”
-用于Slack/Discord/Teams式机构记忆的团队聊天连接器

如果你喜欢雄心勃勃的问题：**本地web UI**、**图形/上下文包**和**评估工具**是下一个最丰富的贡献。打开一个问题来申请一个或开始一个设计讨论。

明确没有计划（好主意，只是不适合这个回购）：完整的静态站点生成器，桌面或移动应用程序，微调，正式的本体引擎，重型图形数据库基础设施。

##要求

Node.js>=24，加上提供者凭证（对于Anthropic：`ANTHROPIC_API_KEY`或`ANTHROPIC_AUTH_TOKEN`）。

##许可证

MIT


##免责声明

没有大语言模型在回购过程中受到伤害。
