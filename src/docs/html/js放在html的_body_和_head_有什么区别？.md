# js放在html的_body_和_head_有什么区别？

作者：![Konata9](https://avatars.githubusercontent.com/u/7352511?s=80&u=69e7e9fa8d3ec0f0c989038b958e673e0d660e37&v=4)[Konata9](https://github/Konata9)

js 放在 `<head>` 中，如果不添加 `async` 或者 `defer` 时，当浏览器遇到 `script` 时，会阻塞 DOM 树的构建，进而影响页面的加载。当 js 文件较多时，页面白屏的时间也会变长。

> 在这个过程中，如果解析器遇到了一个脚本(script)，它就会停下来，并且执行这个脚本，然后才会继续解析 HTML。如果遇到了一个引用外部资源的脚本(script)，它就必须停下来等待这个脚本资源的下载，而这个行为会导致一个或者多个的网络往返，并且会延迟页面的首次渲染时间。

把 js 放到 `<body>` 里（一般在 `</body>` 的上面）时，由于 DOM 时顺序解析的，因此 js 不会阻塞 DOM 的解析。对于必须要在 DOM 解析前就要加载的 js，我们需要放在 `<head>` 中。

参考文章：  
[该把 JS 文件放在 HTML 文档的那个位置](https://zhuanlan.zhihu.com/p/26440626)
