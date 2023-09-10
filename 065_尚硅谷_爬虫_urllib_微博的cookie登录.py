# 适用的场景：在数据采集的时候 需要染过登陆 然后进入到某个页面
# 个人信息页面是utf-8 但是还报错了编码错误，因为并没有进入到个人信息页面 而是跳转到了登录页面
# 然而登录页面不是utf-8，所有报错

# 什么情况下访问不成功？
# 因为请求头的信息不够，所以访问不成功

import urllib.request

url = 'https://weibo.cn/7726823861/info'

headers = {
    # 带:的都不好使 编码encoding也不需要
    # ':authority':' weibo.cn',
    # ':method':' GET',
    # ':path':' /7726823861/info',
    # ':scheme':' https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'accept-encoding':' gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    #   cookie中携带者你的登录信息  如果有登录之后的cookie 那么我们就可以携带者cookie进入到任何页面
    'cookie': '_T_WM=94115e91e8f400c1db20bfc011e8b8ba; MLOGIN=0; SUB=_2A25JDbs_DeRhGeFJ6VQZ8i3EzT2IHXVq8cV3rDV6PUJbkdAGLVLjkW1NfEbYA3dIuNR2ZuvmFNx0kiMdOt-zIt5r; SCF=ApFuvJEDpGTkSy7Ts3vNiBb_vHTjDofT3iERRcqHXulJ5pZOs0ObvZ3WkTsiRQuvzODmLsMl7tqDmuzdTkRbwNo.; SSOLoginState=1678363503',
    # referer : 判断当前路径是不是有上一个路径进来的  一般情况下 作为图片的防盗链
    'referer': 'https://weibo.cn/?tf=5_009',
    'sec-ch-ua': ' "Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': ' ?0',
    'sec-ch-ua-platform': ' "Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': ' same-origin',
    'sec-fetch-user': ' ?1',
    'upgrade-insecure-requests': ' 1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
}
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取响应的数据
content = response.read().decode('utf-8')

# 将数据保存到本地
with open('weibo.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
