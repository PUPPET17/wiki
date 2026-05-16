---
source_url: https://github.com/langchain-ai/context_engineering
fetched_url: https://raw.githubusercontent.com/langchain-ai/context_engineering/main/README.md
source_type: github repo
author: langchain-ai/context_engineering maintainers
source_date: 2025-07-08
ingested: 2026-05-15
sha256: bf04e3d6e9c9d35b041504fd11f7cbb1de9834a49d088c752ef8de166475f065
raw_preservation: full_github_readme_text
extraction_method: github_repo_api_and_raw_readme
github_repo: langchain-ai/context_engineering
stars: 178
open_issues: 3
---

#GitHub存储库：langchain-ai/context_engineering

##源元数据

-来源网址：https://github.com/langchain-ai/context_engineering
-获取的URL：https://raw.githubusercontent.com/langchain-ai/context_engineering/main/README.md
-来源类型：github repo
-作者：langchain-ai/context_engineering maintainers
-来源日期：2025-07-08
-摄入日期：2026-05-15
-可靠性：中-高
-原始保存状态：full_github_readme_text
-提取方式：github_repo_api_and_raw_readme

##解析的源文本

#存储库元数据：langchain-ai/context_engineering

-GitHub网址：https://github.com/langchain-ai/context_engineering
-说明：无
-星级：178
-叉子：42
-未决问题：3
-创建时间：2025-07-08T18：05:15 Z
-更新日期：2026-05-09T07：16:53 Z
-许可证：无

##README.md

#🧱使用LangGraph进行上下文工程

代理需要上下文（例如，指令、外部知识、工具反馈）来执行任务。上下文工程是在代理轨迹的每一步用正确的信息填充上下文窗口的艺术和科学。该存储库在“context_engineering”文件夹中有一组笔记本，涵盖了上下文工程的不同策略，包括**写入、选择、压缩和隔离**。对于每一个，我们用例子解释了LangGraph是如何设计来支持它的。

<img width="1231"height="448"alt="屏幕截图2025-07-13 at 2 57 28 PM"src="https://github.com/user-attachments/assets/8e7b59e0-4bb0-48f6-aeba-2d789ada55e3"/>

##🚀快速入门

