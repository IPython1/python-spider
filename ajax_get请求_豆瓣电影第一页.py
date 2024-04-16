import urllib.parse
import urllib.request
import json
# url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
# url = 'https://movie.douban.com/j/chart/top_list?type=19&interval_id=100%3A90&action=&start='+page+'&limit=20'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}


def getjson(page):
    url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=' + str(
        (page - 1) * 20) + '&limit=20'
    requestObj = urllib.request.Request(url=url, headers=headers)#请求对象的定制
    resp = urllib.request.urlopen(requestObj)
    context = resp.read().decode('utf-8')
    return context


def download(page, context):
    #open方法默认情况下使用的是gbk的编码 如果我们要保存汉字 需要在open方法中指定编码格式为utf-8
    with open("豆瓣电影_第" + str(page) + "页.json", 'w', encoding='utf-8') as fp:
        fp.write(context)


if __name__ == '__main__':
    start_page = int(input("开始页"))
    end_page = int(input("结束页"))
    for page in range(start_page, end_page + 1):
        context = getjson(page)
        if context != '[]':
            download(page, context)
