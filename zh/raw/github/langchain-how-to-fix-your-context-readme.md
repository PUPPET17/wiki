---
source_url: https://github.com/langchain-ai/how_to_fix_your_context
fetched_url: https://raw.githubusercontent.com/langchain-ai/how_to_fix_your_context/main/README.md
source_type: github repo
author: langchain-ai/how_to_fix_your_context maintainers
source_date: 2025-07-17
ingested: 2026-05-15
sha256: f4c8501c28b677ba1e766a2268dc85d0d07001a6bb3569bfda037fe47c10ca6c
raw_preservation: full_github_readme_text
extraction_method: github_repo_api_and_raw_readme
github_repo: langchain-ai/how_to_fix_your_context
stars: 538
open_issues: 2
---

#GitHub存储库：langchain-ai/how_to_fix_your_context

##源元数据

-来源网址：https://github.com/langchain-ai/how_to_fix_your_context
-获取的URL：https://raw.githubusercontent.com/langchain-ai/how_to_fix_your_context/main/README.md
-来源类型：github repo
-作者：langchain-ai/how_to_fix_your_context maintainers
-来源日期：2025-07-17
-摄入日期：2026-05-15
-可靠性：中-高
-原始保存状态：full_github_readme_text
-提取方式：github_repo_api_and_raw_readme

##解析的源文本

#存储库元数据：langchain-ai/how_to_fix_your_context

-GitHub URL：https://github.com/langchain-ai/how_to_fix_your_context
-说明：无
-星级：538
-叉子：105
-未决问题：2
-创建时间：2025-07-17T23：47：00Z
-更新日期：2026-05-13T23：58：22Z
-许可证：无

##README.md

#如何修复您的上下文

