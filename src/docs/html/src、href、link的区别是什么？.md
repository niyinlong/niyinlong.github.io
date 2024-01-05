# src、href、link的区别是什么？

作者：![chenshijin1](https://avatars.githubusercontent.com/u/28537274?s=80&v=4)[chenshijin1](https://github/chenshijin1)

## 谈谈src和href的区别

src和href都是用于外部资源的引入， src一般引入js文件， 图片文件，href一般链接css资源文件，网页资源文件。这里给出几个使用得例子：

  * 引用js文件时：`src="myscript.js"`
  * 引用图片：`src="mypic.jpg"`
  * 引用css文件时：`href="cssfile.css"`
  * 网站链接：`href="http://www.webpage.com"`



它们之间的主要区别可以用这样一句话来概括：

**src用于替代这个元素，而href用于建立这个标签与外部资源之间的关系。**

例如：
``` 
    <a href="www.xxx.com">
    	<img src="1.jpg">
    </a>  
```

`a` 标签里面的内容是一张图片，a标签加上href属性将图片链接到了www.xxx.com这个网站，但并未替换a标签里面的内容。

而`img`标签的src属性则是将这个标签完全替换成了src里面的资源。

**href (Hypertext Reference) 超文本引用**

href这个属性指定web资源的位置，从而定义当前元素（如锚点a）或当前文档（如链接）与目标锚点或目标资源之间的联系。例如当我们写：

`<link href="style.css" rel="stylesheet" />`

浏览器知道这是个样式表文件， **html页面的解析和渲染不会暂停，css文件的加载是同时进行的** ，用[@import](https://github.com/import)添加的样式是在页面载入之后再加载，这可能会导致页面因重新渲染而闪烁。所以我们建议使用link而不是[@import](https://github.com/import)。

**src (Source)源**

这个属性是将资源嵌入到当前文档中元素所在的位置。例如当我们写：

`<script src="script.js"></script> `

当浏览器解析到这句代码时， **html页面的加载和解析都会暂停，直到浏览器加载、编译、执行完毕js文件** 。这就像是把js文件里的内容全部注入到这个script标签中，类似于img，img标签是一个空标签，它的内容就是由src这个属性定义，浏览器会暂停加载直到这个图片加载完成，`iframe`标签也有这样这样得特性。

这也是为什么要将js文件的加载放在body最后的原因（ 在`<body>`前面 ）。

参考：<https://stackoverflow.com/questions/3395359/difference-between-src-and-href>
