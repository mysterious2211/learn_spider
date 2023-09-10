
import urllib.request

# url = 'https://blog.csdn.net/m0_73228832/article/details/129137988'
# url = 'https://blog.csdn.net/m0_73228832/article/details/1291379881'
url = 'http://www.yzp111.com'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
    }


try:
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print('系统正在升级。。。')
except urllib.error.URLError:
    print('系统正在升级啊。。。')


