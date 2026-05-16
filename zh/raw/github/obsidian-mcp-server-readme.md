---
source_url: https://raw.githubusercontent.com/cyanheads/obsidian-mcp-server/main/README.md
retrieved: 2026-05-14
source_type: github
reliability: high
raw_preservation: full_parsed_text
extraction_status: complete
capture_method: raw_github_markdown
content_sha256: b3295f387896d74f36fbe3c42d79ba4709644a52a6bf4fd710dd4b5b448f9184
---

#Obsidian MCP服务器自述文件

##源元数据

-source_url：https://raw.githubusercontent.com/cyanheads/obsidian-mcp-server/main/README.md
-检索日期：2026-05-14
-source_type：github
-capture_method：raw_github_markdown
-extraction_note：direct_raw_markdown_fetch
-content_sha256：`b3295f387896d74f36fbe3c42d79ba4709644a52a6bf4fd710dd4b5b448f9184`

##解析的源文本

<div align="center">
<h1>黑曜石-mcp服务器</h1>
<p><b>用于Obsidian vaults的MCP服务器–通过本地REST API插件读取、写入、搜索和外科手术式编辑注释、标签和frontmatter。STDIO或流式HTTP。</b>
<div>14个工具•3个资源</div>
</p>
</div>

<div align="center">

