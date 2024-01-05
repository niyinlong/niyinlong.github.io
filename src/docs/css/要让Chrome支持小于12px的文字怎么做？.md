# 要让Chrome支持小于12px的文字怎么做？

作者：![Konata9](https://avatars.githubusercontent.com/u/7352511?s=80&u=69e7e9fa8d3ec0f0c989038b958e673e0d660e37&v=4)[Konata9](https://github/Konata9)

Chrome 中有最小字号的限制，一般为 12px。原因是 Chrome 认为小于这个字号会影响阅读。

当需要小于 12px 字体的时候，有以下几个方法可以使用。

  * -webkit-text-size-adjust:none; 这个属性在高版本的 Chrome 中已经被废除。
  * 使用 `transform: scale(0.5, 0.5)`，但使用 `transform` 需要注意下面几点： 
    * `transform` 对行内元素无效，因此要么使用 `display: block;` 要么使用 `display: inline-block;`
    * `transform` 即使进行了缩放，原来元素还是会占据对应的位置。因此需要做调整，最好是在外面再包一层元素，以免影响其他元素。
  * 作为图片。



最好的办法还是进行切图，或者就不要使用小于 12px 的字体。
