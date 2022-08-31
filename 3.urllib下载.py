import urllib.request

#下载网页
url_page = "http://www.baidu.com"

#urllib.request.urlretrieve() 参数：url是下载的地址，filename是文件的名字
urllib.request.urlretrieve(url_page,"baidu.html")

#下载图片
url_img = "http://tiebapic.baidu.com/forum/w%3D580/sign=a39d01fb4c24ab18e016e13f05f8e69a/f40847094b36acafdf26722139d98d1003e99c15.jpg?tbpicau=2022-09-02-05_7c7638329cf0bbf1f33982db36765a07"
urllib.request.urlretrieve(url_img,'色图1.jpg')

#下载视频
url_video = "https://haokan.baidu.com/feda5c4d-5a6a-41d7-ab52-252c66956697"
urllib.request.urlretrieve(url_video,'video.mp4')
