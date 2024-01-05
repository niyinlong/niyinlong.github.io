# 用CSS绘制一个三角形

作者：![xiangshuo1992](https://avatars.githubusercontent.com/u/21164035?s=80&u=8fa0338daad064ce6ed37ce7a3778cf8582ec347&v=4)[xiangshuo1992](https://github/xiangshuo1992)

> > 
```
>>     .triangle{
>>         width: 0;
>>         border-bottom: 35px solid lightgreen;
>>         border-left: 35px solid transparent;
>>     }
```
> 
> wrong
``` 
>     .triangle{
>          width: 0;
>          border: 35px solid transparent;
>          border-bottom: 35px solid lightgreen;
>     }
>     
```

一般会用伪元素来实现这种装饰性的效果，`content` 为空，就不需要 `width` 了，最后 `border` 还可以简单点
``` 
    .triangle:after{
        content: '';
        border: 35px solid transparent;
        border-bottom-color: lightgreen;
    }
```
