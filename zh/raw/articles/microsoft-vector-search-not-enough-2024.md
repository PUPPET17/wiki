---
source_url: https://techcommunity.microsoft.com/blog/azuredevcommunityblog/doing-rag-vector-search-is-not-enough/4161073
fetched_url: https://techcommunity.microsoft.com/blog/azuredevcommunityblog/doing-rag-vector-search-is-not-enough/4161073
source_type: blog
author: Pamela Fox / Microsoft
source_date: 2024-06-06
ingested: 2026-05-14
sha256: 7f823718d50c42f7f8c177c769315c2173b8609d34437445c1636f27ee453c94
raw_preservation: full_html_article_text_candidate
extraction_method: readability_lxml_html2text
html_bytes: 390147
parsed_chars: 15171
---

#做抹布？向量搜索*不够*

##源元数据

-来源网址：https://techcommunity.microsoft.com/blog/azuredevcommunityblog/doing-rag-vector-search-is-not-enough/4161073
-获取的网址：https://techcommunity.microsoft.com/blog/azuredevcommunityblog/doing-rag-vector-search-is-not-enough/4161073
-来源类型：博客
作者：Pamela Fox/微软
-来源日期：2024-06-06
-摄入日期：2026-05-14
-可靠性：高
-原始保存状态：full_html_article_text_candidate
-提取方式：readability_lxml_html2text

##解析的源文本

我很担心我听到的次数，“哦，我们可以用retriever X做RAG，这是向量搜索查询。”是的，你的RAG流的检索器肯定应该支持向量搜索，因为这将让你找到与用户查询语义相似的文档，但是向量搜索是不够的。您的检索器应该支持**完全混合搜索**，这意味着它可以执行向量搜索和全文搜索，然后合并和重新排序结果。这将允许您的RAG流找到语义相似的概念，但也可以找到完全匹配的概念，如专有名称、id和数字。

Azure AI Search提供包含所有这些组件的完整混合搜索：

