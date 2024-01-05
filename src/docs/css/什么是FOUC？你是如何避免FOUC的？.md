# 什么是FOUC？你是如何避免FOUC的？

作者：![Konata9](https://avatars.githubusercontent.com/u/7352511?s=80&u=69e7e9fa8d3ec0f0c989038b958e673e0d660e37&v=4)[Konata9](https://github/Konata9)

FOUC 即 Flash of Unstyled Content，是指页面一开始以样式 A（或无样式）的渲染，突然变成样式B。  
原因是样式表的晚于 HTML 加载导致页面重新进行绘制。

  * 通过 `@import` 方式导入样式表
  * style 标签在 body 中



解决方法：把 `link` 标签将样式放在 `head` 中

参考文档:[什么是 FOUC？如何避免 FOUC？](https://www.cnblogs.com/xianyulaodi/p/5198603.html)
