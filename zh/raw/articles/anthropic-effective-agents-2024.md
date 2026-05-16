---
source_url: https://www.anthropic.com/research/building-effective-agents
fetched_url: https://www.anthropic.com/research/building-effective-agents
source_type: blog
author: Anthropic
source_date: 2024-12-19
ingested: 2026-05-14
sha256: 4104c1e5fe8dd1e015d53b7dc8ba846a83b4378064d87e396c9b6ce9b112f0a6
raw_preservation: full_html_article_text_candidate
extraction_method: readability_lxml_html2text
html_bytes: 178197
parsed_chars: 20396
---

#构建有效的人工智能代理\Anthropic

##源元数据

-来源网址：https://www.anthropic.com/research/building-effective-agents
-获取的网址：https://www.anthropic.com/research/building-effective-agents
-来源类型：博客
-作者：Anthropic
-来源日期：2024-12-19
-摄入日期：2026-05-14
-可靠性：高
-原始保存状态：full_html_article_text_candidate
-提取方式：readability_lxml_html2text

##解析的源文本

在过去的一年里，我们与数十个团队合作，构建了跨行业的大型语言模型（大语言模型）代理。一直以来，最成功的实现都没有使用复杂的框架或专门的库。相反，他们用简单的、可组合的模式来构建。

在本帖中，我们分享了我们从与客户合作和自己构建代理中学到的东西，并为开发人员构建有效代理提供了实用的建议。

##什么是代理？

“代理”可以以几种方式定义。一些客户将代理定义为完全自主的系统，可以长时间独立运行，使用各种工具来完成复杂的任务。其他人使用该术语来描述遵循预定义工作流的更具规范性的实现。在Anthropic，我们将所有这些变体归类为**代理系统**，但在**工作流**和**代理**之间画出了一个重要的架构区别：

***工作流**是通过预定义的代码路径编排大语言模型和工具的系统。
另一方面，***代理**是大语言模型动态指导自己的流程和工具使用的系统，保持对如何完成任务的控制。

下面，我们将详细探讨这两种类型的代理系统。在附录1（“实践中的代理”）中，我们描述了客户在使用这些类型的系统中发现特别有价值的两个领域。

##何时（以及何时不）使用代理

当使用大语言模型构建应用程序时，我们建议尽可能找到最简单的解决方案，并且只在需要时增加复杂性。这可能意味着根本不构建代理系统。代理系统经常以延迟和成本换取更好的任务性能，您应该考虑这种权衡何时有意义。

当需要更多的复杂性时，工作流为定义良好的任务提供了可预测性和一致性，而当大规模需要灵活性和模型驱动的决策时，代理是更好的选择。然而，对于许多应用程序来说，使用检索和上下文示例优化单个大语言模型调用通常就足够了。

##何时以及如何使用框架

