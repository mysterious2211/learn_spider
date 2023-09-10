import urllib.request

url = 'https://www.baidu.com/s?wd=ip'


# edge的请求头
# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
# }

headers = {
    # ':authority': 'cn.bing.com',
    # ':method': 'GET',
    # ':path': '/search?q=ip',
    # ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': 'SRCHD=AF=EMSDS0; SRCHUID=V=2&GUID=F7B3AE25801443A483D616CB07F4A5DD&dmnchg=1; MUID=226105997C5F6407099C149B7D8D6571; MUIDB=226105997C5F6407099C149B7D8D6571; _UR=QS=0&TQS=0; MMCASM=ID=4172DD0607CE4EE09E3053021914C572; _ITAB=STAB=TR; ANON=A=CF46CC8CA02EB981F5280772FFFFFFFF&E=1b59&W=1; PPLState=1; _clck=18psbxv|1|f4x|0; imgv=lodlg=3&gts=20221202&flts=20220824; _tarLang=default=en; _TTSS_IN=hist=WyJpdCIsImVuIiwiemgtSGFucyIsImF1dG8tZGV0ZWN0Il0=; _TTSS_OUT=hist=WyJ6aC1IYW5zIiwiZW4iXQ==; NAP=V=1.9&E=1b6e&C=-Y2I9i3texv3ZfRgDEVBSsUP8nqBTnes0lKDAYxiKNPqbYBFyorYFg&W=1; KievRPSSecAuth=FAB6BBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACFKnxwXhS86XOARQctNLvYGNx4YmA/rcbSqYf9WVE2mSyW6HZ4pWIdKuNwjZQCjBi35K2ztZFJHH4np4U9O3RzuQ9lUDUlB9ryyoQvTSGgmQMwvCtVStW36HD7k701Ka6+EOS6CtEzivAdNCa1EovKtQOiRYfKYqfYcWK1YjOshP3LITZ/oh79rffnVMIMqFgwaaS9rKeuYTL5msn0f7I7fI2BIYj9Qqjzwb8vivNM2iyu4lvSE4kHuAzTGFuf9L6hTzXe4k07/BAOHNSQnkiTkP9gN4vY2istoiiRMPBmRWDYR2qcAig6ob2ROfiyJNe8sfZw5hN1yZhxbDXgTh5+58+PlRZLnWhkI/5MjPY/l843sq5OhdMhyt0AAuUjaZ0V3jztd83BnTIjRrwxEPhYl9uFMEBd8z/YA2+x/+mzPNjkkxBkT/3tgrB+/8HUt3UY0QjmYAWfaHCHo+g/gya198XO4JRyHgBE0uPKiqjBJ8go6W0YHSriMEdMaPl5WtubLT4j7gQFX5qkFoz64+ZgcZwehNvfA5hCa7B/kQdym9SB/c4Ksw6BZBX79AQO6YQndrx8f7ltJlPP/qx2luqigUyHvtkm6haK1IPkXMazC/aNwo65Ah+QHNOkIvCmNx1hOOigrZxGWsLoiR7F/c2RQ6eUmFMAuP9Ss/Rzu+HZGLQJ6UzbtTKQaYufhwGysSJpHhgGfZosdJ+2wrSd48Yo9Xuno+GioSl4tFH821kKRCS4XJxPF7m43hbfazr/0ZExM2sYz1/fSY/nJAA35RuZV8ZSgZa8vZ3NyqHCp7Soslz5PycW4TwLF10HsVe4tn4NhhXINGOWdggnibCj+n5rTD86U/kfpDZFR9MKBdWpDVjjCZLRzEbx815PU8F7jm4SIbY+EGQaMcnWC/5o+MqTthygZyBl/oafXuiSFjC9A9Sw64yZLYWviB3Tp1IzdOQmnVGnmaAD/OZN2jNKaE43wSbbFToE+9EE9h5GlxvCoGxfhOsR8qJI2TqBYhbK75wRR64Y28Ri71pO2sqDEebrbxFnNoAcigErGwk349BZzrLCT90RWWU435SDt91BIMu6Fr/gMuaOlX+iMKIaKvKW37ceyMXAaJ+jPakHMMUWluyVeCmUciUhjdmX/6wH+zT4ClpnvWOqAtoT+DloukqvIgi1LIDmQxPYoNQsOEG2oZnOJHaZ6T5lhncl+H7XluVKL1rxYQNt9jSNoCprru1YcLSHRT1XcUaB5gw+HPR1xK+2Fn4bv9MGGupkw1yAEtS+eRdcdcojWh7x5Z/IDPfd1sMEpg45AXi7cPck8oAf1z2WzZozVdKsE4we8V5+BFVbxhE3FIHnSI+CIlQ3BsM9tEaSw6L+/pHJ285bUjryujoyN0igmh1HbS1rXHg69x3ND7uv5frwFExzcs8jqPh/paypm4i+tsJ9A97IanG/RtEG4UAPiygMMDRGaNhjUY6dTaZx1FpDPA; MicrosoftApplicationsTelemetryDeviceId=e3769721-788a-47ce-b97d-85a38aa72a25; ANIMIA=FRE=1; ZHCHATSTRONGATTRACT=TRUE; _EDGE_S=SID=1D543E422B9062E714EF2C922AF663E4; WLS=C=adf166060227ad09&N=%e6%99%ba%e9%b9%8f; SRCHS=PC=EDGENTP; _SS=SID=1D543E422B9062E714EF2C922AF663E4&PC=EDGENTP&R=200&RB=0&GB=0&RG=200&RP=200; SUID=A; USRLOC=HS=1&ELOC=LAT=31.26334571838379|LON=121.65299224853516|N=%E6%B5%A6%E4%B8%9C%E6%96%B0%E5%8C%BA%EF%BC%8C%E4%B8%8A%E6%B5%B7%E5%B8%82|ELT=2|&CLOC=LAT=31.263345050056106|LON=121.65299119215584|A=733.4464586120832|TS=230310131918|SRC=W; _HPVN=CS=eyJQbiI6eyJDbiI6ODEsIlN0IjoyLCJRcyI6MCwiUHJvZCI6IlAifSwiU2MiOnsiQ24iOjgxLCJTdCI6MCwiUXMiOjAsIlByb2QiOiJIIn0sIlF6Ijp7IkNuIjo4MSwiU3QiOjEsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0wMy0xMFQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6MzYzfQ==; ABDEF=V=13&ABDV=11&MRNB=1678458424009&MRB=0; _U=1uu1mR11LRLMXYLj10dCq1HkMwWzvPgaR_aiAiWmKO1Z5tdTMUH0_XAAct-Il0FpUupXnOXsTlN5dEC0UsCIrGC4zivVIQv1HwIpXVTSvVQ_19v1TsMxlJgqxCobbn55wb513YQ5S60WluR80aK7SkmupTfcUL4qwwM7L9Q_4lHNvnJQcTa69xqKaqVpYglH__ilOx9-h32GlbD1Wmtg8GN4bk2eErt4zU-manUGGGPQ; SNRHOP=I=&TS=; SRCHUSR=DOB=20221125&T=1678462006000&POEX=W; RECSEARCH=SQs=[{"q":"%E7%88%AC%E5%88%B0%E7%9A%84%E7%99%BE%E5%BA%A6%E7%BD%91%E9%A1%B5%E6%98%BE%E7%A4%BA%E7%BD%91%E7%BB%9C%E8%BF%9E%E6%8E%A5%E9%94%99%E8%AF%AF%E6%80%8E%E4%B9%88%E5%8A%9E"%2C"c":1%2C"ad":false}%2C{"q":"ip%E6%9F%A5%E8%AF%A2"%2C"c":1%2C"ad":true}%2C{"q":"%E5%BF%85%E5%BA%94"%2C"c":1%2C"ad":false}%2C{"q":"%E6%9C%AC%E6%9C%BAip"%2C"c":1%2C"ad":false}%2C{"q":"%E7%99%BE%E5%BA%A6%E4%B8%80%E4%B8%8B"%2C"c":1%2C"ad":false}%2C{"q":"chrome"%2C"c":1%2C"ad":false}%2C{"q":"%E4%B8%BA%E4%BB%80%E4%B9%88chrome%E6%89%93%E5%BC%80%E7%BD%91%E9%A1%B5%E4%B8%80%E7%89%87%E7%A9%BA%E7%99%BD"%2C"c":1%2C"ad":true}%2C{"q":"chrome%E6%B5%8F%E8%A7%88%E5%99%A8%E6%80%8E%E4%B9%88%E8%AE%BE%E7%BD%AE%E6%88%90%E7%99%BE%E5%BA%A6"%2C"c":1%2C"ad":false}%2C{"q":"ip"%2C"c":1%2C"ad":false}]; _RwBf=W=1&ilt=472&ihpd=2&ispd=27&rc=200&rb=0&gb=0&rg=200&pc=200&mtu=0&rbb=0&g=0&cid=&clo=0&v=29&l=2023-03-10T08:00:00.0000000Z&lft=2023-02-12T00:00:00.0000000-08:00&aof=0&o=2&p=&c=&t=0&s=0001-01-01T00:00:00.0000000+00:00&ts=2023-03-10T15:26:47.3469851+00:00&rwred=0&wls=&lka=0&lkt=0&TH=; ZHCHATWEAKATTRACT=TRUE; ipv6=hit=1678465609759&t=4; SRCHHPGUSR=SRCHLANG=zh-Hans&PV=15.0.0&BZA=0&BRW=W&BRH=S&CW=1396&CH=252&SCW=1381&SCH=2457&DPR=1.4&UTC=480&DM=0&EXLTT=31&HV=1678462008&WTS=63807454031&PRVCW=1396&PRVCH=720&PR=1.375',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"110.0.1587.63"',
    'sec-ch-ua-full-version-list': '"Chromium";v="110.0.5481.178", "Not A(Brand";v="24.0.0.0", "Microsoft Edge";v="110.0.1587.63"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
}

