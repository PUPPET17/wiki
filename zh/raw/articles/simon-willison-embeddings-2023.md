---
source_url: https://simonwillison.net/2023/Oct/23/embeddings/
fetched_url: https://simonwillison.net/2023/Oct/23/embeddings/
source_type: blog
author: Simon Willison
source_date: 2023-10-23
ingested: 2026-05-14
sha256: 22776b1270a41b054c4651e9e24445f929ba0c33ec36384be0b996a06b6ad441
raw_preservation: full_html_article_text_candidate
extraction_method: readability_lxml_html2text
html_bytes: 68598
parsed_chars: 38050
---

#嵌入：它们是什么以及为什么它们很重要

##源元数据

-来源网址：https://simonwillison.net/2023/Oct/23/embeddings/
-获取的网址：https://simonwillison.net/2023/Oct/23/embeddings/
-来源类型：博客
——作者：西蒙·威廉森
-来源日期：2023-10-23
-摄入日期：2026-05-14
-可靠性：高
-原始保存状态：full_html_article_text_candidate
-提取方式：readability_lxml_html2text

##解析的源文本

##嵌入：它们是什么以及为什么它们很重要

2023年10月23日

嵌入是一个非常巧妙的技巧，通常被包裹在一堆令人生畏的行话中。

如果你能理解这些行话，它们会释放出强大而令人兴奋的技术，可以应用于各种有趣的问题。

