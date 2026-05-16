---
source_url: https://www.langchain.com/blog/context-engineering-for-agents
fetched_url: https://www.langchain.com/blog/context-engineering-for-agents
source_type: blog
author: LangChain Team
source_date: 2025-07-02
ingested: 2026-05-14
sha256: d256b22e99907196f39bbc38b773b2bec50bf04f898e5c38588704df4f03caf9
raw_preservation: full_html_article_text_candidate
extraction_method: readability_lxml_html2text
html_bytes: 192383
parsed_chars: 25444
---

#上下文工程

##源元数据

-来源网址：https://www.langchain.com/blog/context-engineering-for-agents
-获取的网址：https://www.langchain.com/blog/context-engineering-for-agents
-来源类型：博客
-作者：LangChain团队
-来源日期：2025-07-02
-摄入日期：2026-05-14
-可靠性：中-高
-原始保存状态：full_html_article_text_candidate
-提取方式：readability_lxml_html2text

##解析的源文本

##TL；DR

代理需要上下文来执行任务。上下文工程是在代理轨迹的每一步用正确的信息填充上下文窗口的艺术和科学。在这篇文章中，我们通过回顾各种流行的代理和论文来分解上下文工程的一些常见策略——**编写、选择、压缩和隔离——**。然后我们解释LangGraph是如何设计来支持它们的！

