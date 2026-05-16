import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'LLM Wiki',
  description: 'LLM Wiki / Agent Memory Research',
  base: '/wiki/',
  cleanUrls: true,
  lastUpdated: true,
  ignoreDeadLinks: true,
  srcExclude: ['raw/**'],
  markdown: {
    config: (md) => {
      md.options.html = false
    }
  },
  locales: {
    root: {
      label: 'English',
      lang: 'en-US',
      title: 'LLM Wiki',
      description: 'LLM Wiki / Agent Memory Research',
      themeConfig: {
        nav: [
          { text: 'Index', link: '/index' },
          { text: 'Schema', link: '/SCHEMA' },
          { text: 'Log', link: '/log' }
        ],
        sidebar: [
          {
            text: 'Core',
            items: [
              { text: 'Home', link: '/' },
              { text: 'Wiki Index', link: '/index' },
              { text: 'Schema', link: '/SCHEMA' },
              { text: 'Log', link: '/log' }
            ]
          },
          {
            text: 'Concepts',
            items: [
              { text: 'Agent Memory Research Framework', link: '/concepts/llm-wiki-agent-memory-research-framework' },
              { text: 'Hermes Obsidian KB Plan', link: '/concepts/hermes-obsidian-personal-knowledge-base-plan' }
            ]
          }
        ],
        search: {
          provider: 'local'
        }
      }
    },
    zh: {
      label: '简体中文',
      lang: 'zh-CN',
      title: 'LLM Wiki',
      description: 'LLM Wiki / Agent Memory 研究',
      themeConfig: {
        nav: [
          { text: '索引', link: '/zh/index' },
          { text: '规范', link: '/zh/SCHEMA' },
          { text: '日志', link: '/zh/log' }
        ],
        sidebar: [
          {
            text: '核心',
            items: [
              { text: '首页', link: '/zh/' },
              { text: 'Wiki 索引', link: '/zh/index' },
              { text: '维护规范', link: '/zh/SCHEMA' },
              { text: '变更日志', link: '/zh/log' }
            ]
          },
          {
            text: '概念',
            items: [
              { text: 'Agent Memory 研究框架', link: '/zh/concepts/llm-wiki-agent-memory-research-framework' },
              { text: 'Hermes + Obsidian 知识库方案', link: '/zh/concepts/hermes-obsidian-personal-knowledge-base-plan' }
            ]
          }
        ],
        outline: {
          label: '页面导航'
        },
        docFooter: {
          prev: '上一页',
          next: '下一页'
        },
        darkModeSwitchLabel: '外观',
        sidebarMenuLabel: '菜单',
        returnToTopLabel: '返回顶部',
        langMenuLabel: '切换语言',
        search: {
          provider: 'local',
          options: {
            locales: {
              zh: {
                translations: {
                  button: {
                    buttonText: '搜索文档',
                    buttonAriaLabel: '搜索文档'
                  },
                  modal: {
                    noResultsText: '无法找到相关结果',
                    resetButtonTitle: '清除查询条件',
                    footer: {
                      selectText: '选择',
                      navigateText: '切换',
                      closeText: '关闭'
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
})
