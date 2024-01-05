# 写一个获取当前url查询字符串中的参数的方法

作者：![qqdnnd](https://avatars.githubusercontent.com/u/38306185?s=80&v=4)[qqdnnd](https://github/qqdnnd)


```
    function urlParam(){
        const param = {};
        location.search.replace(/([^&=?]+)=([^&]+)/g,(m,$1,$2)=> param[$1] = $2);
        return param;
    }
    
```