**Also, see our video on context engineering**[**here**](https://youtu.be/4GiqzUHD5AA?ref=blog.langchain.com)**.**

上下文工程的一般类别

##上下文工程

As Andrej Karpathy puts it, LLMs are like a [new kind of operating system](https://www.youtube.com/watch?si=-aKY-x57ILAmWTdw&t=620&v=LCEmiRjPEtQ&feature=youtu.be&ref=blog.langchain.com). The LLM is like the CPU and its [context window](https://docs.anthropic.com/en/docs/build-with-claude/context-windows?ref=blog.langchain.com) is like the RAM, serving as the model’s working memory. Just like RAM, the LLM context window has limited [capacity](https://lilianweng.github.io/posts/2023-06-23-agent/?ref=blog.langchain.com) to handle various sources of context. And just as an operating system curates what fits into a CPU’s RAM, we can think about “context engineering” playing a similar role. [Karpathy summarizes this well](https://x.com/karpathy/status/1937902205765607626?ref=blog.langchain.com):

>_[上下文工程是]“……为下一步填充正确信息的上下文窗口的微妙艺术和科学。”_

大语言模型应用中常用的上下文类型

What are the types of context that we need to manage when building LLM applications? Context engineering as an [umbrella](https://x.com/dexhorthy/status/1933283008863482067?ref=blog.langchain.com) that applies across a few different context types:

***说明**–提示、记忆、少量示例、工具说明等
***知识**-事实、记忆等
***工具**-来自工具调用的反馈

##代理的上下文工程

This year, interest in [agents](https://www.anthropic.com/engineering/building-effective-agents?ref=blog.langchain.com) has grown tremendously as LLMs get better at [reasoning](https://platform.openai.com/docs/guides/reasoning?api-mode=responses&ref=blog.langchain.com) and [tool calling](https://www.anthropic.com/engineering/building-effective-agents?ref=blog.langchain.com). [Agents](https://www.anthropic.com/engineering/building-effective-agents?ref=blog.langchain.com) interleave [LLM invocations and tool calls](https://www.anthropic.com/engineering/building-effective-agents?ref=blog.langchain.com), often for [long-running tasks](https://blog.langchain.com/introducing-ambient-agents/). Agents interleave [LLM calls and tool calls](https://www.anthropic.com/engineering/building-effective-agents?ref=blog.langchain.com), using tool feedback to decide the next step.

Agents interleave[ LLM calls and tool calls](https://www.anthropic.com/engineering/building-effective-agents?ref=blog.langchain.com), using tool feedback to decide the next step

However, long-running tasks and accumulating feedback from tool calls mean that agents often utilize a large number of tokens. This can cause numerous problems: it can [exceed the size of the context window](https://cognition.ai/blog/kevin-32b?ref=blog.langchain.com), balloon cost / latency, or degrade agent performance. Drew Breunig [nicely outlined](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html?ref=blog.langchain.com) a number of specific ways that longer context can cause perform problems, including:

来自工具调用的上下文在多个代理回合中累积

With this in mind, [Cognition](https://cognition.ai/blog/dont-build-multi-agents?ref=blog.langchain.com) called out the importance of context engineering:

>_“上下文工程”…实际上是工程师构建人工智能代理的首要工作。_

[Anthropic](https://www.anthropic.com/engineering/built-multi-agent-research-system?ref=blog.langchain.com) also laid it out clearly:

>_代理经常参与跨越数百个回合的对话，需要谨慎的上下文管理策略。_

那么，今天人们是如何应对这一挑战的呢？我们将代理上下文工程的常见策略分为四个部分——**编写、选择、压缩和隔离——**，并从一些流行的代理产品和论文的综述中给出了每个部分的例子。然后我们解释LangGraph是如何设计来支持它们的！

上下文工程的一般类别

##写入上下文

_写入上下文意味着将其保存在上下文窗口之外，以帮助代理执行任务。_

**便笺簿**

When humans solve tasks, we take notes and remember things for future, related tasks. Agents are also gaining these capabilities! Note-taking via a “[scratchpad](https://www.anthropic.com/engineering/claude-think-tool?ref=blog.langchain.com)” is one approach to persist information while an agent is performing a task. The idea is to save information outside of the context window so that it’s available to the agent. [Anthropic’s multi-agent researcher](https://www.anthropic.com/engineering/built-multi-agent-research-system?ref=blog.langchain.com) illustrates a clear example of this:

>_LeadResearcher首先考虑该方法，并将其计划保存到内存中以持久化上下文，因为如果上下文窗口超过200,000个令牌，它将被截断，保留该计划非常重要。_

Scratchpads can be implemented in a few different ways. They can be a [tool call](https://www.anthropic.com/engineering/claude-think-tool?ref=blog.langchain.com) that simply [writes to a file](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem?ref=blog.langchain.com). They can also be a field in a runtime [state object](https://langchain-ai.github.io/langgraph/concepts/low_level/?ref=blog.langchain.com#state) that persists during the session. In either case, scratchpads let agents save useful information to help them accomplish a task.

**回忆**

Scratchpads help agents solve a task within a given session (or [thread](https://langchain-ai.github.io/langgraph/concepts/persistence/?ref=blog.langchain.com#threads)), but sometimes agents benefit from remembering things across _many_ sessions! [Reflexion](https://arxiv.org/abs/2303.11366?ref=blog.langchain.com) introduced the idea of reflection following each agent turn and re-using these self-generated memories. [Generative Agents](https://ar5iv.labs.arxiv.org/html/2304.03442?ref=blog.langchain.com) created memories synthesized periodically from collections of past agent feedback.

大语言模型可用于更新或创建存储器

These concepts made their way into popular products like [ChatGPT](https://help.openai.com/en/articles/8590148-memory-faq?ref=blog.langchain.com), [Cursor](https://forum.cursor.com/t/0-51-memories-feature/98509?ref=blog.langchain.com), and [Windsurf](https://docs.windsurf.com/windsurf/cascade/memories?ref=blog.langchain.com), which all have mechanisms to auto-generate long-term memories that can persist across sessions based on user-agent interactions.

##选择上下文

_选择上下文意味着将其拉入上下文窗口以帮助代理执行任务。_

**便笺簿**

The mechanism for selecting context from a scratchpad depends upon how the scratchpad is implemented. If it’s a [tool](https://www.anthropic.com/engineering/claude-think-tool?ref=blog.langchain.com), then an agent can simply read it by making a tool call. If it’s part of the agent’s runtime state, then the developer can choose what parts of state to expose to an agent each step. This provides a fine-grained level of control for exposing scratchpad context to the LLM at later turns.

**回忆**

If agents have the ability to save memories, they also need the ability to select memories relevant to the task they are performing. This can be useful for a few reasons. Agents might select few-shot examples ([episodic](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#memory-types) [memories](https://arxiv.org/pdf/2309.02427?ref=blog.langchain.com)) for examples of desired behavior, instructions ([procedural](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#memory-types) [memories](https://arxiv.org/pdf/2309.02427?ref=blog.langchain.com)) to steer behavior, or facts ([semantic](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#memory-types) [memories](https://arxiv.org/pdf/2309.02427?ref=blog.langchain.com)) for task-relevant context.

One challenge is ensuring that relevant memories are selected. Some popular agents simply use a narrow set of files that are _always_ pulled into context. For example, many code agent use specific files to save instructions (”procedural” memories) or, in some cases, examples (”episodic” memories). Claude Code uses [`CLAUDE.md`](http://claude.md/?ref=blog.langchain.com). [Cursor](https://docs.cursor.com/context/rules?ref=blog.langchain.com) and [Windsurf](https://windsurf.com/editor/directory?ref=blog.langchain.com) use rules files. 

But, if an agent is storing a larger [collection](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#collection) of facts and / or relationships (e.g., [semantic](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#memory-types) memories), selection is harder. [ChatGPT](https://help.openai.com/en/articles/8590148-memory-faq?ref=blog.langchain.com) is a good example of a popular product that stores and selects from a large collection of user-specific memories.

Embeddings and / or [knowledge](https://arxiv.org/html/2501.13956v1?ref=blog.langchain.com#:~:text=In%20Zep%2C%20memory%20is%20powered,subgraph%2C%20and%20a%20community%20subgraph) [graphs](https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/?ref=blog.langchain.com#:~:text=changes%20since%20updates%20can%20trigger,and%20holistic%20memory%20for%20agentic) for memory indexing are commonly used to assist with selection. Still, memory selection is challenging. At the AIEngineer World’s Fair, [Simon Willison shared](https://simonwillison.net/2025/Jun/6/six-months-in-llms/?ref=blog.langchain.com) an example of selection gone wrong: ChatGPT fetched his location from memories and unexpectedly injected it into a requested image. This type of unexpected or undesired memory retrieval can make some users feel like the context window “ _no longer belongs to them_ ”! 

**工具**

Agents use tools, but can become overloaded if they are provided with too many. This is often because the tool descriptions overlap, causing model confusion about which tool to use. One approach is[ to apply RAG (retrieval augmented generation) to tool descriptions](https://arxiv.org/abs/2410.14594?ref=blog.langchain.com) in order to fetch only the most relevant tools for a task. Some [recent papers](https://arxiv.org/abs/2505.03275?ref=blog.langchain.com) have shown that this improve tool selection accuracy by 3-fold.

**知识**

[RAG](https://github.com/langchain-ai/rag-from-scratch?ref=blog.langchain.com) is a rich topic and it[ can be a central context engineering challenge](https://x.com/_mohansolo/status/1899630246862966837?ref=blog.langchain.com). Code agents are some of the best examples of RAG in large-scale production. Varun from Windsurf captures some of these challenges well:

>_索引代码≠上下文检索…[我们正在进行索引和嵌入搜索…[使用]AST解析代码并沿着语义上有意义的边界进行分块…随着代码库规模的增长，嵌入搜索作为检索启发式变得不可靠…我们必须依赖grep/文件搜索、基于知识图的检索和…重新排序步骤等技术的组合，其中[上下文]按照相关性顺序进行排序。_

##压缩上下文

_压缩上下文涉及仅保留执行任务所需的标记。_

**上下文摘要**

Agent interactions can span [hundreds of turns](https://www.anthropic.com/engineering/built-multi-agent-research-system?ref=blog.langchain.com) and use token-heavy tool calls. Summarization is one common way to manage these challenges. If you’ve used Claude Code, you’ve seen this in action. Claude Code runs “[auto-compact](https://docs.anthropic.com/en/docs/claude-code/costs?ref=blog.langchain.com)” after you exceed 95% of the context window and it will summarize the full trajectory of user-agent interactions. This type of compression across an [agent trajectory](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#manage-short-term-memory) can use various strategies such as [recursive](https://arxiv.org/pdf/2308.15022?ref=blog.langchain.com#:~:text=the%20retrieved%20utterances%20capture%20the,based%203) or [hierarchical](https://alignment.anthropic.com/2025/summarization-for-monitoring/?ref=blog.langchain.com#:~:text=We%20addressed%20these%20issues%20by,of%20our%20computer%20use%20capability) summarization.

可以应用摘要的几个地方

It can also be useful to [add summarization](https://github.com/langchain-ai/open_deep_research/blob/e5a5160a398a3699857d00d8569cb7fd0ac48a4f/src/open_deep_research/utils.py?ref=blog.langchain.com#L1407) at specific points in an agent’s design. For example, it can be used to post-process certain tool calls (e.g., token-heavy search tools). As a second example, [Cognition](https://cognition.ai/blog/dont-build-multi-agents?ref=blog.langchain.com#a-theory-of-building-long-running-agents) mentioned summarization at agent-agent boundaries to reduce tokens during knowledge hand-off. Summarization can be a challenge if specific events or decisions need to be captured. [Cognition](https://cognition.ai/blog/dont-build-multi-agents?ref=blog.langchain.com#a-theory-of-building-long-running-agents) uses a fine-tuned model for this, which underscores how much work can go into this step.

**上下文修剪**

Whereas summarization typically uses an LLM to distill the most relevant pieces of context, trimming can often filter or, as Drew Breunig points out, “[prune](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html?ref=blog.langchain.com)” context. This can use hard-coded heuristics like removing [older messages](https://python.langchain.com/docs/how_to/trim_messages/?ref=blog.langchain.com) from a list. Drew also mentions [Provence](https://arxiv.org/abs/2501.16214?ref=blog.langchain.com), a trained context pruner for Question-Answering.

##隔离上下文

_隔离上下文涉及将其拆分以帮助代理执行任务。_

**多智能体**

One of the most popular ways to isolate context is to split it across sub-agents. A motivation for the OpenAI [Swarm](https://github.com/openai/swarm?ref=blog.langchain.com) library was [separation of concerns](https://openai.github.io/openai-agents-python/ref/agent/?ref=blog.langchain.com), where a team of agents can handle specific sub-tasks. Each agent has a specific set of tools, instructions, and its own context window.

跨多个代理分割上下文

Anthropic’s [multi-agent researcher](https://www.anthropic.com/engineering/built-multi-agent-research-system?ref=blog.langchain.com) makes a case for this: many agents with isolated contexts outperformed single-agent, largely because each subagent context window can be allocated to a more narrow sub-task. As the blog said:

>_[子代理操作]与它们自己的上下文窗口并行，同时探索问题的不同方面。_

Of course, the challenges with multi-agent include token use (e.g., up to [15× more tokens](https://www.anthropic.com/engineering/built-multi-agent-research-system?ref=blog.langchain.com) than chat as reported by Anthropic), the need for careful [prompt engineering](https://www.anthropic.com/engineering/built-multi-agent-research-system?ref=blog.langchain.com) to plan sub-agent work, and coordination of sub-agents.

**与环境的上下文隔离**

HuggingFace’s [deep researcher](https://huggingface.co/blog/open-deep-research?ref=blog.langchain.com#:~:text=From%20building%20,it%20can%20still%20use%20it) shows another interesting example of context isolation. Most agents use [tool calling APIs](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview?ref=blog.langchain.com), which return JSON objects (tool arguments) that can be passed to tools (e.g., a search API) to get tool feedback (e.g., search results). HuggingFace uses a [CodeAgent](https://huggingface.co/papers/2402.01030?ref=blog.langchain.com), which outputs that contains the desired tool calls. The code then runs in a [sandbox](https://e2b.dev/?ref=blog.langchain.com). Selected context (e.g., return values) from the tool calls is then passed back to the LLM.

沙盒可以将上下文与大语言模型隔离开来。

这允许上下文与环境中的大语言模型隔离。Hugging Face指出，这是隔离令牌重对象的好方法，尤其是：

>_[代码代理允许]更好地处理状态…需要存储此图像/音频/其他以备后用吗？没问题，只需将其赋值为变量_[_在您的状态中，然后您[稍后使用它]_](https://deepwiki.com/search/i-am-wondering-if-state-that-i_0e153539-282a-437c-b2b0-d2d68e51b873？ref=blog.langchain.com)_._

**状态**

It’s worth calling out that an agent’s runtime [state object](https://langchain-ai.github.io/langgraph/concepts/low_level/?ref=blog.langchain.com#state) can also be a great way to isolate context. This can serve the same purpose as sandboxing. A state object can be designed with a [schema](https://langchain-ai.github.io/langgraph/concepts/low_level/?ref=blog.langchain.com#schema) that has fields that context can be written to. One field of the schema (e.g., `messages`) can be exposed to the LLM at each turn of the agent, but the schema can isolate information in other fields for more selective use.

##使用LangSmith/LangGraph进行上下文工程

So, how can you apply these ideas? Before you start, there are two foundational pieces that are helpful. First, ensure that you have a way to [look at your data](https://hamel.dev/blog/posts/evals/?ref=blog.langchain.com) and track token-usage across your agent. This helps inform where best to apply effort context engineering. [LangSmith](https://docs.smith.langchain.com/?ref=blog.langchain.com) is well-suited for agent [tracing / observability](https://docs.smith.langchain.com/observability?ref=blog.langchain.com), and offers a great way to do this. Second, be sure you have a simple way to test whether context engineering hurts or improve agent performance. LangSmith enables [agent evaluation](https://docs.smith.langchain.com/evaluation/tutorials/agents?ref=blog.langchain.com) to test the impact of any context engineering effort.

**写入上下文**

LangGraph was designed with both thread-scoped ([short-term](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#short-term-memory)) and [long-term memory](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#long-term-memory). Short-term memory uses [checkpointing](https://langchain-ai.github.io/langgraph/concepts/persistence/?ref=blog.langchain.com) to persist [agent state](https://langchain-ai.github.io/langgraph/concepts/low_level/?ref=blog.langchain.com#state) across all steps of an agent. This is extremely useful as a “scratchpad”, allowing you to write information to state and fetch it at any step in your agent trajectory.

LangGraph’s long-term memory lets you to persist context _across many sessions_ with your agent. It is flexible, allowing you to save small sets of [files](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#profile) (e.g., a user profile or rules) or larger [collections](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#collection) of memories. In addition, [LangMem](https://langchain-ai.github.io/langmem/?ref=blog.langchain.com) provides a broad set of useful abstractions to aid with LangGraph memory management.

**选择上下文**

Within each node (step) of a LangGraph agent, you can fetch [state](https://langchain-ai.github.io/langgraph/concepts/low_level/?ref=blog.langchain.com#state). This give you fine-grained control over what context you present to the LLM at each agent step. 

In addition, LangGraph’s long-term memory is accessible within each node and supports various types of retrieval (e.g., fetching files as well as [embedding-based retrieval on a memory collection).](https://langchain-ai.github.io/langgraph/cloud/reference/cli/?ref=blog.langchain.com#adding-semantic-search-to-the-store) For an overview of long-term memory, see [our Deeplearning.ai course](https://www.deeplearning.ai/short-courses/long-term-agentic-memory-with-langgraph/?ref=blog.langchain.com). And for an entry point to memory applied to a specific agent, see our [Ambient Agents](https://academy.langchain.com/courses/ambient-agents?ref=blog.langchain.com) course. This shows how to use LangGraph memory in a long-running agent that can manage your email and learn from your feedback.

具有用户反馈和长期记忆的电子邮件代理

For tool selection, the [LangGraph Bigtool](https://github.com/langchain-ai/langgraph-bigtool?ref=blog.langchain.com) library is a great way to apply semantic search over tool descriptions. This helps select the most relevant tools for a task when working with a large collection of tools. Finally, we have several [tutorials and videos](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/?ref=blog.langchain.com) that show how to use various types of RAG with LangGraph.

**压缩上下文**

Because LangGraph [is a low-level orchestration framework](https://blog.langchain.com/how-to-think-about-agent-frameworks/), you [lay out your agent as a set of nodes](https://www.youtube.com/watch?v=aHCDrAbH_go&ref=blog.langchain.com), [define](https://blog.langchain.com/how-to-think-about-agent-frameworks/) the logic within each one, and define an state object that is passed between them. This control offers several ways to compress context.

One common approach is to use a message list as your agent state and [summarize or trim](https://langchain-ai.github.io/langgraph/how-tos/memory/add-memory/?ref=blog.langchain.com#manage-short-term-memory) it periodically using [a few built-in utilities](https://langchain-ai.github.io/langgraph/how-tos/memory/add-memory/?ref=blog.langchain.com#manage-short-term-memory). However, you can also add logic to post-process [tool calls](https://github.com/langchain-ai/open_deep_research/blob/e5a5160a398a3699857d00d8569cb7fd0ac48a4f/src/open_deep_research/utils.py?ref=blog.langchain.com#L1407) or work phases of your agent in a few different ways. You can add summarization nodes at specific points or also add summarization logic to your tool calling node in order to compress the output of specific tool calls.

**隔离上下文**

LangGraph is designed around a [state](https://langchain-ai.github.io/langgraph/concepts/low_level/?ref=blog.langchain.com#state) object, allowing you to specify a state schema and access state at each agent step. For example, you can store context from tool calls in certain fields in state, isolating them from the LLM until that context is required. In addition to state, LangGraph supports use of sandboxes for context isolation. See this [repo](https://github.com/jacoblee93/mini-chat-langchain?tab=readme-ov-file&ref=blog.langchain.com) for an example LangGraph agent that uses [an E2B sandbox](https://e2b.dev/?ref=blog.langchain.com) for tool calls. See this [video](https://www.youtube.com/watch?v=FBnER2sxt0w&ref=blog.langchain.com) for an example of sandboxing using Pyodide where state can be persisted. LangGraph also has a lot of support for building multi-agent architecture, such as the [supervisor](https://github.com/langchain-ai/langgraph-supervisor-py?ref=blog.langchain.com) and [swarm](https://github.com/langchain-ai/langgraph-swarm-py?ref=blog.langchain.com) libraries. You can [see](https://www.youtube.com/watch?v=4nZl32FwU-o&ref=blog.langchain.com) [these](https://www.youtube.com/watch?v=JeyDrn1dSUQ&ref=blog.langchain.com) [videos](https://www.youtube.com/watch?v=B_0TNuYi56w&ref=blog.langchain.com) for more detail on using multi-agent with LangGraph.

##结论

上下文工程正在成为代理构建者应该努力掌握的一门手艺。在这里，我们介绍了当今许多流行代理中常见的一些模式：

*_写入上下文-将其保存在上下文窗口之外，以帮助代理执行任务。_
*_选择上下文-将其拉入上下文窗口以帮助代理执行任务。_
*_压缩上下文-仅保留执行任务所需的标记。_
*_隔离上下文—将上下文拆分以帮助代理执行任务。_

LangGraph使实现它们中的每一个都变得容易，LangSmith提供了一种测试代理和跟踪上下文使用的简单方法。LangGraph和LangGraph共同实现了一个良性的反馈循环，用于识别应用上下文工程、实现它、测试它和重复的最佳机会。