Image: Diagram of Azure AI Search hybrid search flow (https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVTpeCRnSEq7lARX_tYJPPmIB36v3jO_MRQHa540EmjUaqvEBQhDhs1lFCP5xJ7B9upHpYJ77B1n8-H5dM7dCUQLBUV759lZOS3qPcouR-z20hatWBqxUzFaItJgYiJVcbfuGHB8eBNUuU1_6JiukM9JrKVJ7WqeQPSzYVi6n6b7CBJ8zSuoa1twfJuQ/s1600/Screenshot%202024-05-31%20at%205.53.32%E2%80%AFAM.png)

  1. It performs a **vector search** using a [distance metric](https://learn.microsoft.com/azure/search/vector-search-ranking#similarity-metrics-used-to-measure-nearness) (typically cosine or dot product).
  2. It performs a **full-text search** using the [BM25 scoring](https://learn.microsoft.com/azure/search/index-similarity-and-scoring) algorithm.
  3. It **merges** the results using [Reciprocal Rank Fusion](https://learn.microsoft.com/azure/search/hybrid-search-ranking) algorithm.
4.它使用语义排名器（Bing使用的一种机器学习模型）对结果进行**重新排名，该模型将每个结果与原始用户查询进行比较，并分配0-4的分数。

The search team even researched all the options against a standard dataset, and wrote [a blog post](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/azure-ai-search-outperforming-vector-search-with-hybrid/ba-p/3929167) comparing the retrieval results for full text search only, vector search only, hybrid search only, and hybrid plus ranker. Unsurprisingly, they found that the best results came from using the full stack, and that's why it's the default configuration we use in the [AI Search RAG starter app](https://github.com/Azure-Samples/azure-search-openai-demo/).

To demonstrate the importance of going beyond vector search, I'll show some queries based off the sample documents in the [AI Search RAG starter app](https://github.com/Azure-Samples/azure-search-openai-demo/). Those documents are from a fictional company and discuss internal policies like healthcare and benefits.

让我们从搜索“什么计划花费45.00美元？”使用AI搜索索引进行纯向量搜索：

search_query="什么计划费用$45.00"
search_vector=get_embedding(search_query)
r=search_client.search(None，top=3，vector_queries=[
VectorizedQuery(search_vector，k_nearest_neighbors=50，fields="embedding")])

该查询的结果包含数字和费用，如字符串“初级保健就诊的共付额通常约为20美元，而专家就诊的共付额约为50美元。”，但没有一个结果包含用户所寻找的确切成本45.00美元。

现在让我们用纯全文搜索来尝试这个查询：

r=search_client.search(search_query，top=3)

该查询的顶部结果包含健康保险计划的成本表，其中一行包含$45.00。

当然，我们不想局限于全文查询，因为许多用户查询可以通过向量搜索更好地回答，所以让我们用hybrid来尝试这个查询：

r=search_client.search(search_query，top=15，vector_queries=[
VectorizedQuery(search_vector，k_nearest_neighbors=10，fields="embedding")])

同样，顶部结果是包含成本和精确字符串$45.00的表。当用户在完整的RAG应用程序中提出这个问题时，他们会得到他们所希望的答案：

Image: image (https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhnhbsEDozPQRYk9JRgftjUk8CTea-6Il7UK26JePl6M9Cn3RPC9ggvj9VlE_6k8icGUkbZevjXLirTSKBxblhey0gWfn4NMyCD1KYD5J_91jV0QPxm4ENSsOH6QbE6DgMHUqg0MSTVrfBKijm6eza2Psz4x3IYbRjNxvkOMTgD02DuB8dzUYZ1lQJt9A/s1600/Screenshot%202024-05-31%20at%205.10.16%E2%80%AFAM.png)

你可能会想，嗯，有多少用户在搜索精确的字符串？考虑一下你在电子邮件中搜索一个特定人的名字的频率，或者你在网络上搜索一个特定编程函数的名字的频率。users_will_make查询可以通过全文搜索更好地回答，这就是为什么我们需要混合搜索解决方案。

这是仅靠向量搜索还不够的另一个原因：假设您使用的是OpenAI模型等通用嵌入模型，那么这些模型通常并不完全适合您的域。他们对某些术语的理解不会与完全根据您的域数据训练的模型相同。使用混合搜索有助于补偿嵌入域中的差异。

既然你有希望相信混合搜索，让我们来谈谈最后一步：根据原始用户查询对结果进行重新排名。

现在，我们将使用混合搜索在相同的文档中搜索“了解水下活动”：

search_query="了解水下活动"
search_vector=get_embedding(search_query)
r=search_client.search(search_query，top=5，vector_queries=[
VectorizedQuery(search_vector，k_nearest_neighbors=10，fields="embedding")])

该查询的第三个结果包含最相关的结果，即提到冲浪课程和水肺潜水课程的福利文档。值得注意的是，短语“水下”没有出现在任何文档中，所以这些结果来自向量搜索组件。

如果我们加入语义排名会发生什么？

search_query="了解水下活动"
search_vector=get_embedding(search_query)
r=search_client.search(search_query，top=5，vector_queries=[
VectorizedQuery(search_vector，k_nearest_neighbors=50，fields="embedding")]，
query_type="semantic", semantic_configuration_name="default")

现在，查询的最高结果是关于冲浪和水肺潜水课程的文档块，因为语义排名者意识到这是与用户查询最相关的结果。当用户在RAG流中提出这样的问题时，他们会得到一个正确的答案，其中包含预期的引用：

Image: Screenshot of user asking question about underwater activities and getting a good answer (https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7OwaG2AUqvCw8doLK6NWTXCKuAlRoCSYDAP2d_EkkCwB4uiknPrvHGVLtumaHku7EUOL83kvRwiGbvGHHGu_hsZHCgzOZ5JdzgT5y4KD5zqwXkIyGeoZfrjUF7ZLUqUg3UVWFaAC2aw1bUwjRETWoLfKUV1wT0SeR4B4XYYThx3Urro0arqT0NVbM4w/s1600/Screenshot%202024-05-31%20at%205.21.04%E2%80%AFAM.png)

我们的搜索在这两种情况下都产生了正确的结果，那么我们为什么要为排名而烦恼呢？对于将搜索结果发送到GPT-3.5等大语言模型的RAG应用程序，我们通常会将结果数量限制在相当低的数量，如3或5个结果。这是因为研究表明，当太多的背景抛给大语言模型时，她们往往会“迷失在中间”。我们希望前N个结果是最相关的结果，并且不包含任何不相关的结果。通过使用重新排名器，我们的顶级结果更有可能包含与查询最接近的匹配内容。

此外，还有一个很大的额外好处：每个结果现在都有一个从0-4的重新排名分数，这使得我们很容易过滤掉重新排名分数低于某个阈值（如<1.5）的结果。请记住，任何包含向量搜索的搜索算法都将_always_find结果，即使这些结果与原始查询根本不是很接近，因为向量搜索只是在整个向量空间中寻找最近的向量。因此，当您的搜索涉及向量搜索时，您理想情况下需要一个重新排名步骤和一个评分方法，这将使您更容易丢弃在绝对规模上不够相关的结果。

正如你从我的例子中看到的，Azure AI Search可以做我们RAG检索解决方案所需的一切（甚至比我们在这里介绍的还要多，比如过滤器和自定义评分算法。但是，您可能正在阅读这篇文章，因为您有兴趣为您的RAG解决方案使用不同的检索器，比如数据库。您应该能够在大多数数据库之上实现混合搜索，前提是它们具有一些文本搜索和向量搜索的能力。

As an example, consider the PostgreSQL database. It already has built-in [full text search](https://www.postgresql.org/docs/current/textsearch.html), and there's a popular extension called [pgvector](https://github.com/pgvector/pgvector-python) for bringing in vector indexes and distance operators. The next step is to combine them together in a hybrid search, which is demonstrated in [this example from the ](https://github.com/pgvector/pgvector-python/blob/master/examples/hybrid_search_rrf.py)[pgvector-python](https://github.com/pgvector/pgvector-python/)[ repository](https://github.com/pgvector/pgvector-python/blob/master/examples/hybrid_search_rrf.py):.

WITH semantic_search AS(
选择id，rank()OVER(ORDER BY embedding<=>%(embedding)s)作为rank
来自文档
按嵌入排序<=>%(嵌入)s
限20
),
keyword_search AS(
选择id, rank()OVER(ORDER BY ts_rank_cd(to_tsvector('english', content), query)DESC)
从文档，plainto_tsquery('english',%(query)s)查询
WHERE to_tsvector('english'，content)@@query
排序依据ts_rank_cd(to_tsvector('english', content), query)DESC
限20
)
选择
将(semantic_search.id、keyword_search.id)合并为id，
合并(1.0/(%(k)s+semantic_search.rank), 0.0)+
合并(1.0/(%(k)s+keyword_search.rank), 0.0)作为分数
来自语义搜索
semantic_search.id=keyword_search.id上的完整外部连接keyword_search
按分数排序DESC
限度5

该SQL通过运行向量搜索和文本搜索并将它们与RRF组合在一起来执行混合搜索。

Another [example from that repo](https://github.com/pgvector/pgvector-python/blob/master/examples/hybrid_search.py) shows how we could bring in a cross-encoding model for a final re-ranking step:

编码器=交叉编码器('交叉编码器/ms-marco-MiniLM-L-6-v2')
scores=encoder.predict([(查询，item[1])for results中的item])
results=[v for_, v in sorted(zip(scores, results), reverse=True)]

该代码将在与PostgreSQL查询的其余部分相同的过程中运行交叉编码模型，因此它可以在本地或测试环境中很好地工作，但不一定在生产环境中很好地扩展。理想情况下，对交叉编码器的调用将在可以访问GPU和专用资源的单独服务中进行。

I have implemented the first three steps of hybrid search in [a RAG-on-PostgreSQL starter app](https://github.com/Azure-Samples/rag-postgres-openai-python/). Since I don't yet have a good way to productionize a call to a cross-encoding model, I have _not_ brought in the final re-ranking step.

After seeing what it takes to replicate full hybrid search options on other database, I am even more appreciative of the work done by the Azure AI Search team. If you've decided that, nevermind, you'll go with Azure AI Search, check out the [AI Search RAG starter app](https://github.com/Azure-Samples/azure-search-openai-demo/). You might also check out open source packages, such as [llamaindex](https://docs.llamaindex.ai/en/stable/) which has at least partial hybrid search support for a number of databases. If you've used or implemented hybrid search on a different database, please share your experience in the comments.

When choosing our retriever and retriever options for RAG applications, we need to evaluate answer quality. I stepped through a few example queries above, but for a user-facing app, we really need to do bulk evaluations of a large quantity of questions (~200) to see the effect of an option on answer quality. To make it easier to run bulk evaluations, I've created the [ai-rag-chat-evaluator](https://github.com/Azure-Samples/ai-rag-chat-evaluator) repository, that can run both GPT-based metrics and code-based metrics against RAG chat apps.

以下是根据我所有个人博客帖子对RAG应用程序合成生成的数据集进行评估的结果：

搜索模式|基础|相关性|答案长度|引用匹配
---|---|---|---|---
仅向量|2.79|1.81|366.73|0.02
仅文本|4.87|4.74|662.34|0.89
混合动力|3.26|2.15|365.66|0.11
与排名者混合|4.89|4.78|670.89|0.92
  
尽管我是这篇博文的作者，但我震惊地看到vector search本身的表现如此之差，平均基础度为2.79（满分5分），只有2%的答案引用与基本事实引用相匹配。全文搜索本身做得相当好，平均基础度为4.87，引用匹配率为89%。没有语义排名器的混合搜索比向量搜索有所改善，平均基础度为3.26，引用匹配率为11%，但使用语义排名器的混合搜索表现更好，平均基础度为4.89，引用匹配率为92%。正如我们所料，这是所有选项中最高的数字。

但是为什么我们看到向量搜索和无排名混合搜索得分如此之低呢？除了我上面谈到的，我认为这也是由于：

***Azure AI Search中的全文搜索选项非常好。**它使用BM25，并且经过了相当多的战斗测试，在矢量搜索变得如此流行之前已经存在了很多年。BM25算法基于TF-IDF，产生类似稀疏向量本身的东西，因此它比简单的子串搜索更高级。人工智能搜索还使用标准的NLP技巧，如词干和拼写检查。许多数据库都具有全文搜索功能，但它们不会都像Azure AI Search全文搜索那样功能齐全。
***我的地面实况数据集偏向于与全文搜索的兼容性。**我通过将我的博客帖子输入GPT-4并要求它根据文本提出好的问答来生成示例问题和答案，所以我认为GPT-4很可能选择使用与我的帖子相似的措辞。一个真正的提问者可能会使用非常不同的措辞——见鬼，他们甚至可能会用不同的语言提问，比如西班牙语或中文！这是向量搜索真正大放异彩的地方，也是全文搜索做得不太好的地方。这很好地提醒了我们为什么需要根据我们的RAG chat用户在现实世界中的询问继续更新评估数据集。

总之，如果我们要走使用向量搜索的道路，我们绝对必须采用**全混合搜索**，包括所有四个步骤，并评估我们的结果，以确保我们使用的是工作的最佳检索选项。
