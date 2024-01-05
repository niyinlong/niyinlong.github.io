# 你对new操作符的理解是什么？手动实现一个new方法

作者：![BeADre](https://avatars.githubusercontent.com/u/34639100?s=80&u=bb30c2c64e53ab781fc8490aff6d589c020b3bac&v=4)[BeADre](https://github/BeADre)

function _new(Fn, ...arg) {  
const obj = Object.create(Fn.prototype);  
const obj1 = Fn.apply(obj, arg);  
return obj1 instanceof Object ? obj1 : obj;  
}

之前在github看另外一个人写的