I gave a talk about embeddings at [PyBay 2023](https://pybay.com/). This article represents an improved version of that talk, which should stand alone even without watching the video.

如果您还不熟悉嵌入，我希望为您提供开始将它们应用于现实世界问题所需的一切。

在本文中：

####38分钟视频版

Here’s [a video](https://www.youtube.com/watch?v=ArnMdc-ICCM&t=50s) of the talk that I gave at PyBay:

The audio quality of the official video wasn’t great due to an issue with the microphone, but I ran that audio through Adobe’s [Enhance Speech tool](https://podcast.adobe.com/enhance) and uploaded my own video with the enhanced audio to YouTube.

####什么是嵌入？

嵌入是一项与更广泛的大型语言模型领域相邻的技术——ChatGPT、Gemini和Claude背后的技术。

Image: On the left, a blog entry titled Storing and serving related documents with oepnai-to-sqlite and embeddings. On the right, a JSON array of floating point numbers, with the caption Fixed zise: 300, 1000, 1536... (https://static.simonwillison.net/static/2023/embeddings/embeddings.002.jpeg)

Embeddings are based around one trick: take a piece of content—in this case [a blog entry](https://til.simonwillison.net/llms/openai-embeddings-related-content)—and turn that piece of content into an array of floating point numbers.

该数组的关键在于，无论内容有多长，它都将始终具有相同的长度。长度由您使用的嵌入模型定义——数组可能有300、1,000或1,536个数字长。

思考这个数字数组的最好方法是把它想象成一个非常奇怪的多维空间中的坐标。

1,536维空间很难可视化，所以这里有一个相同想法的3D可视化：

Image: a 3D chart showing a location in many-multi-dimensional space. 400 randomly placed red dots are scattered around the chart. (https://static.simonwillison.net/static/2023/embeddings/embeddings.003.jpeg)

为什么要在这个空间放置内容？因为我们可以根据该内容的位置——特别是附近的其他内容——了解该内容的有趣之处。

根据嵌入模型对世界的怪异、几乎不可理解的理解，空间内的位置代表了内容的语义。它可能捕获已经嵌入的内容的颜色、形状、概念或各种其他特征。

没有人完全理解这些单个数字的含义，但我们知道它们的位置可以用来找到关于内容的有用信息。

####使用嵌入的相关内容

One of the first problems I solved with embeddings was to build a “related content” feature for [my TIL blog](https://til.simonwillison.net/). I wanted to be able to show a list of related articles at the bottom of each page.

I did this using embeddings—in this case, I used the OpenAI `text-embedding-ada-002` model, which is available [via their API](https://platform.openai.com/docs/guides/embeddings).

我的网站上目前有472篇文章。我计算了每篇文章的1,536维嵌入向量（浮点数数组），并将这些向量存储在我网站的SQLite数据库中。

现在，如果我想查找给定文章的相关文章，我可以计算该文章的嵌入向量与数据库中其他文章之间的_cosine similarity_between，然后按距离返回10个最接近的匹配。

There’s an example at [the bottom of this page](https://til.simonwillison.net/sqlite/sqlite-tg#related). The top five related articles for [Geospatial SQL queries in SQLite using TG, sqlite-tg and datasette-sqlite-tg](https://til.simonwillison.net/sqlite/sqlite-tg) are:

这是一个相当好的列表！

Here’s [the Python function](https://github.com/simonw/llm/blob/bf229945fe57036fa75e8105e59d9e506a720156/llm/__init__.py#L252C1-L256C53) I’m using to calculate those cosine similarity distances:

def余弦相似性（a，b）：
dot_product=sum(x*y对于zip(a，b)中的x，y)
magnitude_a=sum(x*x对于a中的x)**0.5
magnitude_b=sum(x*x对于b中的x)**0.5
返回dot_product/(magnitude_a*magnitude_b)

My TIL site runs on my [Datasette](https://datasette.io/) Python framework, which supports building sites on top of a SQLite database. I wrote more about how that works in [the Baked Data architectural pattern](https://simonwillison.net/2021/Jul/28/baked-data/).

You can browse the SQLite table that stores the calculated embeddings at [tils/embeddings](https://til.simonwillison.net/tils/embeddings).

Image: Screenshot of the embeddings table in Datasette, it has 472, rows each of which consists of a text ID and a binary 6.144 bytes embedding (https://static.simonwillison.net/static/2023/embeddings/til-simonwillison-net-tils-embeddings.png)

Those are binary values. We can [run this SQL query](https://til.simonwillison.net/tils?sql=select+id%2C+hex%28embedding%29+from+embeddings) to view them as hexadecimal:

从嵌入中选择id，十六进制（嵌入）

Image: Running that SQL query in Datasette returns text IDs and long hexadecimal strings for each embedding (https://static.simonwillison.net/static/2023/embeddings/til-simonwillison-net-tils.png)

不过，可读性仍然不强。我们可以使用自定义SQL函数“大语言模型嵌入解码()”将它们转换为JSON数组：

从嵌入限制10中选择id、大语言模型_嵌入_解码(嵌入)

[Try that here](https://til.simonwillison.net/tils?sql=select+id%2C+llm_embed_decode%28embedding%29+from+embeddings+limit+10). It shows that each article is accompanied by that array of 1,536 floating point numbers.

Image: Now the SQL query returns a JSON array of floating point numbers for each ID (https://static.simonwillison.net/static/2023/embeddings/til-simonwillison-net-tils.1.png)

我们可以使用另一个自定义SQL函数“大语言模型嵌入余弦(vector1, vector2)”来计算这些余弦距离并找到最相似的内容。

That SQL function [is defined here](https://github.com/simonw/datasette-llm-embed/blob/ebded67fa9ee19db2c4b1badb1895cef0d58ac4a/datasette_llm_embed.py#L22-L26) in my [datasette-llm-embed](https://datasette.io/plugins/datasette-llm-embed) plugin.

下面是一个查询，返回与我的SQLite TG文章最相似的五篇文章：

选择
身份证，
大语言模型_嵌入_余弦(
嵌入，
(
选择
嵌入
来自
嵌入
哪里
id='sqlite_sqlite-tg.md'
)
）作为分数
来自
嵌入
排序依据
分数描述
限度5

[Executing that query](https://til.simonwillison.net/tils?sql=select%0D%0A++id%2C%0D%0A++llm_embed_cosine%28%0D%0A++++embedding%2C%0D%0A++++%28%0D%0A++++++select%0D%0A++++++++embedding%0D%0A++++++from%0D%0A++++++++embeddings%0D%0A++++++where%0D%0A++++++++id+%3D+%27sqlite_sqlite-tg.md%27%0D%0A++++%29%0D%0A++%29+as+score%0D%0Afrom%0D%0A++embeddings%0D%0Aorder+by%0D%0A++score+desc%0D%0Alimit+5) returns the following results:

id|分数
---|---
sqlite_sqlite-tg.md|1.0
sqlite_geopoly.md|0.8817322855676049
spatialite_viewing-geopackage-data-with-spatialite-and-datasette.md|0.8813094978399854
gis_gdal-sql.md|0.8799581261326747
spatialite_knn.md|0.8692992294266506
  
不出所料，文章与自身的相似度为1.0。其他文章都与SQLite中的地理空间SQL查询有关。

This query takes around 400ms to execute. To speed things up, I pre-calculate the top 10 similarities for every article and store them in a separate table called [tils/similarities](https://til.simonwillison.net/tils/similarities).

Image: The similarities table has 4,922 rows each with an id, other_id and score column. (https://static.simonwillison.net/static/2023/embeddings/til-simonwillison-net-tils-similarities.png)

I wrote a Python function to [look up related documents from that table](https://github.com/simonw/til/blob/a244856c72000760c2939550ae2a78266dee4f07/plugins/template_vars.py#L21-L37) and [called it from the template](https://github.com/simonw/til/blob/a244856c72000760c2939550ae2a78266dee4f07/templates/pages/%7Btopic%7D/%7Bslug%7D.html#L37-L45) that’s used to render the article page.

My [Storing and serving related documents with openai-to-sqlite and embeddings](https://til.simonwillison.net/llms/openai-embeddings-related-content) TIL explains how this all works in detail, including how GitHub Actions are used to fetch new embeddings [as part of the build script](https://github.com/simonw/til/blob/a244856c72000760c2939550ae2a78266dee4f07/.github/workflows/build.yml#L67-L75) that deploys the site.

我在这个项目中使用了OpenAI embeddings API。它非常便宜——在我的TIL网站上，我嵌入了大约402,500个代币，按0.0001美元/1,000个代币计算，相当于0.04美元——只需4美分！

它真的很容易使用：你在它上面发布一些文本和你的API键，它会给你返回浮点数的JSON数组。

Image: Screenshot of curl against api.openai.com/v1/embeddings sending a Bearer token header and a JSON body specifying input text and the text-embedding-ada-002 model. The API responds with a JSON list of numbers. (https://static.simonwillison.net/static/2023/embeddings/embeddings.006.jpeg)

But... it’s a proprietary model. A few months ago OpenAI [shut down some of their older embeddings models](https://openai.com/blog/gpt-4-api-general-availability#deprecation-of-older-embeddings-models), which is a problem if you’ve stored large numbers of embeddings from those models since you’ll need to recalculate them against a supported model if you want to be able to embed anything else new.

Image: Screenshot of the OpenAI First-generation text embedding models list, showing the shutdown date of 4th April 2024 for 7 legacy models. (https://static.simonwillison.net/static/2023/embeddings/embeddings.007.jpeg)

值得称赞的是，OpenAI确实承诺“支付用户使用这些新模型重新嵌入内容的财务成本”。–但这仍然是对依赖专有模型保持谨慎的一个理由。

好消息是，有非常强大的公开许可模型，你可以在自己的硬件上运行，避免任何被关闭的风险。我们稍后会详细讨论这个问题。

####探索这些东西如何与Word2Vec一起工作

谷歌研究在10年前发表了一篇有影响力的论文，描述了他们创建的一个名为Word2Vec的早期嵌入模型。

That paper is [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781), dated 16th January 2013. It’s a paper that helped kick off widespread interest in embeddings.

Word2Vec是一个模型，它将单个单词转换成300个数字的列表。这个数字列表抓住了相关单词的一些含义。

一个演示最好地说明了这一点。

[turbomaze.github.io/word2vecjson](https://turbomaze.github.io/word2vecjson/) is an interactive tool put together by [Anthony Liu](https://anthony.ai/) with a 10,000 word subset of the Word2Vec corpus. You can view [this JavaScript file](https://turbomaze.github.io/word2vecjson/data/wordvecs10000.js) to see the JSON for those 10,000 words and their associated 300-long arrays of numbers.

Image: Screenshot of the Word to Vec JS Demo showing the results for france and the algebra results for germany + paris - france (https://static.simonwillison.net/static/2023/embeddings/word2vec.jpg)

搜索一个单词，根据与其Word2Vec表示的余弦距离查找相似的单词。例如，单词“france”返回以下相关结果：

词|相似性
---|---
法国|1
法语|0.7000748343471224
比利时|0.6933180492111168
巴黎|0.6334910653433325
德国|0.627075617939471
意大利|0.6135215284228007
西班牙|0.6064218103692152
  
那是法国事物和欧洲地理的混合体。

这里你可以做的一件非常有趣的事情是对这些向量执行算术。

取“德国”的向量，加上“巴黎”，减去“法国”。得到的向量最接近“柏林”！

这个模型已经抓住了国籍和地理的概念，以至于你可以使用算术来探索关于世界的其他事实。

Word2Vec接受了16亿字内容的训练。我们今天使用的嵌入模型是在更大的数据集上训练的，并捕获了对底层关系的更丰富的理解。

I’ve been building a command-line utility and Python library called [LLM](https://llm.datasette.io/).

您可以在此处阅读有关大语言模型的更多信息：

大语言模型是一种处理大型语言模型的工具。您可以这样安装：

或通过自制：

You can use it as a command-line tool for interacting with LLMs, or as [a Python library](https://llm.datasette.io/en/stable/python-api.html).

Out of the box it can work with the OpenAI API. Set [an API key](https://llm.datasette.io/en/stable/setup.html#saving-and-using-stored-keys) and you can run commands like this:

大语言模型“宠物鹈鹕的十个有趣名字”

Where it gets really fun is when you start [installing plugins](https://llm.datasette.io/en/stable/plugins/index.html). There are plugins that add entirely new language models to it, including models that run directly on your own machine.

A few months ago [I extended LLM](https://simonwillison.net/2023/Sep/4/llm-embeddings/) to support plugins that can run embedding models as well.

Here’s how to run the catchily titled [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) model using LLM:

Image: Slide showing the commands listed below (https://static.simonwillison.net/static/2023/embeddings/embeddings.014.jpeg)

First, we install `llm` and then use that to install the [llm-sentence-transformers](https://github.com/simonw/llm-sentence-transformers) plugin—a wrapper around the [SentenceTransformers](https://www.sbert.net/) library.

pip安装大语言模型
大语言模型安装大语言模型句子变形金刚

接下来，我们需要注册“all-MiniLM-L6-v2”模型。这将从Hugging Face下载模型到您的计算机：

大语言模型句子-变形金刚寄存器all-MiniLM-L6-v2

我们可以通过嵌入这样一个句子来测试这一点：

大语言模型embed-m句子转换器/all-MiniLM-L6-v2\
-c“你好世界”

这将输出一个JSON数组，其开头如下：

`[-0.03447725251317024, 0.031023245304822922, 0.006734962109476328, 0.026108916848897934,-0.03936201333999634,...`

像这样的嵌入本身并不是很有趣——我们需要存储和比较它们来开始获得有用的结果。

LLM can store embeddings in a “collection”—a SQLite table. The [embed-multi command](https://llm.datasette.io/en/stable/embeddings/cli.html#llm-embed-multi) can be used to embed multiple pieces of content at once and store them in a collection.

这就是下一个命令的作用：

大语言模型嵌入-多自述文件\
--模型句-transformers/all-MiniLM-L6-v2\
--文件~/'**/README.md'--存储

这里我们填充一个名为“readmes”的集合。

“-files”选项接受两个参数：一个要搜索的目录和一个要匹配文件名的glob模式。在本例中，我递归地在主目录中搜索任何名为“自述文件.md”的文件。

“-store”选项使大语言模型除了嵌入向量之外，还将原始文本存储在SQLite表中。

这个命令在我的电脑上运行大约花了30分钟，但是它成功了！我现在有一个名为“readmes”的集合，有16,796行——在我的主目录中找到的每个“README.md”文件对应一行。

####基于共鸣的搜索

Now that we have a collection of embeddings, we can run searches against it using the [llm similar command](https://llm.datasette.io/en/stable/embeddings/cli.html#llm-similar):

Image: A terminal running llm similar and piping the results through jq (https://static.simonwillison.net/static/2023/embeddings/embeddings.015.jpeg)

大语言模型类似自述文件-c'sqlite备份工具'|jq.id

我们要求在“自述文件”集合中提供类似于短语“sqlite备份工具”的嵌入向量的项目。

默认情况下，该命令输出JSON，其中包括自述文件的全文，因为我们之前使用`--store'存储了它们。

通过“jq.id”管道传输结果会导致命令只输出匹配行的id。

最匹配的结果是：

"sqlite-diffable/README.md"
"sqlite-dump/README.md"
"ftstri/salite/ext/repair/README.md"
"simonw/README.md"
"sqlite-generate/README.md"
"sqlite-history/README.md"
"dbf-to-sqlite/README.md"
"ftstri/sqlite/ext/README.md"
"sqlite-utils/README.md"
“ftstri/sqlite/README.md”

这些都是好结果！这些自述文件中的每一个要么描述了一个使用SQLite备份的工具，要么描述了一个以某种方式与备份相关的项目。

有趣的是，不能保证术语“备份”直接出现在这些自述文件的文本中。内容在语义上与该短语相似，但可能不是精确的文本匹配。

我们可以称之为语义搜索。我喜欢把它想象成**基于共鸣的搜索**。

这些自述文件的共鸣与我们的搜索词有关，根据这种奇怪的多维空间表示的词义。

这非常有用。如果你曾经为一个网站建立过搜索引擎，你就会知道完全匹配并不总是能帮助人们找到他们想要的东西。

我们可以使用这种语义搜索来为一大堆不同种类的内容建立更好的搜索引擎。

####使用Symbex的代码嵌入

Another tool I’ve been building is called [Symbex](https://github.com/simonw/symbex). It’s a tool for exploring the symbols in a Python codebase.

I [originally built it](https://simonwillison.net/2023/Jun/18/symbex/) to help quickly find Python functions and classes and pipe them into LLMs to help explain and rewrite them.

然后我意识到我可以用它来计算代码库中所有函数的嵌入，并使用这些嵌入来构建代码搜索引擎。

我添加了一个功能，可以输出JSON或CSV来表示它找到的符号，使用与“大语言模型嵌入多”可以用作输入的输出格式相同的输出格式。

Here’s how I built a collection of all of the functions in my [Datasette](https://github.com/simonw/datasette) project, using a newly released model called [gte-tiny](https://huggingface.co/TaylorAI/gte-tiny)—just a 60MB file!

大语言模型句子-变形金刚寄存器TaylorAI/gte-tiny
    
cd数据集/数据集
    
symbex'*''*：*'--nl|\
大语言模型嵌入式-多功能-\
--范文-transformers/TaylorAI/gte-tiny\
--格式nl\
——商店

`symbex'*''*：*'--nl`查找当前目录中的所有函数(`*`)和类方法（`*：*`模式），并将它们作为换行符分隔的JSON输出。

大语言模型嵌入式多...--format nl`命令需要换行分隔的JSON作为输入，因此我们可以将`symbex`的输出直接通过管道传输到其中。

这默认将嵌入存储在默认的大语言模型SQLite数据库中。您可以添加`--database/tmp/data.db`来指定替代位置。

现在……我可以对我的代码库运行基于vibes的语义搜索！

我可以使用“大语言模型相似”命令，但我也可以使用Datasette本身运行这些搜索。

Here’s a SQL query for that, using the [datasette-llm-embed](https://datasette.io/plugins/datasette-llm-embed) plugin from earlier:

输入为（
选择
大语言模型_嵌入(
'sentence-transformers/TaylorAI/gte-tiny'，
：输入
）作为和
)
选择
身份证，
内容
来自
嵌入，
输入
哪里
collection_id=(
从name='functions'的集合中选择id
)
排序依据
大语言模型_嵌入_余弦（嵌入，input.e）描述
限度5

Datasette会自动将`：input`参数转换为表单字段。

当我运行这个程序时，我得到了与列出插件的概念相关的函数：

Image: Running that query in Datasette with an input of list plugins returns the plugins\(\) function from the cli.py file on line 175 (https://static.simonwillison.net/static/2023/embeddings/list-plugins.jpg)

这里的关键思想是使用SQLite作为集成点——将多种工具组合在一起的基础。

我可以运行单独的工具，从代码库中提取函数，通过嵌入模型运行它们，将这些嵌入写入SQLite，然后对结果运行查询。

任何可以通过管道进入工具的东西现在都可以被这个生态系统的其他组件嵌入和处理。

####使用剪辑将文本和图像嵌入在一起

My current favorite embedding model is [CLIP](https://openai.com/blog/clip/).

CLIP是OpenAI在2021年1月发布的一个令人着迷的模型，当时他们还在公开地做大多数事情，它可以嵌入文本和图像。

至关重要的是，它将它们嵌入到同一个向量空间中。

如果您嵌入字符串“dog”，您将在512维空间中获得一个位置（取决于您的剪辑配置）。

如果你嵌入一张狗的照片，你会在同一个空间得到一个位置...而且在距离上会接近弦“狗”的位置！

这意味着我们可以使用文本搜索相关图像，并使用图像搜索相关文本。

I built [an interactive demo](https://observablehq.com/@simonw/openai-clip-in-a-browser) to help explain how this works. The demo is an Observable notebook that runs the CLIP model directly in the browser.

这是一个相当沉重的页面——它必须加载158MB的资源（64.6 MB用于剪辑文本模型，87.6 MB用于图像模型）——但一旦加载，您就可以使用它来嵌入图像，然后嵌入一串文本并计算两者之间的距离。

我可以给它这张我拍的海滩照片：

Image: A bright blue sky over a beach, with sandy cliffs and the Pacific ocean in the frame (https://static.simonwillison.net/static/2023/embeddings/beach.jpg)

然后键入不同的文本字符串以计算相似性得分，此处显示为百分比：

Image: Animation showing different similarity scores for different text strings (https://static.simonwillison.net/static/2023/embeddings/clip.gif)

文|评分
---|---
海滩|26.946%
城市|19.839%
阳光|24.146%
阳光海滩|26.741%
加州|25.686%
加州海滩|27.427%
  
令人惊讶的是，我们可以在浏览器中运行的JavaScript中完成所有这些工作！

有一个明显的问题：能够随意拍一张照片并说“这和‘城市’这个术语有多相似？”实际上并没有那么有用。

诀窍是在此基础上构建额外的接口。再一次，我们有能力建立基于共鸣的搜索引擎。

这里有一个很好的例子。

####水龙头查找器：用夹子查找水龙头

[Drew Breunig](https://www.dbreunig.com/) used LLM and my [llm-clip](https://github.com/simonw/llm-clip) plugin to build a search engine for faucet taps.

他正在翻新他的浴室，他需要买新的水龙头。因此，他从一家水龙头供应公司收集了20,000张水龙头的照片，并对所有这些照片进行了剪辑。

He used the result to build [Faucet Finder](https://faucet-finder.fly.dev/)—a custom tool (deployed using Datasette) for finding faucets that look similar to other faucets.

Image: The Faucet Finder homepage - six faucets, each with a Find Similar button. (https://static.simonwillison.net/static/2023/embeddings/faucet-finder.jpg)

除此之外，这意味着你可以找到一个你喜欢的昂贵水龙头，然后寻找视觉上相似的更便宜的选择！

Drew wrote more about his project in [Finding Bathroom Faucets with Embeddings](https://www.dbreunig.com/2023/09/26/faucet-finder.html).

Drew的演示使用预先计算的嵌入来显示类似的结果，而不必在服务器上运行剪辑模型。

Inspired by this, I spent some time figuring out [how to deploy a server-side CLIP model](https://til.simonwillison.net/fly/clip-on-fly) hosted by my own [Fly.io](https://fly.io/) account.

Drew’s Datasette instance [includes this table](https://faucet-finder.fly.dev/faucets/embeddings) of embedding vectors, exposed via the Datasette API.

I deployed my own instance with [this API](https://clip-datasette-on-fly.fly.dev/_memory?sql=select+hex\(llm_embed\(%27clip%27%2C+%3Aq\)\)+as+x&q=purple) for embedding text strings, then built an Observable notebook demo that hits both APIs and combines the results.

[observablehq.com/@simonw/search-for-faucets-with-clip-api](https://observablehq.com/@simonw/search-for-faucets-with-clip-api)

现在我可以搜索“金紫”之类的东西，并返回基于vibes的水龙头结果：

Image: Observable notebook: Search for Faucets with CLIP. The search term gold purple produces 8 alarmingly tasteless faucets in those combined colors. (https://static.simonwillison.net/static/2023/embeddings/clip-gold-purple.jpg)

能够在几个小时内启动这种超特定的搜索引擎正是让我兴奋的技巧，因为我的工具箱中有嵌入作为一种工具。

####聚类嵌入

相关内容和基于语义/共鸣的搜索是嵌入的两个最常见的应用，但是你也可以用它们做很多其他有趣的事情。

其中之一是聚类。

I built a plugin for this called [llm-cluster](https://github.com/simonw/llm-cluster) which implements this using [sklearn.cluster](https://scikit-learn.org/stable/modules/clustering.html) from scikit-learn.

To demonstrate that, I used my [paginate-json](https://github.com/simonw/paginate-json) tool and the GitHub issues API to collect the titles of all of the issues in my `simonw/llm` repository into a collection called `llm-issues`:

paginate-json'https://api.github.com/repos/simonw/llm/issues?state=all&filter=all'\
|jq'[.[]|{id：.id, title：.title}]'\
|大语言模型嵌入-多大语言模型-问题-\
——商店

现在我可以创建10组这样的问题：

大语言模型安装大语言模型-集群
    
大语言模型大语言模型集群-第10期

集群作为JSON数组输出，输出如下所示（截断）：

[
{
"id"："2",
“项目”：[
{
"id"："1650662628",
"内容"："初始设计"
},
{
"id"："1650682379",
"content"："记录对SQLite的提示和响应"
}
]
},
{
"id"："4",
“项目”：[
{
"id"："1650760699",
“内容”：“大语言模型web命令-启动web服务器”
},
{
"id"："1759659476",
"content"："`大语言模型模型'命令"
},
{
"id"："1784156919",
"content"："`llm.get_model(alias)`helper"
}
]
},
{
"id"："7",
“项目”：[
{
"id"："1650765575",
"content"："--用于输出代码的代码模式"
},
{
"id"："1659086298",
"content"："接受来自--stdin的提示"
},
{
"id"："1714651657",
"content"："接受标准输入"
}
]
}
]

这些似乎是相关的，但我们可以做得更好。“大语言模型集群”命令有一个“-summary”选项，该选项使它通过一个大语言模型传递结果集群文本，并使用它为每个集群生成一个描述性名称：

大语言模型大语言模型集群-第10期--摘要

This gives back names like “Log Management and Interactive Prompt Tracking” and “Continuing Conversation Mechanism and Management”. See [the README](https://github.com/simonw/llm-cluster/blob/main/README.md#generating-summaries-for-each-cluster) for more details.

####使用主成分分析进行2D可视化

海量多维空间的问题是很难可视化。

我们可以使用一种称为主成分分析的技术来将数据的维度降低到更易于管理的大小——事实证明，较低的维度继续捕获关于内容的有用语义。

[Matt Webb](https://interconnected.org/) used the OpenAI embedding model to generate embeddings for descriptions of every episode of the BBC’s In Our Time podcast. He used these to find related episodes, but also ran PCA against them to create [an interactive 2D visualization](https://interconnected.org/more/2023/02/in_our_time-PCA-plot.html).

Image: Animated screenshot of a cloud of points in 2D space. At one side hovering over them shows things like The War of 1812 and The Battle of Trafalgar - at the other side we get Quantum Gravity and Higgs Boson and Carbon (https://static.simonwillison.net/static/2023/embeddings/cpa.gif)

将1,536个维度减少到只有两个维度仍然产生了一种有意义的探索数据的方式！关于历史战争的剧集出现在彼此附近，在其他地方有一组关于现代科学发现的剧集。

Matt wrote more about this in [Browse the BBC In Our Time archive by Dewey decimal code](https://interconnected.org/home/2023/02/07/braggoscope).

####使用平均位置对句子进行评分

嵌入的另一个技巧是使用它们进行分类。

首先计算您以某种方式分类的一组嵌入的平均位置，然后将新内容的嵌入与这些位置进行比较，以将其分配到一个类别。

Amelia Wattenberger demonstrated a beautiful example of this in [Getting creative with embeddings](https://wattenberger.com/thoughts/yay-embeddings-math).

她想通过鼓励混合使用具体和抽象的句子来帮助人们提高写作水平。但是你如何判断一个句子是具体的还是抽象的呢？

她的诀窍是生成两种类型句子的样本，计算它们的平均位置，然后根据它们与新定义的谱的两端的接近程度给新句子打分。

Image: A document. Different sentences are displayed in different shades of green and purple, with a key on the right hand side showing that green means concreete and purple means abstract, with a gradient between them. (https://static.simonwillison.net/static/2023/embeddings/amelia.jpg)

这个分数甚至可以转换成一种颜色，松散地表示给定句子的抽象或具体程度！

这是一个非常巧妙的演示，展示了您可以在这项技术之上开始构建的创造性界面。

####使用检索增强生成回答问题

我将以最初让我对嵌入感到兴奋的想法来结束。

每个尝试ChatGPT的人最终都会问同样的问题：我如何使用这个版本来回答基于我自己的私人笔记或我公司拥有的内部文档的问题？

人们认为答案是在这些内容的基础上训练一个定制模型，这可能会花费很大的代价。

事实证明这实际上没有必要。您可以使用现成的大型语言模型（托管的或本地运行的）和一个称为检索增强生成（RAG）的技巧。

关键思想是这样的：用户问一个问题。您在私人文档中搜索似乎与问题相关的内容，然后将该内容的摘录与原始问题一起粘贴到大语言模型中（尊重其大小限制，通常在3000到6000字之间）。

然后，大语言模型可以根据您提供的附加内容回答问题。

这种廉价的伎俩惊人地有效。让它的基本版本工作起来是微不足道的——挑战在于考虑到用户可能会问的无限多的问题，让它尽可能好地工作。

RAG中的关键问题是找出包含在大语言模型提示中的最佳内容摘录。

由嵌入驱动的“基于共鸣”的语义搜索正是你需要收集潜在相关内容来帮助回答用户问题的那种东西。

I built a version of this against content from my blog, described in detail in [Embedding paragraphs from my blog with E5-large-v2](https://til.simonwillison.net/llms/embed-paragraphs).

I used a model called [E5-large-v2](https://huggingface.co/intfloat/e5-large-v2) for this. It’s a model trained with this exact use-case in mind.

查找与问题相关的内容的一个挑战是用户的问题——“什么是shot-scraper？”–不能保证被认为在语义上与回答该问题的内容相似。问题和断言有不同的语法。

E5-large-v2通过支持两种类型的内容来解决这个问题。您可以在同一个空间嵌入短语（事实句子）和查询（问题），类似于CLIP支持图像和文本的方式。

我将博客中的19,000段文本嵌入为短语，现在我可以将一个问题嵌入为查询，并使用它来找到最有可能回答该问题的段落。

结果是RAG实现为一行Bash脚本：

大语言模型类似博客-段落-c"查询：$1"\
|jq'.content|sub("passage：";"")'-r\
|大语言模型-m mlc-chat-Llama-2-7b-chat-hf-q4f16_1\
“$1”-s“您将问题作为一个段落回答”

This example uses Llama 2 Chat 7B running on my laptop (with the [llm-mlc](https://github.com/simonw/llm-mlc) plugin), so I’m able to answer questions entirely offline using code running on my laptop.

运行此：

./blog-answer.sh“什么是镜头刮刀？”

输出此：

>Shot-scraper是一个Python实用程序，它包装了Playwright，提供了一个命令行界面和一个YAML驱动的配置流，用于自动化截取网页屏幕截图并使用JavaScript从中抓取数据的过程。它可以用于一次性截图，也可以通过在YAML文件中定义来以可重复的方式拍摄多个截图。此外，它还可以用于在页面上执行JavaScript并返回结果值。

That’s a really good description of my [shot-scraper](https://shot-scraper.datasette.io/) tool. I checked and none of that output is an exact match to content I had previously published on my blog.

###

我的演讲以问答环节结束。以下是总结的问题和答案。

***朗链如何融入其中？**

[LangChain](https://www.langchain.com/) is a popular framework for implementing features on top of LLMs. It covers a _lot_ of ground—my only problem with LangChain is that you have to invest a lot of work in understanding how it works and what it can do for you. Retrieval Augmented Generation is one of the key features of LangChain, so a lot of the things I’ve shown you today could be built on top of LangChain if you invest the effort.

我在这方面的理念与LangChain不同，因为我专注于构建一套可以协同工作的小工具，而不是一个一次性解决所有问题的框架。

***你试过余弦相似度以外的距离函数吗？**

我没有。余弦相似性是默认函数，其他人似乎都在使用，我还没有花任何时间探索其他选项。

实际上，我让ChatGPT编写了我所有不同版本的余弦相似性，包括Python和JavaScript！

RAG的一个迷人之处在于它有这么多不同的旋钮，你可以调整。可以尝试不同的距离函数、不同的嵌入模型、不同的提示策略、不同的大语言模型。这里有很大的实验空间。

***如果你有10亿个对象，你需要调整什么？**

我今天展示的演示都很小——大约有20,000个嵌入。这足够小，您可以对所有内容运行强力余弦相似性函数，并在合理的时间内返回结果。

如果您要处理更多的数据，有越来越多的选项可以提供帮助。

许多初创公司正在推出新的“向量数据库”——这实际上是定制的数据库，可以尽快回答针对向量的最近邻查询。

I’m not convinced you need an entirely new database for this: I’m more excited about adding custom indexes to existing databases. For example, SQLite has [sqlite-vss](https://github.com/asg017/sqlite-vss) and PostgreSQL has [pgvector](https://github.com/pgvector/pgvector).

I’ve also done some successful experiments with Facebook’s [FAISS](https://github.com/facebookresearch/faiss) library, including building a Datasette plugin that uses it called [datasette-faiss](https://datasette.io/plugins/datasette-faiss).

***您对嵌入式模型的哪些改进感到兴奋？**

I’m really excited about multi-modal models. CLIP is a great example, but I’ve also been experimenting with Facebook’s [ImageBind](https://github.com/facebookresearch/ImageBind), which “learns a joint embedding across six different modalities—images, text, audio, depth, thermal, and IMU data.” It looks like we can go a lot further than just images and text!

我也喜欢这些型号变小的趋势。我之前展示了一个新的模型，gte-tiny，它只有60MB。能够在受限制的设备上，或者在浏览器中运行这些东西，对我来说真的很令人兴奋。

####延伸阅读

如果您想深入了解嵌入如何工作的底层细节，我建议您使用以下方法：
