---
source_url: https://raw.githubusercontent.com/coddingtonbear/obsidian-local-rest-api/master/README.md
retrieved: 2026-05-14
source_type: github
reliability: high
raw_preservation: full_parsed_text
extraction_status: complete
capture_method: raw_github_markdown
content_sha256: e2426731a1bf0464f1f9c4d758b09c3c73fceedf4f84a9eadb866923170a4170
---

#Obsidian本地REST API自述文件

##源元数据

-source_url：https://raw.githubusercontent.com/coddingtonbear/obsidian-local-rest-api/master/README.md
-检索日期：2026-05-14
-source_type：github
-capture_method：raw_github_markdown
-extraction_note：direct_raw_markdown_fetch
-content_sha256：`e2426731a1bf0464f1f9c4d758b09c3c73fceedf4f84a9eadb866923170a4170`

##解析的源文本

#Obsidian的本地REST API和MCP服务器

通过安全、经过身份验证的REST API，让您的脚本、浏览器扩展和人工智能代理直接进入您的黑曜石金库。

**交互式API文档：**https://coddingtonbear.github.io/obsidian-local-rest-api/

##你能做什么

Access your vault through the **REST API** or the **built-in [MCP server](https://modelcontextprotocol.io/)** — both interfaces expose the same core capabilities, so scripts, browser extensions, and AI agents all speak the same language.

-**读取、创建、更新或删除注释**-vault中任何文件（包括二进制文件）的完整CRUD
-**外科手术修补特定部分**-以标题、块引用或frontmatter键为目标，仅附加、前置或替换该部分，而不触及文件的其余部分
- **Search your vault** — simple full-text search or structured [JsonLogic](https://jsonlogic.com/) queries against note metadata (frontmatter, tags, path, content)
-**访问活动文件**-读取或写入当前在Obsidian中打开的任何便笺
-**使用定期笔记**-获取或创建每日、每周、每月、每季度和每年的笔记
-**列出并执行命令**-触发任何黑曜石命令，就像使用命令面板一样
-**查询标签**-列出vault中的所有标签及其使用计数
-**在Obsidian中打开文件**-告诉Obsidian在其UI中打开特定注释
- **Extend the API** — other plugins can register their own routes via the [API extension interface](https://github.com/coddingtonbear/obsidian-local-rest-api/wiki/Adding-your-own-API-Routes-via-an-Extension)

所有请求都通过HTTPS提供自签名证书，并通过API密钥身份验证进行门控。

##快速入门

安装并启用插件后，打开**设置→本地REST API**找到您的API密钥和证书。

###休息API

```sh
# Check the server is running (no auth required)
curl -k https://127.0.0.1:27124/

# List files at the root of your vault
curl -k -H "Authorization: Bearer <your-api-key>" \
  https://127.0.0.1:27124/vault/

# Read a note
curl -k -H "Authorization: Bearer <your-api-key>" \
  https://127.0.0.1:27124/vault/path/to/note.md

# Read a specific heading (URL-embedded target)
curl -k -H "Authorization: Bearer <your-api-key>" \
  https://127.0.0.1:27124/vault/path/to/note.md/heading/My%20Section

# Append a line to a specific heading (PATCH with headers)
curl -k -X PATCH \
  -H "Authorization: Bearer <your-api-key>" \
  -H "Operation: append" \
  -H "Target-Type: heading" \
  -H "Target: My Section" \
  -H "Content-Type: text/plain" \
  --data "New line of content" \
  https://127.0.0.1:27124/vault/path/to/note.md
```

为了避免证书警告，您可以从“https://127.0.0.1:27124/obsidian-local-rest-api.crt”下载并信任证书，或者将您的HTTP客户端直接指向它。

###MCP客户端

MCP服务器运行在“https://127.0.0.1:27124/MCP/”，并要求您通过“授权”头（即“授权：承载<your-api-key>”）提供您的承载令牌进行身份验证。因为插件使用自签名证书，所以您可能需要信任操作系统/客户端中的证书，或者使用“http：//127.0.0.1：27123/mcp/”的普通HTTP端点（在**设置→本地REST API→启用HTTP服务器**下启用）。

####克劳德代码

Claude代码具有本机HTTP MCP支持。添加服务器的最快方法是通过CLI：

```sh
claude mcp add --transport http obsidian https://127.0.0.1:27124/mcp/ \
  --header "Authorization: Bearer <your-api-key>"
```

或者将其手动添加到项目根目录中的`.mcp.json`（项目范围）或通过`claude mcp add--scope user`在用户范围内配置它：

```json
{
  "mcpServers": {
    "obsidian": {
      "type": "http",
      "url": "https://127.0.0.1:27124/mcp/",
      "headers": {
        "Authorization": "Bearer <your-api-key>"
      }
    }
  }
}
```

####克劳德桌面

Claude Desktop does not natively support remote HTTP MCP servers, but you can bridge it with [`mcp-remote`](https://www.npmjs.com/package/mcp-remote) (requires Node.js). Add the following to `claude_desktop_config.json`:

-**macOS：**`~/Library/Application Support/Claude/claude_desktop_config.json`
-**Windows：**`%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "npx",
      "args": [
        "mcp-remote@latest",
        "https://127.0.0.1:27124/mcp/",
        "--header",
        "Authorization: Bearer <your-api-key>"
      ]
    }
  }
}
```

保存文件后重新启动Claude Desktop。

####光标

游标支持流式HTTP MCP传输。将以下内容添加到`~/.cursor/mcp.json`（全局）或`.cursor/mcp.json`（特定于项目）：

```json
{
  "mcpServers": {
    "obsidian": {
      "url": "https://127.0.0.1:27124/mcp/",
      "headers": {
        "Authorization": "Bearer <your-api-key>"
      }
    }
  }
}
```

####其他客户

任何支持流式HTTP传输的MCP客户端都可以使用“Authorization：Bearer<your-api-key>”头连接到“https：//127.0.0.1：27124/MCP/”。有关确切的配置格式，请查阅客户的文档。

##API概述

端点方法描述
|---|---|---|
|`/vault/{path}`|获取PUT PATCH POST DELETE|读取、写入或删除vault中的任何文件|
|`/active/`|GET PUT PATCH POST DELETE|对当前打开的文件进行操作|
|`/periodic/{period}/`|GET PUT PATCH POST DELETE|今天的定期备注（`daily`、`weekly`等）|
|`/periodic/{period}/{year}/{month}/{day}/`|GET PUT PATCH POST DELETE|特定日期的定期注释|
|`/search/simple/`|POST|跨所有笔记全文搜索|
|`/search/`|发布|通过JsonLogic进行结构化搜索|
|`/commands/`|获取|列出可用的黑曜石命令|
|`/commands/{commandId}/`|POST|执行命令|
|`/tags/`|获取|列出所有具有使用计数的标签|
|`/open/{path}`|POST|在Obsidian UI中打开文件|
|`/`|获取|服务器状态和身份验证检查|
|`/mcp/`|获取POST|MCP（模型上下文协议）服务器-将AI代理直接连接到您的保险库|

For full request/response details, see the [interactive docs](https://coddingtonbear.github.io/obsidian-local-rest-api/).

##修补程序说明

“补丁”方法是这个API最有用的特性之一。它允许您在不重写整个文件的情况下进行有针对性的编辑。

指定一个**目标**（标题、块引用或frontmatter键）和一个**操作**（`append`、`prepend`或`replace`），插件将精确地应用更改：

```sh
# Replace the value of a frontmatter field
curl -k -X PATCH \
  -H "Authorization: Bearer <your-api-key>" \
  -H "Operation: replace" \
  -H "Target-Type: frontmatter" \
  -H "Target: status" \
  -H "Content-Type: application/json" \
  --data '"done"' \
  https://127.0.0.1:27124/vault/path/to/note.md
```

See the [interactive docs](https://coddingtonbear.github.io/obsidian-local-rest-api/) for the full list of request headers and options.

##针对特定部分

您可以读取或写入注释的特定部分（标题、块引用或frontmatter字段），而无需获取或替换整个文件。这适用于GET、PUT、POST和PATCH请求。

有两种方法可以指定目标：

**标头**-在任何请求中添加“Target-Type”和“Target”：

```sh
# Read the content under a specific heading
curl -k -H "Authorization: Bearer <your-api-key>" \
  -H "Target-Type: heading" \
  -H "Target: My Section" \
  https://127.0.0.1:27124/vault/path/to/note.md

# Read a frontmatter field
curl -k -H "Authorization: Bearer <your-api-key>" \
  -H "Target-Type: frontmatter" \
  -H "Target: status" \
  https://127.0.0.1:27124/vault/path/to/note.md
```

**URL路径段**（仅限GET、PUT和POST）-在文件名后附加`/<target-type>/<target>`：

```sh
# Read a specific heading
curl -k -H "Authorization: Bearer <your-api-key>" \
  https://127.0.0.1:27124/vault/path/to/note.md/heading/My%20Section

# Read a nested heading (levels separated by ::)
curl -k -H "Authorization: Bearer <your-api-key>" \
  https://127.0.0.1:27124/vault/path/to/note.md/heading/Work/Meetings

# Read a frontmatter field
curl -k -H "Authorization: Bearer <your-api-key>" \
  https://127.0.0.1:27124/vault/path/to/note.md/frontmatter/status

# Replace the content of a heading via PUT
curl -k -X PUT \
  -H "Authorization: Bearer <your-api-key>" \
  -H "Content-Type: text/plain" \
  --data "Updated content" \
  https://127.0.0.1:27124/vault/path/to/note.md/heading/My%20Section

# Append to a heading via POST
curl -k -X POST \
  -H "Authorization: Bearer <your-api-key>" \
  -H "Content-Type: text/plain" \
  --data "Appended content" \
  https://127.0.0.1:27124/vault/path/to/note.md/heading/My%20Section
```

支持的目标类型：“标题”、“块”、“前端问题”。在同一个请求上提供URL嵌入的目标和等效的头会返回“422不可处理的实体”。

##搜索

`发布/搜索/简单/？query=your+terms`运行Obsidian的内置模糊搜索，并返回带有评分上下文片段的匹配文件名。

`POST /search/` accepts a [JsonLogic](https://jsonlogic.com/) expression (content type `application/vnd.olrapi.jsonlogic+json`) and evaluates it against each note's metadata (frontmatter, tags, path, content).

##MCP（模型上下文协议）

>[！注释]
>存在几个Obsidian的第三方MCP服务器，但它们不再是必需的-此插件附带了一个内置的MCP服务器，该服务器在Obsidian内部运行，可以直接访问您的vault的实时元数据、活动文件、定期注释和命令面板。如果您目前使用的是第三方服务器，切换到这个服务器可能会给您带来更好的结果。

该插件包括一个位于`/mcp/`的内置MCP服务器，因此人工智能代理和MCP兼容客户端可以与您的保险库进行交互，而无需手工制作HTTP请求。

**传输：**需要流式HTTP-API密钥身份验证。

###连接客户端

将您的MCP客户端连接到“https：//127.0.0.1：27124/MCP/”。身份验证使用不记名令牌-在**设置→本地REST API**下找到您的API密钥，然后将其传递为：

```
Authorization: Bearer <your-api-key>
```

The exact config syntax varies by client; see the [Quick start](#mcp-clients) examples above or consult your client's documentation for Streamable HTTP remote MCP servers.

>[！警告]
>要安全地连接到MCP服务器，您的客户端必须信任插件的自签名证书。您可以从“https：//127.0.0.1：27124/obsidian-local-rest-api.crt”下载并信任它，或者将您的客户端配置为跳过“127.0.0.1”的TLS验证。
>
>如果在您的环境中无法信任自签名证书，则可以使用`http://127.0.0.1:27123/mcp/`进行不安全的连接
>如果您已在**设置→本地REST API→启用HTTP服务器**下启用HTTP端点，而不是“https://127.0.0.1:27124/mcp/”。

###可用工具

工具说明
|---|---|
|`vault_list`|列出vault目录中的文件和子目录|
|`vault_read`|读取文件的内容、frontmatter、标记和stat|
|`vault_write`|创建或覆盖vault文件|
|`vault_append`|将内容追加到vault文件的末尾|
|`vault_patch`|修补特定标题、块引用或frontmatter字段|
|`vault_delete`|删除vault文件|
|`vault_get_document_map`|列出文件中的标题、块引用和frontmatter字段|
|`active_file_get_path`|返回当前在Obsidian中打开的文件的保管库路径|
|`periodic_note_get_path`|返回当前定期票据的保管库路径（`每日`、`每周`、`每月`、`季度`、`每年`）|
| `search_query` | Search using a [JsonLogic](https://jsonlogic.com/) query against note metadata |
|`search_simple`|使用Obsidian内置搜索进行全文搜索|
|`tag_list`|列出vault中具有使用计数的所有标记|
|`command_list`|列出所有注册的Obsidian命令|
|`command_execute`|按ID执行黑曜石命令|
|`open_file`|在Obsidian UI中打开文件|

###可用资源

URI描述
|---|---|
|`obsidian：//local-rest-api/openapi.yaml`|此REST API的完整OpenAPI规范|

##贡献

See [CONTRIBUTING.md](CONTRIBUTING.md). If you want to add functionality without modifying core, consider building an [API extension](https://github.com/coddingtonbear/obsidian-local-rest-api/wiki/Adding-your-own-API-Routes-via-an-Extension) instead — extensions can be developed and released independently.

##学分

Inspired by [Vinzent03](https://github.com/Vinzent03)'s [advanced-uri plugin](https://github.com/Vinzent03/obsidian-advanced-uri), with the goal of expanding automation options beyond the constraints of custom URL schemes.

##提取注释

-保存获取的降价/文本，用作Hermes+Obsidian个人知识库计划中的实施证据。
