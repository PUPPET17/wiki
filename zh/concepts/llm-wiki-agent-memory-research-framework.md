---
title: LLM Wiki / Agent Memory Research Framework
created: 2026-05-14
updated: 2026-05-15
type: concept
tags: [llm-wiki, agent-memory, rag, context-engineering, knowledge-integration, personal-ai-os, memory-architecture, retrieval, compression, indexing, tradeoff, failure-case, opportunity]
sources: [raw/articles/karpathy-llm-wiki-gist-2026.md, raw/papers/memgpt-2023.md, raw/papers/generative-agents-2023.md, raw/papers/coala-2023.md, raw/papers/rag-survey-2023.md, raw/articles/anthropic-effective-agents-2024.md, raw/articles/anthropic-multi-agent-research-2025.md, raw/articles/langchain-context-engineering-2025.md, raw/articles/harrison-chase-sequoia-context-engineering-2025.md, raw/articles/simon-willison-embeddings-2023.md, raw/articles/microsoft-vector-search-not-enough-2024.md, raw/community/hn-karpathy-style-wiki-2026.md, raw/community/hn-memgpt-2023.md, raw/community/hn-letta-code-2025.md, raw/product-docs/openai-chatgpt-memory-2024-2025.md, raw/product-docs/letta-memory-2026.md, raw/papers/raptor-2024.md, raw/papers/self-rag-2023.md, raw/papers/memorag-2024.md, raw/community/reddit-memory-systems-2026.md, raw/github/mem0-issue-4573-memory-audit-junk.md, raw/github/letta-issue-652-per-conversation-context-scoping.md, raw/github/mem0-repo-readme.md, raw/github/letta-code-repo-readme.md, raw/github/wuphf-repo-readme.md, raw/github/llm-wiki-compiler-repo-readme.md, raw/github/langchain-context-engineering-repo-readme.md, raw/github/langchain-how-to-fix-your-context-readme.md]
confidence: medium
contested: true
---

＃ 执行摘要

本文档是针对不断发展的 LLM Wiki / 代理内存 / 上下文压缩 / 知识集成框架的第一个稳定的研究综合。

核心发现：Karpathy 的 LLM Wiki 模式最好理解为原始源和瞬态模型上下文之间的持久、可编辑、由代理维护的中间表示。它不仅仅是具有降价输出的 RAG。它的主要区别在于编译：声明、实体、冲突、摘要和交叉链接一次增量集成，然后重用和修改。资料来源：Andrej Karpathy 自己的要点和 X 线程，2026 年，类型：要点/推文，声明状态：有关其提案的事实；可行性仍处于部分推测阶段。 [原始/文章/karpathy-llm-wiki-gist-2026.md]

当今最实用的架构是本地优先的 markdown+git 作为事实来源，加上明确的来源出处、BM25/全文搜索、元数据、可选嵌入和定期 lint/reflection。这得到了 Karpathy 的提案、WUPHF 的 HN 描述的实现、Letta 的 MemFS 文档、Simon Willison 的小规模嵌入实践以及 Microsoft 的混合搜索论点的支持。声明状态：工程推论，而非普遍证明。 [raw/articles/karpathy-llm-wiki-gist-2026.md] [raw/community/hn-karpathy-style-wiki-2026.md] [raw/product-docs/letta-memory-2026.md] [raw/articles/simon-willison-embeddings-2023.md] [raw/articles/microsoft-vector-search-not-enough-2024.md]

最强大的技术镜头是上下文工程：在窗口外编写上下文、选择相关上下文、压缩大量上下文以及跨代理/文件/子上下文隔离工作。这完全映射到 LLM Wiki 操作：摄取/写入、查询/选择、汇总/压缩、子代理/层/隔离。资料来源：LangChain 2025 上下文工程博客和 Harrison Chase 采访。索赔状态：社区/工程框架。 [原始/文章/langchain-context-engineering-2025.md] [原始/文章/harrison-chase-sequoia-context-engineering-2025.md]

主要瓶颈不是存储。它是记忆质量：保存什么，何时检索，如何表示矛盾，以及如何防止陈旧或幻觉的摘要硬化为公认的知识。 OpenAI 的 ChatGPT 内存控制和围绕 Letta 的 HN 讨论表明用户需要透明度、删除性和可审计性。声明状态：交叉验证的产品/社区关注。 [raw/product-docs/openai-chatgpt-memory-2024-2025.md] [raw/community/hn-letta-code-2025.md]

目前 Reddit 证据不足。搜索结果找到了相关的 LocalLLaMA 线程，但直接提取被阻止。它们在 Source Map 中被列为低可靠性，并且在通过可靠的 API/存档/手动审查检索之前不得锚定核心结论。 [原始/社区/reddit-memory-systems-2026.md]

# 核心论文

