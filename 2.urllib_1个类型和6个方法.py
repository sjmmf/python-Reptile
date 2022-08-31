import urllib.request

url = "http://www.baidu.com"

#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

#一个类型
print(type(response))  #<class 'http.client.HTTPResponse'>

#六个方法

#1.read()  按照一字节一字节去读
content = response.read()
print(content)
#注：read(num)  表示读取num个字节
content = response.read(5)
print(content)

#2.readline()  只能读取一行
content = response.readline()
print(content)

#3.redlines()  读取所有行
content = response.readlines()
print(content)

#4.response.getcode()  返回状态码，200是正确的
print(response.getcode())

#5.response.geturl()  返回url地址
print(response.geturl())

#6.response.getheaders()  获取状态信息
print(response.getheaders)