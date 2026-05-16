# 维基日志

> 所有 wiki 操作的时间记录。仅追加。
> 格式：`## [YYYY-MM-DD] 操作 |主题`

## [2026-05-14] 创建 |维基初始化
- 领域：LLM Wiki / 代理内存 / 上下文压缩 / 知识集成。
- 创建了 SCHEMA.md、index.md、log.md、raw/、entities/、concepts/、comparations/、querys/。

## [2026-05-14] 摄取 |初始 LLM Wiki / Agent Memory 源批次
- 在 raw/articles、raw/papers、raw/community、raw/product-docs 下创建了 20 个原始源文件。
- 创建了概念/llm-wiki-agent-memory-research-framework.md。
- 来源包括 Karpathy gist、MemGPT、Generative Agents、CoALA、RAG 调查、Anthropic 代理帖子、LangChain 上下文工程、Simon Willison 嵌入、Microsoft 混合搜索、HN 讨论、OpenAI/Letta 内存文档、RAPTOR、Self-RAG、MemoRAG。
- Reddit 提取被阻止；可靠性明显较低/证据不足。

## [2026-05-14] 更正 |原料来源保存政策
- 用户更正了摄取策略：原始来源应保留解析后的原始/源文本，而不仅仅是 source_url 和关键提取的声明。
- 更新了 SCHEMA.md，要求在可访问时解析原始/源文本，并在阻止、截断或汇总时使用显式的 raw_preservation / extract_status 标记。
- 重写现有的原始源文件，以包括从可访问的获取/提取的降价中获取的“##解析的源文本”部分。
- 重要警告：web_extract 通常会返回长源的上限/摘要降价；这些文件现在在适当的地方标记为“tool_parsed_or_summarized_text”，并且应该在以后的过程中使用完整的 PDF/API/浏览器提取进行升级。

## [2026-05-14] 计划 | Hermes+黑曜石个人知识库
- 继续研究 Obsidian 集成选项：Obsidian URI、Web Clipper、Properties/Bases、Dataview、Local REST API、MCP 样式集成和 Hermes 内存文档。
- 在 raw/product-docs 和 raw/github 下添加了 9 个用于 Obsidian/Hermes 集成证据的原始源文件。
- 创建了概念/hermes-obsidian-personal-knowledge-base-plan.md。
- 计划推荐：保留 markdown+git 作为规范内存，使用 Obsidian 作为人工审阅/编辑工作区，并使用 Hermes 作为摄取/检索/合成/lint 自动化。让 Hermes 内置内存受限于紧凑的转向事实；在黑曜石中存储更多的个人/研究/项目知识。

## [2026-05-16] 精炼 | Hermes + 黑曜石 KB 真理边界
- 使用单一真相来源模型扩展了概念/hermes-obsidian-personal-knowledge-base-plan.md：不可变的原始来源作为证据，可变的维基注释作为综合，仅附加日志，有界的 Hermes 内存作为转向缓存，派生索引作为可重建的非规范工件。
- 强化原始来源规则：原始资源必须是原始文本/工件记录或代理可以定位和读取的确切本地存储路径；摘要不能代替原始证据。
- 为 raw_source、concept、decision、session_summary 和 procedure Notes 添加了严格的全局和每注释模式。
- 为转换后的源添加了“source_derivation”，例如 OCR 输出、转录清理、解析的 PDF、翻译版本、规范化 HTML 提取和 Markdown 清理过程。
- 添加了自动化/权限边界、文件夹策略、人工确认触发器和 MVP 摄取/真相查找/会话到知识循环。

## [2026-05-14] 升级 |原始源全文通行证
- 使用 arXiv PDF + PyMuPDF 页面文本提取将 7 个 arXiv 论文原始源升级为“raw_preservation: full_pdf_text”：MemGPT、Generative Agents、CoALA、RAG Survey、RAPTOR、Self-RAG、MemoRAG。
- 使用 readability-lxml + html2text 将 8 个网络/博客/产品源升级为“raw_preservation：full_html_article_text_candidate”。这些是候选完整文章文本，因为站点呈现的动态内容可能仍会省略隐藏部分。
- 将 3 个黑客新闻讨论升级为完整评论树文本：通过 Algolia API 的 HN Karpathy 风格 wiki（115 条评论）、通过 Firebase API 的 HN MemGPT（106 条评论）、通过 Firebase API 的 HN Letta 代码（37 条评论）。
- 剩余差距：Reddit LocalLLaMA 内存线程保持“extraction_blocked”；全线程仍然需要浏览器/API/存档/手动导出。