有用的代理内存系统不应该是一袋检索到的块。它应该是一个可编辑的知识基础，具有四个属性：

1. 耐用：在会话、模型更改和应用程序运行时中仍然存在。
2. 可检查：人类和代理可以阅读、比较、引用和编辑它。
3. 集成：新证据更新现有页面/事实，而不是创建重复的片段。
4. 操作：它具有摄取、检索、编辑、摘要、linting、衰减和冲突解决工作流程。

Karpathy 的关键举措是用累积编译取代重复的查询时重新推导。 RAG 回答：现在哪些块是相关的？ LLM Wiki 问：长期存在的知识库现在应该相信什么，应该如何改变？资料来源：卡帕蒂要点。声明状态：基于主要来源的解释。 [原始/文章/karpathy-llm-wiki-gist-2026.md]

# 关键概念

- 原始来源：不可变的源文档。事实：Karpathy 明确将原始来源与 LLM 维护的 wiki 分开。 [原始/文章/karpathy-llm-wiki-gist-2026.md]
- Wiki 层：LLM 生成的实体、概念、摘要、比较、矛盾和查询的降价页面。关于提案的事实。 [原始/文章/karpathy-llm-wiki-gist-2026.md]
- Schema：代理维护者的操作手册。有关提案的事实；实际必要性推断。 [原始/文章/karpathy-llm-wiki-gist-2026.md]
- 内存层：活动上下文、固定内存、可搜索内存、原始存档。 MemGPT/Letta 类系统中的事实； LLM Wiki 的架构推断。 [raw/papers/memgpt-2023.md] [raw/product-docs/letta-memory-2026.md]
- 上下文工程：决定为模型步骤编写、选择、压缩或隔离什么内容。资料来源：浪链博客 / Harrison Chase 采访。 [原始/文章/langchain-context-engineering-2025.md] [原始/文章/harrison-chase-sequoia-context-engineering-2025.md]
- 反思/整合：从经验流中生成更高级别的摘要或内存编辑。生成代理中的纸质支持； Letta 睡眠时间反射文档中的产品支持。 [raw/papers/generative-agents-2023.md] [raw/product-docs/letta-memory-2026.md]
- 混合检索：矢量+全文+合并+重新排序。由微软博客提供工程支持；尚未证明具有普遍性。 [raw/articles/microsoft-vector-search-not-enough-2024.md]

# Karpathy要点分析

Karpathy 的要点定义了三个层次：原始来源、wiki 和模式。它定义了三种操作：摄取、查询、lint。它还强调index.md和log.md作为导航和时间顺序。这些是主要来源的事实。 [原始/文章/karpathy-llm-wiki-gist-2026.md]

最重要的见解：问题结果本身可以成为持久的页面。这将探索转化为持久的知识，而 RAG 聊天机器人和文件上传产品往往缺少这种知识。有关提案的事实；实用价值是一种工程假设。 [原始/文章/karpathy-llm-wiki-gist-2026.md]

其要点是故意抽象的。它没有指定评估方法、源质量评分、出处模式、并发模型、访问控制、冲突解决算法或超出粗略指导的扩展阈值。这些是差距，而不是批评。主张状态：直读/推理。 [原始/文章/karpathy-llm-wiki-gist-2026.md]

该要点的中等规模主张，即索引优先导航在大约 100 个源/数百页左右工作，应该被视为轶事。 WUPHF 的 HN 项目声称使用 BM25 对 500 个工件实现了 85% 的召回率@20，这令人鼓舞，但仍然是针对特定项目的，而不是通用基准。 [原始/文章/karpathy-llm-wiki-gist-2026.md] [原始/社区/hn-karpathy-style-wiki-2026.md]

# 架构模式

## 模式A：Markdown+Git 规范内存

使用 Markdown 文件作为规范的人类/代理可读内存；使用 git 进行差异、出处、回滚、分支和审查。这是 Karpathy 的隐式堆栈、WUPHF 的显式堆栈和 Letta MemFS 的记录堆栈。声明状态：作为新兴工程模式进行验证，未正式进行基准测试。 [raw/articles/karpathy-llm-wiki-gist-2026.md] [raw/community/hn-karpathy-style-wiki-2026.md] [raw/product-docs/letta-memory-2026.md]

权衡：出色的可检查性和便携性；除非建立索引，否则对于大容量低延迟检索较弱。

## 模式 B：仅附加事实 + 合成页面

将原子事实/事件存储为仅附加 JSONL 或记录，然后重建人类可读的实体简介/摘要。 WUPHF 声明每个实体的 JSONL 事实和综合工作人员。生成代理存储经验流并合成反射。 [raw/community/hn-karpathy-style-wiki-2026.md] [raw/papers/generative-agents-2023.md]

权衡：更好的来源和再生；比编辑页面更复杂。

## 模式 C：分层摘要

