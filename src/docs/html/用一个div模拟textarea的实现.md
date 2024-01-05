# 用一个div模拟textarea的实现

作者：![AnsonZnl](https://avatars.githubusercontent.com/u/29278068?s=80&u=d0989f3ba8a133fbfef695a84b63c07a08d0d841&v=4)[AnsonZnl](https://github/AnsonZnl)

哈哈 ，在补充一点，加上`overflow:auto;`会更像哦；  
补充一下完整代码：
``` 
    <!DOCTYPE html>
    <html>
    <head>
        <title>用一个div模拟textarea的实现</title>
    </head>
    <style>
    .edit{
        width: 300px;
        height: 200px;
        padding: 5px;
        border: solid 1px #ccc;
        resize: both;
        overflow:auto;
    }
    </style>
    <body>
        <h3>用一个div模拟textarea的实现</h3>
          <div class="edit" contenteditable="true">
            这里是可以编辑的内容，配合容器的 overflow ，多行截断，自定义滚动条，简直好用的不要不要的。
        </div>
    </body>
    </html>
    
```

我在codepen上做了一个演示地址，有兴趣的可以查看：<https://codepen.io/ansonznl/pen/LozrgK>
