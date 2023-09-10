# urllib
# (1) 一个类型以及六个方法
# (2) get请求
# (3) post请求    百度翻译
# (4) ajax的get请求
# (5) ajax的post请求
# (6) cookie登录 微博
# (7) 代理


# requests
# (1) 一个类型以及六个属性
# (2) get请求
# (3) post请求
# (4) 代理
# (5) cookie  验证码


import requests

url = 'http://www.baidu.com/s?'
# url = 'http://www.baidu.com/s?wd=%E5%8C%97%E4%BA%AC'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'Cache-Control': 'max-age=0',
    # 'Connection': 'keep-alive',
    'Cookie': 'BIDUPSID=7B2D91344BF8E1CAFCD457ECBAE72FA3; PSTM=1638507561; __yjs_duid=1_d2802d5a64fc3b95e978a26a2193a1231638796369978; BAIDUID=C616C53F8E56C78BEDD58FDDDFE0C0C2:FG=1; BDUSS=WhXeG9sdTZzdE1RRXIzN1N5V1c5bmZ4dDNSLUJIM3dlWjhPY2RRdFB3Y2RFTVZpRVFBQUFBJCQAAAAAAQAAAAEAAAAAj5QiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB2DnWIdg51iT; BDUSS_BFESS=WhXeG9sdTZzdE1RRXIzN1N5V1c5bmZ4dDNSLUJIM3dlWjhPY2RRdFB3Y2RFTVZpRVFBQUFBJCQAAAAAAQAAAAEAAAAAj5QiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB2DnWIdg51iT; newlogin=1; BD_UPN=12314753; BAIDUID_BFESS=C616C53F8E56C78BEDD58FDDDFE0C0C2:FG=1; __bid_n=183f05e27624cf9c964207; ZFY=XvtPPxbwGA69ju6wCgwe7nI6QeMz7:Bt6D93vmNCvYbE:C; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1678693450; COOKIE_SESSION=17_0_9_9_11_15_0_0_7_4_3_4_331343_0_32_0_1678693451_0_1678693419%7C9%231638255_81_1658154212%7C9; FPTOKEN=3k3tRBA0MGQGEVnG+KS65PxFHmCcXB6HsHQWTXGT5nsLAgsXUs4Jm0+BwU8klBPAE0VhtJoK1qRkGMXrkV/KfIqAqKdGGYk9WNLpnXqoS3xhEPh/NbrtagTXoIC1IkclGu5ao5cvHcZxPy32nyR3S/kypNRkdYjPx8ClTB7V6a1g1NFLznLzSqpuO6u9BcpyQSuLTTR+GkJoTlV3Gm+4FGvwlOwpEPt0HlpIM47WIC7bwt9ZB+DX7y4IG/tF+iJSIIqrRTXaKcE0g+c1q/t40Trz6BS2XvsyWvO/V2ag3eGyYVGSXQYuFh6AFZNuhetYU/s6vhLBPuABwgHgoG0ier+F944KJJJSPYPEksotzexzEqKNImmVOJaF89QHIcW2ndwqqomdPxgm2/9Iz05/ig==|LB2ADFj8FmKnMIosV5aE0NSyclDHM1VeowcyREyLN1Q=|10|90e1347917572e1a7e9c19d18b294d71; BD_HOME=1; BA_HECTOR=01a120al2ha1a481050ka0br1i1anm61n; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BD_CK_SAM=1; PSINO=5; delPer=0; H_PS_PSSID=38185_36548_38353_37862_38172_38290_38375_36803_37927_38315_38382_38285_38040_26350_38423_38281_37881; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; sugstore=1; H_PS_645EC=05c82aCd5cAiJXEA2NDUXNPHIxnKGnFdjO7y0sl79nenLHrhvYEThAZBT8U; baikeVisitId=929e4a4e-e81d-44dd-a8f8-5159c3397fd8; B64_BOT=1',
    # 'Host': 'www.baidu.com',
    # 'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'Sec-Fetch-Dest': 'document',
    # 'Sec-Fetch-Mode': 'navigate',
    # 'Sec-Fetch-Site': 'none',
    # 'Sec-Fetch-User': '?1',
    # 'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43',
}

# headers = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43',
# }

data = {
    'wd': '北京'
}

# url  请求资源路径
# params  参数
# kwargs： 字典
response = requests.get(url=url, params=data, headers=headers)
# response = requests.get(url=url, headers=headers)

response.encoding = 'utf-8'

content = response.text

print(content)

"""
总结：
    1.参数使用params传递
    2.参数无需urlencode编码
    3.不需要请求对象的定制
    4.请求资源路径中的？可以加也可以不加

"""