使用页面摘要、主题图和递归抽象。 RAPTOR 提供的论文证据表明，在某些任务中，树状组织摘要可以比仅块检索改进检索。 wiki 是这种层次结构的人类可编辑变体。 [raw/papers/raptor-2024.md]

权衡：摘要会丢失细节并且可能产生幻觉；必须保留原始证据的链接。

## 模式 D：虚拟上下文/内存分页

受操作系统虚拟内存的启发，MemGPT 将长期交互定义为在内存层之间移动信息。 Letta 操作内存块和 MemFS。 [raw/papers/memgpt-2023.md] [raw/product-docs/letta-memory-2026.md]

权衡：强大的抽象；当操作系统隐喻夸大其词时，社区会予以反击。 [原始/社区/hn-memgpt-2023.md]

## 模式 E：混合搜索和重新排名

使用 BM25/全文获取确切的名称、ID、字符串、数字；用于语义回忆的嵌入；重新排名前 k 质量。微软认为仅靠矢量搜索无法实现精确匹配查询。 Simon Willison 表明，嵌入在小规模下很便宜/有用，但不透明且依赖于模型。 [原始/文章/microsoft-vector-search-not-enough-2024.md] [原始/文章/simon-willison-embeddings-2023.md]

权衡：比普通降价有更多的活动部件；更好的检索稳健性。

# 现有项目

- Karpathy LLM Wiki 想法文件：主要概念种子；没有固定的实现。 [原始/文章/karpathy-llm-wiki-gist-2026.md]
- MemGPT / Letta：受操作系统启发的虚拟上下文和内存优先代理。 [raw/papers/memgpt-2023.md] [raw/product-docs/letta-memory-2026.md]
- Letta Code / MemFS：长寿命编码代理，具有跨模型的便携式内存； `/init`、`/remember`、`/clear` 和技能学习。该存储库将与 Claude Code/Codex/Gemini CLI 的区别定义为基于代理的持久性与独立会话。 [raw/product-docs/letta-memory-2026.md] [raw/github/letta-code-repo-readme.md]
- LettaBot 上下文范围问题：具体的设计讨论表明，当在对话中相同地重用时，代理级内存块和 MemFS 文件会成为隐私、注意力和令牌成本问题。建议的解决方案：对话级上下文包含/排除或每个文件的 frontmatter 范围。 [raw/github/letta-issue-652-per-conversation-context-scoping.md]
- WUPHF：独立检查的存储库自述文件确认了本地/自托管的“协作办公室”，其中包含每个代理笔记本+共享工作区 wiki、git 原生 Markdown 内存、新会话、每个代理作用域工具以及声称的平面令牌/缓存经济学。 [raw/community/hn-karpathy-style-wiki-2026.md] [raw/github/wuphf-repo-readme.md]
- llm-wiki-compiler：使用“ingest”、“compile”、“query”、“query --save”、“lint”、“watch”、“serve” MCP、审查队列、声明级出处标记、页面元数据和行范围引用直接实现 Karpathy 模式。它明确指出了局限性：早期的软件最适合小型高信号语料库、基于索引的路由和诚实的截断元数据。 [raw/github/llm-wiki-compiler-repo-readme.md]
- Mem0：通用存储层项目，具有面向生产的主张：单遍 ADD-only 提取、实体链接、多信号检索、时间推理和开放评估框架。然而，下面的 GitHub 问题审核为内存质量提供了一个严峻的反例。 [raw/github/mem0-repo-readme.md] [raw/github/mem0-issue-4573-memory-audit-junk.md]
- LangChain 上下文工程存储库：可运行的笔记本实现写入/选择/压缩/隔离，以及 RAG、工具加载、上下文隔离、上下文修剪、上下文摘要和上下文卸载的“如何修复上下文”示例。 [raw/github/langchain-context-engineering-repo-readme.md] [raw/github/langchain-how-to-fix-your-context-readme.md]
- LangMem：SDK 框架语义、情景、程序内存和命名空间。 [raw/articles/langchain-context-engineering-2025.md]
- OpenAI ChatGPT Memory：产品化保存的记忆和带有控件的聊天历史个性化。 [原始/产品文档/openai-chatgpt-memory-2024-2025.md]

# 社区共识

有证据支持的共识：

1. 记忆必须透明且可编辑。 HN Letta 线程将白盒内存与 ChatGPT 风格的黑盒内存进行了对比，后者可以积累不良事实。 OpenAI 自己的文档强调控制。 [原始/社区/hn-letta-code-2025.md] [原始/产品文档/openai-chatgpt-memory-2024-2025.md]

2. 对于可靠的知识系统来说，仅使用Vector DB是不够的。微软给出了具体的精确匹配失败示例； WUPHF 报告 BM25 首次表现； Simon Willison 认为嵌入很有用，但并不神奇。 [raw/articles/microsoft-vector-search-not-enough-2024.md] [raw/community/hn-karpathy-style-wiki-2026.md] [raw/articles/simon-willison-embeddings-2023.md]

