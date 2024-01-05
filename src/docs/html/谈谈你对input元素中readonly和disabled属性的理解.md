# 谈谈你对input元素中readonly和disabled属性的理解

作者：![yxkhaha](https://avatars.githubusercontent.com/u/36123736?s=80&u=aa0740dcf27f2cb0e05f45ada2553d231f249cc4&v=4)[yxkhaha](https://github/yxkhaha)

  * 相同点：都会使文本框变成只读，不可编辑。
  * 不同点：  
1.disabled属性在将input文本框变成只读不可编辑的同时，还会使文本框变灰，但是readonly不会。  
2.disabled属性修饰后的文本框内容，在不可编辑的同时，通过js也是获取不到的。但是用readonly修饰后的文本框内容，是可以通过js获取到的，也就只是简单的不可编辑而已！  
3.disabled属性对input文本框，单选radio,多选checkbox都适用，但是readonly就不适用，用它修饰后的单选以及多选按钮仍然是可以编辑状态的。


