# 列举CSS优化、提高性能的方法

作者：![xiangshuo1992](https://avatars.githubusercontent.com/u/21164035?s=80&u=8fa0338daad064ce6ed37ce7a3778cf8582ec347&v=4)[xiangshuo1992](https://github/xiangshuo1992)

## 加载性能

  1. 压缩CSS
  2. 通过link方式加载，而不是[@import](https://github.com/import)
  3. 复合属性其实分开写，执行效率更高，因为CSS最终也还是要去解析如 `margin-left: left;`



## 选择器性能

  1. 尽量少的使用嵌套，可以采用BEM的方式来解决命名冲突
  2. 尽量少甚至是不使用标签选择器，这个性能实在是差，同样的还有`*`选择器
  3. 利用继承，减少代码量



## 渲染性能

  1. 慎重使用高性能属性：浮动、定位；
  2. 尽量减少页面重排、重绘；
  3. css雪碧图
  4. 自定义web字体，尽量少用
  5. 尽量减少使用昂贵属性，如box-shadow/border-radius/filter/透明度/:nth-child等
  6. 使用`transform`来变换而不是宽高等会造成重绘的属性



暂且先这样吧，看来想回答好，得好好梳理下了。
