---
source_url: https://github.com/mem0ai/mem0
fetched_url: https://raw.githubusercontent.com/mem0ai/mem0/main/README.md
source_type: github repo
author: mem0ai/mem0 maintainers
source_date: 2023-06-20
ingested: 2026-05-15
sha256: 8dc335626a13035b7031d016e068249b31e67413a1f4dd118185f933973b778a
raw_preservation: full_github_readme_text
extraction_method: github_repo_api_and_raw_readme
github_repo: mem0ai/mem0
stars: 55709
open_issues: 348
---

#GitHub存储库：mem0ai/mem0

##源元数据

-来源网址：https://github.com/mem0ai/mem0
-获取的URL：https://raw.githubusercontent.com/mem0ai/mem0/main/README.md
-来源类型：github repo
-作者：mem0ai/mem0维护者
-来源日期：2023-06-20
-摄入日期：2026-05-15
-可靠性：高
-原始保存状态：full_github_readme_text
-提取方式：github_repo_api_and_raw_readme

##解析的源文本

#存储库元数据：mem0ai/mem0

-GitHub网址：https://github.com/mem0ai/mem0
-描述：AI代理的通用内存层
-星星：55709
-叉子：6341
-未决问题：348
-创建时间：2023-06-20T08：58：36Z
-更新日期：2026-05-14T17：42：54Z
-许可证：Apache-2.0

##README.md

<p align="center">
<a href="https://github.com/mem0ai/mem0">
<img src="docs/images/banner-sm.png"width="800px"alt="Mem0-个性化AI的内存层">
</a>
</p>
<p align="center"style="display：flex;justify-content：center;gap：20px;align-items：center;">
<a href="https://trendshift.io/repositories/11194"target="blank">
<img src="https://trendshift.io/api/badge/repositories/11194"alt="mem0ai%2Fmem0|trendshift"width="250"height="55"/>
</a>
</p>

<p align="center">
<a href="https://mem0.ai">了解更多</a>
·
<a href="https://mem0.dev/DiG">加入Discord</a>
·
<a href="https：//mem0.dev/demo">演示</a>
</p>

<p align="center">
<a href="https://mem0.dev/DiG">
<img src="https://img.shields.io/badge/discord-%235865F2.svg？&logo=discord&logoColor=white"alt="Mem0 Discord">
</a>
<a href="https://pepy.tech/project/mem0ai">
<img src="https://img.shields.io/pypi/dm/mem0ai"alt="mem0 pypi-downloads">
</a>
<a href="https://github.com/mem0ai/mem0">
<img src="https://img.shields.io/github/commit-activity/m/mem0ai/mem0？style=flat-square"alt="GitHub提交活动">
</a>
<a href="https://pypi.org/project/mem0ai"target="blank">
<img src="https://img.shields.io/pypi/v/mem0ai?color=%2334D058&label=pypi%20package"alt="Package version">
</a>
<a href="https://www.npmjs.com/package/mem0ai"target="blank">
<img src="https://img.shields.io/npm/v/mem0ai"alt="Npm package">
</a>
<a href="https://www.ycombinator.com/companies/mem0">
<img src="https://img.shields.io/badge/Y%20Combinator-S24-orange？style=flat-square"alt="Y Combinator S24">
</a>
</p>

<p align="center">
<a href="https://mem0.ai/research"><strong>📄基准测试Mem0的令牌高效内存算法→</strong></a>
</p>

##新内存算法（2026年4月）

|基准|旧|新|令牌|延迟p50|
|---|---|---|---|---|
|**火车头**|71.4|**91.6**|7.0 k|0.88 s|
|**LongMemEval**|67.8|**94.8**|6.8 K|1.09 s|
|**梁(1M)**|-|**64.1**|6.7 K|1.00 s|
|**梁(10M)**|-|**48.6**|6.9 K|1.05 S|

所有基准测试都运行在相同的生产代表模型堆栈上。单程检索（一次调用，无代理循环）。

**更改内容：**
-**单程仅添加提取**——一次大语言模型调用，无更新/删除。记忆积累；没有任何内容被覆盖。
-**代理生成的事实是一流的**--当代理确认一个动作时，该信息现在以相等的权重存储。
-**实体链接**-实体被提取、嵌入并跨存储器链接以增强检索。
-**多信号检索**-语义、BM25关键字和实体匹配并行评分并融合。
-**时间推理**--时间感知检索，对有关当前状态、过去事件和即将到来的计划的查询的正确日期实例进行排序。

