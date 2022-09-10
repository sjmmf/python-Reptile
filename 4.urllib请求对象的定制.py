import urllib.request

url = "https://www.baidu.com"

#url的组成
#1.协议：http/https
#2.主机：如www.baidu.com
#3.端口号，常见端口号如下：
 
# http          80
# https         443
# mysql         3306
# oracle        1521
# redis         6379
# mongodb       27017

#4.路径
#5.参数
#6.锚点


# response = urllib.request.urlopen(url)
# content = response.read().decode('utf-8')
# print(content)

#下面是上述代码运行后结果，不完整的原因：UA（User Agent）——用户代理
# <html>
# <head>
#         <script>
#                 location.replace(location.href.replace("https://","http://"));
#         </script>
# </head>
# <body>
#         <noscript><meta http-equiv="refresh" content="0;url=http://www.baidu.com/"></noscript>
# </body>
# </html>


#在浏览器中点击“检查”，点击“网络”，然后刷新页面，找到对应网站，点击后拉到最下面复制User-Agent，并以字典形式进行存储
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

#因为urlopen方法中不能存储字典，所以headers不能传递进去，需要进行请求对象定制
request = urllib.request.Request(url = url ,headers = headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)


