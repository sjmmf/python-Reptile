import urllib.request
import urllib.parse
import json

url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"

headers = {
    #这里面最关键的就是Cookie，反爬的一种形式就是Cookie

    'Accept':' */*',
    #'Accept-Encoding':' gzip, deflate, br',
    #上面这句话一定要注释掉，因为我们要是用的格式为utf-8
    'Accept-Language':' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Acs-Token':' 1662793377676_1662820210080_ZPNVBscPJFn5yfxk6Z04xr8hfDbQlZHV9JiKgeawDcYbmu4Hna3RJ+55X8potGZdTr7d08j9X6PicJBjru2DVEsQEdP8zbZncU3sc91p6mUKW/KbSeni+rL3UmwvlSStJWAgIGC0EzYtRsqYJcX38dyVFd2z1EWwNbCava9HVdFEFmihGVgE3GpLNG1vy7/B2DcMmDbq1GFKVodsgRSAV3hLe+zxOWHx5OcCiJvigJRKA5pMYdZDu93+8s/1yVIRMgv4B1+PtBfd8YIyXn9kfk7obhjX0oTip9wGGTp3EC2P5zcw6ULL48ewYSZ/Fyoz2ygxqNE1MSu4pBVTm3j5Ag==',
    'Connection':' keep-alive',
    'Content-Length':' 136',
    'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=57BE3C6969603538703436AC4D9152D6; PSTM=1657202875; BAIDUID=57BE3C69696035384D97F70FFFE21BF6:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; BDUSS=RNdHdnMUh-aklsaHZvWW52Y0p3SE9jbXI5S0JaODNQajJSdHNSTFNrWDd6UkpqRVFBQUFBJCQAAAAAAAAAAAEAAACy5xmqbG1zMjIyMjMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPtA62L7QOtiZ1; BDUSS_BFESS=RNdHdnMUh-aklsaHZvWW52Y0p3SE9jbXI5S0JaODNQajJSdHNSTFNrWDd6UkpqRVFBQUFBJCQAAAAAAAAAAAEAAACy5xmqbG1zMjIyMjMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPtA62L7QOtiZ1; BAIDUID_BFESS=57BE3C69696035384D97F70FFFE21BF6:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1661956011,1662112942,1662634017,1662816636; BDRCVFR[lNj8FFCrJQ_]=aVHnJ_nap9nrHR1PW03QhPEUf; H_PS_PSSID=26350; BA_HECTOR=20aha50k21a10l2kag84lgf31hhp5mh18; ZFY=Rv7iMgNWQ84UOkYba8Og9dUBegVywEhB4sKWNlLRJfw:C; delPer=0; PSINO=6; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1662820182; ab_sr=1.0.1_OWRlZWQ5MDhkZmZlYjRlZTI0NTIxMjQ0ZDQ2YzdkMzY3OWI0YWQ0NmMxM2JmNmJjY2Y0MDExNzc4ZDVjNDFlNTNmOTUzYzliZjA2Y2NhOWYxOTNmMDRkYjA0NmFjMjFkYzIwOTRkM2I5MzMxY2JjZDhhNWMxMTc0YzlkZGU0ZTkxYTE2NGZlMWIwYjQyYmVkZjdhMjZlNDdkZWQyNWFmNTk5YjcxMmQyNTY0NDU3MTEwNTViODhhNTI2NzVmNTgw',
    'Host':' fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'sec-ch-ua':' "Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"',
    'sec-ch-ua-mobile':' ?0',
    'sec-ch-ua-platform':' "Windows"',
    'Sec-Fetch-Dest':' empty',
    'Sec-Fetch-Mode':' cors',
    'Sec-Fetch-Site':' same-origin',
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
    'X-Requested-With':' XMLHttpRequest'
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'spider',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '63766.268839',
    'token': 'bbb727e3d63cf3f03f8b352692d68bb9',
    'domain': 'common'
}

new_data = urllib.parse.urlencode(data).encode("utf-8")

request = urllib.request.Request(url = url, data = new_data, headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

print(content)

content = json.loads(content)

print(content)
#如果headers只有User-Agent，结果是：
#{'errno': 997, 'errmsg': '未知错误', 'query': 'spider', 'from': 'en', 'to': 'zh', 'error': 997}