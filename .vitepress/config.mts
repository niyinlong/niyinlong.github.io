import { defineConfig } from 'vitepress'
import { generateSidebar } from 'vitepress-sidebar'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  srcDir: './src/docs',
  title: "niyinlong",
  description: "a fe interview docs",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    i18nRouting: false,
    search: {
      provider: 'local'
    },
    lastUpdated: { text: '最后更新于' },
    editLink: {
      text: '在 GitHub 上编辑此页面',
      pattern: 'https://github.com/niyinlong/niyinlong.github.io/edit/master/src/docs/:path'
    },
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Examples', link: '/markdown-examples' }
    ],
    // 动态生成侧边栏
    sidebar: generateSidebar({ documentRootPath: './src/docs' }),
    socialLinks: [
      { icon: 'github', link: 'https://github.com/niyinlong/niyinlong.github.io' }
    ],
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2023-present niyinlong'
    }
  }
})
