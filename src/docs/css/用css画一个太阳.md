# 用css画一个太阳

作者：![Vi-jay](https://avatars.githubusercontent.com/u/22879017?s=80&u=2796148dbcb3372ff3ac0cc63a70eb049a6e7220&v=4)[Vi-jay](https://github/Vi-jay)


```
     <section class="c-sun">
          <div class="c-sun__circle"></div>
          <div class="c-sun__arrow" v-for="i in 10" :key="i"></div>
        </section>
```
``` 
        .c-sun {
          display: inline-block;
          position: relative;
          &__circle {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: yellow;
          }
          &__arrow {
            width: 100%;
            position: absolute;
            top: 50%;
            left: 50%;
            @for $i from 1 to 12 {
              &:nth-child(#{$i}) {
                transform: translate(-50%, -50%) rotateZ($i * 36deg);
              }
            }
            &:after {
              position: absolute;
              right: -25px;
              content: "";
              display: block;
              border: 10px solid transparent;
              border-left-color: #ffdc18;
              animation: flashing 1s ease-in-out alternate-reverse infinite;
            }
          }
          @keyframes flashing {
            from {
              opacity: .5;
              transform: translate(10%, 10%);
            }
          }
        }
    
```

[![抖个激灵](https://user-images.githubusercontent.com/22879017/62183554-3c9a0c00-b38d-11e9-98cb-3203ae8cfe99.gif)](https://user-images.githubusercontent.com/22879017/62183554-3c9a0c00-b38d-11e9-98cb-3203ae8cfe99.gif)
