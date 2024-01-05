# label都有哪些作用？并举相应的例子说明

作者：![MartinsYong](https://avatars.githubusercontent.com/u/15402214?s=80&u=473f03a1d4b8e2361c9a39f813ae732556ef7916&v=4)[MartinsYong](https://github/MartinsYong)

前面那些同学已经说到`input`与`label`互相关联的机制，这里我就说一下具体实例：

  1. 利用`label`"模拟"`button`来解决不同浏览器原生`button`样式不同的问题


``` 
    <input type="button" id="btn">
    <label for="btn">Button</label>
    
    <style>
    input[type='button'] {
      display: none;
    }
    
    label {
      display: inline-block;
      padding: 10px 20px;
      background: #456;
      color: #fff;
      cursor: pointer;
      box-shadow: 2px 2px 4px 0 rgba(0,0,0,.3);
      border-radius: 2px;
    }
    </style>
```

  2. 结合`checkbox`、`radio`表单元素实现纯CSS状态切换，这样的实例就太多了。比如控制CSS动画播放和停止。下面是一部分代码。[详细实例地址](https://codepen.io/mts123/pen/EzqdbM)


``` 
    <input type="checkbox" id="controller">
    <label class="icon" for="controller">
      <div class="play"></div>
      <div class="pause"></div>
    </label>
    <div class="animation"></div>
    
    <style>
    ...
    #controller:checked ~ .animation {
      animation-play-state: paused;
    }
    ...
    </style>
```

还有一个基于 `radio` 的实例：[摩斯密码键盘](https://codepen.io/mts123/pen/vqpQvR)

  3. `input`的`focus`事件会触发锚点定位，我们可以利用`label`当触发器实现选项卡切换效果。下面代码选自张鑫旭《CSS世界》。[实际效果链接](https://demo.cssworld.cn/6/4-3.php)


``` 
    <div class="box">
      <div class="list"><input id="one" readonly>1</div>
      <div class="list"><input id="two" readonly>2</div>
      <div class="list"><input id="three" readonly>3</div>
      <div class="list"><input id="four" readonly>4</div>
    </div>
    <div class="link">
      <label class="click" for="one">1</label>
      <label class="click" for="two">2</label>
      <label class="click" for="three">3</label>
      <label class="click" for="four">4</label>
    </div>
    
    <style>
    .box {
      width: 20em;
      height: 10em;
      border: 1px solid #ddd;
      overflow: hidden;
    }
    .list {
      height: 100%;
      background: #ddd;
      text-align: center;
      position: relative;
    }
    .list > input { 
      position: absolute; top:0; 
      height: 100%; width: 1px;
      border:0; padding: 0; margin: 0;
      clip: rect(0 0 0 0);
    }
    </style>
```
