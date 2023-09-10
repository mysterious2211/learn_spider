import urllib.request

url = 'https://www.baidu.com'

"""
url的组成：
    1.协议：http/https：相比于http。https新加如了一个ssl加密，更加安全
    2.主机：域名,例如：www.baidu.com
    3.端口号
        http: 80
        https: 443
        mysql: 3306
        oracle:1521
        redis: 6379
        mongodb: 27017
    4.路径
    5.参数
    6.锚点

"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
}

# 因为urlopen方法中不能存储字典，所有headers不能传递进去
# 请求对象的定制，因为urlopen方法中可以传入request的对象作为参数
# 注意因为参数顺序的问题，不能直接写url和headers  中间还有data，所以我们需要关键字传参
request = urllib.request.Request(url=url, headers=headers)


response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)