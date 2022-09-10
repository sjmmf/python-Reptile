import urllib.request
import urllib.parse

# url = "https://www.baidu.com/s?wd=周杰伦"    #此处周杰伦中文是在ascil码127个之外的，直接解码会报错，除非用unicode编码

url = "https://www.baidu.com/s?wd="

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"}

#将“周杰伦”三个字变成Unicode编码的格式
#需要引入urllib.parse
name = urllib.parse.quote('周杰伦')
url = url + name

request = urllib.request.Request(url = url, headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

print(content)

#get请求方法是指在浏览器“检查” —— “网络” —— “对应网站” —— “General”中的Request method中显示GET