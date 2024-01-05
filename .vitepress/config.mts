import { defineConfig } from 'vitepress'
import { generateSidebar } from 'vitepress-sidebar'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  srcDir: './src/docs',
  title: "niyinlong",
  description: "a fe interview docs",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    search: {
      provider: 'local'
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
