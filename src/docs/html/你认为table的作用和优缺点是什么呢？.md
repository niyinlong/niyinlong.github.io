# 你认为table的作用和优缺点是什么呢？

作者：![Konata9](https://avatars.githubusercontent.com/u/7352511?s=80&u=69e7e9fa8d3ec0f0c989038b958e673e0d660e37&v=4)[Konata9](https://github/Konata9)

`table` 用于表格数据的展示，并且很符合人们的直观认知。

在 `div`+`css` 布局流行之前，普遍使用 `table` 进行布局。曾经的神器 Dreamweaver 的可视化拖拽也是基于 `table` 布局。

`table` 布局的好处在于样式好控制，特别是居中、对齐。缺点在于会多处非常多的 DOM 节点（想想一个 `td` 里面再来一个 `table`），会导致页面加载变慢、不利于 SEO（`table` 原本就不是用来布局的）。也因此，在 CSS 成熟之后，`table` 布局马上就变成历史了。