See the [migration guide](https://docs.mem0.ai/migration/oss-v2-to-v3) for upgrade instructions. The [evaluation framework](https://github.com/mem0ai/memory-benchmarks) is open-sourced so anyone can reproduce the numbers.

##研究亮点
-**91.6 on LoCoMo**--+20分比上一个算法
-**94.8 longmemeval**--+27分，辅助记忆回忆+53.6
-**64.1 on BEAM(1M)**--1M令牌下的生产规模内存评估
- [Read the full paper](https://mem0.ai/research)

#简介

[Mem0](https://mem0.ai) ("mem-zero") enhances AI assistants and agents with an intelligent memory layer, enabling personalized AI interactions. It remembers user preferences, adapts to individual needs, and continuously learns over time—ideal for customer support chatbots, AI assistants, and autonomous systems.

###关键功能和用例

**核心能力：**
-**多级内存**：通过自适应个性化无缝保留用户、会话和代理状态
-**开发人员友好**：直观的API、跨平台SDK和完全托管的服务选项

**应用：**
-**人工智能助手**：一致、上下文丰富的对话
-**客户支持**：回忆过去的票证和用户历史以获得定制的帮助
-**医疗保健**：跟踪患者偏好和病史以获得个性化护理
-**生产力和游戏**：基于用户行为的自适应工作流程和环境

##🚀快速入门指南<a name="quickstart"></a>

>**代理模式-用于自动设置Mem0的AI代理。**运行`mem0 init-agent-agent-caller<your-name>--json`（在`pip install mem0-cli`或`npm install-g@mem0/cli`之后），将`<your-name>`替换为您的AI代理身份（例如`claude-code`、`cursor`、`codex`）。这在不到5秒的时间内创建了一个评估Mem0 API密钥——没有电子邮件，没有仪表板，没有动态口令。如果您忘记传递“-agent-caller”，请在init后运行“mem0 identify<your-name>”。立即在平台或MCP服务器上使用密钥。人类所有者可以在以后用“mem0 init-email<thir-email>”来声明所有权：记忆转移，相同的密钥继续工作，代理不会被中断。

||库|自托管服务器|云平台|
|---|---------|-------------------|----------------|
|**最适合**|测试、原型制作|在自己的基础架构上运行的团队|零操作生产使用|
| **Setup** | `pip install mem0ai` | `docker compose up` | Sign up at [app.mem0.ai](https://app.mem0.ai?utm_source=oss&utm_medium=readme) |
| **Dashboard** | -- | [Yes](https://docs.mem0.ai/open-source/setup) | Yes |
|**身份验证和API密钥**|--|是|是|
|**高级功能**|--|预告片|全部包含|

只是测试？使用图书馆。为团队建设？自托管。想要零操作？云。

###库（pip/npm）

```bash
pip install mem0ai
```

要使用BM25关键字匹配和实体提取增强的混合搜索，请安装NLP支持：

```bash
pip install mem0ai[nlp]
python -m spacy download en_core_web_sm
```

通过npm安装sdk：

```bash
npm install mem0ai
```

###自托管服务器

> **Note:** Self-hosted auth is on by default. Upgrading from a pre-auth build? Set `ADMIN_API_KEY`, register an admin through the wizard, or `AUTH_DISABLED=true` for local dev only. See [upgrade notes](https://docs.mem0.ai/open-source/setup#upgrade-notes).

```bash
# Recommended: one command — start the stack, create an admin, issue the first API key.
cd server && make bootstrap

# Manual: start the stack and finish setup via the browser wizard.
cd server && docker compose up -d    # http://localhost:3000
```

See the [self-hosted docs](https://docs.mem0.ai/open-source/overview) for configuration.

###云平台

1. Sign up on [Mem0 Platform](https://app.mem0.ai?utm_source=oss&utm_medium=readme)
2.通过SDK或API密钥嵌入内存层

##

从终端管理内存：

```bash
npm install -g @mem0/cli   # or: pip install mem0-cli

mem0 init
mem0 add "Prefers dark mode and vim keybindings" --user-id alice
mem0 search "What does Alice prefer?" --user-id alice
```

See the [CLI documentation](https://docs.mem0.ai/platform/cli) for the full command reference.

###特工技能

教你的AI编码助手（Claude Code、Codex、Cursor、Windsurf、OpenCode、OpenClaw和任何支持技能标准的工具）如何用Mem0构建。两类：

**参考技能-始终在线**（SDK知识加载到助手的上下文中）：

```bash
npx skills add https://github.com/mem0ai/mem0 --skill mem0
npx skills add https://github.com/mem0ai/mem0 --skill mem0-cli
npx skills add https://github.com/mem0ai/mem0 --skill mem0-vercel-ai-sdk
```

**管道技能-按需运行**（在现有存储库中执行端到端工作流）：

```bash
npx skills add https://github.com/mem0ai/mem0 --skill mem0-integrate
npx skills add https://github.com/mem0ai/mem0 --skill mem0-test-integration
```

Use `/mem0-integrate` to wire Mem0 into an existing repo via a test-first pipeline, then `/mem0-test-integration` to verify. See the [skills catalog](./skills/) or [Vibecoding with Mem0](https://docs.mem0.ai/vibecoding) for the full picture.

###基本用法

Mem0 requires an LLM to function, with `gpt-5-mini` from OpenAI as the default. However, it supports a variety of LLMs; for details, refer to our [Supported LLMs documentation](https://docs.mem0.ai/components/llms/overview).

Mem0 uses `text-embedding-3-small` from OpenAI as the default embedding model. For best results with hybrid search (semantic + keyword + entity boosting), we recommend using at least [Qwen 600M](https://huggingface.co/Alibaba-NLP/gte-Qwen2-1.5B-instruct) or a comparable embedding model. See [Supported Embeddings](https://docs.mem0.ai/components/embedders/overview) for configuration details.

第一步是实例化内存：

```python
from openai import OpenAI
from mem0 import Memory

openai_client = OpenAI()
memory = Memory()

def chat_with_memories(message: str, user_id: str = "default_user") -> str:
    # Retrieve relevant memories
    relevant_memories = memory.search(query=message, filters={"user_id": user_id}, top_k=3)
    memories_str = "\n".join(f"- {entry['memory']}" for entry in relevant_memories["results"])

    # Generate Assistant response
    system_prompt = f"You are a helpful AI. Answer the question based on query and memories.\nUser Memories:\n{memories_str}"
    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": message}]
    response = openai_client.chat.completions.create(model="gpt-5-mini", messages=messages)
    assistant_response = response.choices[0].message.content

    # Create new memories from the conversation
    messages.append({"role": "assistant", "content": assistant_response})
    memory.add(messages, user_id=user_id)

    return assistant_response

def main():
    print("Chat with AI (type 'exit' to quit)")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        print(f"AI: {chat_with_memories(user_input)}")

if __name__ == "__main__":
    main()
```

For detailed integration steps, see the [Quickstart](https://docs.mem0.ai/quickstart) and [API Reference](https://docs.mem0.ai/api-reference).

##🔗集成和演示

- **ChatGPT with Memory**: Personalized chat powered by Mem0 ([Live Demo](https://mem0.dev/demo))
- **Browser Extension**: Store memories across ChatGPT, Perplexity, and Claude ([Chrome Extension](https://chromewebstore.google.com/detail/onihkkbipkfeijkadecaafbgagkhglop?utm_source=item-share-cb))
- **Langgraph Support**: Build a customer bot with Langgraph + Mem0 ([Guide](https://docs.mem0.ai/integrations/langgraph))
- **CrewAI Integration**: Tailor CrewAI outputs with Mem0 ([Example](https://docs.mem0.ai/integrations/crewai))

##📚文档和支持

-完整文档：https://docs.mem0.ai
- Community: [Discord](https://mem0.dev/DiG) · [X (formerly Twitter)](https://x.com/mem0ai)
-联系人：founders@mem0.ai

##引文

我们现在有一篇论文可以引用：

```bibtex
@article{mem0,
  title={Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory},
  author={Chhikara, Prateek and Khant, Dev and Aryan, Saket and Singh, Taranjeet and Yadav, Deshraj},
  journal={arXiv preprint arXiv:2504.19413},
  year={2025}
}
```

##⚖️执照

Apache 2.0 — see the [LICENSE](https://github.com/mem0ai/mem0/blob/main/LICENSE) file for details.