有许多框架使Agent系统更容易实现，包括：

  * The [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview); 
  * [Strands Agents SDK by AWS](https://strandsagents.com/latest/);
  * [Rivet](https://rivet.ironcladapp.com/), a drag and drop GUI LLM workflow builder; and 
  * [Vellum](https://www.vellum.ai/), another GUI tool for building and testing complex workflows.

这些框架通过简化标准的低级任务，如调用大语言模型、定义和解析工具以及将调用链接在一起，使入门变得容易。然而，它们通常会创建额外的抽象层，从而掩盖底层的提示和响应，从而使它们更难调试。当更简单的设置就足够了时，它们也会增加复杂性。

我们建议开发人员从直接使用大语言模型API开始：许多模式可以在几行代码中实现。如果您确实使用框架，请确保您理解底层代码。对引擎盖下的东西的不正确假设是客户错误的常见来源。

See our [cookbook](https://platform.claude.com/cookbook/patterns-agents-basic-workflows) for some sample implementations.

##构建块、工作流和代理

在本节中，我们将探索我们在生产中看到的代理系统的常见模式。我们将从我们的基础构建块——增强大语言模型——开始，逐步增加复杂性，从简单的组合工作流到自主代理。

###积木：增强型大语言模型

代理系统的基本构建模块是一个大语言模型，通过检索、工具和记忆等增强功能得到增强。我们当前的模型可以积极地使用这些功能——生成自己的搜索查询，选择适当的工具，并确定要保留哪些信息。

Image: image (https://www-cdn.anthropic.com/images/4zrzovbb/website/d3083d3f40bb2b6f477901cc9a240738d3dd1371-2401x1000.png)The augmented LLM

We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol), which allows developers to integrate with a growing ecosystem of third-party tools with a simple [client implementation](https://modelcontextprotocol.io/tutorials/building-a-client#building-mcp-clients).

在本文的剩余部分，我们将假设大语言模型的每个电话都可以访问这些增强的功能。

###工作流程：提示链接

提示链接将任务分解为一系列步骤，其中每个大语言模型调用都处理前一个调用的输出。您可以在任何中间步骤上添加程序化检查（参见下图中的“门”），以确保流程仍在正轨上。

Image: image (https://www-cdn.anthropic.com/images/4zrzovbb/website/7418719e3dab222dccb379b8879e1dc08ad34c78-2401x1000.png)The prompt chaining workflow

**何时使用此工作流：**此工作流非常适合任务可以轻松、干净地分解为固定子任务的情况。主要目标是通过使每个大语言模型调用变得更容易，来权衡延迟以获得更高的准确性。

**提示链接有用的示例：**

*生成营销文案，然后将其翻译成不同的语言。
*编写文档大纲，检查大纲是否符合某些标准，然后根据大纲编写文档。

###工作流程：路由

路由对输入进行分类，并将其定向到专门的后续任务。此工作流允许分离关注点，并构建更专业的提示。如果没有此工作流，针对一种输入进行优化可能会损害其他输入的性能。

Image: image (https://www-cdn.anthropic.com/images/4zrzovbb/website/5c0c0e9fe4def0b584c04d37849941da55e5e71c-2401x1000.png)The routing workflow

**何时使用此工作流：**路由非常适用于复杂任务，其中存在可以更好地单独处理的不同类别，并且可以通过大语言模型或更传统的分类模型/算法准确地处理分类。

**路由有用的示例：**

*将不同类型的客户服务查询（一般问题、退款请求、技术支持）导向不同的下游流程、提示和工具。
*将简单/常见问题路由到Claude Haiku 4.5等更小、更具成本效益的模型，将困难/不寻常的问题路由到Claude Sonnet 4.5等功能更强大的模型，以优化最佳性能。

###工作流：并行

大语言模型有时可以同时处理一项任务，并以编程方式聚合其输出。这个工作流程，即并行化，体现在两个关键的变体中：

***分段**：将任务分解成并行运行的独立子任务。
***投票：**多次运行同一任务以获得不同的输出。

Image: image (https://www-cdn.anthropic.com/images/4zrzovbb/website/406bb032ca007fd1624f261af717d70e6ca86286-2401x1000.png)The parallelization workflow

**何时使用此工作流：**当划分的子任务可以并行化以提高速度时，或者当需要多个视角或尝试以获得更高置信度的结果时，并行化是有效的。对于具有多个考虑因素的复杂任务，当每个考虑因素都由单独的大语言模型调用处理时，大语言模型通常会表现得更好，从而可以将注意力集中在每个特定方面。

**并行化有用的示例：**

***切片**：
*实现护栏，其中一个模型实例处理用户查询，而另一个模型实例筛选不适当的内容或请求。这往往比让同一个大语言模型呼叫处理护栏和核心响应表现更好。
*用于评估大语言模型性能的自动评估，其中每个大语言模型调用在给定提示下评估模型性能的不同方面。
***投票**：
*审查一段代码的漏洞，其中几个不同的提示检查并标记代码，如果他们发现问题。
*评估给定内容是否不合适，多个提示评估不同方面或要求不同投票阈值以平衡误报和误报。

###工作流：Orchestrator-workers

在orchestrator-workers工作流中，中央大语言模型动态地分解任务，将它们委托给workers大语言模型，并综合它们的结果。

Image: image (https://www-cdn.anthropic.com/images/4zrzovbb/website/8985fc683fae4780fb34eab1365ab78c7e51bc8e-2401x1000.png)The orchestrator-workers workflow

**何时使用此工作流：**此工作流非常适合无法预测所需子任务的复杂任务（例如，在编码中，需要更改的文件数量以及每个文件中更改的性质可能取决于任务）。尽管它在拓扑上是相似的，但与并行化的关键区别在于它的灵活性——子任务不是预定义的，而是由编排器基于特定输入确定的。

**orchestrator-workers有用的示例：**

*每次对多个文件进行复杂更改的编码产品。
*涉及从多个来源收集和分析信息以寻找可能的相关信息的搜索任务。

###工作流程：Evaluator-optimizer

在评估器-优化器工作流中，一个大语言模型调用生成响应，而另一个调用在循环中提供评估和反馈。

Image: image (https://www-cdn.anthropic.com/images/4zrzovbb/website/14f51e6406ccb29e695da48b17017e899a6119c7-2401x1000.png)The evaluator-optimizer workflow

**何时使用此工作流：**当我们有明确的评估标准时，以及当迭代细化提供可测量的价值时，此工作流尤其有效。良好契合的两个标志是，首先，当人类表达他们的反馈时，大语言模型反应可以明显改善；第二，大语言模型可以提供这样的反馈。这类似于人类作者在制作精美文档时可能经历的迭代写作过程。

**使用evaluator-optimizer的示例：**

*在文学翻译中，译者大语言模型最初可能无法捕捉到细微差别，但评价者大语言模型可以提供有用的评论。
*需要多轮搜索和分析以收集全面信息的复杂搜索任务，由评估员决定是否需要进一步搜索。

###代理

随着大语言模型在关键能力（理解复杂输入、参与推理和规划、可靠地使用工具以及从错误中恢复）方面的成熟，代理正在生产中出现。代理通过来自人类用户的命令或与人类用户的交互式讨论开始他们的工作。一旦任务明确，代理独立计划和操作，潜在地返回给人类以获得进一步的信息或判断。在执行过程中，对于代理来说，在每个步骤（如工具调用结果或代码执行）从环境中获得“基本事实”以评估其进度是至关重要的。然后，代理可以在检查点或遇到拦截器时暂停以获得人工反馈。任务通常在完成后终止，但通常包含停止条件（如最大迭代次数）来保持控制。

代理可以处理复杂的任务，但它们的实现通常很简单。她们通常只是大语言模型，在循环中使用基于环境反馈的工具。因此，清晰、深思熟虑地设计工具集及其文档至关重要。我们在附录2（“快速设计您的工具”）中详细介绍了工具开发的最佳实践。

Image: image (https://www-cdn.anthropic.com/images/4zrzovbb/website/58d9f10c985c4eb5d53798dea315f7bb5ab6249e-2401x1000.png)Autonomous agent

**何时使用代理：**代理可用于难以或不可能预测所需步骤数以及无法硬编码固定路径的开放式问题。大语言模型可能会运行很多回合，你必须对它的决策有一定程度的信任。代理的自主性使其成为在可信环境中扩展任务的理想选择。

代理的自主性质意味着更高的成本和复合错误的可能性。我们建议在沙盒环境中进行广泛的测试，并使用适当的护栏。

**试剂有用的实例：**

以下示例来自我们自己的实现：

  * A coding Agent to resolve [SWE-bench tasks](https://www.anthropic.com/research/swe-bench-sonnet), which involve edits to many files based on a task description;
  * Our [“computer use” reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo), where Claude uses a computer to accomplish tasks.

Image: image (https://www-cdn.anthropic.com/images/4zrzovbb/website/4b9a1f4eb63d5962a6e1746ac26bbc857cf3474f-2400x1666.png)High-level flow of a coding agent

##组合和定制这些模式

这些构建模块不是规定性的。它们是开发人员可以塑造和组合以适应不同用例的常见模式。与任何大语言模型特性一样，成功的关键是衡量性能和迭代实现。重复一遍：您应该考虑添加complexity_only，当它明显改善结果时。

##总结

大语言模型领域的成功并不在于构建最复杂的系统。它是关于为您的需求构建_right_system。从简单的提示开始，用综合评估对其进行优化，只有在更简单的解决方案不足时才添加多步代理系统。

在实现Agent时，我们尽量遵循三个核心原则：

1.在您的代理设计中保持**简单**。
2.通过明确显示代理的计划步骤来优先考虑**透明度**。
3.通过彻底的工具**文档和测试**精心制作您的代理-计算机接口（ACI）。

框架可以帮助您快速入门，但是当您转向生产时，不要犹豫减少抽象层并使用基本组件进行构建。通过遵循这些原则，您可以创建不仅功能强大，而且可靠、可维护并受到用户信任的代理。

###确认

作者：Erik S.和Barry Zhang。这项工作借鉴了我们在Anthropic建立代理的经验以及客户分享的宝贵见解，对此我们深表感谢。

##附录1：实践中的代理

我们与客户的合作揭示了人工智能代理的两个特别有前途的应用，展示了上面讨论的模式的实用价值。这两个应用程序都说明了代理如何为需要对话和行动的任务增加最大价值，具有明确的成功标准，启用反馈循环，并集成有意义的人工监督。

###A。客户支持

客户支持通过工具集成将熟悉的聊天机器人界面与增强的功能相结合。这自然适合更多开放式代理，因为：

*支持交互自然地遵循对话流程，同时需要访问外部信息和操作；
*可以集成工具来拉取客户数据、订单历史和知识库文章；
*可以通过编程方式处理诸如签发退款或更新机票等操作；和
*通过用户定义的解决方案可以清楚地衡量成功。

几家公司已经通过基于使用的定价模型证明了这种方法的可行性，该模型仅对成功的解决方案收费，显示出对其代理有效性的信心。

###B.编码剂

软件开发领域已经显示出大语言模型功能的巨大潜力，能力从代码完成发展到自主解决问题。药剂特别有效，因为：

*代码解决方案可通过自动化测试进行验证；
*代理可以使用测试结果作为反馈对解决方案进行迭代；
*问题空间定义明确且结构化；和
*输出质量可以客观测量。

In our own implementation, agents can now solve real GitHub issues in the [SWE-bench Verified](https://www.anthropic.com/research/swe-bench-sonnet) benchmark based on the pull request description alone. However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements.

##附录2：提示设计您的工具

No matter which agentic system you're building, tools will likely be an important part of your agent. [Tools](https://www.anthropic.com/news/tool-use-ga) enable Claude to interact with external services and APIs by specifying their exact structure and definition in our API. When Claude responds, it will include a [tool use block](https://docs.anthropic.com/en/docs/build-with-claude/tool-use#example-api-response-with-a-tool-use-content-block) in the API response if it plans to invoke a tool. Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts. In this brief appendix, we describe how to prompt engineer your tools.

通常有几种方法可以指定同一个操作。例如，您可以通过写入diff或重写整个文件来指定文件编辑。对于结构化输出，您可以在markdown或JSON中返回代码。在软件工程中，像这样的差异是表面的，可以无损地从一个到另一个转换。然而，对于大语言模型来说，有些格式比其他格式更难编写。编写diff需要在编写新代码之前知道块头中有多少行发生了变化。在JSON内部编写代码（与markdown相比）需要额外转义换行符和引号。

我们对决定工具格式的建议如下：

*在模型把自己写进角落之前，给它足够的标记来“思考”。
*保持格式接近模型在互联网上看到的文本中自然出现的内容。
*确保没有格式化“开销”，例如必须保持数千行代码的准确计数，或者对它编写的任何代码进行字符串转义。

一个经验法则是考虑在人机界面（HCI）上投入了多少精力，并计划投入同样多的精力来创建良好的代理计算机界面（ACI）。以下是关于如何做到这一点的一些想法：

*设身处地为模特着想。根据描述和参数，如何使用这个工具是否显而易见，或者您需要仔细考虑？如果是这样，那么模型可能也是如此。一个好的工具定义通常包括示例用法、边缘案例、输入格式要求以及与其他工具的明确界限。
*如何更改参数名称或描述以使事情更明显？把这想象成为你团队中的初级开发人员编写一个很棒的文档字符串。这在使用许多类似工具时尤其重要。
  * Test how the model uses your tools: Run many example inputs in our [workbench](https://console.anthropic.com/workbench) to see what mistakes the model makes, and iterate.
  * [Poka-yoke](https://en.wikipedia.org/wiki/Poka-yoke) your tools. Change the arguments so that it is harder to make mistakes.

While building our agent for [SWE-bench](https://www.anthropic.com/research/swe-bench-sonnet), we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly.
