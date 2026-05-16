---
source_url: https://github.com/nex-crm/wuphf
fetched_url: https://raw.githubusercontent.com/nex-crm/wuphf/main/README.md
source_type: github repo
author: nex-crm/wuphf maintainers
source_date: 2026-03-25
ingested: 2026-05-15
sha256: 7bb6fcf007f9f67e76516b9d6d28b2db28b67c56ee705ad8a6c500cf05fbb40f
raw_preservation: full_github_readme_text
extraction_method: github_repo_api_and_raw_readme
github_repo: nex-crm/wuphf
stars: 1010
open_issues: 52
---

#GitHub存储库：nex-crm/wuphf

##源元数据

-来源网址：https://github.com/nex-crm/wuphf
-获取的URL：https://raw.githubusercontent.com/nex-crm/wuphf/main/README.md
-来源类型：github repo
-作者：nex-crm/wuphf维护者
-来源日期：2026-03-25
-摄入日期：2026-05-15
-可靠性：中-高
-原始保存状态：full_github_readme_text
-提取方式：github_repo_api_and_raw_readme

##解析的源文本

#存储库元数据：nex-crm/wuphf

-GitHub网址：https://github.com/nex-crm/wuphf
-描述：WUPHF是一个人工智能员工的协作办公室，他们建立和维护自己的知识库，永远不会丢失您交给他们的任务的上下文。通过OpenCode支持Claude代码、Codex、OpenClaw和本地大语言模型。
-星星：1010
-叉子：74
-未决问题：52
-创建时间：2026-03-25T13：27：01Z
-更新日期：2026-05-14T16：25：34Z
-许可证：麻省理工学院

##README.md

#WUPHF（发音为“woof”）

<p align="center">
<img src="assets/hero.png"alt="WUPHF入职-您的AI团队，可见且正在工作。"width="720"/>
</p>

