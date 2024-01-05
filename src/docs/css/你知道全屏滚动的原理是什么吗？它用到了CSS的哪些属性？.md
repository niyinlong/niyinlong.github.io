# 你知道全屏滚动的原理是什么吗？它用到了CSS的哪些属性？

作者：![klren0312](https://avatars.githubusercontent.com/u/10903843?s=80&u=c8175b9cfc03d354c34a55a3d23dec5114b43bae&v=4)[klren0312](https://github/klren0312)

# 全屏滚动

## 1.知识点

  * JS 滚动监听事件
  * JS 移动端touch监听事件
  * 函数节流
  * DOM操作



## 2.示例GIF

[![示例GIF](https://user-images.githubusercontent.com/10903843/63244980-775ada00-c291-11e9-9da9-be713eb8c347.gif)](https://user-images.githubusercontent.com/10903843/63244980-775ada00-c291-11e9-9da9-be713eb8c347.gif)

## 3.代码分析

### 1.CSS

html, body设置 overflow 为 hidden, 让视图中只包括一个分页;设置滑动分页的长宽都是 100%; 外部容器设置 transition 过渡效果, 并设置为相对定位, 滚动是修改外部容器的 Top 值, 实现滚动效果.
``` 
    html,
    body {
      padding: 0;
      margin: 0;
      overflow: hidden;
    }
    .page-container {
      position: relative;
      top: 0;
      transition: all 1000ms ease;
      touch-action: none;
    }
    .page-item {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
      height: 100%;
      border: 1px solid #ddd;
    }
```

### 2.HTML

初始三个分页
``` 
    <div class="page-container">
      <div class="page-item">1</div>
      <div class="page-item">2</div>
      <div class="page-item">3</div>
    </div>
```

### 3.JavaScript

1.初始化值  
容器高度设置为窗口高度
``` 
    var container = document.querySelector('.page-container')
    // 获取根元素高度, 页面可视高度
    var viewHeight = document.documentElement.clientHeight
    // 获取滚动的页数
    var pageNum = document.querySelectorAll('.page-item').length
    // 初始化当前位置, 距离原始顶部距离
    var currentPosition = 0
    // 设置页面高度
    container.style.height = viewHeight + 'px'
```

2.初始化滚动事件  
向下滚动时, 当 `currentPosition` 比 `-整体分页高度` 大的时候(绝对值相比小的时候), 向下滚动;向上滚动时, 当 `currentPosition` 大于 `0` 的时候, 向上滚动.
``` 
    // 向下滚动页面
    function goDown () {
      if (currentPosition > - viewHeight * (pageNum - 1)) {
        currentPosition = currentPosition - viewHeight
        container.style.top = currentPosition + 'px'
      }
    }
    
    // 向上滚动页面
    function goUp () {
      if (currentPosition < 0) {
        currentPosition = currentPosition + viewHeight
        container.style.top = currentPosition + 'px'
      }
    }
```

3.节流函数  
即在规定时间内只会触发一次指定方法, 用于滚动时防止多次触发
``` 
    function throttle (fn, delay) {
      let baseTime = 0
      return function () {
        const currentTime = Date.now()
        if (baseTime + delay < currentTime) {
          fn.apply(this, arguments)
          baseTime = currentTime
        }
      }
    }
```

4.监听鼠标滚动  
滚动事件`firefox`与其他浏览器的事件不同, 所以需要进行判断. `deltaY`大于`0`的时候, 想下滚动; 反之, 向上滚动.
``` 
    var handlerWheel = throttle(scrollMove, 1000)
    // https://developer.mozilla.org/en-US/docs/Web/API/Element/mousewheel_event#The_detail_property
    // firefox的页面滚动事件其他浏览器不一样
    if (navigator.userAgent.toLowerCase().indexOf('firefox') === -1) {
      document.addEventListener('mousewheel', handlerWheel)
    } else {
      document.addEventListener('DOMMouseScroll', handlerWheel)
    }
    function scrollMove (e) {
      if (e.deltaY > 0) {
        goDown()
      } else {
        goUp()
      }
    }
```

5.监听移动端touch操作  
当 touch 的最终位置大于起始位置时, 则页面向上滚动; 反之, 向下滚动.
``` 
    var touchStartY = 0
    document.addEventListener('touchstart', event => {
      touchStartY = event.touches[0].pageY
    })
    var handleTouchEnd = throttle(touchEnd, 500)
    document.addEventListener('touchend', handleTouchEnd)
    function touchEnd (e) {
      var touchEndY = e.changedTouches[0].pageY
      if (touchEndY - touchStartY < 0) { // 向上滑动, 页面向下滚动
        goDown()
      } else {
        goUp()
      }
    }
```

## 4.参考资料

  * <https://developer.mozilla.org/zh-CN/docs/Web/API/Document/documentElement>
  * <https://developer.mozilla.org/zh-CN/docs/Web/API/Element/clientHeight>
  * <https://developer.mozilla.org/en-US/docs/Web/API/Element/mousewheel_event#The_detail_property>
  * <https://developer.mozilla.org/en-US/docs/Web/API/Touch_events>