###先决条件
-Python 3.9或更高版本
- [uv](https://docs.astral.sh/uv/) package manager
- [Deno](https://docs.deno.com/runtime/getting_started/installation/) required for the sandboxed environment in the `4_isolate_context.ipynb` notebook

###安装
1.克隆仓库并激活虚拟环境：
```bash
git clone https://github.com/langchain-ai/context_engineering
cd context_engineering
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

4.然后，您可以运行`context_engineering`文件夹中的笔记本：

```
context_engineering/
├── 1_write_context.ipynb      # Examples of saving context externally
├── 2_select_context.ipynb     # Examples of retrieving relevant context
├── 3_compress_context.ipynb   # Examples of context compression techniques
└── 4_isolate_context.ipynb    # Examples of context isolation methods
```

##📚背景

As Andrej Karpathy puts it, LLMs are like a [new kind of operating system](https://www.youtube.com/watch?si=-aKY-x57ILAmWTdw&t=620&v=LCEmiRjPEtQ&feature=youtu.be). The LLM is like the CPU and its [context window](https://docs.anthropic.com/en/docs/build-with-claude/context-windows) is like the RAM, serving as the model’s working memory. Just like RAM, the LLM context window has limited [capacity](https://lilianweng.github.io/posts/2023-06-23-agent/) to handle various sources of context. And just as an operating system curates what fits into a CPU’s RAM, we can think about “context engineering” playing a similar role. [Karpathy summarizes this well](https://x.com/karpathy/status/1937902205765607626):

>[上下文工程是]“…用正确的信息填充上下文窗口以进行下一步的精细艺术和科学。”

What are the types of context that we need to manage when building LLM applications? We can think of context engineering as an [umbrella](https://x.com/dexhorthy/status/1933283008863482067) that applies across a few different context types:

-**说明**-提示、记忆、少量示例、工具说明等
-**知识**-事实、记忆等
-**工具**-来自工具调用的反馈

##代理挑战

However, long-running tasks and accumulating feedback from tool calls mean that agents often utilize a large number of tokens. This can cause numerous problems: it can [exceed the size of the context window](https://cognition.ai/blog/kevin-32b), balloon cost / latency, or degrade agent performance. Drew Breunig [nicely outlined](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html) a number of specific ways that longer context can cause perform problems. 

With this in mind, [Cognition](https://cognition.ai/blog/dont-build-multi-agents) called out the importance of context engineering with agents:

>“上下文工程”…实际上是工程师构建人工智能代理的首要工作。

[Anthropic](https://www.anthropic.com/engineering/built-multi-agent-research-system) also laid it out clearly:

>*座席经常参与跨越数百个回合的对话，需要谨慎的上下文管理策略。*
>

##上下文工程策略

在本报告中，我们通过回顾各种流行的代理和论文，介绍了代理上下文工程的一些常见策略——编写、选择、压缩和隔离。然后我们解释LangGraph是如何设计来支持它们的！

***写入上下文**-将其保存在上下文窗口之外，以帮助代理执行任务。
***选择上下文**-将其拉入上下文窗口以帮助代理执行任务。
***压缩上下文**-仅保留执行任务所需的令牌。
***隔离上下文**-将其拆分以帮助代理执行任务。

###1.写入上下文
**说明**：在上下文窗口之外保存信息以帮助座席执行任务。

### 📚 **What's Covered in [1_write_context.ipynb](context_engineering/1_write_context.ipynb)**
-**LangGraph**中的暂存板：使用状态对象在代理会话期间持久化信息
-使用TypedDict实现结构化数据的StateGraph
-将上下文写入状态并跨节点访问它
-容错和暂停/恢复工作流的检查点
-**内存系统**：跨多个会话的长期持久性
-InMemoryStore用于存储具有命名空间的内存
-与检查点集成以实现全面的内存管理
-使用用户上下文存储和检索笑话的示例

##2.选择上下文
**描述**：将信息拉入上下文窗口以帮助代理执行任务。

### 📚 **What's Covered in [2_select_context.ipynb](context_engineering/2_select_context.ipynb)**
-**暂存板选择**：从代理状态获取特定上下文
-LangGraph节点中的选择性状态访问
-在节点之间传递上下文的多步骤工作流
-**记忆检索**：为当前任务选择相关记忆
-基于命名空间的内存检索
-上下文感知记忆选择，以避免不相关信息
-**刀具选择**：针对大型刀具集的基于RAG的刀具检索
-用于语义工具搜索的LangGraph Bigtool库
-基于嵌入的工具描述匹配
-数学库函数和语义检索示例
-**知识检索**：外部知识的RAG实现
-使用文档拆分创建矢量存储
-与LangGraph代理集成的检索工具
-具有上下文感知检索的多轮对话

##3.压缩上下文
**描述**：仅保留执行任务所需的令牌。

### 📚 **What's Covered in [3_compress_context.ipynb](context_engineering/3_compress_context.ipynb)**
-**对话摘要**：管理长座席轨迹
-任务完成后的端到端对话总结
-令牌使用优化（演示从115k减少到60k令牌）
-**工具输出压缩**：减少令牌密集型工具响应
-RAG检索结果总结
-与LangGraph工具节点集成
-博客文章检索和摘要的实际示例
-**基于状态的压缩**：使用LangGraph状态进行上下文管理
-带有摘要字段的自定义状态模式
-基于上下文长度的条件摘要

##4.隔离上下文
**描述**：拆分上下文以帮助代理执行任务。

### 📚 **What's Covered in [4_isolate_context.ipynb](context_engineering/4_isolate_context.ipynb)**
-**多代理系统**：跨专业代理分离关注点
-用于任务委派的主管架构
-具有隔离上下文窗口的专业代理（数学专家、研究专家）
-LangGraph Supervisor库实现
-**沙盒环境**：隔离执行环境中的上下文
-用于安全代码执行的PyodideSandboxTool
-大语言模型上下文窗口外的状态隔离
-沙盒变量中的上下文存储示例
-**基于状态的隔离**：使用LangGraph状态模式进行上下文分离
-用于选择性上下文暴露的结构化状态设计
-代理状态对象内基于字段的隔离
