

import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'


# headers中的参数中，cookie起到决定性作用
headers = {
'Accept': '*/*',
# 'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language':' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Acs-Token': '1678286074893_1678286146135_lzGioHa6uy3xRYeUgSF9qZzGFMX9JVlkOZzgG2CXqzqZrXMRebHAYLrJ1xAsDOY29fLt+fBn+pbrodN6dIaBlORu1T9q9kZefMs/bE74/ez9bEnyuGm0TwbxtmRAJFBXRG81RAnD1Sw9ilZqudzlHEL+w0bAjx+kxFpF3+So+QAOA21coi0Ss2v6ZuqW07UT3Ylo42/DTxKV88tKQC2bTTrxhuaLTdNPMc3VRVheLgRSkBTxgWZWrAGe/KdWWPl+ITUvU1dXuwWggGoj05UIqWyUiunzFgfKbRbjlZO/9B0J3f6dtu+fAUCBAiBPm+nMEK8YbWI9ZWhZD+rLePAyIlMfSsQWJfFCMD3ucKq2OfYTRL0XJddE9zgdLSSjo0go',
'Connection': 'keep-alive',
'Content-Length': '133',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'BIDUPSID=7B2D91344BF8E1CAFCD457ECBAE72FA3; PSTM=1638507561; __yjs_duid=1_d2802d5a64fc3b95e978a26a2193a1231638796369978; SOUND_SPD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=C616C53F8E56C78BEDD58FDDDFE0C0C2:FG=1; BDUSS=WhXeG9sdTZzdE1RRXIzN1N5V1c5bmZ4dDNSLUJIM3dlWjhPY2RRdFB3Y2RFTVZpRVFBQUFBJCQAAAAAAQAAAAEAAAAAj5QiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB2DnWIdg51iT; BDUSS_BFESS=WhXeG9sdTZzdE1RRXIzN1N5V1c5bmZ4dDNSLUJIM3dlWjhPY2RRdFB3Y2RFTVZpRVFBQUFBJCQAAAAAAQAAAAEAAAAAj5QiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB2DnWIdg51iT; newlogin=1; BAIDUID_BFESS=C616C53F8E56C78BEDD58FDDDFE0C0C2:FG=1; BA_HECTOR=84a100a1ag810525042k2k581i0gf531m; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZFY=Ps3IovrWju:A7ITBBiGxqLEA85NiV8kwnXnBho1FIAhc:C; delPer=0; PSINO=5; H_PS_PSSID=38185_36548_38270_37911_37862_38172_38290_36803_38035_37927_38315_38322_38040_26350_38281_37881; APPGUIDE_10_0_2=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1678264687; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1678264687',
'Host': 'fanyi.baidu.com',
'Origin': 'https://fanyi.baidu.com',
'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': 'Windows',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'lo',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '646722.867699',
    'token': 'f44ca90b8c2235cfb5e6d6287083d3d2',
    'domain': 'common'
}

# post请求的参数 必须进行编码 并且要调用encode方法
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象的定制
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')

obj = json.loads(content)

print(obj)

