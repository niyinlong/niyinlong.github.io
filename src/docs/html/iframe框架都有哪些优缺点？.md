# iframe框架都有哪些优缺点？

作者：![Konata9](https://avatars.githubusercontent.com/u/7352511?s=80&u=69e7e9fa8d3ec0f0c989038b958e673e0d660e37&v=4)[Konata9](https://github/Konata9)

#### 优点：

  * 可以实现异步刷新，单个 `iframe` 刷新不影响整体窗口的刷新（可以实现无刷新上传，在 `FormData` 无法使用时）
  * 可以实现跨域，每个 `iframe` 的源都可以不相同（方便引入第三方内容）
  * 多页面应用时，对于共同的 `header`, `footer` 可以使用 `iframe` 加载，拆分代码（导航栏的应用）



#### 缺点：

  * 每一个 `iframe` 都对应着一个页面，也就意味着多余的 `css`, `js` 文件的载入，会增加请求的开销
  * 如果 `iframe` 内还有滚动条，会严重影响用户体验
  * `window.onload` 事件会在所有 `iframe` 加载完成后才触发，因此会造成页面阻塞



参考文章: [Iframe 有什么好处，有什么坏处？国内还有哪些知名网站仍用Iframe，为什么？有哪些原来用的现在抛弃了？又是为什么？](https://www.zhihu.com/question/20653055)
