# window对象和document对象有什么区别？

作者：![AnsonZnl](https://avatars.githubusercontent.com/u/29278068?s=80&u=d0989f3ba8a133fbfef695a84b63c07a08d0d841&v=4)[AnsonZnl](https://github/AnsonZnl)

## window对象

代表浏览器中的一个打开的窗口或者框架，window对象会在或者每次出现时被自动创建，在客户端JavaScript中，Window对象是全局对象global，所有的表达式都在当前的环境中计算，要引用当前的窗口不需要特殊的语法，可以把那个窗口属性作为全局变量使用，例如：可以只写`document`，而不必写`window.document`。同样可以把窗口的对象方法当做函数来使用，如：只写`alert()`，而不必写`window.alert`.  
window对象实现了核心JavaScript所定义的全局属性和方法。

## document对象

代表整个HTML文档，可以用来访问页面中的所有元素 。  
每一个载入浏览器的HTML文档都会成为document对象。document对象使我们可以使用脚本(js)中对HTML页面中的所有元素进行访问。  
**document对象是window对象的一部分** 可以通过window.document属性对其进行访问  
HTMLDocument接口进行了扩展，定义HTML专用的属性和方法，很多属性和方法都是HTMLCollection对象，其中保存了对锚、表单、链接以及其他可脚本元素的引用。
