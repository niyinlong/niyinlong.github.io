# 用css创建一个三角形，并简述原理

作者：![poporeki](https://avatars.githubusercontent.com/u/22537106?s=80&u=993e76236b7f7b2583ea5ca2eb78ce15298fae00&v=4)[poporeki](https://github/poporeki)


```
    <div class='rect'></div>
    <style>
        .rect {
          width: 0;
          height: 0;
          background-color: #fff;
          border-right: 100px solid rgb(34, 230, 220);
          border-left: 100px solid rgb(202, 146, 25);
          border-top: 100px solid rgb(29, 156, 194);
          border-bottom: 100px solid rgb(16, 204, 101);
        }
      </style>
```

[![image](https://camo.githubusercontent.com/55fd8e7668cbeaba0f03a7f45df97657eb2d006f36d406fc9d8a0488bdfbc0b7/687474703a2f2f696d6167652e79616e736b2e636e2f466c4d6861416b7445694171746f6255525757357a4c327049424a61)](https://camo.githubusercontent.com/55fd8e7668cbeaba0f03a7f45df97657eb2d006f36d406fc9d8a0488bdfbc0b7/687474703a2f2f696d6167652e79616e736b2e636e2f466c4d6861416b7445694171746f6255525757357a4c327049424a61)  
创建一个div，宽高都为0，实现效果如下，发现border的四个边都是一个三角形，要实现三角形只需将其中几个边`background`设置为`transparent`，即可得到三角形
``` 
      <style>
        .rect {
          width: 0;
          height: 0;
          background-color: #fff;
          border-right: 100px solid transparent;
          border-left: 100px solid transparent;
          border-top: 100px solid rgb(29, 156, 194);
          border-bottom: 100px solid transparent;
        }
      </style>
```

[![image](https://camo.githubusercontent.com/488c469314e7e7328af71eec7a68f0d7621e8083a262df8d898642ef68b0bfc0/687474703a2f2f696d6167652e79616e736b2e636e2f466d31393433597530565252364e4177794c31767266454642476b53)](https://camo.githubusercontent.com/488c469314e7e7328af71eec7a68f0d7621e8083a262df8d898642ef68b0bfc0/687474703a2f2f696d6167652e79616e736b2e636e2f466d31393433597530565252364e4177794c31767266454642476b53)
