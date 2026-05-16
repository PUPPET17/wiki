import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'LLM Wiki',
  description: 'LLM Wiki / Agent Memory / Context Compression / Knowledge Integration research wiki',
  base: '/wiki/',
  cleanUrls: true,
  lastUpdated: true,
  ignoreDeadLinks: true,
  markdown: {
    html: false,
    toc: { level: [2, 3] },
    config(md) {
      md.renderer.rules.image = (tokens, idx) => {
        const token = tokens[idx]
        const src = token.attrGet('src') || ''
        const alt = token.content || ''
        return `[image: ${alt || src}]`
      }
      const htmlBlock = md.block.ruler.getRules('html_block')[0]
      const htmlInline = md.inline.ruler.getRules('html_inline')[0]
      if (htmlBlock) md.block.ruler.disable(['html_block'])
      if (htmlInline) md.inline.ruler.disable(['html_inline'])
    }
  },
  themeConfig: {
    logo: undefined,
    siteTitle: 'LLM Wiki',
    repo: 'PUPPET17/wiki',
    editLink: {
      pattern: 'https://github.com/PUPPET17/wiki/edit/main/:path',
      text: 'Edit this page on GitHub'
    },
    search: {
      provider: 'local'
    },
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Index', link: '/index' },
      { text: 'Schema', link: '/SCHEMA' },
      { text: 'Log', link: '/log' },
      { text: 'GitHub', link: 'https://github.com/PUPPET17/wiki' }
    ],
    sidebar: [
      {
        text: 'Wiki',
        items: [
          { text: 'Home', link: '/' },
          { text: 'Wiki Index', link: '/index' },
          { text: 'Schema / 维护规范', link: '/SCHEMA' },
          { text: '变更日志', link: '/log' }
        ]
      },
      {
        text: 'Concepts',
        collapsed: false,
        items: [
          { text: 'LLM Wiki / Agent Memory Research Framework', link: '/concepts/llm-wiki-agent-memory-research-framework' },
          { text: 'Hermes Obsidian Personal Knowledge Base Plan', link: '/concepts/hermes-obsidian-personal-knowledge-base-plan' }
        ]
      },
      {
        text: 'Raw Sources',
        collapsed: true,
        items: [
          {
            text: 'Articles',
            collapsed: true,
            items: [
              { text: 'Anthropic Effective Agents 2024', link: '/raw/articles/anthropic-effective-agents-2024' },
              { text: 'Anthropic Multi-Agent Research 2025', link: '/raw/articles/anthropic-multi-agent-research-2025' },
              { text: 'Harrison Chase: Context Engineering 2025', link: '/raw/articles/harrison-chase-sequoia-context-engineering-2025' },
              { text: 'Karpathy LLM Wiki Gist 2026', link: '/raw/articles/karpathy-llm-wiki-gist-2026' },
              { text: 'LangChain Context Engineering 2025', link: '/raw/articles/langchain-context-engineering-2025' },
              { text: 'Microsoft: Vector Search Is Not Enough 2024', link: '/raw/articles/microsoft-vector-search-not-enough-2024' },
              { text: 'Simon Willison Embeddings 2023', link: '/raw/articles/simon-willison-embeddings-2023' }
            ]
          },
          {
            text: 'Papers',
            collapsed: true,
            items: [
              { text: 'CoALA 2023', link: '/raw/papers/coala-2023' },
              { text: 'Generative Agents 2023', link: '/raw/papers/generative-agents-2023' },
              { text: 'MemGPT 2023', link: '/raw/papers/memgpt-2023' },
              { text: 'MemoRAG 2024', link: '/raw/papers/memorag-2024' },
              { text: 'RAG Survey 2023', link: '/raw/papers/rag-survey-2023' },
              { text: 'RAPTOR 2024', link: '/raw/papers/raptor-2024' },
              { text: 'Self-RAG 2023', link: '/raw/papers/self-rag-2023' }
            ]
          },
          {
            text: 'Product Docs',
            collapsed: true,
            items: [
              { text: 'Hermes Agent Memory Docs 2026', link: '/raw/product-docs/hermes-agent-memory-docs-2026' },
              { text: 'Hermes Agent Memory Providers 2026', link: '/raw/product-docs/hermes-agent-memory-providers-docs-2026' },
              { text: 'Letta Memory 2026', link: '/raw/product-docs/letta-memory-2026' },
              { text: 'Obsidian Bases 2026', link: '/raw/product-docs/obsidian-bases-2026' },
              { text: 'Obsidian Properties 2026', link: '/raw/product-docs/obsidian-properties-2026' },
              { text: 'Obsidian URI 2026', link: '/raw/product-docs/obsidian-uri-2026' },
              { text: 'Obsidian Web Clipper 2026', link: '/raw/product-docs/obsidian-web-clipper-2026' },
              { text: 'OpenAI ChatGPT Memory 2024-2025', link: '/raw/product-docs/openai-chatgpt-memory-2024-2025' }
            ]
          },
          {
            text: 'Community',
            collapsed: true,
            items: [
              { text: 'HN Karpathy Style Wiki 2026', link: '/raw/community/hn-karpathy-style-wiki-2026' },
              { text: 'HN Letta Code 2025', link: '/raw/community/hn-letta-code-2025' },
              { text: 'HN MemGPT 2023', link: '/raw/community/hn-memgpt-2023' },
              { text: 'Reddit Memory Systems 2026', link: '/raw/community/reddit-memory-systems-2026' }
            ]
          },
          {
            text: 'GitHub',
            collapsed: true,
            items: [
              { text: 'LangChain Context Engineering README', link: '/raw/github/langchain-context-engineering-repo-readme' },
              { text: 'LangChain How to Fix Your Context README', link: '/raw/github/langchain-how-to-fix-your-context-readme' },
              { text: 'Letta Code README', link: '/raw/github/letta-code-repo-readme' },
              { text: 'Letta Issue 652 Context Scoping', link: '/raw/github/letta-issue-652-per-conversation-context-scoping' },
              { text: 'LLM Wiki Compiler README', link: '/raw/github/llm-wiki-compiler-repo-readme' },
              { text: 'Mem0 Issue 4573 Memory Audit Junk', link: '/raw/github/mem0-issue-4573-memory-audit-junk' },
              { text: 'Mem0 README', link: '/raw/github/mem0-repo-readme' },
              { text: 'Obsidian Dataview Docs Overview', link: '/raw/github/obsidian-dataview-docs-overview' },
              { text: 'Obsidian Local REST API README', link: '/raw/github/obsidian-local-rest-api-readme' },
              { text: 'Obsidian MCP Server README', link: '/raw/github/obsidian-mcp-server-readme' },
              { text: 'WUPHF README', link: '/raw/github/wuphf-repo-readme' }
            ]
          }
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/PUPPET17/wiki' }
    ],
    footer: {
      message: 'Generated from a markdown+git research wiki.',
      copyright: 'Copyright © 2026 PUPPET17'
    }
  }
})
