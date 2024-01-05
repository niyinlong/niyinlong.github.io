# 举例子说明javascript的变量声明提升和函数声明提升

作者：![wenyejie](https://avatars.githubusercontent.com/u/4539115?s=80&u=83563ed60a057c87570d7631833f3835dfbf3479&v=4)[wenyejie](https://github/wenyejie)

> 
```
>     var getName = function(){
>       console.log(4)
>     }
>     
>     function getName() {
>       console.log(5)
>     }
>     
>     getName() // 4 函数声明优先级高于var声明,  故 4 覆盖了 5
```

不是4的优先级是高于5, 而是5的优先级高于4,  
5先声明, 但是后来它被4覆盖而已
