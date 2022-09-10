import urllib.request
import urllib.parse

#urlencode的应用场景：多个参数的时候，如：https://www.baidu.com/s?wd=周杰伦&sex=男&location=中国台湾省
#同样要引入urllib.parse

#声明一个基础的url与new_data进行拼接
base_url = "https://www.baidu.com/s?"

data = {
    "wd":"周杰伦",
    "sex":"男",
    "location":"中国台湾省"
}

new_data = urllib.parse.urlencode(data)
#会自动将字典中的每个value转换为Unicode编码并用&符号连接
url = base_url + new_data

headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
}

request = urllib.request.Request(url = url, headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

print(content)