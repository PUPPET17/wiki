---
source_url: https://github.com/letta-ai/letta-code
fetched_url: https://raw.githubusercontent.com/letta-ai/letta-code/main/README.md
source_type: github repo
author: letta-ai/letta-code maintainers
source_date: 2025-10-25
ingested: 2026-05-15
sha256: 8f812ee3141a82d3cfc55727243ce11bf5af49b49fb956545de3df6c0ba2f39f
raw_preservation: full_github_readme_text
extraction_method: github_repo_api_and_raw_readme
github_repo: letta-ai/letta-code
stars: 2477
open_issues: 157
---

#GitHub存储库：letta-ai/letta-code

##源元数据

-来源网址：https://github.com/letta-ai/letta-code
-获取的URL：https://raw.githubusercontent.com/letta-ai/letta-code/main/README.md
-来源类型：github repo
-作者：letta-ai/letta-code maintainers
-来源日期：2025-10-25
-摄入日期：2026-05-15
-可靠性：高
-原始保存状态：full_github_readme_text
-提取方式：github_repo_api_and_raw_readme

##解析的源文本

#存储库元数据：letta-ai/letta-code

-GitHub网址：https://github.com/letta-ai/letta-code
-描述：内存优先编码代理
-星星：2477
-叉子：252
-未决问题：157
-创建时间：2025-10-25T04：17:51 Z
-更新日期：2026-05-14T17：40：17Z
-许可证：Apache-2.0

##README.md

#读取代码

[Image: npm (https://img.shields.io/npm/v/@letta-ai/letta-code.svg?style=flat-square)](https://www.npmjs.com/package/@letta-ai/letta-code) [Image: Discord (https://img.shields.io/badge/discord-join-blue?style=flat-square&logo=discord)](https://discord.gg/letta)

Letta Code是一种内存优先的编码工具，专为可以从经验中学习的长期代理而设计。

您不是在独立的会话中工作，而是使用一个持久化的代理，该代理的内存可以跨模型（Claude、GPT、Gemini、GLM、Kimi等等）移植。

Run Letta Code in the [**CLI**](https://docs.letta.com/letta-code/cli), or download the [**desktop app**](https://docs.letta.com/letta-code/desktop-app) for MacOS, Windows, and Linux.
You can also access Letta Code via [your phone](https://docs.letta.com/letta-code/remote-mobile) and [Slack/Telegram/Discord](https://docs.letta.com/letta-code/channels).

Image: image (https://github.com/letta-ai/letta-code/blob/main/assets/letta-code-demo.gif)

##开始
Install the package via [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm):
```bash
npm install -g @letta-ai/letta-code
```
Navigate to your project directory and run `letta` (see various command-line options [on the docs](https://docs.letta.com/letta-code/commands)). 

运行`/connect`配置您自己的大语言模型API密钥（OpenAI/ChatGPT、Anthropic、zAI编码计划等。），并使用`/model`交换模型。

对于速度较慢的本地推理服务器，请在连接时配置提供程序级超时。例如，LM Studio兼容的llama服务器后端需要10分钟进行大上下文压缩，可以使用：

```bash
letta --backend local connect lmstudio --base-url http://127.0.0.1:1234/v1 --timeout 600s
```

每个本地提供程序以毫秒为单位存储超时；传递“-no-timeout”或“-timeout false”以禁用提供程序超时。

You can also download the [**desktop app**](https://docs.letta.com/letta-code/desktop-app) for MacOS, Windows, and Linux. Agents created in the CLI are available via the desktop app, and vice versa.

##哲学
Letta代码是围绕长寿命代理构建的，这些代理在会话中持续存在，并随着使用而改进。每个会话都绑定到一个学习的持久代理，而不是在独立的会话中工作。

**Claude Code/Codex/Gemini CLI**（基于会话）
-会话是独立的
-会话之间没有学习
-Context=当前会话中的消息+`AGENTS.md`
-关系：每一次谈话都像是遇到一个新的承包商

**莱塔代码**（基于代理）
-跨会话的相同代理
-随着时间的推移，持久的记忆和学习
-`/clear`启动一个新的会话（又名“线程”或“会话”），但内存仍然存在
-关系：比如有一个学习和记忆的同事或学员

##代理记忆与学习
如果您是第一次使用Letta代码，您可能需要运行`/init`命令来初始化代理的内存系统：
```bash
> /init
```

随着时间的推移，代理将在学习时更新其记忆。要主动引导代理内存，可以使用`/remember`命令：
```bash
> /remember [optional instructions on what to remember]
```
Letta Code works with skills (reusable modules that teach your agent new capabilities in a `.skills` directory), but additionally supports [skill learning](https://www.letta.com/blog/skill-learning). You can ask your agent to learn a skill from its current trajectory with the command: 
```bash
> /skill [optional instructions on what skill to learn]
```

Read the docs to learn more about [skills and skill learning](https://docs.letta.com/letta-code/skills).

Community maintained packages are available for Arch Linux users on the [AUR](https://aur.archlinux.org/packages/letta-code):
```bash
yay -S letta-code # release
yay -S letta-code-git # nightly
```

---

制造于💜在旧金山
