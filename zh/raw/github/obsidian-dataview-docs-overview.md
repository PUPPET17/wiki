---
source_url: https://raw.githubusercontent.com/blacksmithgu/obsidian-dataview/master/docs/docs/index.md
retrieved: 2026-05-14
source_type: github
reliability: high
raw_preservation: full_parsed_text
extraction_status: complete
capture_method: raw_github_markdown
content_sha256: 7d26a2ba66020c8ad5a2879e552ff34842342bfecaae16b2a43019bb27dce3b8
---

#Obsidian Dataview文档概述

##源元数据

-source_url：https://raw.githubusercontent.com/blacksmithgu/obsidian-dataview/master/docs/docs/index.md
-检索日期：2026-05-14
-source_type：github
-capture_method：raw_github_markdown
-extraction_note：direct_raw_markdown_fetch
-content_sha256：`7d26a2ba66020c8ad5a2879e552ff34842342bfecaae16b2a43019bb27dce3b8`

##解析的源文本

#概述

Dataview is a live index and query engine over your personal knowledge base. You can [**add metadata**](annotation/add-metadata.md) to your notes and **query** them with the [**Dataview Query Language**](queries/structure.md) to list, filter, sort or group your data. Dataview keeps your queries always up to date and makes data aggregation a breeze.

你可以

-通过记录在每日笔记中来跟踪您的睡眠，并自动创建每周睡眠时间表表。
-自动收集笔记中的书籍链接，并按评级排序。
-自动收集与今天日期相关联的页面，并将其显示在您的每日笔记中。
-查找没有标签的页面以进行后续操作，或显示带有特定标签的页面的漂亮视图。
-创建动态视图，显示笔记中记录的即将到来的生日或事件

还有更多的事情。

!!!提示“Dataview为您提供了一种快速搜索、显示和操作vault中索引数据的方法！”

Dataview是高度通用和高性能的，可以毫无问题地扩展到数十万个注释。

If the built in [query language](queries/structure.md) is insufficient for your purpose, you can run arbitrary
JavaScript against the [dataview API](api/intro.md) and build whatever utility you might need yourself, right in your notes.

