import urllib.parse
import urllib.request
import json

url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
headers = {
    # "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    # 'Accept':'*/*',
    # 'Accept-Encoding':'gzip, deflate, br',
    # 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
    # 'Connection':'keep-alive',
    # 'Content-Length':'148',
    # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'BIDUPSID=E4EED4AD32F68A0029150518B71E6473; PSTM=1644069814; BAIDUID=E4EED4AD32F68A00C795D774149F4DCE:FG=1; __yjs_duid=1_03f1094640beee76272a007638c459db1644071304166; BDUSS=dsWE1lc0kxbWdZTHNLejFRanNJOVNvZjVQSjJaZnpFWFlIa2t6ZXAyYnhqaWxpSVFBQUFBJCQAAAAAAAAAAAEAAAA0MjAmb285OTU5MzE1NzYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPEBAmLxAQJiR1; BDUSS_BFESS=dsWE1lc0kxbWdZTHNLejFRanNJOVNvZjVQSjJaZnpFWFlIa2t6ZXAyYnhqaWxpSVFBQUFBJCQAAAAAAAAAAAEAAAA0MjAmb285OTU5MzE1NzYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPEBAmLxAQJiR1; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; APPGUIDE_10_0_2=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1644391469,1644461433; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=5; BAIDUID_BFESS=0434881F591F38E40670B2C4E152E2CB:FG=1; H_PS_PSSID=34430_35104_31254_35489_34584_35490_35542_35797_35320_26350_35746; BA_HECTOR=0l0g008g802g8h8ljs1h09avc0r; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1644474869; ab_sr=1.0.1_NjFhODYxOTg3ODkzNmExOThhNGNmZjNkYWQ1MGUyYjgyNWEzMTMzOTcxM2IzY2Q1NDk3ZjE4YzgyZDhlNzIyNTdlYTBhZjY5MTFjOWRiYzgzYTg5ZGExNjQxNGVkM2U1YjQyNzVjMDc4N2M0YTVjYzcyYzAyODMyNjY0MDEyMTM0MTQ4NzllMmFiZTM3MDNlYzY3OTUzMTBmMWE2NzM2YmY5ZDQ5Nzk1NDMzMWI0MWI0ZTg4NDNkNTFmM2M4ZTFm'
    # 'Host':'fanyi.baidu.com',
    # 'Origin': 'https://fanyi.baidu.com',
    # 'Referer': 'https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh',
    # 'sec-ch-ua': '"Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': "Windows",
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'X-Requested-With': 'XMLHttpRequest'
}
data = {
    'from': 'zh',
    'to': 'en',
    'query': '房子',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '289459.35202',
    'token': '1ee0174682b16644fbbcde79861a56e5',
    'domain': 'common',
}
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
#post请求的参数必须进行编码 并且调用encode方法    这个是post请求跟get请求的不同之处
key = urllib.parse.urlencode(data).encode('utf-8')
#请求对象的定制
requestObj = urllib.request.Request(url,key,headers)
#模拟浏览器发送数据
resp = urllib.request.urlopen(requestObj)
context = resp.read().decode('utf-8')
str = json.loads(context)
print(str)
