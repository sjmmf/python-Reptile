#第一页的内容：
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post
# cname: 成都
# pid: 
# pageIndex: 1
# pageSize: 10

#第二页的内容：
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post
# cname: 成都
# pid: 
# pageIndex: 2
# pageSize: 10

import urllib.request
import urllib.parse
import json

#下载前十页的信息

#请求对象定制（post）
def create_request(page):
    base_url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"

    data = {
        'cname':'成都',
        'pid':'',
        'pageIndex':page,
        'pageSize':'10'
    }

    new_data = urllib.parse.urlencode(data).encode("utf-8")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
    }

    request = urllib.request.Request(url=base_url, data=new_data, headers=headers)

    return request

def get_content(request):
    response = urllib.request.urlopen(request)

    content = response.read().decode("utf-8")

    return content

def download(page,content):
    with open("kendeji" + str(page) + ".json","w",encoding="utf-8") as fp:
        fp.write(content)


if __name__ == "__main__":
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))

    for page in range(start_page,end_page + 1):
        request = create_request(page)
        content = get_content(request)
        download(page,content)
