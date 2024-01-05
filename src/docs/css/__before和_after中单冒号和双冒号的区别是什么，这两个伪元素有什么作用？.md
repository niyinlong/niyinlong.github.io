# __before和_after中单冒号和双冒号的区别是什么，这两个伪元素有什么作用？

作者：![xiangshuo1992](https://avatars.githubusercontent.com/u/21164035?s=80&u=8fa0338daad064ce6ed37ce7a3778cf8582ec347&v=4)[xiangshuo1992](https://github/xiangshuo1992)

发现这道题和后面的题目有点类似，都是讲伪元素 `:before` 和 `:after` ，直接看这道题的解释吧，同样可以回答这个问题。

[[css] 第19天 css的属性content有什么作用呢？有哪些场景可以用到？](https://github.com/haizlin/fe-interview/issues/63)

针对这道题写了篇blog，原文链接：<https://xiangshuo.blog.csdn.net/article/details/89843456>  
以下是回答。

## 认识 `:before` 和 `:after`

  * 默认 `display: inline`；
  * 必须设置 `content` 属性，否则一切都是无用功， `content` 属性也只能应用在 `:before` 和 `:after` 伪元素上；
  * 默认user-select: none，就是 `:before` 和 `:after` 的内容无法被用户选中；
  * 伪元素可以和伪类结合使用形如：`.target:hover:after`。
  * `:before` 和 `:after` 是在CSS2中提出来的，所以兼容IE8；
  * `::before` 和 `::after` 是CSS3中的写法，为了将伪类和伪元素区分开；
  * CSS 中其他的伪元素有：`::before`、`::after`、`::first-letter`、`::first-line`、`::selection` 等；
  * 不可通过DOM使用，它只是纯粹的表象。在特殊情况下，从一个访问的角度来看，当前屏幕阅读不支持生成的内容。



## `content` 定义用法

`content` 属性与 `:before` 及 `:after` 伪元素配合使用，在元素头或尾部来插入生成内容。

**说明：** 该属性用于定义元素之前或之后放置的生成内容。默认地，这往往是行内内容，不过该内容创建的盒子类型可以用属性 display 控制。

MDN 对 `content` 的取值描述：
``` 
    content: normal                                /* Keywords that cannot be combined with other values */
    content: none
    
    content: 'prefix'                              /* <string> value, non-latin characters must be encoded e.g. \00A0 for &nbsp; */
    content: url(http://www.example.com/test.html) /* <uri> value */
    content: chapter_counter                       /* <counter> values */
    content: attr(value string)                    /* attr() value linked to the HTML attribute value */
    content: open-quote                            /* Language- and position-dependant keywords */
    content: close-quote
    content: no-open-quote
    content: no-close-quote
    
    content: open-quote chapter_counter            /* Except for normal and none, several values can be used simultaneously */
    
    content: inherit
```

### content: `<string>` value 字符串

可以加入任何字符，包括 Unicode 编码等各种字符。
``` 
    <a class="demo" href="https://www.xunlei.com/" title="精彩，一下就有">精彩，一下就有</a>
    
    .demo:after{
    	content: "↗"
    }
```

[![在这里插入图片描述](https://camo.githubusercontent.com/fbaa66be4033f20e4fbfadc3d97521d2e9fa419c243cfd230575367687ac14a3/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383038343834323935362e706e67)](https://camo.githubusercontent.com/fbaa66be4033f20e4fbfadc3d97521d2e9fa419c243cfd230575367687ac14a3/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383038343834323935362e706e67)  
我们还可以通过 `content` 内字符串的变化，实现类似 加载中... 的动画效果
``` 
    .demo:after{
    	animation: dot 1.6s linear both;
    }
    @keyframe dot{
    	0%{ content: "." }
    	33%{ content: ".." }
    	66%{ content: "..." }
    	100%{ content: "." }
    }
```

[![在这里插入图片描述](https://camo.githubusercontent.com/aab8a92ed05edb02a7f071eaacaf3412118088d3d551225a4646c3214602c8db/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383039343130353830342e676966)](https://camo.githubusercontent.com/aab8a92ed05edb02a7f071eaacaf3412118088d3d551225a4646c3214602c8db/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383039343130353830342e676966)  
类似的，还有种实现方式，steps阶梯函数实现元素位移
``` 
    <a class="demo" href="https://www.xunlei.com/" title="精彩，一下就有">精彩，一下就有<dot>...</dot></a>
```
``` 
    dot {
       display: inline-block;
        height: 1em;
        line-height: 1;
        text-align: left;
        vertical-align: -.25em;
        overflow: hidden;
    }
    
    dot::before {
        display: block;
        content: '...\A..\A.';
        white-space: pre-wrap;
        animation: dot2 1.6s infinite step-start both;
    }
    
    @keyframes dot2 {
        33% {
            transform: translateY(-2em);
        }
    
        66% {
            transform: translateY(-1em);
        }
    }
```

### content: `<uri>` value 外部资源

用于引用媒体文件，图片，图标，SVG等。
``` 
    .demo:after{
    	content: url(https://img-vip-ssl.a.88cdn.com/img/xunleiadmin/5b9889e14dcdc.png);
    }
```

[![在这里插入图片描述](https://camo.githubusercontent.com/55fba1c824252d55e284c3595d28a51143af2c688909bcc7c3341db184bb725a/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383038353232303334392e706e67)](https://camo.githubusercontent.com/55fba1c824252d55e284c3595d28a51143af2c688909bcc7c3341db184bb725a/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383038353232303334392e706e67)  
受 `background-image: url()` 可以用渐变实现背景启发，类似的，一些函数是不是可以放在 `content` 中来实现？
``` 
    .demo:after {
      content: radial-gradient(circle at 35% 35%, white 10%, pink 70%);
      display: inline-block;
      border-radius: 50%;
      width: 100px;
      height: 100px;
      overflow: hidden;
    }
```

[![在这里插入图片描述](https://camo.githubusercontent.com/97c10b3cff5b9d82d8f03d02045dd6721cb711bba6f581eb0d48d828478e7f17/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383039323132353336392e706e67)](https://camo.githubusercontent.com/97c10b3cff5b9d82d8f03d02045dd6721cb711bba6f581eb0d48d828478e7f17/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383039323132353336392e706e67)  
完美！当然本来就伪元素背景就可以实现，又为什么要放 `content` 呢？

### content: attr() value 属性值的引用

调用当前元素的属性，可以方便的比如将图片的 Alt 提示文字或者链接的 Href 地址显示出来。
``` 
    .demo:after{
    	content: attr(href);
    }
```

[![在这里插入图片描述](https://camo.githubusercontent.com/e6be060104229d07f77911c465e76b04a52a0899235be622e3e0bb7b9fc55932/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383038353530343234382e706e67)](https://camo.githubusercontent.com/e6be060104229d07f77911c465e76b04a52a0899235be622e3e0bb7b9fc55932/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383038353530343234382e706e67)
``` 
    .demo:after{
    	content: attr(class);
    }
```

[![在这里插入图片描述](https://camo.githubusercontent.com/25798d6e403da7968400647745f85c36ebeac46d702b83208ff82dc8a9807ac6/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383038353631323533322e706e67)](https://camo.githubusercontent.com/25798d6e403da7968400647745f85c36ebeac46d702b83208ff82dc8a9807ac6/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383038353631323533322e706e67)

### content: `<counter>` values

调用计数器，可以不使用列表元素实现序号功能。具体请参见 `counter-increment` 和 `counter-reset` 属性的用法。
``` 
    <h1>大标题</h1>
    <h2>中标题</h2>
    <h3>小标题</h3>
    <h3>小标题</h3>
    <h2>中标题</h2>
    <h3>小标题</h3>
    <h3>小标题</h3>
    <h1>大标题</h1>
    <h2>中标题</h2>
    <h3>小标题</h3>
    <h3>小标题</h3>
    <h2>中标题</h2>
    <h3>小标题</h3>
    <h3>小标题</h3>
```
``` 
    h1::before{
        content:counter(h1)'.';
    }
    h1{
        counter-increment:h1;
        counter-reset:h2;
    }
    h2::before{
        content:counter(h1) '-' counter(h2);
    }
    h2{
        counter-increment:h2;
        counter-reset:h3;
        margin-left:40px;
    }
    h3::before{
        content:counter(h1) '-' counter(h2) '-' counter(h3);
    }
    h3{
        counter-increment:h3;
        margin-left:80px;
    }
```

[![在这里插入图片描述](https://camo.githubusercontent.com/2a932f2c2eb5eec2ef3e4446e923f99d4622787caab923fd5c92a080734509f0/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383039303630323132302e706e67)](https://camo.githubusercontent.com/2a932f2c2eb5eec2ef3e4446e923f99d4622787caab923fd5c92a080734509f0/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383039303630323132302e706e67)

### 引用符号

属于引用符号的取值有 4 种，共 2 对，在 CSS 中用了语义较为清晰的关键词来表示： open-quote、 close-quote、no-open-quote、no-close-quote。

默认：
``` 
    .demo::before {
      content: open-quote;
    }
    .demo::after {
      content: close-quote;
    }
```

[![在这里插入图片描述](https://camo.githubusercontent.com/7626f9ac4e7ba3460a1595403d5b3605bd69f03dfa41823d32d700c4c3f164df/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383039313232363538362e706e67)](https://camo.githubusercontent.com/7626f9ac4e7ba3460a1595403d5b3605bd69f03dfa41823d32d700c4c3f164df/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383039313232363538362e706e67)  
自定义引用符号：
``` 
    .demo {
      quotes: "『" "』";
    }
    .demo::before {
      content: open-quote;
    }
    .demo::after {
      content: close-quote;
    }
```

[![在这里插入图片描述](https://camo.githubusercontent.com/6681881d642195d63a85df6c59e37e7f5ee47bf94e7b41b49ee54076088d9bb5/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383039313331333236392e706e67)](https://camo.githubusercontent.com/6681881d642195d63a85df6c59e37e7f5ee47bf94e7b41b49ee54076088d9bb5/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383039313331333236392e706e67)  
`quotes` 可以设置多组引用符号，用以应对次级引用：
``` 
    .demo {
      quotes: "«" "»" "‹" "›";
    }
    .demo::before {
      content: no-open-quote open-quote;
    }
    .demo::after {
      content: close-quote;
    }
```

[![在这里插入图片描述](https://camo.githubusercontent.com/e407c366865bbd399a57fbb8c342cfa4267edaa288842665464459cfc694d950/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383039313531393731392e706e67)](https://camo.githubusercontent.com/e407c366865bbd399a57fbb8c342cfa4267edaa288842665464459cfc694d950/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303139303530383039313531393731392e706e67)

## 总结

以上我们主要了解了 `content` 的一些用法和巧用，当然 `:before` 和 `:after` 本身作为元素，也可以实现多种应用效果，比如：三角形（border）、装饰元素、阴影等。希望通过以上介绍，能让大家对 `content` 有更深入的了解，帮助我们在平时的布局和样式以及用户体验中发挥更大的价值。

Demo codepen 地址：<https://codepen.io/xiangshuo1992/pen/zQGyBW>

END.