#  chromed请求头
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Connection': 'keep-alive',
#     'Cookie': 'BIDUPSID=479246B94DF84A7ACB3E4B8C1E917770; PSTM=1678458218; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=479246B94DF84A7AFE684267484C8B37:SL=0:NR=10:FG=1; sug=3; ORIGIN=0; bdime=0; BDUSS=MyNUVWdFliLXd6N0k2MWh3TUJRSjB-RmhpdVA5RC1xZlg4bFNtaGJXeXEwekprSVFBQUFBJCQAAAAAAQAAAAEAAAAAj5QiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKpGC2SqRgtkUX; BDUSS_BFESS=MyNUVWdFliLXd6N0k2MWh3TUJRSjB-RmhpdVA5RC1xZlg4bFNtaGJXeXEwekprSVFBQUFBJCQAAAAAAQAAAAEAAAAAj5QiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKpGC2SqRgtkUX; BAIDUID_BFESS=479246B94DF84A7AFE684267484C8B37:SL=0:NR=10:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=5; BA_HECTOR=al8480a52l2k8gaga101205r1i0mi891m; ZFY=Bal5gsXxsmMIQTS1ZLtGQ2yPTQp:BvgwCspaAfUhPeJ4:C; BD_HOME=1; sugstore=1; H_PS_PSSID=38188_36556_37514_38125_38174_38290_38237_37935_38312_37900_26350_37959_38283_37881; H_PS_645EC=1b40dgGdm5ZMR%2Bpcs6kNGw7y2Ip%2FRLQQIgm4M6K9OPvh9MEI2RUOwCvxH6YX6MGlFgBw; baikeVisitId=0dcf8830-1ca2-4603-ae38-5f5b5abf1e73; BDSVRTM=271; COOKIE_SESSION=0_0_1_1_0_2_1_0_1_1_3_0_0_0_0_0_0_0_1678458219%7C1%230_0_1678461277%7C1%7C1',
#     'Host': 'www.baidu.com',
#     'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'none',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
# }

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器访问服务器
# response = urllib.request.urlopen(request)

proxies = {
    'http': '27.42.168.46:55481'
}
#
# handler   build_opener   open
handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

# 获取响应的信息
content = response.read().decode('utf-8')
print(content)

# 保存
with open('ip1.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
