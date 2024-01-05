# 说说position的absolute和fixed共同与不同点分别是什么？

作者：![alowkeyguy](https://avatars.githubusercontent.com/u/27432265?s=80&u=5f2e8c4bb8e4f353bb7f1840c85abc09974b3c3b&v=4)[alowkeyguy](https://github/alowkeyguy)

  * 共同点，脱离文档流，形成独立的渲染区（可以用优化动画性能）
  * 不同点，position根据第一个不为static的祖先元素定位，fixed定位当元素祖先的 transform 属性非 none 时，容器定位由相对于视口改为相对于该祖先元素


