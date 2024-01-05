# 说下line-height三种赋值方式有何区别？

作者：![Konata9](https://avatars.githubusercontent.com/u/7352511?s=80&u=69e7e9fa8d3ec0f0c989038b958e673e0d660e37&v=4)[Konata9](https://github/Konata9)

`line-height` 可以有带单位及不带单位的写法（感觉其实是两种）。
``` 
    div{
    	line-height: 24px;
    	line-height: 1.5;
    	line-height: 1.5em;
    	line-height: 150%;
    }
```

对于应用在单个元素上，这几种写法的效果都是一样的（除了 px 需要一些计算）。但由于 `line-height` 是可以被继承的，因此会影响内部子元素的 `line-height`。简单的可以总结为：

  * 带有单位的 `line-height` 会被计算成 `px` 后继承。子元素的 `line-height` = 父元素的 `line-height` * `font-size` （如果是 px 了就直接继承）

  * 而不带单位的 `line-height` 被继承的是倍数，子元素的 `line-height` = 子元素的 `font-size` * 继承的倍数




简单的示例： <https://codepen.io/Konata9/pen/oNvZGqo>

参考文章：  
[line-height 3种设置方式的区别](https://juejin.im/post/5a6dd1356fb9a01cb0499177)
