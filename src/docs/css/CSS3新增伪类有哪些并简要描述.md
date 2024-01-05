# CSS3新增伪类有哪些并简要描述

作者：![Konata9](https://avatars.githubusercontent.com/u/7352511?s=80&u=69e7e9fa8d3ec0f0c989038b958e673e0d660e37&v=4)[Konata9](https://github/Konata9)

CSS3 中规定伪类使用一个 `:` 来表示；伪元素则使用 `::` 来表示。

CSS3 中新增的伪元素有以下这些:

  * `:first-child / :last-child` 表示子元素结构关系的
  * `:nth-child() / nth-last-child()` 用来控制奇数、偶数行的（控制表单奇数、偶数行的样式）
  * `:first-of-type / :last-of-type` 表示一组兄弟元素中其类型的第一个元素 [MDN](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:first-of-type)
  * `:nth-of-type() / :nth-last-of-type()` 这个选择器匹配那些在相同兄弟节点中的位置与模式 an+b 匹配的相同元素` [MDN](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:nth-of-type)
  * `:root` html 根元素
  * `:not()` 否定选择器，用的比较多
  * `:only-child` 只有一个子元素时才会生效
  * `:empty` 选择连空格都没有的元素


