# 关于_form_标签的enctype属性你有哪些了解？

作者：![chenfaxiang](https://avatars.githubusercontent.com/u/14236469?s=80&u=eb5a665ca894e2d777ad0c19d9638a80a9f986bc&v=4)[chenfaxiang](https://github/chenfaxiang)

form 标签的 enctype 属性指定将数据回发到服务器时浏览器如果对表单数据进行编码，其有三种编码形式：

  1. application/x-www-form-urlencoded(也是默认格式)  
application/x-www-form-urlencoded编码类型会将表单中发送到服务器之前都会进行编码(空格转换为 "+" 加号，特殊符号转换为 ASCII HEX 值)，数据编码成键值对的形式，当表单的action为post时，它会把form数据封装到 http body 中，然后发送到服务器；当表单的action位get时，它会把表单中发送的数据转换成一个字符串(如：a=1&b=2&c=3)并使用?连接到 url 后面。在不指定 enctype 属性时 application/x-www-form-urlencoded 是默认属性。
  2. multipart/form-data  
它不对字符进行编码，在使用包含文件(如图片、mp4等文件)上传控件的表单时必须使用该值
  3. text/plain  
数据以纯文本格式进行编码，空格转换为 "+" 加号，但不对特殊字符编码


