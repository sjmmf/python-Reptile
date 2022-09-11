import urllib.request
import urllib.parse

url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20"

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
}

request = urllib.request.Request(url = url, headers = headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
print(content)

#数据下载到文件
#可以看到数据是以json的数组形式和对象形式结合呈现的，则保存的文件格式为.json
fp = open('douban.json','w',encoding = "utf-8")
#如果数据含有中文，就一定要用  encoding = "utf-8"
fp.write(content)
fp.close()