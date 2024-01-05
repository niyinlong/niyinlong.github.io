# 说说你对arguments的理解，它是数组吗？

作者：![zhangkuibao](https://avatars.githubusercontent.com/u/48234478?s=80&u=7f958f85ad54a25693900fc106c4903c22ce587d&v=4)[zhangkuibao](https://github/zhangkuibao)


```
            1.实参列表,是类数组,不是数组
            2.是传入参数的一个镜像(浅拷贝)
            3.arguments.callee是函数本身, 严格模式禁用arguments.callee
    
```
