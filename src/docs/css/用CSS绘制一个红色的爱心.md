# 用CSS绘制一个红色的爱心

作者：![xn213](https://avatars.githubusercontent.com/u/49441268?s=80&u=bd10beb99881d3dfdb215c6c54f20cbc354c0ea7&v=4)[xn213](https://github/xn213)


```
    // 用过 就给贴过来了
        .heart {
          position: relative;
          width: 100px;
          height: 90px;
        }
        .heart:before,
        .heart:after {
          position: absolute;
          content: "";
          left: 50px;
          top: 0;
          width: 50px;
          height: 80px;
          background: red;
          border-radius: 50px 50px 0 0;
          transform: rotate(-45deg);
          transform-origin: 0 100%;
        }
        .heart:after {
          left: 0;
          transform: rotate(45deg);
          transform-origin: 100% 100%;
        }
```
