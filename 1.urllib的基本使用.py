#使用urllib获取百度首页的源码

import urllib.request

#1.定义一个url（就是要访问的地址）
url = 'http://www.baidu.com'

#2.模拟浏览器向服务器发送请求，并用一个变量（响应）进行接收
response = urllib.request.urlopen(url)

#3.获取响应中页面源码，并用一个变量进行接收

content = response.read().decode('utf-8')     
#read方法   返回的是字节形式的二进制数据
#将二进制数据转化为字符串——解码  decode('编码的格式')

#4.打印数据
print(content)