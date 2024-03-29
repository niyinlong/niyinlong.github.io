# 你理解的_use strict_;是什么_使用它有什么优缺点？

作者：![github-linong](https://avatars.githubusercontent.com/u/30680461?s=80&u=b2980c6c1dd2b5e1d2b7d86f04f86057df580d1d&v=4)[github-linong](https://github/github-linong)

严格模式，其实就是更严格了

> 设立"严格模式"的目的，主要有以下几个：  
>  \- 消除Javascript语法的一些不合理、不严谨之处，减少一些怪异行为;  
>  \- 消除代码运行的一些不安全之处，保证代码运行的安全；  
>  \- 提高编译器效率，增加运行速度；  
>  \- 为未来新版本的Javascript做好铺垫。

我放几个常见的吧，详情可以去下面的文章中看

  1. 禁止this关键字指向全局对象
  2. 禁止在函数内部遍历调用栈
  3. 全局变量必须显式声明
  4. arguments不再追踪参数的变化


``` 
    (function(){
    	"use strict"
    	b=1//Uncaught ReferenceError: b is not defined
    })()
    
```

<https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Strict_mode>  
<http://www.ruanyifeng.com/blog/2013/01/javascript_strict_mode.html>
