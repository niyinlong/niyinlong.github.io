# 写一个方法，使得sum(x)(y)和sum(x,y)返回的结果相同

作者：![AnsonZnl](https://avatars.githubusercontent.com/u/29278068?s=80&u=d0989f3ba8a133fbfef695a84b63c07a08d0d841&v=4)[AnsonZnl](https://github/AnsonZnl)

  * 写一个方法，使得sum(x)(y)和sum(x,y)返回的结果相同


``` 
    var sum= function(x){
        if(arguments[1]){
            return x + arguments[1];
        }else{
            return function (y){
                return x + y
            }
        }
    }
    console.log(sum(1)(2))//3
    console.log(sum(1,2))//3
    
```

  * 群里的提议 增加点难度 使得sum(x)(y)(z)(...)(a)和sum(x,y,z,... a)返回的结果相同


``` 
    function sum(x){
        if(arguments[1]){
            var arr = Array.prototype.slice.apply(arguments);
                x = arr.reduce((a, c)=> a+ c)
            return x;
        }else{
            function add(b) { 
                x = x + b; 
                return add;
            }
            add.toString = function() { 
                return x;
            }
            return add; 
        }
    }
    var res1 = sum(1)(2)(3)(4)(5)(6);
    var res2 = sum(1,2,3,4,5,6);
    console.log(res1)//21
    console.log(res2)//21
    
```

在 [JavaScript 高阶函数浅析](https://github.com/yygmind/blog/issues/36) 获取的灵感