[Image: npm (https://img.shields.io/npm/v/obsidian-mcp-server?style=flat-square&logo=npm&logoColor=white)](https://www.npmjs.com/package/obsidian-mcp-server) [Image: Version (https://img.shields.io/badge/Version-3.1.9-blue.svg?style=flat-square)](./CHANGELOG.md) [Image: Framework (https://img.shields.io/badge/Built%20on-@cyanheads/mcp--ts--core-259?style=flat-square)](https://www.npmjs.com/package/@cyanheads/mcp-ts-core) [Image: MCP SDK (https://img.shields.io/badge/MCP%20SDK-^1.29.0-green.svg?style=flat-square)](https://modelcontextprotocol.io/)

[Image: License (https://img.shields.io/badge/License-Apache%202.0-orange.svg?style=flat-square)](./LICENSE) [Image: TypeScript (https://img.shields.io/badge/TypeScript-^6.0.3-3178C6.svg?style=flat-square)](https://www.typescriptlang.org/) [Image: Bun (https://img.shields.io/badge/Bun-v1.3.11-blueviolet.svg?style=flat-square)](https://bun.sh/)

</div>

---

##工具

按形状分组的14个工具——阅读器获取笔记和元数据，作者创建或外科手术式编辑内容，管理者协调标签和frontmatter，一个受保护的逃生舱口发送黑曜石命令-调色板命令。

|工具名称|描述|
|:----------|:------------|
|`obsidian_get_note`|将注释读取为原始内容、完整结构化形式（content+frontmatter+tags+stat，带有可选的传出链接）、结构化文档映射或单个部分。|
|`obsidian_list_notes`|列出vault路径上的注释和子目录，其递归遍历（默认深度2-结构概述；最大20）以1000个条目的上限为界。可选的“extension”和“nameRegex”过滤器适用于整个树；正则表达式过滤的目录会被跳过，而不会递归到它们中。在渲染输出中返回平面“entries[]”和一个方框绘制树；每个目录的“truncated：true”标志深度限制切断递归的位置。|
|`obsidian_list_tags`|列出在vault中找到的每个标记及其使用计数，包括分层父标记。|
|`obsidian_list_commands`|列出可供执行的黑曜石命令-调色板命令。**通过`OBSIDIAN_ENABLE_COMMANDS=true`**（与`obsidian_execute_command`配对）选择加入。|
|`obsidian_search_notes`|通过文本、Dataview DQL或JSONLogic搜索vault。文本模式匹配返回周围的上下文窗口(`contextLength`)-上限为100次点击，带有溢出指示器。|
|`obsidian_write_note`|创建一个注释，在适当的位置替换单个部分，或者-使用`overwrite：true'-删除现有文件。默认情况下，拒绝对现有路径进行整个文件写入。|
|`obsidian_append_to_note`|将内容附加到注释。如果没有“section”，它会创建文件，如果丢失-您的内容将成为整个文件。使用“section”，附加到该标题/block/frontmatter（补丁；文件必须存在）。|
|`obsidian_patch_note`|Surgical`append`/`prepend`/`replace`针对标题、块引用或frontmatter字段。|
|`obsidian_replace_in_note`|全身搜索-在单个音符内替换。文字或正则表达式匹配，带有“wholeWord”、“flexibleWhitespace”、“区分大小写”、“replaceAll”和“$1”/“$&”捕获组。|
|`obsidian_manage_frontmatter`|单个frontmatter键上的原子`获取`/`设置`/`删除`。|
|`obsidian_manage_tags`|添加、删除或列出标签-协调frontmatter`tags：`和内联`#tag`语法。|
|`obsidian_delete_note`|永久删除注释。当客户支持时，引起人工确认。|
|`obsidian_open_in_ui`|使用`failIfMissing`和`newLeaf`切换在Obsidian应用程序UI中打开文件。|
|`obsidian_execute_command`|按ID执行黑曜石命令-调色板命令。**通过`OBSIDIAN_ENABLE_COMMANDS=true`选择加入。**|

###`黑曜石_get_note`

在四个投影中的一个中读取注释，由vault path、活动文件或定期注释（“每日”、“每周”、“每月”、“季度”、“每年”）寻址。

-`格式：“内容”`-原始markdown正文
-`格式：“完整”`-内容、frontmatter、标签和文件元数据；传递“includeLinks：true”以解析来自正文的传出wiki和markdown链接引用（仅限保险库内部-过滤外部URL）
-`格式：“文档映射”`-标题、块引用和frontmatter字段的目录
-`格式：“section”`-单个标题/块/frontmatter section值(需要`section`)；标题部分包括该标题下的完整子树

将文档映射投影与“obsidian_patch_note”配对，以便在修补前发现编辑目标。

---

###`黑曜石搜索注释`

通过“模式”选择三种搜索模式：

-`text`-子字符串与周围的上下文窗口匹配。“contextLength”控制每个匹配每边的上下文字符（默认值为100；每次命中时，将其提升以获得更多上下文）。可选的“pathPrefix”过滤器（仅文本模式-在“dataview”或“jsonlogic”模式下传递“pathPrefix”将被“path_prefix_invalid_mode”拒绝）。
-`dataview`-用于路径/日期/元数据查询的Dataview DQL(`TABLE…`)；“文件时间”、“文件路径”等是可查询的
-`jsonlogic`-针对`路径`、`内容`、`frontmatter.<key>`、`tags`和`stat.{ctime，mtime，size}`评估的jsonlogic树；自定义“glob”和“regexp”运算符

结果上限为100次点击。当上游返回更多时，一个“排除”指示器会显示溢出计数和一个缩小查询范围的提示。文本模式的点击会在“maxMatchesPerHit”（默认为10）处对每个文件进行额外的剪辑，因此单个匹配重音符不会超出响应预算——剪辑的点击带有“truncated：true”和“totalMatches”。

---

###`黑曜石_write_note`

创建或外科手术替换，默认情况下可以防止意外的整个文件覆盖。

-不带“section”-完整文件“PUT”。**拒绝重写现有文件**，除非设置了`overwrite：true'。“file_exists”(“Conflict”)错误提示“obsidian_patch_note”/“obsidian_append_to_note”/“obsidian_replace_in_note”进行就地编辑。
-with`section`-`PATCH`-with-replace针对命名的heading/block/frontmatter字段，保持文件的其余部分不变。在分段模式下，“覆盖”标志被忽略。

当调用使一个新文件存在时，输出报告“created：true”；当它替换现有的一个或以一个部分为目标时，为“false”。每个mutating工具还返回“previousSizeInBytes”和“currentSizeInBytes”，以便代理可以发现意外的重击、意外的上游行为或落在错误文件上的打字错误路径。

---

###`黑曜石_append_to_note`

镜像上游本地REST API行为的组合upsert+section-append原语：

-不带“section”-“POST”到“/vault/{path}”。当文件存在时追加，当文件不存在时**创建文件，将您的内容作为整个正文。**输出的“created：true”标记第二个分支，以便代理可以注意到打字错误路径或尚未创建的每日笔记何时悄悄地变成了一个全新的文件。
-with`section`-`PATCH`-with-append针对命名的标题、块引用或frontmatter字段。该文件必须存在（否则修补程序预检将抛出“note_missing”）。传递“createTargetIfMissing：true”以使节本身在现有文件中存在。块引用目标连接到块行附近，没有分隔符——如果需要，可以在“内容”中包含一个前导换行符。

“previousSizeInBytes”在upsert-create分支上为“0”，否则为实际文件大小；“currentSizeInBytes”是操作后从上游读取的写后大小。将增量与“缓冲区”进行比较。字节长度（内容）”以检测自动换行注入或并发写入器。

---

###`obsidian_patch_note`

在单个文档目标上进行外科编辑。

-`操作：“append”`在节后添加
-`操作：“prepend”`在节前添加
-`操作：“替换”`将其换出
-目标：标题路径、块参考ID或frontmatter字段

使用`obsidian_get_note`和`format："document-map"`在修补前发现存在哪些目标。

---

###`黑曜石_replace_in_note`

全身搜索-替换不符合“obsidian_patch_note”结构目标的编辑。获取注释，顺序应用替换（每个替换都看到前一个输出），结果在一个“PUT”中写回。

每次更换选项：

-`useRegex`-将`search`视为ECMAScript正则表达式。对于“useRegex：true”，替换将接受“$1”/“$&”捕获组引用。
-`区分大小写`-当`false`时，不区分大小写匹配
-`wholeWord`-将模式包装在`\b…\b`中；适用于文字和正则表达式模式
-`flexibleWhitespace`-用`\s+`替换`搜索`中的任何空白。仅文字模式——当“useRegex：true”（直接表达）时不起作用。
-`replaceAll`-当`false`时，仅替换第一个匹配项

文字模式在替换中保留“$1”/“$&”——仅“useRegex：true”扩展捕获组引用。

---

###`黑曜石管理标签`

在便笺上添加、删除或列出标签。协调两种表示：

-Frontmatter`tags：`array
-正文中的内联`#tag`语法

“添加”确保标签存在于请求的位置中；“移除”将其剥离。围栏代码块中的内联“#tag”事件被有意保留。

---

###`黑曜石_删除_注释`

永久删除便笺。当客户端支持“引出”时，服务器在发出“删除”之前请求人工确认，并且提示包括文件的字节大小——在用户确认之前可见的破坏性爆炸半径。在没有启发的情况下，“destructiveHint”注释会在主机的批准流中显示操作。输出报告“previousSizeInBytes”（删除时的大小）和“currentSizeInBytes：0”。

---

###`黑曜石执行命令`

按ID调度黑曜石命令-调色板命令（可通过`obsidian_list_commands`发现）。行为依赖于命令——一些命令打开UI，另一些命令删除文件或关闭vault。

**当“OBSIDIAN_ENABLE_COMMANDS”未设置时，“obsidian_execute_command”及其发现伙伴“obsidian_list_commands”都用“disabledTool()”包装——不存在于“tools/list”中（大语言模型不能调用它们），但在面向操作员的清单中仍然可见，并带有启用它们的提示。

---

##路径策略（文件夹范围权限）

三个可选的环境变量控制每个工具可以瞄准的保险库路径。**默认unset=full vault**用于读取和写入-向后兼容。

|目标|配置|
|:---|:---|
|默认值（当前行为）|全部未设置|
|随处读取，仅在`projects/`和`scratch/`中写入|`OBSIDIAN_WRITE_PATHS=projects/, scratch/`|
|只读`public/`,仅写`public/inbox/`|`OBSIDIAN_READ_PATHS=public/`,`OBSIDIAN_WRITE_PATHS=public/inbox/`|
|只读部署-不在任何地方写入|`OBSIDIAN_READ_ONLY=true`|

**匹配是基于前缀的，带有隐式递归**，不区分大小写，尾部斜杠归一化。“projects/”匹配“projects/a.md”、“projects/sub/b.md”等。

**写入路径是隐式可读的**–您无法理智地编辑您看不到的内容。因此，当目标匹配`READ_PATHS`*或*`WRITE_PATHS`时，读取通过。

**`OBSIDIAN_READ_ONLY=true`在路径检查之前短路**-每个写入工具和命令-调色板对在启动时都用`disabledTool()`包装（不在`tools/list`中），并且无论`WRITE_PATHS`如何，仍然到达服务的任何写入在运行时都被拒绝。

拒绝被键入为“path_forbidden”（JSON-RPC代码“forbidden”），活动范围在“data.recovery.hint”和“data.activeScope”中回显，因此大语言模型可以在不检查服务器日志的情况下自我纠正。来自“obsidian_search_notes”的搜索结果会根据“READ_PATHS”进行无声过滤——显示“我们隐藏了N次点击”指示器会击败该门。

启动横幅记录活动范围，以便操作员可以在启动时验证他们的配置。

---

##资源

类型URI描述
|:---|:---|:---|
|Resource|`obsidian：//vault/{+path}`|vault中的注释–内容、frontmatter、标签和文件元数据。|
|Resource|`obsidian：//tags`|在整个保管库中找到的所有标签，以及使用计数。|
|Resource|`obsidian：//status`|服务器可达性、身份验证状态、插件/obsidian版本信息和插件清单。|

所有资源数据也可以通过工具访问——“obsidian_get_note”用于“obsidian：//vault/{+path}”，“obsidian_list_tags”用于“obsidian：//tags”。资源适用于喜欢将特定便笺或vault快照附加到对话的客户端。

##功能

Built on [`@cyanheads/mcp-ts-core`](https://www.npmjs.com/package/@cyanheads/mcp-ts-core):

-声明性工具和资源定义-每个原语单个文件，框架处理注册和验证
-统一的错误处理-处理程序抛出，框架捕获，分类和格式化。工具通过类型化的“errors[]”契约来宣传它们的故障表面。
-HTTP传输上的可插拔身份验证：“无”、“jwt”、“oauth”
-带有可选OpenTelemetry跟踪的结构化日志记录
-STDIO和流式HTTP传输

服务器本身是无状态的——每个工具调用都直接命中本地REST API。这里没有使用框架的存储后端、请求状态KV和进度流；黑曜石是单保险库，在通话之间没有什么可以坚持的。

黑曜石特定：

- Wraps the [Obsidian Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) plugin — typed client, deterministic error mapping
-通过带有目标的“修补”操作，跨标题、块引用和frontmatter字段进行节感知编辑
-两种表示之间的标记协调：frontmatter`tags：`array和inline`#tag`语法（跳过隔离代码块）
-跨三种模式进行搜索：文本、Dataview DQL、JSONLogic-当结果超过100次点击的上限时，带有溢出指示器
-通过“ctx.elicit”对破坏性删除进行可选的人在回路确认
-通过`OBSIDIAN_READ_PATHS`/`OBSIDIAN_WRITE_PATHS`和全局`OBSIDIAN_READ_ONLY`kill switch-denies的文件夹范围读/写权限被键入`path_forbidden`，活动范围在错误数据中回显
-选择加入命令-调色板对(`obsidian_list_commands`+`obsidian_execute_command`)-仅在`OBSIDIAN_ENABLE_COMMANDS=true`时注册
-宽恕`obsidian_get_note`和`obsidian_open_in_ui`上的路径解析-根据规范文件名静默重试大小写不匹配的路径，对不明确的大小写匹配抛出`冲突'，并用`你的意思是：…？`仅存在接近匹配时的建议。“obsidian_delete_note”被故意排除在外—破坏性操作不应该静默地重写目标路径。

##入门

Add the following to your MCP client configuration file. The Obsidian Local REST API plugin must be installed and enabled in your vault — see [Prerequisites](#prerequisites).

```json
{
  "mcpServers": {
    "obsidian": {
      "type": "stdio",
      "command": "bunx",
      "args": ["obsidian-mcp-server@latest"],
      "env": {
        "MCP_TRANSPORT_TYPE": "stdio",
        "MCP_LOG_LEVEL": "info",
        "OBSIDIAN_API_KEY": "your-local-rest-api-key"
      }
    }
  }
}
```

或使用npx（不需要Bun）：

```json
{
  "mcpServers": {
    "obsidian": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "obsidian-mcp-server@latest"],
      "env": {
        "MCP_TRANSPORT_TYPE": "stdio",
        "MCP_LOG_LEVEL": "info",
        "OBSIDIAN_API_KEY": "your-local-rest-api-key"
      }
    }
  }
}
```

For Streamable HTTP, set the transport and start the server. Inline env vars work for one-off runs; for repeated use, copy values into `.env` (see [`.env.example`](./.env.example)) and run `bun run start:http`.

```sh
MCP_TRANSPORT_TYPE=http OBSIDIAN_API_KEY=... bun run start:http
# Server listens at http://127.0.0.1:3010/mcp by default
```

###先决条件

- [Bun v1.3.11](https://bun.sh/) or higher (or Node.js v24+).
- The [Obsidian Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) plugin installed and enabled in your vault. Generate an API key in **Settings → Community Plugins → Local REST API** and copy it into `OBSIDIAN_API_KEY`.
-为简单起见，此服务器默认为“http://127.0.0.1:27123”。在插件设置中启用**“非加密（HTTP）服务器”**来使用它。要改用始终在线的HTTPS端口，请设置`OBSIDIAN_BASE_URL=https：//127.0.0.1:27124`；插件的自签名证书由`OBSIDIAN_VERIFY_SSL=false`（默认值）处理。

###安装

1.**克隆存储库：**

```嘘
git克隆https://github.com/cyanheads/obsidian-mcp-server.git
```

2.**导航到目录：**

```嘘
cd黑曜石-mcp服务器
```

3.**安装依赖项：**

```嘘
bun安装
```

4.**配置环境：**

```嘘
cp.环境示例。环境
#编辑.env并设置OBSIDIAN_API_KEY
```

##配置

|变量|描述|默认|
|:---------|:------------|:--------|
|`OBSIDIAN_API_KEY`|**必填。**黑曜石本地REST API插件的不记名令牌。|—|
|`OBSIDIAN_BASE_URL`|本地REST API插件的基本URL。使用“https://127.0.0.1:27124”作为始终在线的HTTPS端口（自签名证书）。|`http://127.0.0.1:27123`|
|`OBSIDIAN_VERIFY_SSL`|验证TLS证书。默认为“false”，因为插件使用自签名证书。在节点上，调度程序的“rejectUnauthorized”选项处理此问题，而无需进行任何进程范围的更改。在Bun上，运行时忽略该选项，因此服务额外设置`NODE_TLS_REJECT_UNAUTHORIZED=0`—该回退的作用域仅限于Bun。|`false`|
|`OBSIDIAN_REQUEST_TIMEOUT_MS`|每次请求超时，单位为毫秒。|`30000`|
|`OBSIDIAN_ENABLE_COMMANDS`|命令-调色板对的选择加入标志(`obsidian_list_commands`+`obsidian_execute_command`)。默认关闭——黑曜石命令是不透明的，可能具有破坏性。|`false`|
|`OBSIDIAN_READ_PATHS`|用于读取操作的逗号分隔的vault相对文件夹允许列表。基于前缀的隐式递归；不区分大小写；尾随斜杠标准化。未设置=完整保险库。写路径是隐式可读的。|未设置|
|`OBSIDIAN_WRITE_PATHS`|用于写入操作的逗号分隔的vault相对文件夹允许列表。语法与`OBSIDIAN_READ_PATHS`相同。未设置=完整保险库。|未设置|
|`OBSIDIAN_READ_ONLY`|全局终止开关。当为“true”时，无论“OBSIDIAN_WRITE_PATHS”如何，都拒绝每次写入，并抑制“OBSIDIAN_ENABLE_COMMANDS”对（命令可以变化）。|`false`|
|`MCP_TRANSPORT_TYPE`|传输：`stdio`或`http`。|`stdio`|
|`MCP_HTTP_HOST`|HTTP服务器的主机。|`127.0.0.1`|
|`MCP_HTTP_PORT`|HTTP服务器的端口。|`3010`|
|`MCP_HTTP_ENDPOINT_PATH`|JSON-RPC处理程序的端点路径。|`/mcp`|
|`MCP_PUBLIC_URL`|用于终止TLS的反向代理部署的公共源覆盖（登录页面、服务器卡、RFC 9728元数据）。|未设置|
|`MCP_AUTH_MODE`|身份验证模式：`无`、`jwt`或`oauth`。|`无`|
|`MCP_AUTH_SECRET_KEY`|**当`MCP_AUTH_MODE=jwt`时需要。**≥32个字符的共享密钥，用于验证传入的jwt。|—|
|`MCP_AUTH_DISABLE_SCOPE_CHECKS`|当`true`时，在auth-context存在检查后绕过每个工具的范围强制。令牌签名、受众、发行者和到期验证保持不变。仅当无法注入自定义声明时使用，并与`OBSIDIAN_READ_PATHS`/`OBSIDIAN_WRITE_PATHS`/`OBSIDIAN_READ_ONLY`组合以进行访问控制。每当旁路处于活动状态时，启动时都会记录“警告”。|`false`|
|`MCP_LOG_LEVEL`|日志级别(RFC 5424)。|`信息`|
日志文件的|`LOGS_DIR`|目录（仅限Node.js）。|`<project-root>/logs`|
|`OTEL_ENABLED`|启用OpenTelemetry。|`false`|

See [`.env.example`](./.env.example) for the full list of optional overrides.

##正在运行服务器

当地发展

-**构建并运行生产版本：**

```嘘
#一次性构建
bun run重建

#运行构建的服务器
bun运行开始：stdio
#或
bun运行启动：http
```

-**运行检查和测试：**

```嘘
bun run devcheck#Lint、格式、类型检查、安全性、变更日志同步
bun运行测试#Vitest测试套件
bun运行lint：MCP#根据质量标准验证MCP定义
```

###码头工人

```sh
docker build -t obsidian-mcp-server .
docker run --rm -e OBSIDIAN_API_KEY=your-key -p 3010:3010 obsidian-mcp-server
```

Dockerfile默认为HTTP传输、无状态会话模式，并将日志记录到`/var/log/obsidian-mcp-server'。OpenTelemetry对等依赖项是默认安装的——使用`--build-arg OTEL_ENABLED=false`构建以省略它们。

映像绑定到容器内部的“0.0.0.0”（Docker端口映射所需）。对于在您自己的机器之外可访问的任何部署，请设置`MCP_AUTH_MODE=jwt`（带有`MCP_AUTH_SECRET_KEY`）或`oauth`-否则侦听器会代表每个调用者将您的`OBSIDIAN_API_KEY`转发到vault。

##项目结构

|目录|目的|
|:----------|:--------|
|`src/index.ts`|`createApp()`入口点-注册工具/资源并初始化Obsidian服务。|
|`src/config`|使用Zod解析特定于服务器的环境变量(`OBSIDIAN_*`)。|
|`src/services/obsidian`|本地REST API客户端、frontmatter操作、部分提取器、域类型。|
|`src/mcp-server/tools`|工具定义(`*.tool.ts`)和共享输入模式。|
|`src/mcp-server/resources`|资源定义(`*.resource.ts`)。|
|`src/mcp-server/prompts`|提示定义（当前为空-CRUD/search形状不受益于结构化模板）。|
|`tests/`|Vitest测试镜像`src/`。|
|`docs/`|本地REST API插件和生成的`tree.md`的上游OpenAPI规范。|
|`changelog/`|每个版本的发行说明；“CHANGELOG.md”是重新生成的汇总。|

##开发指南

See [`CLAUDE.md`](./CLAUDE.md) for development guidelines and architectural rules. The short version:

-处理程序抛出，框架捕获-工具逻辑中没有“try/catch”
-使用“ctx.log”进行请求范围的日志记录，使用“ctx.state”进行租户范围的存储
-通过“src/mcp-server/*/definitions/index.ts”中的桶注册新工具和资源
-包装外部API调用：验证原始→规范化为域类型→返回输出模式；切勿捏造缺失字段

##贡献

欢迎问题和拉取请求。提交前运行检查和测试：

```sh
bun run devcheck
bun run test
```

##许可证

Apache-2.0 — see [LICENSE](LICENSE) for details.

##提取注释

-保存获取的降价/文本，用作Hermes+Obsidian个人知识库计划中的实施证据。
