# 爬取百度首页中的所有url链接
# 爬取超链接中的url
import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.baidu.com/'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
soup = BeautifulSoup(content, 'lxml')
url_list = soup.select('a')

for url_ba4 in url_list:
    url = url_ba4.attrs.get('href')
    if url != '' and url != None:
        if url[0:2] == '//':
            url = 'https:' + url
            print(url)
        elif url[0:1] == 'h':
            print(url)
