# 请描述css的权重计算规则

作者：![Vi-jay](https://avatars.githubusercontent.com/u/22879017?s=80&u=2796148dbcb3372ff3ac0cc63a70eb049a6e7220&v=4)[Vi-jay](https://github/Vi-jay)

> 这道题去年推特上一个大神发的，几千个人只有一半人对。。。
> 
> 两个123颜色是啥？
``` 
>     <div class="red blue">123</div>
>     <div class="blue red">123</div>
>     
```
``` 
>     .red {
>       color: red;
>     }
>     
>     .blue {
>       color: blue
>     }
```

都是蓝色  
障眼法  
css计算规则和class先后顺序无关
