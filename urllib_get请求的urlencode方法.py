import urllib.parse
import urllib.request

data = {
    'query':'蝙蝠侠',
    'w':'01019900'
}

searchWord = urllib.parse.urlencode(data)
print(searchWord)
preUrl = 'https://www.sogou.com/web?'
url = preUrl+searchWord

requestObj = urllib.request.Request(url,[],headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'})

resp = urllib.request.urlopen(requestObj)
context = resp.read().decode("utf-8")
# print(context)
