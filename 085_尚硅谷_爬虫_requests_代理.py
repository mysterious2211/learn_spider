
import requests

url = 'http://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43',
}

# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#     # 'Connection': 'keep-alive',
#     'Cookie': 'BIDUPSID=7B2D91344BF8E1CAFCD457ECBAE72FA3; PSTM=1638507561; __yjs_duid=1_d2802d5a64fc3b95e978a26a2193a1231638796369978; BAIDUID=C616C53F8E56C78BEDD58FDDDFE0C0C2:FG=1; BDUSS=WhXeG9sdTZzdE1RRXIzN1N5V1c5bmZ4dDNSLUJIM3dlWjhPY2RRdFB3Y2RFTVZpRVFBQUFBJCQAAAAAAQAAAAEAAAAAj5QiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB2DnWIdg51iT; BDUSS_BFESS=WhXeG9sdTZzdE1RRXIzN1N5V1c5bmZ4dDNSLUJIM3dlWjhPY2RRdFB3Y2RFTVZpRVFBQUFBJCQAAAAAAQAAAAEAAAAAj5QiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB2DnWIdg51iT; newlogin=1; BD_UPN=12314753; BAIDUID_BFESS=C616C53F8E56C78BEDD58FDDDFE0C0C2:FG=1; __bid_n=183f05e27624cf9c964207; ZFY=XvtPPxbwGA69ju6wCgwe7nI6QeMz7:Bt6D93vmNCvYbE:C; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1678693450; FPTOKEN=3k3tRBA0MGQGEVnG+KS65PxFHmCcXB6HsHQWTXGT5nsLAgsXUs4Jm0+BwU8klBPAE0VhtJoK1qRkGMXrkV/KfIqAqKdGGYk9WNLpnXqoS3xhEPh/NbrtagTXoIC1IkclGu5ao5cvHcZxPy32nyR3S/kypNRkdYjPx8ClTB7V6a1g1NFLznLzSqpuO6u9BcpyQSuLTTR+GkJoTlV3Gm+4FGvwlOwpEPt0HlpIM47WIC7bwt9ZB+DX7y4IG/tF+iJSIIqrRTXaKcE0g+c1q/t40Trz6BS2XvsyWvO/V2ag3eGyYVGSXQYuFh6AFZNuhetYU/s6vhLBPuABwgHgoG0ier+F944KJJJSPYPEksotzexzEqKNImmVOJaF89QHIcW2ndwqqomdPxgm2/9Iz05/ig==|LB2ADFj8FmKnMIosV5aE0NSyclDHM1VeowcyREyLN1Q=|10|90e1347917572e1a7e9c19d18b294d71; BD_HOME=1; BA_HECTOR=01a120al2ha1a481050ka0br1i1anm61n; BD_CK_SAM=1; PSINO=5; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; B64_BOT=1; shifen[1912263_91638]=1679124256; BCLID=11967729452334587777; BCLID_BFESS=11967729452334587777; BDSFRCVID=hzIOJexroG07VWbfQfI4UOJWIuweG7bTDYrEOwXPsp3LGJLVFe3JEG0Pts1-dEu-S2OOogKK0eOTHkCF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=hzIOJexroG07VWbfQfI4UOJWIuweG7bTDYrEOwXPsp3LGJLVFe3JEG0Pts1-dEu-S2OOogKK0eOTHkCF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC_-tDvDqTrP-trf5DCShUFsanTAB2Q-XPoO3KtbSx3PblQtyj0AXP6UBRQf5mkf3fbgy4op8P3y0bb2DUA1y4vp0tLeWeTxoUJ2-KDVeh5Gqq-KXU4ebPRiJPQ9QgbW5hQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjK2j5OP; H_BDCLCKID_SF_BFESS=tRAOoC_-tDvDqTrP-trf5DCShUFsanTAB2Q-XPoO3KtbSx3PblQtyj0AXP6UBRQf5mkf3fbgy4op8P3y0bb2DUA1y4vp0tLeWeTxoUJ2-KDVeh5Gqq-KXU4ebPRiJPQ9QgbW5hQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjK2j5OP; ab_sr=1.0.1_OTUwMmQxZDU5YmRmMzU3NzJhMjcxMzFiMmE3ZWViMDk1N2EyMDQyYTQ4NTNjY2EzNDI1YjM4MmRkMzg2MTM0YjBiMzcyNDlhMjQ5MzgwZDkwNWFiYjBmNDQ3NmIxYjJjODI5OGNjMGU0NTU0MDZiZTRkZGNmMGJiYjJhNTBlYWJhNmJiZDBlOTAyZWIzNTdlYzFhNGE4Nzk2Y2ZlZDk3NmI3NWY4ZGJlOGJhYjkxYjZhNGRjNzZmNGJhYWZiZmVm; H_PS_PSSID=38185_36548_38353_37862_38172_38290_38375_36803_37927_38315_38382_38285_38040_26350_38423_38281_37881; COOKIE_SESSION=17_0_9_9_11_15_1_0_7_4_3_4_331343_0_32_0_1678693451_0_1678693419%7C9%231638255_81_1658154212%7C9; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; sugstore=1; H_PS_645EC=eab9h7HN35K1ysCD%2BJcdZBIpo%2Bb4epSaCWFSb5nVGbq5wjbklli2AD8fP0ziVt4IbM5g; baikeVisitId=c52b16c3-9e3f-4454-a3b3-8495fed52da3',
#     # 'Host': 'www.baidu.com',
#     # 'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
#     # 'sec-ch-ua-mobile': '?0',
#     # 'sec-ch-ua-platform': '"Windows"',
#     # 'Sec-Fetch-Dest': 'document',
#     # 'Sec-Fetch-Mode': 'navigate',
#     # 'Sec-Fetch-Site': 'none',
#     # 'Sec-Fetch-User': '?1',
#     # 'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43',
# }

data = {
    'wd': 'ip'
}

proxy = {
    'http': '27.42.168.46:55481'
}

response = requests.get(url=url, params=data, headers=headers,proxies=proxy)
# response = requests.get(url=url, params=data, headers=headers)

response.encoding = 'utf-8'

content = response.text

print(content)

with open('daili.html','w',encoding='utf-8') as fp:
    fp.write(content)
