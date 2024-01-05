# 请说下你对__proto__和prototype的理解

作者：![myprelude](https://avatars.githubusercontent.com/u/20411555?s=80&u=987fffe199ce170f884390cff09c1590de6f940c&v=4)[myprelude](https://github/myprelude)

  * 只有函数对象才有prototype属性；prototype对象上存放共用的方法和属性
  * 对象都有__proto__属性，__proto__是指向该对象构造函数的原型属性（即prototype）


``` 
    function Parent(name){
      this.name = name
    }
    Parent.prototype = {
      contructor:Parent,
      speak:function(){
        console.log(`我是${this.name}`)
      }
    }
    var children = new Parent('xiaoming')
    children.name  // xiaoming
    children.speak() // 我是xiaoming
    children.__proto__ ===Parent.prototype  // true       
    Parent.prototype.__proto__ === Object.prototype  // true  
    children.toString()  // "[object Object]"
```

上面可以看出通过__proto__属性我们可以拿到Object原型对象上的属性和方法，原型对象上的__proto__又指向该构造函数的prototype，从而形成了一条原型链。上面children能够使用toString方法的原因。
