---
source_url: https://help.obsidian.md/uri
retrieved: 2026-05-14
source_type: product-docs
reliability: high
raw_preservation: full_parsed_text
extraction_status: complete
capture_method: obsidian_help_preloaded_markdown
content_sha256: d401a97319322d3d3abf993dc18ab859c127060a54927b01a901781addecd5c1
---

# 黑曜石 URI

## 源元数据

- 来源网址：https://help.obsidian.md/uri
- 检索时间：2026-05-14
- 来源类型：产品文档
- capture_method: obsidian_help_preloaded_markdown
- extract_note：preloaded_markdown_url：https://publish-01.obsidian.md/access/f786db9fac45774fa4f0d8112e232d67/Extending%20Obsidian/Obsidian%20URI.md
- content_sha256：`d401a97319322d3d3abf993dc18ab859c127060a54927b01a901781addecd5c1`

## 解析后的源文本

---
别名：
  - 使用黑曜石 URI
  - 高级主题/使用黑曜石 URI
  - 概念/黑曜石 URI
  - 扩展黑曜石/黑曜石 URI
永久链接： uri
---
Obsidian URI 是 Obsidian 支持的自定义 URI 协议，可让您触发各种操作，例如打开便笺或创建便笺。 Obsidian URI 支持自动化和跨应用程序工作流程。

## URI 格式

Obsidian URI 使用以下格式：

```
obsidian://action?param1=value&param2=value
```

“action”参数是您要执行的操作。可用的操作包括：

- “打开”打开笔记。
- “新建”用于创建或添加到现有笔记。
- “每日”创建或打开您的每日笔记。
- “unique”创建新的独特注释。
- “搜索”打开搜索。
- “选择保管库”打开保管库管理器。

