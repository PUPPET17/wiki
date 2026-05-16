---
source_url: https://github.com/letta-ai/lettabot/issues/652
fetched_url: https://api.github.com/repos/letta-ai/lettabot/issues/652
source_type: github issue
author: letta-ai/lettabot contributors
source_date: 2026-03-27
ingested: 2026-05-15
sha256: de7404e5cbc4987eecacac17d00678a3a2f40576d35ce13f6b7d350409a0cf9d
raw_preservation: full_github_issue_api_text
extraction_method: github_rest_issue_and_comments
github_repo: letta-ai/lettabot
github_issue: 652
comments_fetched: 0
---

#Letta问题652：每个对话上下文范围

##源元数据

-来源网址：https://github.com/letta-ai/lettabot/issues/652
-获取的URL：https://api.github.com/repos/letta-ai/lettabot/issues/652
-来源类型：github问题
-作者：letta-ai/lettabot贡献者
-来源日期：2026-03-27
-摄入日期：2026-05-15
-可靠性：中等
-原始保存状态：full_github_issue_api_text
-提取方式：github_rest_issue_and_comments

##解析的源文本

#功能：每个对话的上下文范围（每个对话的memfs/块固定）

-GitHub问题：https://github.com/letta-ai/lettabot/issues/652
-API URL：https://api.github.com/repos/letta-ai/lettabot/issues/652
-状态：打开
-作者：ezra-letta
-创建时间：2026-03-27T03：02:05 Z
-更新日期：2026-03-27T18：37：30Z
-评论：0
-标签：增强

##发行主体

##问题

所有代理上下文——memfs`system/`文件、内存块、工具、系统提示——都是代理级的，并且在每个会话中相同地共享。没有办法将上下文范围限制到特定的对话。

这意味着：
-制鞋讨论组查看无关游戏朋友的用户配置文件
-公共Discord服务器获得与私有DM相同的角色详细信息
-IoT传感器数据对话加载社交聊天上下文，反之亦然
-每个对话都支付整个代理知识的全部代币成本，而不管相关性如何

随着代理扩展到跨更多通道的更多对话（跨通道对话路由参见#651），这变得越来越浪费，并且可能会分散代理的注意力。

##当前架构

|层|范围|
|-------|---------|
|消息历史|每次对话（已隔离）|
|Memfs`system/`文件|代理级（固定到所有对话）|
|内存块|代理级（附加到代理，而不是对话）|
|工具|代理级（到处都是相同的工具集）|
|系统提示|代理级（编译一次，全部相同）|

##建议能力

允许将特定的memfs文件或内存块固定到特定的对话（或来自#651的对话组）：

```yaml
conversations:
  routes:
    gaming-squad:
      - discord:333
      - telegram:ccc
      context:
        include:
          - system/users/gaming-friends.md
          - system/rules/gaming-rules.md
        exclude:
          - system/users/work-contacts.md
    work:
      - discord:444
      context:
        include:
          - system/projects/
          - system/users/work-contacts.md
```

或者，memfs中的每个文件元数据：
```yaml
# system/users/gaming-friends.md frontmatter
---
description: Gaming friend group profiles
conversations: [gaming-squad]  # only pinned to this conversation group
---
```

##实施注意事项

-系统提示编译需要成为每个会话（目前是代理级）
-这是比会话路由更深层次的架构变化（#651）
-可能需要更改Letta服务器的编译管道，而不仅仅是LettaBot
-可以从一个更简单的版本开始：从config注入对话级“additionalContext”，而不改变核心编译

##用例

-**隐私边界**：用户配置文件仅在该用户参与的对话中可见
-**注意力管理**：座席在集中对话中不会被不相关的上下文分散注意力
-**令牌效率**：每次对话的有效上下文越小=压缩越少，成本越低
-**IoT/机器人**：仅在相关控制会话中加载传感器数据模式
-**工作/个人分离**：在社交对话中不可见的工作项目文件

##与其他问题的关系

这建立在#651（跨通道会话路由）的基础上。路由定义哪些聊天共享对话；这定义了每个对话看到的上下文。这两者都是完整的多会话代理体验所必需的。

##评论
