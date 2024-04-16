import urllib.request
url = 'https://www.baidu.com'
#UA定制  解决反爬的手段之一
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

#url的组成
# 协议   主机   端口号（http 80,https 443,mysql 3306,oracle 1521,redis 6379,mongodb 27017） 路径  参数  锚点
#因为urlopen方法中不能存储字典  所以headers不能传递进去
#请求对象的定制
#注意  因为参数顺序的问题 不能直接写url和headers
request =urllib.request.Request(url,[],headers)

response = urllib.request.urlopen(request)
print(response)#response 得到的是一个 HTTPResponse 对象
# 可以通过调用 response.read() 方法读取响应内容，最后使用 .decode("utf-8") 方法将内容解码为字符串形式，从而得到网页的 HTML 内容。
# print(response.read().decode("utf-8")) #读取响应内容，并将其解码为 UTF-8 编码的字符串