3. 代理系统应该从简单开始。 Anthropic 明确建议简单的可组合模式，并仅在结果改善时增加复杂性。 [raw/articles/anthropic- effective-agents-2024.md]

4. 长视野智能体需要痕迹/上下文可观察性。哈里森·蔡斯认为，痕迹揭示了进入每个步骤的背景。 [raw/articles/harrison-chase-sequoia-context-engineering-2025.md]

5. 对于某些生产设置，不加选择的内存存储比没有内存更糟糕。 mem0 生产审计报告了 32 天内的 10,134 个条目，审计后只有 224 个幸存者，并认为瓶颈在于提取/存储策略，而不仅仅是模型能力。将其视为单用户生产案例研究，而不是通用统计数据。 [raw/github/mem0-issue-4573-memory-audit-junk.md]

6. 对于多对话代理来说，上下文范围不是可选的。 LettaBot 问题 #652 描述了当代理级内存被相同地固定到不相关的对话中时，隐私泄露、注意力污染和令牌浪费。 [raw/github/letta-issue-652-per-conversation-context-scoping.md]

Reddit 共识：未知。存在相关线索，但证据不足，因为提取失败。 [原始/社区/reddit-memory-systems-2026.md]

# 主要辩论

## 辩论 1：Wiki 与 RAG

立场 A：Wiki 击败 RAG 因为知识复合和矛盾是预先整合的。资料来源：卡帕蒂要点。 [原始/文章/karpathy-llm-wiki-gist-2026.md]

立场 B：RAG 仍然是必要的，因为验证和长尾细节仍然需要原始证据检索。来源：RAG 调查、微软混合搜索。 [raw/papers/rag-survey-2023.md] [raw/articles/microsoft-vector-search-not-enough-2024.md]

综合：LLM Wiki 不应取代 RAG；它应该位于其上方。 wiki 是编译层，而 RAG/search 则检索原始证据和页面详细信息。

## 辩论 2：图存储器 vs 向量存储器 vs 符号存储器

图形存储器：显式实体/边支持检查、冲突解决和用户控制。但图提取很脆弱且模式繁重。

向量记忆：廉价的语义回忆和模糊匹配。但嵌入是不透明的，对于精确字符串来说很弱，并且依赖于模型。 [原始/文章/simon-willison-embeddings-2023.md] [原始/文章/microsoft-vector-search-not-enough-2024.md]

符号/降价内存：最可检查和可编辑。但检索和一致性需要纪律和工具。

合成：开始符号+BM25；添加向量和图形索引作为派生索引，而不是事实来源。

## 辩论3：个人AI操作系统

MemGPT 的操作系统隐喻在技术上对于内存层、中断、读/写操作非常有用。但 HN 的批评表明，如果按字面解释，这句话会引起炒作。 [raw/papers/memgpt-2023.md] [raw/community/hn-memgpt-2023.md]

综合：将 MVP 称为个人知识基础或内存文件系统。保留个人人工智能操作系统，以便以后在跨工作流程协调应用程序、权限、身份、工具和内存时使用。

# 失败案例

1. 上下文中毒：幻觉或不正确的内容进入记忆并随后被信任。资料来源：LangChain 上下文故障分类。 [raw/articles/langchain-context-engineering-2025.md]

2. 内存垃圾堆积：HN Letta 线程中社区关注 ChatGPT 内存被无用或不正确的语句填充。 [原始/社区/hn-letta-code-2025.md]

3. 大规模生产内存垃圾：mem0 问题 #4573 报告了为期 32 天的生产审核，其中 10,134 个条目中的 97.8% 被判定为垃圾，包括启动文件重述、心跳/cron 噪音、系统架构转储、瞬态任务状态、幻觉用户配置文件、身份混淆和敏感操作泄漏。可靠性：中等，因为它是单个 GitHub 问题/案例研究，但它很详细，并且包含建议缓解措施的评论。 [raw/github/mem0-issue-4573-memory-audit-junk.md]

4. 反馈循环放大：同一个 mem0 审计报告了一个幻觉的“用户更喜欢 Vim”内存在出现在召回上下文中后被反复重新提取，产生了数百个副本。这是当召回的记忆没有与新的用户输入分开标记时，记忆中毒变得自我强化的具体例子。 [raw/github/mem0-issue-4573-memory-audit-junk.md]

5.更好的提取模型不会自动修复内存质量：mem0审计报告从2B本地模型切换到Claude Sonnet减少了一些幻觉，但导致系统架构和操作细节的忠实过度提取，因为提示/管道仍然是宽松的。工程意义：存储策略和质量门与模型质量一样重要。 [raw/github/mem0-issue-4573-memory-audit-junk.md]