> [!警告] 编码
> 确保您的值经过正确的 URI 编码。例如，正斜杠字符“/”必须编码为“%2F”，空格字符必须编码为“%20”。
> 
 这一点尤其重要，因为编码不正确的“保留”字符可能会破坏 URI 的解释。 [详细信息请参见此处](https://en.wikipedia.org/wiki/Percent-encoding)。

## 打开笔记

“打开”操作打开黑曜石保管库，或打开该保管库内的文件。

### 示例

- `黑曜石://open?vault=my%20vault`
  这将打开保险库“我的保险库”。如果保险库已经打开，请将注意力集中在窗口上。
- `黑曜石://open?vault=ef6ca3e3b524d22f`
  这将打开 ID 为“ef6ca3e3b524d22f”的保管库。
- `黑曜石://open?vault=my%20vault&file=my%20note`
  这将在保管库“myVault”中打开注释“mynote.md”，假设该文件存在。
- `黑曜石://open?path=%2Fhome%2Fuser%2Fmy%20vault%2Fpath%2Fto%2Fmy%20note`
  这将查找包含路径“/home/user/myVault/path/to/mynote”的任何保管库。然后，路径的其余部分将传递给“file”参数。例如，如果保管库存在于“/home/user/myVault”，则这相当于“file”参数设置为“path/to/my note”。


> [!tip] 打开标题或块
> 通过正确的 URI 编码，您可以导航到注释中的标题或块。 `Note%23Heading` 将导航到名为“Heading”的标题，而 `Note%23%5EBlock` 将导航到名为“Block”的块。

＃＃＃ 参数

- `vault` 可以是文件库名称或文件库 ID[^1]。
- `file` 可以是文件名，也可以是从库根到指定文件的路径。如果文件扩展名是“md”，则可以省略扩展名。
- `path` 文件的绝对文件系统路径。
  - 使用此参数将覆盖“vault”和“file”。
  - 这将导致应用程序搜索包含指定文件路径的最具体的保管库。
  - 然后路径的其余部分替换“file”参数。
- `prepend` 将添加到文件顶部并尝试合并属性。
- `append` 将添加到文件末尾并尝试合并属性。
- `paneType`（可选）确定注释将在 UI 中打开的位置。
  - 如果不存在，则替换最后一个活动选项卡。
  - `paneType=tab` 在新选项卡中打开。
  - `paneType=split` 在新选项卡组中打开。
  - `paneType=window` 在弹出窗口中打开（仅限桌面）。

## 创建笔记

“新建”操作会在保管库中创建一个新注释，并可选择包含一些内容。

### 示例

- `黑曜石://new?vault=my%20vault&name=my%20note`
  这将打开保管库“我的保管库”，并创建一个名为“我的笔记”的新笔记。
- `黑曜石://new?vault=my%20vault&file=path%2Fto%2Fmy%20note`
  这将打开保管库“我的保管库”，并在“path/to/my note”处创建一个新笔记。

＃＃＃ 参数

- `vault` 可以是文件库名称，也可以是文件库 ID[^1]。与“打开”操作相同。
- `name` 要创建的文件名。如果指定了此项，将根据您的“新笔记的默认位置”首选项选择文件位置。
- `file` 库绝对路径，包括名称。如果指定，将覆盖“name”。
- `path` 全局绝对路径。与“open”操作中的“path”选项类似，它将覆盖“vault”和“file”。
- `paneType`（可选）确定注释将在 UI 中打开的位置。与“打开”操作相同。
- `content`（可选）注释的内容。
- `clipboard`（可选）使用剪贴板的内容而不是指定`content`。
- 如果您不想打开新笔记，则“silent”（可选）包含此参数。
- `append`（可选）包含此参数以附加到现有文件（如果存在）。
- `overwrite` （可选）覆盖现有文件（如果存在），但前提是未设置 `append`。
- `x-success`（可选）请参阅[[#使用 x-callback-url 参数]]。

## 创建或打开每日笔记

“每日”操作创建或打开您的每日笔记。必须启用[[每日笔记]]插件。

### 示例

- `黑曜石://daily?vault=my%20vault`
  这将打开保管库“我的保管库”，并创建或打开每日笔记。

＃＃＃ 参数

“daily”操作接受与“new”操作相同的参数。

## 独特的注释

“独特”操作会在保管库中创建新的独特注释。必须启用 [[插件/独特笔记创建者|独特笔记创建者]] 插件。

### 示例

- `黑曜石://unique?vault=my%20vault`
  这将打开保管库“我的保管库”，并创建一个新的独特注释。
- - `黑曜石://unique?vault=my%20vault&content=Hello%20World`
  这将打开保管库“我的保管库”，并创建一个内容为“Hello World”的新的唯一注释。

＃＃＃ 参数

- `vault` 可以是文件库名称，也可以是文件库 ID[^1]。与“打开”操作相同。
- `paneType`（可选）确定注释将在 UI 中打开的位置。与“打开”操作相同。
- `content`（可选）注释的内容。
- `clipboard`（可选）使用剪贴板的内容而不是指定`content`。
- `x-success`（可选）请参阅[[#使用 x-callback-url 参数]]。

## 打开搜索

“搜索”操作会在指定的保管库中打开 [[搜索]]，并可选择执行搜索项。

### 示例

- `黑曜石://search?vault=my%20vault`
  这将打开保管库“我的保管库”，并打开[[搜索]]。
- `黑曜石://search?vault=my%20vault&query=黑曜石`
  这将打开保管库“我的保管库”，打开[[搜索]]，然后搜索“黑曜石”。

＃＃＃ 参数

- `vault` 可以是文件库名称，也可以是文件库 ID[^1]。与“打开”操作相同。
- `query`（可选）要执行的搜索词。

## 打开保管库管理器

“选择保管库”操作会打开 [[管理保管库|保管库管理器]]。

### 示例

- `黑曜石://选择金库`

## 与 Hook 集成

This Obsidian URI action is to be used with [Hook](https://hookproductivity.com/). 

＃＃＃ 例子

`黑曜石://hook-get-address`

＃＃＃ 参数

- “vault”（可选）可以是文件库名称，也可以是文件库 ID[^1]。如果未提供，则将使用当前或最后一个聚焦的保管库。
- `x-success`（可选）请参阅[[#使用 x-callback-url 参数]]。
- `x-error`（可选）请参阅[[#使用 x-callback-url 参数]]。

如果定义了“x-success”，则此 API 将使用它作为 x-callback-url。否则，它会将当前焦点笔记的 Markdown 链接复制到剪贴板，作为“obsidian://open” URL。

## 使用 x-callback-url 参数

某些端点将接受 x-callback-url 参数“x-success”和“x-error”。提供后，Obsidian 将向“x-success”回调提供以下内容：

- `name` 文件名，不带文件扩展名。
- `url` 该文件的 `obsidian://` URI。
- `file`（仅限桌面）该文件的 `file://` URL。

例如，如果黑曜石收到
`obsidian://.....x-success=myapp://x-callback-url`，响应将是 `myapp://x-callback-url?name=...&url=obsidian%3A%2F%2Fopen...&file=file%3A%2F%2F...`

## 简写格式

除了上述格式之外，还有两种“速记”格式可用于打开保管库和文件：

1. `obsidian://vault/myVault/mynote` 相当于 `obsidian://open?vault=my%20vault&file=my%20note`。
2. `obsidian:///absolute/path/to/my note` 相当于 `obsidian://open?path=%2Fabsolute%2Fpath%2Fto%2Fmy%20note`。

## 故障排除

### 注册黑曜石 URI

在 Windows 和 macOS 上，运行一次应用程序就足以在您的计算机上注册 Obsidian URI 协议。

在 Linux 上，这是一个更加复杂的过程：

1. Ensure you create a `obsidian.desktop` file. [See here for details](https://developer.gnome.org/documentation/guidelines/maintainer/integrating.html#desktop-files).
2. 确保您的桌面文件将“Exec”字段指定为“Exec=executable %u”。 `%u` 用于将 `obsidian://` URI 传递给应用程序。
3. 如果您使用 AppImage 安装程序，则可能需要使用“Obsidian-x.y.z.AppImage --appimage-extract”将其解压。然后确保“Exec”指令指向解压的可执行文件。


[^1]：保管库 ID 是分配给保管库的随机 16 个字符代码，例如“ef6ca3e3b524d22f”。此 ID 对于计算机上的每个文件夹都是唯一的。可以通过打开保管库切换器并单击所需保管库的上下文菜单中的“复制保管库 ID”来找到该 ID。

## 摘录笔记

- 保留获取的降价/文本，用作 Hermes + Obsidian 个人知识库计划中的实施证据。