!!!信息“Dataview是关于显示，而不是编辑”
    Dataview is meant for displaying and calculating data. It is not meant to edit your notes/metadata and will always leave them untouched (... except if you're checking a [Task](queries/query-types.md#task) through Dataview.)

##如何使用Dataview

Dataview由两个大的构建模块组成：**数据索引**和**数据查询**。

!!!信息“有关链接文档页面的更多详细信息”
下面的部分应该会给你一个关于你可以用dataview做什么以及如何做的概述。请务必访问链接页面，了解有关各个部分的更多信息。

###数据索引

Dataview operates on metadata in your Markdown files. It cannot read everything in your vault, but only specific data. Some of your content, like tags and bullet points (including tasks), are [available automatically](annotation/add-metadata.md#implicit-fields) in Dataview. You can add other data through **fields**, either on top of your file [per YAML Frontmatter](annotation/add-metadata.md#frontmatter) or in the middle of your content with [Inline Fields](annotation/add-metadata.md#inline-fields) via the `[key:: value]` syntax. Dataview _indexes_ these data to make it available for you to query. 

!!! hint "Dataview indexes [certain information](annotation/add-metadata.md#implicit-fields) like tags and list items and the data you add via fields. Only indexed data is available in a Dataview query!"

例如，文件可能如下所示：

```markdown
---
author: "Edgar Allan Poe"
published: 1845
tags: poems
---

# The Raven

Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore—
```

或者像这样：

```markdown
#poems

# The Raven

From [author:: Edgar Allan Poe], written in (published:: 1845)

Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore—
```

In terms of indexed metadata (or what you can query), they are identical, and only differ in their annotation style. How you want to [annotate your  metadata](annotation/add-metadata.md) is up to you and your personal preference. With this file, you'd have the **metadata field** `author` available and everything Dataview provides you [automatically as implicit fields](annotation/metadata-pages.md), like the tag or note title. 

!!!注意“数据需要索引”
在上面的示例中，you_do_not_have poem本身在Dataview中可用：它是一个段落，而不是元数据字段，也不是Dataview自动索引的内容。它不是Dataviews索引的一部分，因此您无法查询它。

###数据查询

您可以在**查询**的帮助下访问**索引数据**。

There are **three different ways** you can write a Query: With help of the [Dataview Query Language](queries/dql-js-inline.md#dataview-query-language-dql), as an [inline statement](queries/dql-js-inline.md#inline-dql) or in the most flexible but most complex way: as a [Javascript Query](queries/dql-js-inline.md#dataview-js). 

The **Dataview Query Language** (**DQL**) gives you a broad and powerful toolbelt to query, display and operate on your data. An [**inline query**](queries/dql-js-inline.md#inline-dql) gives you the possibility to display exactly one indexed value anywhere in your note. You can also do calculations this way. With **DQL** at your hands, you'll be probably fine without any Javascript through your data journey.

DQL查询由几个部分组成：

- Exactly one [**Query Type**](queries/query-types.md) that determines what your Query Output looks like
- None or one [**FROM statement**](queries/data-commands.md#from) to pick a specific tag or folder (or another [source](reference/sources.md)) to look at
- None to multiple [**other Data Commands**](queries/data-commands.md) that help you filter, group and sort your wanted output

例如，查询可以如下所示：

~~~markdown
```dataview
LIST
```
~~~

其中列出了保险库中的所有文件。

!!!信息“除查询类型外的所有内容都是可选的”
    The only thing you need for a valid DQL Query is the Query Type (and on [CALENDAR](queries/query-types.md#calendar)s, a date field.)

更受限制的查询可能如下所示：

~~~markdown
```dataview
LIST
FROM #poems
WHERE author = "Edgar Allan Poe"
```
~~~

which lists all files in your vault that have the tag `#poems` and a [field](annotation/add-metadata.md) named `author` with the value `Edgar Allan Poe`. This query would find our example page from above. 

`LIST` is only one out of four [Query Types](queries/query-types.md) you can use. For example, with a `TABLE`, we could add some more information to our output: 


~~~markdown
```dataview
TABLE author, published, file.inlinks AS "Mentions"
FROM #poems
```
~~~

这将返回如下结果：

|档案(3)|作者|发表|提及|
|--------|-------|----------|--------|
|钟声|埃德加·爱伦·坡|1849|
|新巨像|艾玛·拉撒路|1883|-[[最喜欢的诗]]|
《乌鸦》埃德加·爱伦·坡1845-[[最喜欢的诗]]

That's not where the capabilities of dataview end, though. You can also **operate on your data** with help of [**functions**](reference/functions.md). Mind that these operations are only made inside your query - your **data in your files stays untouched**.

~~~markdown
```dataview
TABLE author, date(now).year - published AS "Age in Yrs", length(file.inlinks) AS "Counts of Mentions"
FROM #poems
```
~~~

还给你

|文件（3）|作者|年龄（岁）|提及次数|
|--------|-------|----------|--------|
钟声|埃德加·爱伦·坡|173|0|
|新巨像|艾玛·拉撒路|139|1|
|乌鸦|埃德加爱伦坡|177|1|

!!! info "Find more examples [here](resources/examples.md)."

如您所见，dataview不仅允许您快速聚合数据并始终保持最新，还可以帮助您进行操作，为您提供有关数据集的新见解。浏览文档，了解有关如何与数据交互的更多信息。

祝你以新的方式探索你的金库愉快！

##资源和帮助

This documentation is not the only place that can help you out on your data journey. Take a look at [Resources and Support](./resources/resources-and-support.md) for a list of helpful pages and videos.

##提取注释

-保存获取的降价/文本，用作Hermes+Obsidian个人知识库计划中的实施证据。
