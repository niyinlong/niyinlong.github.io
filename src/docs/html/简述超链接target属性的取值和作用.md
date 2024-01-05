# 简述超链接target属性的取值和作用

作者：![Konata9](https://avatars.githubusercontent.com/u/7352511?s=80&u=69e7e9fa8d3ec0f0c989038b958e673e0d660e37&v=4)[Konata9](https://github/Konata9)

`a` 标签的 `target` 属性一共有四个值。

  * `_self`

默认属性。在当前窗口或者框架中加载目标文档。

  * `_blank`

打开新的窗口或者新的标签页。在使用这个属性时，最好添加 `rel="noopener norefferrer"` 属性，防止打开的新窗口对原窗口进行篡改。防止 `window.opener` API 的恶意行为。

  * `_parent`

在 `frame` 或者 `iframe` 中使用较多。在父级框架中载入目标文档，当 `a` 标签本身在顶层时，与 `_self` 相同。

  * `_top`

在 `frame` 或者 `iframe` 中使用较多。直接在顶层的框架中载入目标文档，加载整个窗口。