## [2026-05-14] 更新 | Git同步要求
- 用户请求通过 git 存储库同步未来的更改。
- 更新了 SCHEMA.md 以要求检查 git 状态、暂存相关文件、使用明确的消息提交以及在远程配置/可用时进行推送。

## [2026-05-15] 摄取 |代理内存系统的 GitHub 问题/存储库证据
- 在 raw/github/ 下添加了原始 GitHub 源：
  - mem0 问题 #4573 生产内存审核：10,134 个条目，报告 97.8% 垃圾、反馈环路放大、质量门建议。
  - LettaBot 问题 #652：MemFS/内存块的每个对话上下文范围。
  - mem0、Letta Code、WUPHF、llm-wiki-compiler、LangChain context_engineering 和 LangChain how_to_fix_your_context 的自述文件快照。
- 使用有关内存故障模式、上下文范围、现有项目、摄取质量门和源映射行的新 GitHub 支持的证据更新了 ideas/llm-wiki-agent-memory-research-framework.md。
- 更新了index.md摘要。

## [2026-05-16] 更新 |负记忆熵滤波器
- 在concepts/hermes-obsidian-personal-knowledge-base-plan.md中添加负内存过滤规则：熵意味着低未来检索值，而不是香农熵。
- 默认策略：拒绝瞬态，除非它成为持久的偏好、事实、决策、可重用的过程、源支持的综合或跟踪的后续行动。
- 明确拒绝 shell/工具输出日志、代理思维链、重复检索摘录、会话脚手架、已完成的任务跟踪以及未跟踪的未来可能的操作状态。

## [2026-05-16] 更新 |内存管道和提取阈值
- 添加了内存管道：交互 -> 工作上下文 -> 临时暂存 -> 候选提取 -> 熵过滤器 -> 持久知识 -> 检索索引。
- 将知识定义为压缩的状态转换，而不是交互历史。
- 更新了 session_summary 结构，以包括持久结果、决策、新知识、可重复使用的程序、未解决的问题、添加的证据以及拒绝/不存储。
- 增加了内存提取阈值：仅当架构发生变化、持久偏好、可重用过程、来源、决策、长期综合或有价值的未解决问题出现时，才创建持久会话笔记。
- 从稳定的会话笔记中明确排除文字记录、时间顺序重播、工具日志和思想链部分。

## [2026-05-16] 更新 |会话半衰期生命周期方案
- 增加了会话半衰期机制：会话是候选知识的临时容器，而不是永久的长期知识。
- 添加了内存类模型：规范、语义、操作和情景，检索优先级基于类而不是文件夹。
- 添加了自适应保留阶段：活动、腐烂、存档候选、压缩和需要人工确认的罕见删除。
- 增加了强化模型：检索/引用计数可以增加检索权重，因此在噪音衰减的同时，有价值的操作记忆仍然存在。
- 添加了规范化管道：从会话笔记中提取持久项目，将其提升为概念/决策/程序/项目内存/用户配置文件，然后降低会话重要性。
- 添加了最小内存指标并推荐“50-sessions/active/”加上“50-sessions/archive/”布局。

## [2026-05-16] 更新 |工作集装配标准 v1
- 添加了工作集程序集 v1 作为从范围检索结果到角色分离、令牌预算、语义压缩执行上下文的确定性管道。
- 定义结构化的CandidateNote、Cluster 和WorkingSetOutput 模式，以防止中间工件中的自由文本漂移。
- 具有固定评分权重和令牌预算的指定检索、排名、聚类、压缩、重复数据删除、按角色隔离和组装步骤。
- 添加了版本控制、指标和“--debug-working-set”可观察性要求。
- 强化核心原则：检索是探索，簇是意义单元，工作集是运行时工件而不是存储结构。