6. 仅矢量检索会错过准确的事实：矢量搜索未能检索准确价格“$45.00”的 Microsoft 示例。 [raw/articles/microsoft-vector-search-not-enough-2024.md]

7. 总结偏差：重复总结可以消除细微差别或来源警告。通过对原始来源的需求间接支持；具体基准未知。现状：可能存在工程风险，直接证据不足。

8. 过度代理的复杂性：人类警告代理会增加成本、延迟、复杂性和复合错误。 [raw/articles/anthropic- effective-agents-2024.md]

9. AI-slop 知识库：HN 关于 AI 生成的 Show HN 帖子的讨论表明，当生成的合成缺乏结构、校对或明确的作者身份时，社区持怀疑态度。 [raw/community/hn-karpathy-style-wiki-2026.md]

# 工程限制

- 延迟：多步摄取、反射和 linting 比普通索引慢。
- 代币成本：人择报告代理使用约 4 倍的聊天代币，多代理系统使用约 15 倍的聊天代币。 [原始/文章/anthropic-multi-agent-research-2025.md]
- 检索质量：需要混合搜索和重新排序才能实现类似生产的召回。 [raw/articles/microsoft-vector-search-not-enough-2024.md]
- 来源：每次合成都必须追溯到原始来源；否则内存将变得无法验证。
- 并发：多个代理编辑 Markdown 可能会发生冲突；需要 git 分支/PR 或锁。
- 隐私：个人内存需要命名空间、删除、临时/无内存模式和审核。 [原始/产品文档/openai-chatgpt-memory-2024-2025.md]
- 上下文范围：内存和工具上下文必须按对话、渠道、用户、项目或任务确定范围。在多对话系统中，代理全局固定内存会带来隐私风险、注意力污染和不必要的令牌成本。 [raw/github/letta-issue-652-per-conversation-context-scoping.md]
- 提取/存储质量门：候选记忆在存储之前需要反例、拒绝动作、起源意识、角色保留、重要性评分和反馈循环预防。 [raw/github/mem0-issue-4573-memory-audit-junk.md]
- 模型依赖性：在细致入微的综合、矛盾检测和仔细编写方面，前沿模型仍然优于本地模型。本地模型可以处理索引、聚类、简单提取和草稿摘要，但更好的模型本身不能修复不良的内存管道。 [raw/github/mem0-issue-4573-memory-audit-junk.md]

# 实用的集成蓝图

## 系统架构

规范商店：
- 原始/不可变来源
- 事实/仅附加 JSONL 记录，包含 ID、源范围、时间戳、置信度
- 实体、概念、比较、综合的 wiki/ Markdown 页面
- 模式/代理操作说明
-index.md 和 log.md
- 用于历史记录和审查的 git 存储库

衍生指标：
- SQLite 元数据：页面、来源、事实、标签、时间戳、链接、校验和
- BM25/全文索引，精确检索
- 用于语义搜索的可选向量索引
- 从实体/边生成的可选图形索引，而不是规范源

代理服务：
- 摄入剂
- 检索代理
- 编辑器/合成剂
- Lint/审计代理
- 引文验证器
- 可选的背景反射/修剪剂

## 数据流

1. 源捕获：URL/PDF/paste/repo -> 包含 URL、日期、哈希值的原始文件。
2. 提取：解析标题、作者、日期、来源类型、声明、实体、引用。
3. 事实记录：以源跨度和置信度编写原子声明。
4.集成：更新现有页面；仅在超过阈值后创建新页面。
5. 交叉链接：添加维基链接和反向链接。
6.索引：更新SQLite、BM25、向量索引。
7. 验证：运行引文检查和断开链接检查。
8. Git 提交/审查：保留差异和出处。

## 内存生命周期

观察 -> 捕获原始数据 -> 提取事实 -> 集成 wiki -> 检索任务 -> 生成新的合成 -> 文件有用的合成 -> lint -> 衰减/修剪/存档 -> 当源漂移时重新摄取。

## 摄取管道

原型：
- 完整原始捕获/手动剪辑 -> 原始降价
- 法学硕士摘要 -> 一个概念页
- 手动更新索引/日志

最有价值球员：
- 确定性的原始 frontmatter 和哈希值
- 声明/实体的提取提示
- 不应该存储什么的反面例子
- 持久化之前拒绝/DO_NOT_STORE 操作
- 写作前搜索现有页面
- 源映射表更新
- 引文验证者通过

可扩展：
- 基于队列的摄取
- 块/源跨度 ID
- 保留角色的提取上下文，因此用户/系统/助理/工具/召回的内存内容不会扁平化在一起
- 明确标记回忆的记忆，这样它们就不能被重新提取为新的事实
- 候选记忆质量门，具有重要性、置信度、隐私性和陈旧性评分
- 批量事实提取
- 人工审查用户界面以进行高影响力的更改
- PR 上的 CI lint

