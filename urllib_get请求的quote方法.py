import urllib.parse
import urllib.request



#将周杰伦三个字变为unicode编码的格式
#我们需要依赖于urllib.parse
name=urllib.parse.quote('周杰伦')#是为了确保 URL 中的中文字符不会引起歧义或错误解析。
print(name)

url = 'https://www.sogou.com/web?query=' + name
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}


requestObj = urllib.request.Request(url=url, headers=headers)
resp = urllib.request.urlopen(requestObj)
context = resp.read().decode("utf-8")
print(context)