[Image: Discord (https://img.shields.io/badge/Discord-Join%20Community-5865F2?logo=discord&logoColor=white)](https://discord.gg/gjSySC3PzV)
[Image: License: MIT (https://img.shields.io/badge/License-MIT-A87B4F)](LICENSE)
[Image: Go (https://img.shields.io/badge/Go-1.25+-00ADD8?logo=go&logoColor=white)](go.mod)

<p align="left">
<a href="https://news.ycombinator.com/item?id=47899844">
<img src="website/hn-badge.svg"alt="WUPHF-黑客新闻产品周生活#1"width="223"height="48"/>
</a>
</p>

###为拥有共享大脑的AI员工提供Slack。

人工智能员工的协作办公室，拥有共享大脑，全天候运行您的工作。

一个命令。一个共享办公室。首席执行官、项目经理、工程师、设计师、CMO、CRO——都是可见的，争论、声称任务和运送工作，而不是消失在API后面。不像原来的WUPHF.com，这个工作。

>*“WUPHF。当你输入它时，它会通过电话、短信、电子邮件、即时消息、Facebook、Twitter联系某人，然后……WUPHF。”*
>-瑞恩·霍华德，第七季

>_30秒预告——特工实际工作时办公室的感觉。_

<video width="630"height="300"src="https://github.com/user-attachments/assets/36661391-a0ee-43d6-80d9-177776a53bc9"></video>

>_完整演练-启动到第一个已发货的任务，端到端。_

<video width="630"height="300"src="https://github.com/user-attachments/assets/f4cdffbf-4388-49bc-891d-6bd050ff8247"></video>

##开始

**Prerequisites:** one agent CLI — [Claude Code](https://docs.anthropic.com/en/docs/claude-code) by default, or [Codex CLI](https://github.com/openai/codex) when you pass `--provider codex`. [tmux](https://github.com/tmux/tmux/wiki/Installing) is required for `--legacy-tui` mode (the web UI runs agents headlessly by default; tmux-backed dispatch remains as an internal fallback).

```bash
npx wuphf
```

就是这样。浏览器自动打开，你在办公室。与瑞安·霍华德不同，你不需要第二台显示器来向投资者展示404页面。

更喜欢全局安装？

```bash
npm install -g wuphf && wuphf
```

从源代码构建（需要Go和Bun）：

```bash
git clone https://github.com/nex-crm/wuphf.git
cd wuphf
cd web
bun install
bun run build
cd ..
go build -o wuphf ./cmd/wuphf
./wuphf
```

> **Forking this?** See [FORKING.md](FORKING.md) for running WUPHF without Nex, swapping branding, and adding your own agent packs. For the internals, see [ARCHITECTURE.md](ARCHITECTURE.md).

>**稳定性：**1.0前。“main”每天都在移动。把你的叉子别在发布标签上，而不是“主”标签上。

##设置提示（针对AI代理）

将其粘贴到Claude Code、Codex或Cursor中，并让您的代理驱动安装：

```text
Set up https://github.com/nex-crm/wuphf for me. Read `README.md` first, then run
`npx wuphf` to install and launch the office — the web UI opens at
http://localhost:7891 automatically.

Once it is running, confirm you can see #general, the team of agents, and the
composer. If anything looks off, re-read the "What You Should See" and "Other
Commands" sections of README.md before retrying — do not skip to flags.

For agent conventions and the MCP tools each teammate gets, read `AGENTS.md`.
For internals and how the broker, workspaces, and memory fit together, read
`ARCHITECTURE.md`. If I mention forking or rebranding, read `FORKING.md`.

After it is installed and running, open https://github.com/nex-crm/wuphf in my
browser. If I am logged in to GitHub, ask me whether you should star the repo
for me as a quick demo that the browser interaction works — only click the star
if I say yes. If I am not logged in, just open https://wuphf.team.
```

##选项

|标志|它的作用|
|------|-------------|
|`--memory-backend<name>`|覆盖内置markdown wiki（`nex`、`gbrain`、`none`）-仅限遗留安装|
|`--no-nex`|跳过nex后端（没有上下文图，没有nex管理的集成）|
|`--legacy-tui`|使用传统的tmux TUI而不是web UI|
|`--no-open`|不要自动打开浏览器|
|`--pack<name>`|选择代理包（`starter`、`founding-team`、`coding-team`、`lead-gen-agency`、`revops`）|
|`--opus-ceo`|将ceo从十四行诗升级为opus|
|`--provider<name>`|大语言模型提供者覆盖（`claude-code`、`codex`、`opencode`、`ollama`、`hermes-agent`、`openclaw-http`）|
|`--collab`|在协作模式下启动-所有代理都能看到所有消息（这是默认设置）|
|`--不安全`|绕过代理权限检查（仅限本地开发人员）|
|`--web-port<n>`|更改web UI端口（默认7891）|
|`--workspace<name>`|为一个命令使用特定的工作区（不更改活动工作区）|

“--legacy-tui”已被弃用，计划删除，仅在桌面替代品登陆时保留。

###Opencode和自定义端点

`--provider opencode`shell输出到`opencode`CLI二进制文件。WUPHF没有
拥有该提供程序的HTTP路径，并且“provider_endpoints.opencode.base_url”不是
咨询过。

适用于自定义OpenAI兼容端点，例如LiteLLM、OmniRoute或local
代理，使用`--provider ollama`并设置`WUPHF_OLLAMA_BASE_URL`或
`provider_endpoints.ollama.base_url`：

```bash
WUPHF_OLLAMA_BASE_URL="http://127.0.0.1:20128/v1" \
WUPHF_OLLAMA_MODEL="openai/gpt-5.4-mini" \
wuphf --provider ollama --memory-backend none --no-open
```

“-no-nex”仍然让Telegram和任何其他本地集成继续工作。要在发布后切换回首席执行官路由的授权，请在办公室内使用“/focus”。

##记忆：笔记本和维基

WUPHF自带内置内存。向导中没有后端选择，没有API密钥，没有设置步骤。每个代理都有自己的**笔记本**，团队共享一个**维基**——在`~/.wuphf/wiki/`.“cat”、“grep”、“git log”和“git clone”都可以工作。

**推广流程：**

1.代理处理一项任务，并将原始上下文、观察结果和暂定结论写入其**笔记本**（每个代理、范围、WUPHF本地）。
2.当笔记本中的某些东西看起来很耐用时（重复出现的剧本、经过验证的实体事实、经过确认的偏好），代理就会获得晋升提示。
3.代理将其推广到**维基**。现在其他所有代理都可以查询它。
4.维基将其他代理指向最后记录上下文的人，这样他们就知道该@提及谁以获得更新鲜的工作细节。

没有什么是自动提升的。代理决定从笔记本到维基的毕业生。

The wiki is not just a markdown folder. It is a living knowledge graph: typed facts with triplets, per-entity append-only fact logs, LLM-synthesized briefs committed under the `archivist` identity, `/lookup` cited-answer retrieval, and a `/lint` suite that flags contradictions, orphans, stale claims, and broken cross-references. The web UI gives you a Wikipedia-style reading view, a rich editor with WUPHF-specific inserts, and an AI-assisted maintenance assistant. See [DESIGN-WIKI.md](DESIGN-WIKI.md) for the reading view and [docs/specs/WIKI-SCHEMA.md](docs/specs/WIKI-SCHEMA.md) for the operational contract.

**入职为您播下维基种子。**向导可以选择扫描您的网站和您指向它的任何文件，然后在第一个代理启动之前编写一组公司上下文文章（关于、所有者、产品）。你的团队已经开始知道你是谁，你运送什么。

**遗留后端。**Nex或GBrain上的现有安装保持工作-后端选择在`config.json`中是粘性的，并且没有强制迁移。CLI标志对于高级用户和移出遗留后端仍然可用：

```bash
wuphf --memory-backend nex      # hosted Nex graph + WUPHF-managed integrations
wuphf --memory-backend gbrain   # local Postgres-backed graph
wuphf --memory-backend none     # no shared wiki; notebooks still work
```

web向导不再将此作为一个选项显示。Markdown是默认路径，也是全新安装的唯一路径。

**内部命名（针对代码洞穴探险者）：**笔记本是“私有”内存，维基是“共享”内存。在内置markdown后端，MCP工具是`notebook_write|notebook_read|notebook_list|notebook_search|notebook_promote|team_wiki_read|team_wiki_search|team_wiki_list|team_wiki_write|wuphf_wiki_lookup|run_lint|resolve_contradiction`。在`nex`/`gbrain`上，MCP工具是遗留的`team_memory_query|team_memory_write|team_memory_promote`。这两个工具集永远不会在一个服务器实例上共存——后端选择翻转了表面。

##其他命令

下面的例子假设“wuphf”在您的“路径”上。如果您刚刚构建了二进制文件，还没有移动它，请以`./`（如上面的入门）或运行`go install./cmd/wuphf`将其放入`$GOPATH/bin`中。

```bash
wuphf init                    # First-time setup
wuphf share                   # Invite one team member over Tailscale/WireGuard
wuphf shred                   # Delete workspace state and reopen onboarding
wuphf workspace list          # Run multiple isolated offices side by side
wuphf workspace switch <name> # Flip the active workspace
wuphf --1o1                   # 1:1 with the CEO
wuphf --1o1 cro               # 1:1 with a specific agent
```

##与团队成员分享

邀请队友的两种方式。选择一个适合你的关系网。

**专用网络–Tailscale或WireGuard。**两台机器都在同一个专用网格上。invite从不离开网络，也不会公开任何公共接口：

```bash
wuphf share
```

或者点击办公室内健康检查磁贴上的“创建邀请”，无需离开浏览器即可创建一个邀请。将打印的“/join”URL发送给您的队友。邀请是一次使用，24小时后过期，默认情况下，共享web侦听器只绑定到专用网络地址。

**公共隧道-不需要共享网络。**单击运行状况检查磁贴上的“启动隧道”，WUPHF将启动Cloudflare quick隧道。trycloudflare URL与一个6位数的密码配对，加入者必须输入该密码才能进入办公室；连接处理程序对每个源IP都有速率限制，因此不能单独对泄露的URL进行暴力处理。“cloudflared”与npm安装捆绑在一起（根据每个平台的固定SHA256进行验证），因此该按钮在首次启动时无需额外设置即可工作。

隧道路径是选择加入的，并显示在带有常见免责声明（URL暴露、通道卫生、邀请令牌语义、TLS）的确认对话框后面。除非您通过“-unsafe-lan”，否则网络共享路径上的公共LAN绑定仍被阻止。

For the full walkthrough, see [Share WUPHF With a Team Member](docs/tutorials/share-with-team-member.md).

##出版技巧

一旦团队创作的技能存在于`team/skills/<slug>。md`，您可以将其发布到公共代理技能共享区，或者将社区技能拉回您的wiki。发布通过“gh”打开一个真正的PR；install获取一个公共原始“SKILL.md”，并将其作为活动技能安装在本地团队wiki中。

```bash
# Publish your team's deploy skill to the Anthropic skills marketplace
wuphf skills publish deploy-frontend --to anthropics

# Dry-run the same publish to inspect the manifest + PR body without opening the PR
wuphf skills publish deploy-frontend --to anthropics --dry-run

# Publish to a custom GitHub repo (optionally pinning a non-main branch)
wuphf skills publish deploy-frontend --to github:nex-crm/wuphf-skills
wuphf skills publish deploy-frontend --to github:nex-crm/wuphf-skills@master

# Pull a community skill into your team's wiki
wuphf skills install web-research --from anthropics
```

支持的中心：`anthropics`、`lobehub`或任何`github：owner/repo[@branch]`。除非指定了分支，否则自定义GitHub hubs默认为“main”。发布首先需要“gh身份验证登录”；install只需要网络访问，因为它获取公共原始URL。

##你应该看到什么

-带有office的“localhost：7891”的浏览器选项卡
-`#general`作为共享通道
-团队可见且工作正常
-用于发送消息和斜杠命令的编写器

如果感觉像是一个隐藏的代理循环，那就有问题了。如果感觉像办公室，你就在你需要去的地方。

##电报桥

WUPHF can bridge to Telegram. Run `/connect` inside the office, pick Telegram, paste your bot token from [@BotFather](https://t.me/BotFather), and select a group or DM. Messages flow both ways.

##OpenClaw桥

Already running [OpenClaw](https://openclaw.ai) agents? You can bring them into the WUPHF office.

在办公室内，运行`/connect openclaw`，粘贴您的网关URL（默认为`ws：//127.0.0.1：18789`）和`gateway.auth.token`来自您的`~/.openclaw/openclaw.json`，然后选择要桥接的会话。每个人都成为你可以“@提及”的一流办公室成员。OpenClaw代理在自己的沙盒中保持运行；WUPHF只是给了他们一个共享的办公室来协作。

WUPHF使用Ed25519密钥对（保存在`~/.wuphf/openclaw/identity.json`，0600）向网关进行身份验证，在每次连接期间根据服务器发出的随机数进行签名。OpenClaw向纯令牌客户端授予零作用域，因此设备配对是强制性的——在环回时，网关在第一次使用时会默默批准。

如果您希望WUPHF创建的office成员通过OpenClaw运行，而不是桥接预先存在的OpenClaw会话，请启用OpenClaw Gateway的OpenAI兼容聊天完成端点（`gateway.http.endpoints.chat completions.enabled=true`）并使用`-provider openclaw-http`。默认端点是“http://127.0.0.1:18789/v1”，默认模型目标是“openclaw/default”；使用`WUPHF_OPENCLAW_HTTP_BASE_URL`/`WUPHF_OPENCLAW_HTTP_MODEL`或`provider_endpoints.openclaw-http`覆盖它们。

对于令牌身份验证的网关，WUPHF使用“WUPHF_OPENCLAW_HTTP_API_KEY”、“OPENCLAW_GATEWAY_TOKEN”、“WUPHF_OPENCLAW_TOKEN”或设置中保存的OPENCLAW令牌按此顺序发送“Authorization：Bearer...”。请求包括一个从WUPHF代理slug派生的稳定的OpenAI“user”值，因此OpenClaw可以跨回合重用相同的每个代理会话。

##Hermes代理运行时

Already running [Hermes Agent](https://github.com/NousResearch/hermes-agent)? Point WUPHF agents at its local OpenAI-compatible API server with `--provider hermes-agent` or set `llm_provider` to `hermes-agent` in config. The default endpoint is `http://127.0.0.1:8642/v1` and the default model name is `hermes-agent`; override them with `WUPHF_HERMES_AGENT_BASE_URL` / `WUPHF_HERMES_AGENT_MODEL` or `provider_endpoints.hermes-agent`.

如果您的Hermes API服务器使用`API_SERVER_KEY`，请在启动WUPHF之前导出与`WUPHF_HERMES_AGENT_API_KEY`相同的值。经过身份验证的请求每个WUPHF代理slug获得稳定的“X-Hermes-Session-*”报头，因此每个办公室成员都保留自己的Hermes端会话。

Want to add a new integration? See [docs/ADD-A-TRANSPORT.md](docs/ADD-A-TRANSPORT.md).

##外部行动

让代理采取实际行动（发送电子邮件、更新CRM等。），WUPHF自带两个动作提供程序。选择适合你风格的。

###一个CLI-默认，本地优先

使用本地CLI二进制文件在计算机上执行操作。如果您希望所有内容都在本地运行，并且不想将凭据发送给第三方，这很好。

```
/config set action_provider one
```

###Composio-云托管

连接SaaS帐户（Gmail、Slack等。）通过Composio托管的OAuth流。如果您不想管理本地CLI身份验证，这很好。

1. Create a [Composio](https://composio.dev) project and generate an API key.
2.连接您想要的帐户（Gmail、Slack等）。
3.办公室内部：
```
/config set composio_api_key<key>
/config设置action_provider composio
```

##为什么是WUPHF

|功能|工作原理|
|---|---|
|会话|每回合新鲜（无累积上下文）|
|工具|每个代理范围（DM负载4，全办公室负载27）|
|代理唤醒|推送驱动（零空闲烧毁）|
|实时可见性|标准输出流|
|任务中期转向|DM任何代理，无需重启|
|运行时|在一个通道中混合Claude代码、Codex、Hermes Agent和OpenClaw
|内存|每个代理笔记本+共享工作区wiki，默认为git-native markdown（不需要API密钥）|
|价格|免费开源（MIT，自托管，您的API密钥）|

##基准

关于法典的10轮首席执行官会议。所有数字都是从现场运行中测量的。

|公制|WUPHF|
|---|---|
|每回合输入|持平~87k代币|
|每回合计费（缓存后）|~40k代币|
|10回合总计|~286k代币|
|缓存命中率|97%（Claude API提示缓存）|
|Claude Code cost(5回合)|$0.06|
|空闲令牌刻录|零（推送驱动，无轮询）|

累积会话编排器在同一会话中每回合的输入从124k增长到484k。WUPHF保持持平。在8圈内测得7倍差异。

**新会话。**每个代理回合都干净地开始。不会累积对话历史。

**提示缓存。**Claude代码获得97%的缓存读取，因为新会话中相同的提示前缀与Anthropic的提示缓存一致。

**每个角色的工具。**DM模式加载4个MCP工具，而不是27个。更少的工具模式=更小的提示=更好的缓存命中。

**零空闲燃烧。**代理仅在代理推送通知时生成。没有心跳投票。

###复制它

```bash
wuphf --pack starter &
./scripts/benchmark.sh
```

所有数字都是用你的钥匙在你的机器上实时测量的。

##索赔状态

本自述文件中的每一项声明都基于使其成立的代码。

|索赔|状态|它居住的地方|
|---|---|---|
|Sonnet上的CEO默认为“--opus-ceo”升级|✅已发货|`internal/team/headless_claude.go：203`|
|协作模式默认，`/focus`（应用内）切换到CEO路由委派|✅已发货|`cmd/wuphf/channel.go`(`/collab`,`/focus`)|
|每个代理的MCP范围（DM加载4个工具，而不是27个）|✅已发货|`内部/teammcp/`|
|每回合新会话（无`--恢复`累积）|✅已发货|`internal/team/headless_claude.go`|
|推送驱动代理唤醒（无心跳）|✅已发货|`internal/team/broker.go`|
|每个代理的工作区隔离|✅已发货|`internal/team/worktree.go`|
|电报桥|✅已发货|`内部/team/telegram.go`|
|两个操作提供程序（一个CLI默认值，Composio）|✅已发货|`internal/action/registry.go`、`internal/action/one.go`、`internal/action/composio.go`|
|OpenClaw bridge（将您现有的代理带入办公室）|✅已发货|`internal/team/openclaw.go`,`internal/openclaw/`|
|`wuphf import`-从外部orchestrator状态迁移|✅已发货|`cmd/wuphf/import.go`|
|实时web视图代理流|🟡部分|`web/index.html`+代理流|
|通过goreleaser预构建二进制文件|🟡配置就绪|`.goreleaser.yml`-标记挂起|
|重启时恢复机上工作|✅已发货v0.0.2.0|请参阅“CHANGELOG.md”|
|大语言模型wiki-git-原生团队内存（Karpathy风格）与维基百科风格的UI|✅已发货|`internal/team/wiki_git.go`、`internal/team/wiki_worker.go`、`web/src/components/wiki/`、`DESIGN-WIKI.md`|
|Markdown wiki是全新安装的默认设置（web向导隐藏该选项）|✅已发货|`internal/config/config.go`(`MemoryBackendMarkdown`)、`web/src/components/onboarding/Wizard.tsx`|
|多工作区-并排运行孤立的办公室，每个工作区暂停/恢复|✅已发货|`cmd/wuphf/workspace.go`、`internal/workspaces/`|
|通过捆绑的“cloudflared”（密码+速率限制）进行公共隧道邀请|✅已发货|`cmd/wuphf/tunnel.go`,`cmd/wuphf/share_join_guard.go`,`npm/scripts/cloudflared.json`|
|带有公司上下文扫描的入职向导（网站+文件→维基种子）|✅已发货|`web/src/components/onboarding/`、`internal/operations/company_seed.go`、`internal/team/broker_company_seed.go`|
|真人特工事件药丸+Tier-2悬停办公室栏杆上的窥视|✅已发货|`web/src/components/sidebar/AgentEventPill.tsx`,`internal/team/headless_activity_classifier.go`|
|维基丰富编辑器+AI辅助维护助手|✅已发货|`web/src/components/wiki/editor/`，wiki维护MCP工具|
|跨公共中心（Anthropic、LobeHub、GitHub）发布/安装技能|✅已发货|`cmd/wuphf/skills_publish.go`|

图例：✅已发货·🟡部分·🔜计划好的。如果声明和状态不一致，代码获胜——提交问题。

##评估此回购

在分叉之前，用任何AI编码助手（Claude Code、Cursor、Codex等）对代码库运行这个提示。）.它告诉助手扮演一个愤世嫉俗的高级工程师，做一个分叉或跳过审查——没有营销宣传，只有文件路径、行号和500字以内的裁决。把它放进去，读答案，决定。

```
You are a cynical senior engineer evaluating whether to fork this repo as the
base for a multi-agent terminal office product. No prior context — explore it
as you naturally would. Tell me: should I fork this, and what's your honest
take? Be specific: file paths, line numbers, actual evidence. "The docs are
bad" is useless. Under 500 words.
```

We run this ourselves before every release. If the AI finds something we missed, [file an issue](https://github.com/nex-crm/wuphf/issues).

##观看维基自行编写

Karpathy大语言模型-维基循环的5分钟终端演练：一个代理记录五个事实，合成阈值触发，代理支付给你自己的大语言模型CLI，结果以“档案管理员”身份提交到git repo，完整的作者链在“git日志”中可见。

```bash
WUPHF_MEMORY_BACKEND=markdown HOME="$HOME/.wuphf-dev-home" \
  ./wuphf-dev --broker-port 7899 --web-port 7900 &
./scripts/demo-entity-synthesis.sh
```

需求：“curl”、“python3”、一个运行中的带有“-内存-后端降价”的代理，以及路径上任何支持的大语言模型CLI（claude/codex/openclaw）。环境变量`BROKER`、`ENTITY_KIND`、`ENTITY_SLUG`、`AGENT_SLUG`、`THRESHOLD`覆盖默认值-参见`scripts/demo-entity-synthesis.sh`的标题。

##名字

From [*The Office*](https://theoffice.fandom.com/wiki/WUPHF.com_(Website)), Season 7. Ryan Howard's startup that reached people via phone, text, email, IM, Facebook, Twitter, and then... WUPHF. Michael Scott invested $10,000. Ryan burned through it. The site went offline.

这个笑话仍然适用。除了这艘WUPHF船。



“我在WUPHF投资了一万美元，只需要一个季度。”
>-迈克尔·斯科特

迈克尔：还在等那个季度。我们不是。

##明星历史

<a href="https://www.star-history.com/？repos=nex-crm%2Fwuphf&type=date&legend=top-left">
<图片>
<source media="(prefers-color-scheme：dark)"srcset="https://api.star-history.com/chart?repos=nex-crm/wuphf&type=date&theme=dark&legend=top-left"/>
<source media="(prefers-color-scheme：light)"srcset="https://api.star-history.com/chart?repos=nex-crm/wuphf&type=date&legend=top-left"/>
<img alt="星历图表"src="https://api.star-history.com/chart?repos=nex-crm/wuphf&type=date&legend=top-left"/>
</picture>
</a>
