# 通过登陆  然后进入到主界面


"""
通过找登陆接口我们发现 登陆的时候需要的参数很多

    __VIEWSTATE: yVyOV291S+hMSvHVTftCmeYlRPbw/whtCvyMsdYS2YtyRUxquzOv8PKKLPwUJu6ti8041/QGyDg+bRbp7wNFV7kyV3vC1x7tfiVNB+J9XHZapjj0aRGIppx+UfrwV5M1pvlrKnf5wkTHdK6JaIUe0+k7J5M=
    __VIEWSTATEGENERATOR: C93BE1AE
    from: http://so.gushiwen.cn/user/collect.aspx
    email: 1252207841@qq.com
    pwd: qerwqe
    code: CBWX
    denglu: 登录

我们观察到__VIEWSTATE  __VIEWSTATEGENERATOR  code是一个可以变化的量

难点：(1) __VIEWSTATE  __VIEWSTATEGENERATOR
    我们观察到这两个数据在页面的源码中，所以我们需要获取页面的源码 然后进行解析就可以获取了
     (2) 验证码


"""

import requests

# 这是登陆界面的url地址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43',
}

response = requests.get(url=url, headers=headers)
content = response.text
# print(content)


# 解析页面源码  然后获取 __VIEWSTATE  __VIEWSTATEGENERATOR

from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'lxml')

# 获取__VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')

# 获取__VIEWSTATEGENERATOR
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn' + code
print(code_url)


# import urllib.request
# urllib.request.urlretrieve(url=code_url, filename='code.jpg')
# 但是使用此方法不行.
# 因为：使用urllib访问下载后
# 验证码就刷新了
# 和后面requests访问的登录就不同了

# requests 里面有一个方法session() 通过session的返回值 就能使请求变成同一个对象
session = requests.session()
# 验证码的url的内容
response_code = session.get(code_url)
# 注意 此时要使用二进制数据 因为我们要使用的是图片的下载
content_code = response_code.content
# wb的模式就是将二进制数据写入到文件中
with open('code.jpg', 'wb',) as fp:
    fp.write(content_code)

"""
    获取了验证码的图片之后 下载到本地 然后观察验证码观察之后，然后在控制台输入这个验证码
    就可以将这个值给code的参数 就可以登录

"""

code_name = input("请输入你的验证码：")


# 点击登录

url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {

    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '1252207841@qq.com',
    'pwd': 'YZPgsw71923',
    'code': code_name,
    'denglu': '登录'

}

response_post = session.post(url=url, data=data_post, headers=headers)

content_post = response_post.text

with open('gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(content_post)



"""
    难点：
        1.隐藏域
        2.验证码


"""

