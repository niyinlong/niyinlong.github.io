# 说说你对同构和SSR的理解

作者：![thisisandy](https://avatars.githubusercontent.com/u/9465232?s=80&u=a20f27fc62eafd722f1e911ec634d28ae074d1dd&v=4)[thisisandy](https://github/thisisandy)

Isomorphism, 同构，指一套代码既可以在server端工作，也可以在web 客户端运行，可以无缝在server端和client端渲染两种模式间切换。这个概念由airbnb的Rendr发扬光大。  
所以一楼说的其实指的并不是同构JS，而是Universal Javascript.

在PWA 大行其道的环境下，因为爬虫需要和框架初始化容易白屏等等问题，服务端渲染的呼声又物论沸腾。SSR其实就是在server端把需要的页面和数据组装起来发给客户端而已。

SSR的好处

  * SEO友好
  * 首页加载更快
  * 减少请求