## 检索管道

原型：
- 读取index.md，search_files，读取相关页面

最有价值球员：
- BM25 通过 wiki+raw
- 按源类型/日期/可靠性过滤元数据
- 用于语义回忆的可选嵌入
- 在上下文组装之前重新排序
- 生成需要引用的答案

可扩展：
- 查询规划器选择精确/BM25/向量/图形
- 遵循 Self-RAG 原则的自适应检索：仅在需要时检索并批评证据 [raw/papers/self-rag-2023.md]
- 具有预算、多样性、新近度、置信度的上下文打包器

## 编辑管道

- 提出 diff，不要默默地覆盖。
- 如果矛盾：保留两个声明的日期和来源。
- 如果置信度低：将置信度标记为低/中。
- 如果页面超过大小阈值：拆分并链接。
- 每次编辑都会更新索引/日志和源映射。

## 总结管道

- 单一源摘要：页面级源摘要。
- 多源综合：具有段落级出处的主题/概念页面。
- 分层摘要：主题图和递归摘要，灵感来自 RAPTOR。 [raw/papers/raptor-2024.md]
- Guardrail：摘要是派生的工件；原始来源和原子事实仍然是规范的。

## 冲突解决

1. 检查来源可靠性和日期。
2. 检查权利要求的范围或定义是否不同。
3. 如果未解决，请保留两者。
4.添加有争议的：真实和冲突注释。
5. 当冲突影响架构推荐时，请人工审核。

## 内存衰减/修剪

- 存档页面被后来的合成所取代。
- 在 N 天后未经证实的情况下降级陈旧的低可信度声明。
- 永远保留原始来源，除非用户删除它们。
- 仅保留事实日志附加，但标记事实被取代而不是删除。
- 对孤立声明、陈旧声明、损坏链接、低可信度单一来源声明进行定期 lint。

## 个性化策略

- 独立的用户配置文件、项目内存、源知识和程序内存。
- 需要对个人事实进行明确的用户可见的内存更改。
- 提供类似于 OpenAI 产品控件的询问/忘记/导出控件。 [原始/产品文档/openai-chatgpt-memory-2024-2025.md]
- 正如 LangMem 建议的那样，命名空间可以防止用户/项目之间的泄漏。 [raw/articles/langchain-context-engineering-2025.md]
- 添加固定内存文件和内存块的对话/频道/项目范围；默认拒绝不相关的用户配置文件和项目文件。 [raw/github/letta-issue-652-per-conversation-context-scoping.md]
- 以不同于直接用户断言的方式对待助手生成的事实、回忆的记忆、系统提示和工具输出；除非得到确认，否则不要以同样的信心存储它们。 [raw/github/mem0-issue-4573-memory-audit-junk.md]

# MVP 计划

## 原型：1-2 天

- Markdown 目录，包含 SCHEMA.md、index.md、log.md、raw/、concepts/。
- 手动摄取 10-20 个核心源。
- 代理严格遵循源映射表。
- 通过 ripgrep/BM25 或文件搜索进行搜索。
- 无矢量数据库。

复杂度：低。
风险：重复页面、出处薄弱。

## MVP：2-4 周

- 每次摄取自动提交的 Git 存储库。
- SQLite 元数据索引。
- BM25 搜索。
- 用于语义搜索的可选 sqlite-vec。
- 具有稳定 ID 和源范围的事实 JSONL。
- Lint 命令：损坏的链接、孤立页面、源漂移、低可信度、有争议的页面。
- 页面编辑的人工审核工作流程。
- 评估集：50个代表性问题；衡量recall@k、引用正确性、答案忠实度、更新延迟。

复杂性：中等。
风险：引文验证器和冲突检测可能很脆弱。

## 可扩展架构：2-6 个月

- 事件驱动的摄取队列。
- 多智能体研究人员进行源发现和合成。
- 重新排名器和上下文打包器。
- 源自事实/实体的图表索引。
- Web UI/Obsidian 插件供审核。
- 内存权限、命名空间、删除/导出。
- 预定的重新摄取/源漂移检测。

复杂性：高。
风险：成本、延迟、同步冲突、幻觉合成。

# 推荐堆栈

本地优先 MVP：
- 存储：markdown + git + SQLite
- 搜索：BM25优先；天德勤/Bleve/SQLite FTS5；仅在需要时添加 sqlite-vec 或 LanceDB
- Notes UI：Obsidian 或 VS Code
- 代理：Claude Code/Codex/OpenCode/Hermes 风格的工具使用代理
- 解析：web_extract、trafilatura/readability、pymupdf/PDF 标记
- 出处：原始哈希值、源 URL、引用/跨度 ID
- Eval：小型 YAML/JSON 查询集；手动+LLM-法官引文检查

