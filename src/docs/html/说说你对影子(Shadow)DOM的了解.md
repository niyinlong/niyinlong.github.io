# 说说你对影子(Shadow)DOM的了解

作者：![Konata9](https://avatars.githubusercontent.com/u/7352511?s=80&u=69e7e9fa8d3ec0f0c989038b958e673e0d660e37&v=4)[Konata9](https://github/Konata9)

`Shadow DOM` 可以想象成我们在 Vue 或者 React 中使用的一个个组件，是一种将 HTML 结构、Style 封装起来的结构。我们熟悉的 `<video>` 标签，其实就是 `Shadow DOM` 的封装。

[![](https://camo.githubusercontent.com/2e219d46e9a923f0649297ed164d16d7c3771c349df6eea0d6e3600a9fd498cc/68747470733a2f2f696d6731322e333630627579696d672e636f6d2f6c696e672f6a66732f74312f38313530372f33352f323234362f3730373333372f35643038646165394562643234373230612f396663623835623732616433333738392e706e67)](https://camo.githubusercontent.com/2e219d46e9a923f0649297ed164d16d7c3771c349df6eea0d6e3600a9fd498cc/68747470733a2f2f696d6731322e333630627579696d672e636f6d2f6c696e672f6a66732f74312f38313530372f33352f323234362f3730373333372f35643038646165394562643234373230612f396663623835623732616433333738392e706e67)

借用 MDN 上的图，可以看到 `Shadow DOM` 允许我们在 DOM 文档中插入一个 DOM 的子树。`Shadow Tree` 会挂在 `Shadow host` 对应的 DOM 上。之后，`Shadow DOM` 与外层 DOM 不会相互影响，因此可以放心用来做组件。

[![](https://camo.githubusercontent.com/d2c13c36d235c616c7a9e2efa6e5d43abda56f206cb11b847300b5bbaad03d74/68747470733a2f2f6d646e2e6d6f7a696c6c6164656d6f732e6f72672f66696c65732f31353738382f736861646f772d646f6d2e706e67)](https://camo.githubusercontent.com/d2c13c36d235c616c7a9e2efa6e5d43abda56f206cb11b847300b5bbaad03d74/68747470733a2f2f6d646e2e6d6f7a696c6c6164656d6f732e6f72672f66696c65732f31353738382f736861646f772d646f6d2e706e67)

具体的例子可以参考 MDN 给出的案例[`<popup-info-box>`](https://github.com/mdn/web-components-examples/tree/master/popup-info-box-web-component)

这个例子告诉我们可以利用 `Shadow DOM` 封装自己的 `tag` 标签，并且可以在网页中使用。

参考文章：  
[使用 shadow DOM](https://developer.mozilla.org/zh-CN/docs/Web/Web_Components/Using_shadow_DOM)  
[神奇的 Shadow DOM](https://aotu.io/notes/2016/06/24/Shadow-DOM/index.html)
