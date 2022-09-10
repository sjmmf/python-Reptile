#post请求

import urllib.request
import urllib.parse
import json

url = " https://fanyi.baidu.com/sug"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33"
}

data = {
    "kw":"spider"
}

#post的请求参数必须要进行编码，即在urlencode后还要进行encode
new_data = urllib.parse.urlencode(data).encode("utf-8")

#在urllib.request.Request()中第二个参数为"data = "
#post的请求参数是不会拼接在url的后面，而是需要放在请求对象定制的参数中
request = urllib.request.Request(url = url, data = new_data, headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

#此时content是字符串类型
print(type(content))

#打印会发现有许多json字符串无法阅读，所以需要json.loads()来解码
print(content)
#结果如下：
#{"errno":0,"data":[{"k":"spider","v":"n. \u8718\u86db; \u661f\u5f62\u8f6e\uff0c\u5341\u5b57\u53c9; \u5e26\u67c4\u4e09\u811a\u5e73\u5e95\u9505; \u4e09\u811a\u67b6"},{"k":"Spider","v":"[\u7535\u5f71]\u8718\u86db"},{"k":"SPIDER","v":"abbr. SEMATECH process induced damage effect revea"},{"k":"spiders","v":"n. \u8718\u86db( spider\u7684\u540d\u8bcd\u590d\u6570 )"},{"k":"spidery","v":"adj. \u50cf\u8718\u86db\u817f\u4e00\u822c\u7ec6\u957f\u7684; \u8c61\u8718\u86db\u7f51\u7684\uff0c\u5341\u5206\u7cbe\u81f4\u7684"}]}

content = json.loads(content)

#此时将看到编码后的结果
print(content)
#结果如下：
#{'errno': 0, 'data': [{'k': 'spider', 'v': 'n. 蜘蛛; 星形轮，十字叉; 带柄三脚平底锅; 三脚架'}, {'k': 'Spider', 'v': '[电影]蜘蛛'}, {'k': 'SPIDER', 'v': 'abbr. SEMATECH process induced damage effect revea'}, {'k': 'spiders', 'v': 'n. 蜘蛛( spider的名词复数 )'}, {'k': 'spidery', 'v': 'adj. 像蜘蛛腿一般细长的; 象蜘蛛网的，十分精致的'}]}