为什么不从矢量 DB 开始：纯矢量故障模式对于精确匹配和域术语都有详细记录。 [raw/articles/microsoft-vector-search-not-enough-2024.md]

为什么不从图形数据库开始：图形提取稍后很有用，但它会在 wiki 拥有足够稳定的概念之前增加模式和实体解析负担。

# 未解决的问题

- 如何评估几个月的记忆质量，而不是单个 QA 任务。
- 如何防止低质量的总结成为持久的错误信念。
- 如何在段落中引用生成的综合或声明粒度，而无需过多的开销。
- 如何决定不记住什么。
- 如何安全地合并冲突的代理编辑。
- 如何支持跨本地/云代理的隐私保护个人内存。
- 如何在不使代理僵化或过度个性化的情况下使记忆变得有用。

# 研究问题

1. 哪种检索组合可以最好地回忆 wiki+原始语料库：BM25、向量、混合、图形或学习重排序？
2. 防止幻觉记忆强化的最小起源模式是什么？
3. 反射/合并应该多久运行一次，什么会触发它：时间、令牌计数、压缩、新源、失败的任务？
4. 源映射规则可以自动化而不会使写入速度太慢吗？
5. LLM 维护的 wiki 何时在纵向研究任务上优于标准 RAG？
6. 哪些记忆衰退策略可以在减少混乱的同时保留有用性？
7. 哪些内存编辑需要人工批准？

# 个人开发者机会

为什么现在：
- Frontier 模型可以可靠地编辑多文件 Markdown、合成源并使用工具。
- 嵌入和本地搜索很便宜。
- Git/markdown/SQLite 提供持久的原语。
- 用户越来越因在聊天中重复上下文而感到痛苦。

对于个人来说已经可行：
- 个人研究维基
- 编码代理内存仓库
- 文献综述助理
- 黑曜石+代理摄取管道
- 带有来源引用的团队决策日志
- 内存检查/审核工具

仍然需要前沿模型：
- 高质量的矛盾检测
- 细致入微的跨源综合
- 强大的源质量评估
- 长期自主研究
- 人类级的写作和编辑

大机遇：
- 内存可观察性：痕迹、检索原因、内存差异。
- 白盒个人记忆系统。
- 针对具有高上下文流失的领域的基于源的研究维基。
- 记忆质量评估工具。
- 代理原生知识 IDE。

可能的伪需求：
- 作为内存销售的通用矢量数据库包装器。
- 黑盒个性化，无需审查/删除/导出。
- 针对高风险个人/公司数据的完全自主内存编辑。
- 图形数据库优先产品，没有明确的编辑工作流程。

护城河：
- 积累的私人源语料库和策划的维基。
- 工作流程集成和审查用户体验。
- 出处/评估工具。
- 信任、隐私和本地优先同步。

将被基础模型吞噬：
- 基本聊天记忆。
- 简单总结。
- 上传文件的通用 RAG。
- 浅嵌入搜索用户界面。

# 源图

