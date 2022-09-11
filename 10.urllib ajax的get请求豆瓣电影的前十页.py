import urllib.request
import urllib.parse

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=40&limit=20

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=60&limit=20

#page   1   2   3   4
#start  0   20  40  60   -->  start = (page-1)*limit
#limit = 20

#下载豆瓣电影前十页的数据
#（1）请求对象的定制
#（2）获取响应的数据
#（3）下载数据

#每一页的请求对象定制
def create_request(page):
    base_url = "https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&start=0&limit=20"

    data = {
        'start':(page-1)*20,
        'limit':20
    }

    #get请求后面不需要再加    .encode("utf-8")
    new_data = urllib.parse.urlencode(data)

    url = base_url + new_data

    print(url)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
    }

    request = urllib.request.Request(url = url, headers = headers)
    
    #返回相应的定制
    return request


#获取相应数据
def get_content(request):
    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    return content


#内容的下载
def download_content(page, content):
    with open("douban" + str(page) + ".json","w",encoding="utf-8") as fp:
        fp.write(content)


#程序的入口：
if __name__ == '__main__':
    start_page = int(input('请输入起始的页码：'))
    end_page = int(input('请输入结束的页码：'))

    #注意此处range是左闭右开
    for page in range(start_page,end_page+1):
        request = create_request(page)
        content = get_content(request)
        download_content(page,content)
