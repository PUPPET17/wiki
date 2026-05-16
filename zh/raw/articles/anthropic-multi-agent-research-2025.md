---
source_url: https://www.anthropic.com/engineering/built-multi-agent-research-system
fetched_url: https://www.anthropic.com/engineering/built-multi-agent-research-system
source_type: blog
author: Anthropic
source_date: 2025-06-13
ingested: 2026-05-14
sha256: 48a6617e1b55db7bfe7c79a5d51f3be2aefc13432a75428998fc09a184b96841
raw_preservation: full_html_article_text_candidate
extraction_method: readability_lxml_html2text
html_bytes: 173053
parsed_chars: 26925
---

#我们如何建立我们的多智能体研究系统

##源元数据

-来源网址：https://www.anthropic.com/engineering/built-multi-agent-research-system
-获取的网址：https://www.anthropic.com/engineering/built-multi-agent-research-system
-来源类型：博客
-作者：Anthropic
-来源日期：2025-06-13
-摄入日期：2026-05-14
-可靠性：高
-原始保存状态：full_html_article_text_candidate
-提取方式：readability_lxml_html2text

##解析的源文本

Claude now has [Research capabilities](https://www.anthropic.com/news/research) that allow it to search across the web, Google Workspace, and any integrations to accomplish complex tasks.

这个多智能体系统从原型到生产的旅程教会了我们关于系统架构、工具设计和即时工程的重要课程。多智能体系统由多个智能体（大语言模型在循环中自主使用工具）一起工作组成。我们的研究功能涉及一个基于用户查询计划研究过程的代理，然后使用工具创建同时搜索信息的并行代理。具有多个代理的系统在代理协调、评估和可靠性方面引入了新的挑战。

这篇文章分解了对我们有效的原则——我们希望你会发现它们在构建你自己的多智能体系统时有用。

###多智能体系统的好处

研究工作涉及开放式问题，很难提前预测所需的步骤。你不能硬编码一个固定的路径来探索复杂的主题，因为这个过程本质上是动态的和依赖于路径的。当人们进行研究时，他们倾向于根据调查过程中出现的线索，根据发现不断更新他们的方法。

这种不可预测性使得人工智能代理特别适合研究任务。随着调查的展开，研究需要灵活地转向或探索切向的联系。该模型必须自主运行许多回合，根据中间发现决定追求哪个方向。线性的一次性管道无法处理这些任务。

搜索的本质是压缩：从庞大的语料库中提取见解。子代理通过与它们自己的上下文窗口并行操作来促进压缩，在为主要研究代理压缩最重要的令牌之前同时探索问题的不同方面。每个子代理还提供关注点的分离——不同的工具、提示和探索轨迹——这减少了路径依赖，并实现了彻底、独立的调查。

一旦智能达到阈值，多智能体系统就成为扩展性能的重要方式。例如，尽管在过去的10万年里，人类个体变得更加聪明，但由于我们的集体智慧和协调能力，人类社会在信息时代变得更加强大。即使是一般智能的代理在作为个体操作时也面临限制；代理团队可以完成更多的事情。

我们的内部评估表明，多智能体研究系统尤其擅长于涉及同时追求多个独立方向的广度优先查询。我们发现，在我们的内部研究评估中，以Claude Opus 4为主导代理和Claude Sonnet 4子代理的多代理系统比单代理Claude Opus 4的性能高出90.2%。例如，当被要求识别信息技术标准普尔500公司的所有董事会成员时，多代理系统通过将其分解为子代理的任务来找到正确答案，而单代理系统通过缓慢的顺序搜索无法找到答案。

Multi-agent systems work mainly because they help spend enough tokens to solve the problem. In our analysis, three factors explained 95% of the performance variance in the [BrowseComp](https://openai.com/index/browsecomp/) evaluation (which tests the ability of browsing agents to locate hard-to-find information). We found that token usage by itself explains 80% of the variance, with the number of tool calls and the model choice as the two other explanatory factors. This finding validates our architecture that distributes work across agents with separate context windows to add more capacity for parallel reasoning. The latest Claude models act as large efficiency multipliers on token use, as upgrading to Claude Sonnet 4 is a larger performance gain than doubling the token budget on Claude Sonnet 3.7. Multi-agent architectures effectively scale token usage for tasks that exceed the limits of single agents.

有一个缺点：在实践中，这些架构会快速烧毁令牌。在我们的数据中，代理通常使用的令牌比聊天交互多约4倍，多代理系统使用的令牌比聊天多约15倍。为了经济可行性，多智能体系统需要任务的价值足够高以支付增加的性能。此外，一些要求所有代理共享相同上下文或涉及代理之间的许多依赖关系的域不太适合当今的多代理系统。例如，大多数编码任务涉及的真正可并行化任务比研究任务少，大语言模型代理还不擅长实时协调和委托给其他代理。我们发现，多智能体系统擅长于涉及大量并行化、超出单个上下文窗口的信息以及与众多复杂工具接口的有价值的任务。

###研究架构概述

我们的研究系统使用具有协调器-工作器模式的多代理架构，其中一个领导代理协调过程，同时委托给并行操作的专门子代理。

Image: image (https://www-cdn.anthropic.com/images/4zrzovbb/website/1198befc0b33726c45692ac40f764022f4de1bf2-4584x2579.png)The multi-agent architecture in action: user queries flow through a lead agent that creates specialized subagents to search for different aspects in parallel.

当用户提交查询时，引导代理会对其进行分析，制定策略，并生成子代理来同时探索不同的方面。如上图所示，子代理充当智能过滤器，通过迭代使用搜索工具来收集信息，在本例中是关于2025年的AI代理公司，然后将公司列表返回给牵头代理，以便它可以编译最终答案。

使用检索增强生成（RAG）的传统方法使用静态检索。也就是说，它们获取与输入查询最相似的一组块，并使用这些块生成响应。相比之下，我们的架构使用多步骤搜索，动态查找相关信息，适应新的发现，并分析结果以制定高质量的答案。

Image: image (https://www-cdn.anthropic.com/images/4zrzovbb/website/3bde53c9578d74f6e05c3e515e20b910c5a8c20a-4584x4584.png)Process diagram showing the complete workflow of our multi-agent Research system. When a user submits a query, the system creates a LeadResearcher agent that enters an iterative research process. The LeadResearcher begins by thinking through the approach and saving its plan to Memory to persist the context, since if the context window exceeds 200,000 tokens it will be truncated and it is important to retain the plan. It then creates specialized Subagents (two are shown here, but it can be any number) with specific research tasks. Each Subagent independently performs web searches, evaluates tool results using [interleaved thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking), and returns findings to the LeadResearcher. The LeadResearcher synthesizes these results and decides whether more research is needed—if so, it can create additional subagents or refine its strategy. Once sufficient information is gathered, the system exits the research loop and passes all findings to a CitationAgent, which processes the documents and research report to identify specific locations for citations. This ensures all claims are properly attributed to their sources. The final research results, complete with citations, are then returned to the user.

###研究代理的即时工程和评估

多智能体系统与单智能体系统有关键区别，包括协调复杂性的快速增长。早期的代理犯了一些错误，比如为简单的查询生成50个子代理，无休止地在网络上搜索不存在的资源，以及用过多的更新分散彼此的注意力。由于每个代理都受提示控制，提示工程是我们改进这些行为的主要杠杆。以下是我们了解到的提示代理的一些原则：

  1. **Think like your agents.** To iterate on prompts, you must understand their effects. To help us do this, we built simulations using our [Console](https://console.anthropic.com/) with the exact prompts and tools from our system, then watched agents work step-by-step. This immediately revealed failure modes: agents continuing when they already had sufficient results, using overly verbose search queries, or selecting incorrect tools. Effective prompting relies on developing an accurate mental model of the agent, which can make the most impactful changes obvious.
2.**教orchestrator如何委派**在我们的系统中，lead agent将查询分解为子任务，并将其描述给子agent。每个子代理都需要一个目标、一种输出格式、关于要使用的工具和源的指导以及清晰的任务边界。如果没有详细的任务描述，代理会重复工作、留下空白或找不到必要的信息。我们首先允许牵头代理给出简单、简短的指令，如“研究半导体短缺”，但发现这些指令往往非常模糊，以至于子代理会误解任务或执行与其他代理完全相同的搜索。例如，一个子代理探索了2021年的汽车芯片危机，而另外两个子代理重复了调查当前2025年供应链的工作，没有有效的分工。
3.**缩放查询复杂性的努力。**代理很难判断不同任务的适当努力，因此我们在提示中嵌入了缩放规则。简单的事实发现只需要1个代理进行3-10次工具调用，直接比较可能需要2-4个子代理，每个子代理进行10-15次调用，而复杂的研究可能使用10个以上的子代理，职责分工明确。这些明确的指导方针有助于lead agent有效地分配资源，并防止在简单查询中过度投资，这在我们早期版本中是一种常见的失败模式。
  4. **Tool design and selection are critical.** Agent-tool interfaces are as critical as human-computer interfaces. Using the right tool is efficient—often, it’s strictly necessary. For instance, an agent searching the web for context that only exists in Slack is doomed from the start. With [MCP servers](https://modelcontextprotocol.io/introduction) that give the model access to external tools, this problem compounds, as agents encounter unseen tools with descriptions of wildly varying quality. We gave our agents explicit heuristics: for example, examine all available tools first, match tool usage to user intent, search the web for broad external exploration, or prefer specialized tools over generic ones. Bad tool descriptions can send agents down completely wrong paths, so each tool needs a distinct purpose and a clear description.
5、**让代理商提升自己**。我们发现克劳德4模型可以成为优秀的提示工程师。当得到提示和故障模式时，他们能够诊断代理失败的原因并提出改进建议。我们甚至创建了一个工具——测试代理——当给定一个有缺陷的MCP工具时，它会尝试使用该工具，然后重写工具描述以避免失败。通过对该工具进行数十次测试，该代理发现了关键的细微差别和错误。这种改进工具人体工程学的过程使使用新描述的未来代理的任务完成时间减少了40%，因为他们能够避免大多数错误。
6.**从广泛开始，然后缩小范围。**搜索策略应该反映专家的人类研究：在深入细节之前先探索景观。代理通常默认为返回很少结果的过长、特定的查询。我们通过提示代理从简短、广泛的查询开始，评估可用的内容，然后逐渐缩小关注点来抵消这种趋势。
  7. **Guide the thinking process.** [Extended thinking mode](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking), which leads Claude to output additional tokens in a visible thinking process, can serve as a controllable scratchpad. The lead agent uses thinking to plan its approach, assessing which tools fit the task, determining query complexity and subagent count, and defining each subagent’s role. Our testing showed that extended thinking improved instruction-following, reasoning, and efficiency. Subagents also plan, then use [interleaved thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking) after tool results to evaluate quality, identify gaps, and refine their next query. This makes subagents more effective in adapting to any task.
8.**并行工具调用转换速度和性能**复杂的研究任务自然涉及探索许多来源。我们早期的特工执行顺序搜索，速度慢得令人痛苦。为了提高速度，我们引入了两种并行化：（1）lead agent并行而不是串行地旋转3-5个子agent；（2）子代理并行使用3+工具。这些变化将复杂查询的研究时间缩短了90%，允许研究在几分钟而不是几小时内完成更多工作，同时覆盖比其他系统更多的信息。

我们的提示策略侧重于灌输良好的启发式方法，而不是僵化的规则。我们研究了熟练的人类如何处理研究任务，并将这些策略编码在我们的提示中——如将困难的问题分解成更小的任务，仔细评估来源的质量，根据新信息调整搜索方法，以及识别何时关注深度（详细调查一个主题）与广度（并行探索许多主题）等策略。我们还通过设置明确的护栏来防止药物失控，从而主动减轻意外的副作用。最后，我们关注了一个具有可观察性和测试用例的快速迭代循环。

###药剂的有效性评价

良好的评估对于构建可靠的人工智能应用程序至关重要，代理也不例外。然而，评估多智能体系统提出了独特的挑战。传统的评估通常假设AI每次都遵循相同的步骤：给定输入X，系统应该遵循路径Y来产生输出Z。但是多智能体系统不是这样工作的。即使起点相同，代理也可能采取完全不同的有效路径来达到他们的目标。一个代理可能搜索三个源，而另一个搜索十个源，或者他们可能使用不同的工具来找到相同的答案。因为我们并不总是知道正确的步骤是什么，所以我们通常不能只检查代理是否遵循了我们事先规定的“正确”步骤。相反，我们需要灵活的评估方法来判断代理是否实现了正确的结果，同时也遵循了合理的过程。

**立即开始小样本评估**。在早期的代理开发中，变化往往会产生巨大的影响，因为有大量唾手可得的果实。迅速调整可能会将成功率从30%提高到80%。由于效果大小如此之大，您只需几个测试用例就可以发现变化。我们从一组大约20个表示真实使用模式的查询开始。测试这些查询通常可以让我们清楚地看到变化的影响。我们经常听到AI开发团队延迟创建评估，因为他们认为只有拥有数百个测试用例的大型评估才有用。然而，最好马上用几个例子开始小规模测试，而不是等到你可以建立更彻底的评估。

**如果做得好，大语言模型作为法官的评估量表。**研究成果很难以编程方式进行评估，因为它们是自由形式的文本，很少有单一的正确答案。大语言模型是分级输出的天然选择。我们使用了一个大语言模型法官，根据一个标题中的标准评估每个输出：事实准确性（声明与来源匹配吗？）、引用准确性（引用的来源与声明相符吗？）、完整性（是否涵盖了所有要求的方面？）、来源质量（它是否使用了一手资料而不是低质量的二手资料？），以及工具效率（它是否使用了正确的工具合理的次数？）.我们用多个法官来评估每个组件，但发现一个大语言模型呼叫与一个提示输出0.0-1.0的分数和一个通过-失败等级是最一致的，与人类的判断一致。当eval测试用例有明确答案时，这种方法尤其有效，我们可以使用大语言模型判断来简单地检查答案是否正确（即它是否准确地列出了研发预算前3名的制药公司？）。使用大语言模型作为法官使我们能够可扩展地评估数百个输出。

**人工评估捕捉自动化遗漏的内容。**人员测试代理发现评估遗漏的边缘案例。这些包括对不寻常查询、系统故障或微妙的来源选择偏差的幻觉答案。在我们的案例中，人类测试人员注意到，我们的早期代理始终选择SEO优化的内容农场，而不是权威但排名不太高的来源，如学术pdf或个人博客。在我们的提示中添加源质量试探有助于解决这个问题。即使在自动化评估的世界里，手动测试仍然是必不可少的。

Multi-agent systems have emergent behaviors, which arise without specific programming. For instance, small changes to the lead agent can unpredictably change how subagents behave. Success requires understanding interaction patterns, not just individual agent behavior. Therefore, the best prompts for these agents are not just strict instructions, but frameworks for collaboration that define the division of labor, problem-solving approaches, and effort budgets. Getting this right relies on careful prompting and tool design, solid heuristics, observability, and tight feedback loops.**** See the [open-source prompts in our Cookbook](https://platform.claude.com/cookbook/patterns-agents-basic-workflows) for example prompts from our system.

###生产可靠性和工程挑战

在传统软件中，bug可能会破坏功能、降低性能或导致停机。在代理系统中，微小的变化会级联成大的行为变化，这使得为必须在长时间运行的进程中保持状态的复杂代理编写代码变得非常困难。

**代理是有状态的，错误是复合的。**代理可以长时间运行，在许多工具调用中保持状态。这意味着我们需要持久地执行代码并处理过程中的错误。如果没有有效的缓解措施，轻微的系统故障对代理来说可能是灾难性的。当错误发生时，我们不能从头开始重启：重启对用户来说代价高昂且令人沮丧。相反，我们构建了可以从错误发生时代理所在的位置恢复的系统。我们还使用模型的智能来优雅地处理问题：例如，让代理知道工具何时出现故障，并让它进行调整，效果出奇地好。我们将构建在Claude上的人工智能代理的适应性与重试逻辑和常规检查点等确定性安全措施相结合。

**调试受益于新方法。**代理做出动态决策，并且在运行之间是不确定的，即使提示相同。这使得调试更加困难。例如，用户会报告代理“没有找到明显的信息”，但我们不明白为什么。代理是否使用了错误的搜索查询？选择不良来源？击中工具故障？添加完整的生产跟踪使我们能够诊断代理失败的原因并系统地修复问题。除了标准的可观察性，我们还监控代理决策模式和交互结构——所有这些都不监控单个对话的内容，以维护用户隐私。这种高级可观察性帮助我们诊断根本原因、发现意外行为并修复常见故障。

**Deployment needs careful coordination.** Agent systems are highly stateful webs of prompts, tools, and execution logic that run almost continuously. This means that whenever we deploy updates, agents might be anywhere in their process. We therefore need to prevent our well-meaning code changes from breaking existing agents. We can’t update every agent to the new version at the same time. Instead, we use [rainbow deployments](https://brandon.dimcheff.com/2018/02/rainbow-deploys-with-kubernetes/) to avoid disrupting running agents, by gradually shifting traffic from old to new versions while keeping both running simultaneously.

**同步执行会产生瓶颈。**目前，我们的主代理同步执行子代理，等待每组子代理完成后再继续。这简化了协调，但在代理之间的信息流中产生了瓶颈。例如，主代理不能引导子代理，子代理不能协调，并且在等待单个子代理完成搜索时，整个系统可能会被阻塞。异步执行将实现额外的并行性：代理并发工作，并在需要时创建新的子代理。但是这种异步性增加了跨子代理的结果协调、状态一致性和错误传播方面的挑战。由于模型可以处理更长、更复杂的研究任务，我们预计性能的提高将证明复杂性是合理的。

###结论

在构建AI代理时，最后一英里往往成为旅程的大部分。在开发人员机器上工作的代码库需要大量的工程才能成为可靠的生产系统。代理系统中错误的复合性质意味着传统软件的小问题可能会使代理完全脱轨。一步失败可能会导致代理探索完全不同的轨迹，导致不可预测的结果。由于这篇文章中描述的所有原因，原型和生产之间的差距通常比预期的要大。

尽管存在这些挑战，多智能体系统已被证明对于开放式研究任务是有价值的。用户表示，Claude帮助他们找到了他们没有考虑过的商业机会，导航复杂的医疗保健选项，解决了棘手的技术错误，并通过发现他们不会单独找到的研究联系节省了长达数天的工作。通过仔细的工程设计、全面的测试、注重细节的提示和工具设计、稳健的操作实践以及对当前代理能力有深刻理解的研究、产品和工程团队之间的紧密协作，多代理研究系统可以大规模可靠地运行。我们已经看到这些系统改变了人们解决复杂问题的方式。

Image: image (https://www-cdn.anthropic.com/images/4zrzovbb/website/09a90e0aca54859553e93c18683e7fd33ff16d4c-2654x2148.png)A [Clio](https://www.anthropic.com/research/clio) embedding plot showing the most common ways people are using the Research feature today. The top use case categories are developing software systems across specialized domains (10%), develop and optimize professional and technical content (8%), develop business growth and revenue generation strategies (8%), assist with academic research and educational material development (7%), and research and verify information about people, places, or organizations (5%).

###确认

作者：Jeremy Hadfield、Barry Zhang、Kenneth Lien、Florian朔尔茨、Jeremy Fox和Daniel Ford。这项工作反映了Anthropic的几个团队的集体努力，他们使这项研究成为可能。特别感谢Anthropic apps工程团队，他们的奉献精神将这个复杂的多智能体系统投入生产。我们也感谢早期用户的出色反馈。

##附录

下面是多智能体系统的一些额外的杂项提示。

**对在许多回合中改变状态的代理的最终状态评估。**评估跨多回合对话修改持久状态的代理提出了独特的挑战。与只读研究任务不同，每个操作都可以改变后续步骤的环境，从而创建传统评估方法难以处理的依赖性。我们发现专注于最终状态评估而不是逐次分析是成功的。不要判断代理是否遵循了特定的过程，而是评估它是否达到了正确的最终状态。这种方法承认代理可以找到实现同一目标的替代路径，同时仍然确保他们交付预期的结果。对于复杂的工作流，将评估分解为应该发生特定状态更改的离散检查点，而不是尝试验证每个中间步骤。

**长期对话管理。**生产代理经常参与跨越数百个回合的对话，需要仔细的上下文管理策略。随着对话的扩展，标准上下文窗口变得不够，需要智能压缩和记忆机制。我们实现了一些模式，在这些模式中，代理总结已完成的工作阶段，并在继续执行新任务之前将重要信息存储在外部存储器中。当上下文限制接近时，代理可以产生具有干净上下文的新子代理，同时通过仔细的切换保持连续性。此外，他们可以从他们的内存中检索存储的上下文，如研究计划，而不是在达到上下文限制时丢失以前的工作。这种分布式方法防止上下文溢出，同时保持扩展交互中的对话一致性。

**子代理输出到文件系统，以最大限度地减少“电话游戏”。**对于某些类型的结果，直接子代理输出可以绕过主协调器，从而提高保真度和性能。不要要求子代理通过领导代理来传达一切，而是实现工件系统，在工件系统中，专门的代理可以创建独立持久的输出。子代理调用工具将其工作存储在外部系统中，然后将轻量级引用传递回协调器。这防止了多阶段处理期间的信息丢失，并减少了通过会话历史复制大输出的令牌开销。该模式特别适用于结构化输出，如代码、报告或数据可视化，其中子代理的专用提示比通过通用协调器过滤产生更好的结果。
