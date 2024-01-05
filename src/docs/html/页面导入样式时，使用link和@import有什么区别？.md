# 页面导入样式时，使用link和@import有什么区别？

作者：![yxkhaha](https://avatars.githubusercontent.com/u/36123736?s=80&u=aa0740dcf27f2cb0e05f45ada2553d231f249cc4&v=4)[yxkhaha](https://github/yxkhaha)

区别：  
1.link是HTML标签，[@import](https://github.com/import)是css提供的。  
2.link引入的样式页面加载时同时加载，[@import](https://github.com/import)引入的样式需等页面加载完成后再加载。  
3.link没有兼容性问题，[@import](https://github.com/import)不兼容ie5以下。  
4.link可以通过js操作DOM动态引入样式表改变样式，而[@import](https://github.com/import)不可以。