|主题 |索赔 |来源 |类型 |可靠性 |笔记|
|---|---|---|---|---|---|
|法学硕士维基 | Wiki 是原始文档和聊天之间持久的复合工件 | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f |要点 |高|作者主要来源；可行性部分推测|
|法学硕士维基 | X 线程有很大的参与度和框架要点作为想法文件 | https://x.com/karpathy/status/2040470801506541998 |推特 |中等|通过网络摘要提取；如果公开使用参与度数字，应重新检查 |
|抹布| RAG 有助于消除幻觉/过时的知识，但存在检索/生成的挑战 | https://arxiv.org/abs/2312.10997 |纸|高|调查 |
|内存架构|虚拟上下文管理使用类似操作系统的内存层https://arxiv.org/abs/2310.08560 |纸|高|记忆GPT |
|内存架构|内存流+反射+检索支持代理行为 | https://arxiv.org/abs/2304.03442 |纸|高|生成代理 |
|代理架构|代理需要模块化的记忆/动作/决策框架 | https://arxiv.org/abs/2309.02427 |纸|高|科阿拉 |
|代理简单|从简单开始；仅当结果改善时才增加复杂性 | https://www.anthropic.com/research/building- effective-agents |博客 |高|人为工程建议|
|研究代理|搜索就是压缩；多代理研究成本约为 15 倍聊天代币 | https://www.anthropic.com/engineering/built-multi-agent-research-system |博客 |高|人择内部系统；特定于上下文的数字 |
|情境工程 |写入/选择/压缩/隔离上下文| https://www.langchain.com/blog/context-engineering-for-agents |博客 |中高 |框架供应商；有用的分类法|
|线束工程|跟踪显示什么上下文进入代理步骤 N | https://sequoiacap.com/podcast/context-engineering-our-way-to-long-horizo​​n-agents-langchains-harrison-chase/|采访 |中高 |哈里森·蔡斯观点|
|嵌入 |嵌入有用但不透明/依赖于模型 | https://simonwillison.net/2023/Oct/23/embeddings/|博客 |高|工程经验|
|检索|仅矢量搜索会错过精确的字符串；需要混合搜索| https://techcommunity.microsoft.com/blog/azuredevcommunityblog/doing-rag-vector-search-is-not-enough/4161073 |博客 |高|微软具体例子|
|实际实施| WUPHF 使用 markdown+git、BM25、SQLite、仅附加事实 | https://news.ycombinator.com/item?id=47899844 | hn/github 讨论 |中等|需要回购检查以进行全面验证 |
|社区辩论 | MemGPT 操作系统名称被批评过于宽泛；作者阐明了内存层次结构的意图https://news.ycombinator.com/item?id=37894403 |嗯|中等|包括作者评论 |
|产品记忆 | Letta内存优先编码代理使用内存块/MemFS和命令 | https://docs.letta.com/letta-code/memory |产品文档 |高|产品行为；营销未经证实|
|产品记忆 | ChatGPT 内存已保存记忆/聊天历史和控件 | https://openai.com/index/memory-and-new-controls-for-chatgpt/|产品文档 |高|产品文档 |
|层次检索|递归摘要改进了一些检索任务 | https://arxiv.org/abs/2401.18059 |纸|高|猛禽 |
|自适应检索 |修复 top-k 检索可能会造成伤害；模型应该决定何时检索/批评 | https://arxiv.org/abs/2310.11511 |纸|高|自我抹布|
|长上下文 |传统的 RAG 假设明确的查询/结构良好的知识；经常是假的| https://arxiv.org/abs/2409.05591 |纸|高|备忘录 |
| Reddit 记忆练习 |相关 LocalLLaMA 内存线程存在，但提取被阻止 | https://www.reddit.com/r/LocalLLaMA/comments/1r21ojm/weve_built_memory_into_4_ Different_agent_systems/|红迪网 |低|证据不足；还不依赖|
|内存故障 |生产 mem0 审计报告 32 天后 97.8% 的垃圾内存和 10,134 个条目 | https://github.com/mem0ai/mem0/issues/4573 | https://github.com/mem0ai/mem0/issues/4573 github 问题 |中等|单一案例研究；足够详细以告知故障模式和缓解措施|
|内存故障 |必须对回忆的记忆进行标记，以便提取时不会将它们重新存储为新事实 | https://github.com/mem0ai/mem0/issues/4573 | https://github.com/mem0ai/mem0/issues/4573 github 问题 |中等|解释反馈环路放大；上下文中毒的交叉链接|
|内存设计 |代理全局内存块在对话中造成隐私、注意力和令牌成本问题https://github.com/letta-ai/lettabot/issues/652 | https://github.com/letta-ai/lettabot/issues/652 github 问题 |中高 | LettaBot 直接设计问题；没有评论，但有具体建议|
| LLM 维基实施 | llm-wiki-compiler 实现摄取/编译/查询/lint/watch/MCP/审查队列和声明级出处 | https://github.com/atomicstrata/llm-wiki-compiler | github 仓库 |中高 |自述文件；独立获取；仍需要代码检查以确保实施质量 |
|代理内存产品| Letta Code 框架持久化代理内存，与基于会话的编码 CLI 不同https://github.com/letta-ai/letta-code | github 仓库 |高|自述文件/产品存储库；与 docs/HN 配对以获取社区视图 |
|团队特工记忆| WUPHF 使用每个代理笔记本 + 共享工作区 wiki 和新会话来避免累积上下文 | https://github.com/nex-crm/wuphf | github 仓库 |中高 |自述文件；性能声明应在视为一般性声明之前进行复制 |
|上下文工程实施| LangChain上下文工程仓库实现写入/选择/压缩/隔离和六种上下文修复技术 | https://github.com/langchain-ai/context_engineering | github 仓库 |中高 |可运行的笔记本；有用的实施参考|

# 当前的更正/证据差距

- Reddit 分析要求尚未满足。直接提取受阻；仅搜索片段可用。现状：证据不足。
- Twitter/X 分析是片面的。 Karpathy 的 X 摘要已被摘录，但更广泛的 X 高质量讨论仍有待收集。
- GitHub 问题/存储库讨论得到改进，但仍然不完整。此阶段添加了 Mem0、LettaBot、Letta Code、WUPHF、llm-wiki-compiler 和 LangChain 上下文工程存储库/问题。下一步 GitHub 通行证应该检查代码路径和其他讨论，而不仅仅是自述文件/问题。
- 尚无独立基准显示 LLM Wiki 在纵向研究工作流程上优于 RAG。这仍然是猜测。
