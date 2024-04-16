import urllib.request


#下载网页
url_page='http://www.baidu.com'
resp = urllib.request.urlopen(url_page)
print(resp)
context = resp.read().decode("utf-8")
print(context)
#在python中可以写变量的名字  也可以直接写值
#返回类型HttpResponse

# urllib.request.urlretrieve(url_page,'baidu.html')

#下载图片

# url_image='https://img0.baidu.com/it/u=448817627,3885560910&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=750'
# urllib.request.urlretrieve(url_image,'lisa.png')

#下载视频
url_video='https://haokan.baidu.com/cc59fa2d-dc85-4475-a220-1cc6384d569c'
urllib.request.urlretrieve(url_video,'qgrd.mp4')