As Karpathy [said](https://x.com/karpathy/status/1937902205765607626), [Context Engineering](https://blog.langchain.com/context-engineering-for-agents/) is the *delicate art and science of filling the context window with just the right information for the next step.* There [are](https://cognition.ai/blog/dont-build-multi-agents) [many](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) ways to do this. In Drew Breunig's post ["How to Fix Your Context"](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html), he outlines 6 common context engineering techniques. This repository demonstrates each technique using LangGraph.

<img width="4777"height="1983"alt="context_eng_drew"src="https://github.com/user-attachments/assets/b6c07894-f6c6-41d0-9d95-e5e7030189b3"/>

##🚀快速入门

###先决条件
-Python 3.9或更高版本
- [uv](https://docs.astral.sh/uv/) package manager

###安装
1.克隆仓库并激活虚拟环境：
```bash
git clone https://github.com/langchain-ai/how_to_fix_your_context
cd how_to_fix_your_context
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
2.安装依赖项：
```bash
uv pip install -r requirements.txt
```

3.为要使用的模型提供程序设置环境变量：
```bash
export OPENAI_API_KEY="your-openai-api-key"
export ANTHROPIC_API_KEY="your-anthropic-api-key"
```

##背景

###上下文问题

Chroma's report on [Context Rot](https://research.trychroma.com/context-rot) explains that LLMs do not treat every token in their context window equally. Across 18 models (including GPT‑4.1, Claude 4, Gemini 2.5, Qwen3, etc.), they show that performance on even very simple tasks degrades—often in non‑uniform and surprising ways—as the input length grows. Drew Breunig outlined four failure modes that help to explain [why long contexts fail](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html):

1.**上下文中毒**-进入上下文并被重复引用的幻觉或错误
2.**上下文分散**-当上下文变得如此之大，以至于模型更关注累积的历史而不是训练时
3.**上下文混淆**-影响响应质量的多余内容，因为模型感到必须使用所有可用的上下文
4.**上下文冲突**-累积上下文内的冲突信息会降低推理能力

##上下文工程

Drew outlined [6 context engineering techniques](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html) to help fix these failure modes, including: 

*RAG（检索增强生成）
*工具装载
*上下文隔离
*上下文修剪
*上下文摘要
*上下文卸载

我们使用LangGraph在一组Jupyter笔记本中实现了这些技术中的每一种，如下所述。

##

LangGraph is a low [is a low-level orchestration framework](https://blog.langchain.com/how-to-think-about-agent-frameworks/) for building AI applications. You can [lay out agents or workflows as a set of nodes](https://www.youtube.com/watch?v=aHCDrAbH_go), [define](https://blog.langchain.com/how-to-think-about-agent-frameworks/) the logic within each one, and define a state object that is passed between them. A [StateGraph](https://langchain-ai.github.io/langgraph/concepts/low_level/#stategraph) is LangGraph's primary abstraction for building these stateful workflows and agents with:

-**节点**是接收当前状态并返回更新的处理步骤
-**边**连接节点以创建执行流（线性、条件或循环）
-**状态**充当节点之间的共享暂存器

这种低级控制使得实现每种上下文工程技术变得容易。

###1.检索增强生成
**Notebook**: [notebooks/01-rag.ipynb](notebooks/01-rag.ipynb)

*检索增强生成（RAG）是有选择地添加相关信息以帮助大语言模型生成更好响应的行为。*

**实现**：使用LangGraph创建一个RAG代理，并使用从Lilian Weng的博客文章构建的检索工具。代理在回答问题之前使用Claude Sonnet智能地搜索相关上下文。

**关键组件**：
-使用RecursiveCharacterTextSplitter进行文档加载和分块
-使用OpenAI嵌入创建矢量存储
-用于工具调用的具有条件边的LangGraph状态图
-引导座席在检索前明确研究范围的系统提示

**性能**：使用25k令牌进行关于奖励黑客类型的复杂查询，由令牌密集型工具调用驱动。

###2.工具装载
**Notebook**: [notebooks/02-tool-loadout.ipynb](notebooks/02-tool-loadout.ipynb)

*工具加载是指仅选择相关的工具定义以添加到上下文中的行为。*

**实现**：通过索引向量存储中的所有Python数学库函数并根据用户查询仅动态选择相关工具来演示语义工具选择。

**关键组件**：
-具有所有数学函数的UUID映射的工具注册表
-使用嵌入的工具描述的向量存储索引
-基于语义相似度搜索的动态工具绑定（限制5个工具）
-扩展状态类以跟踪每个对话中选择的工具

**优点**：与加载所有可用工具相比，避免了重叠工具描述造成的上下文混乱，并提高了工具选择的准确性。

###3.上下文隔离
**Notebook**: [notebooks/03-context-quarantine.ipynb](notebooks/03-context-quarantine.ipynb)

*上下文隔离是将上下文隔离在它们自己的专用线程中的行为，每个线程由一个或多个大语言模型单独使用。*

**实现**：使用LangGraph Supervisor架构创建Supervisor多代理系统，该架构具有具有隔离上下文窗口的专用代理。

**关键组件**：
-将任务路由到适当专家的主管代理
-具有加法/乘法工具和集中数学提示的数学专家代理
-具有web搜索功能和以研究为重点的提示的研究专家代理
-基于任务类型的明确授权规则（研究与计算）

**好处**：每个代理在自己的上下文窗口中操作，防止上下文冲突和分心。对于需要多种技能的复杂任务，主管使用基于工具的切换在代理之间进行协调。

###4.上下文修剪
**Notebook**: [notebooks/04-context-pruning.ipynb](notebooks/04-context-pruning.ipynb)

*上下文修剪是从上下文中删除不相关或不需要的信息的行为。*

**实现**：通过智能修剪步骤扩展RAG代理，在将检索到的文档传递给主大语言模型之前，从它们中删除不相关的内容。

**关键组件**：
-工具修剪提示，指示较小的大语言模型仅提取相关信息
-GPT-4o-mini作为削减成本的修剪模型
-具有用于上下文压缩的摘要字段的扩展状态类
-基于原始用户请求进行修剪以保持相关性

**性能改进**：与基本RAG相比，相同查询的令牌使用量从25k减少到11k，在保持回答质量的同时展示了显著的上下文压缩。

###5.上下文摘要
**Notebook**: [notebooks/05-context-summarization.ipynb](notebooks/05-context-summarization.ipynb)

*上下文摘要是将累积的上下文浓缩成浓缩摘要的行为。*

**实现**：通过添加一个总结步骤，在RAG代理的基础上构建，该步骤可以压缩工具调用结果，以减少上下文大小，同时保留基本信息。

**关键组件**：
-创建全面而简洁的文档版本的工具摘要提示
-GPT-4o-mini作为成本效率的总结模型
-保留所有关键信息同时消除冗长的准则（减少50-70%的目标）
-具有用于跟踪压缩内容的摘要字段的扩展状态类

**方法**：与删除不相关内容的修剪不同，摘要将所有信息压缩成更紧凑的格式，使其适用于所有检索到的内容都相关但冗长的情况。

###6.上下文卸载
**Notebook**: [notebooks/06-context-offloading.ipynb](notebooks/06-context-offloading.ipynb)

*上下文卸载是在大语言模型上下文之外存储信息的行为，通常通过存储和管理数据的工具。*

**实现**：演示了上下文卸载的两种方法——会话期间的临时暂存器存储和使用LangGraph的存储接口的持久跨线程内存。

**关键组件**：
-具有用于临时存储的暂存板字段的扩展状态类
-用于记笔记的WriteToScratchpad和ReadFromScratchpad工具
-InMemoryStore用于持久跨线程内存
-维护有组织的笔记并建立在以前的研究基础上的研究工作流程

**两种存储模式**：
1.**会话暂存板**：单个会话线程内的临时存储
2.**持久内存**：使用跨不同会话持久的命名空间键值对的跨线程存储

**好处**：使智能体能够维护研究计划，积累发现，并在多次交互中访问以前的工作，类似于Anthropic的多智能体研究员和ChatGPT等产品实现记忆的方式。

##参考文献

- [How to Fix Your Context](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html) by Drew Breunig
- [How Contexts Fail and How to Fix Them](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html) by Drew Breunig
