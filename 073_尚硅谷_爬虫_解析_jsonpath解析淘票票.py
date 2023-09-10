

import urllib.request

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1678702638170_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=tru'

headers = {
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?activityId&_ksTS=1678702638170_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'bx-v': '2.2.3',
    'cookie': 'cna=FuYxGtzzg2QCAbSgafXXyCQ5; _samesite_flag_=true; cookie2=1f4a38cbd1a8137e8b9c42cf3e2ed085; t=68a300120f3ad5735aa63c3380fafd38; _tb_token_=57691d1189e38; v=0; xlly_s=1; tfstk=cnpcBDTCCI5fFLH9PE6jKSExCoGRZiGVldJyU0w6Zw-N21vPi8VzTr7EqZ3Iu51..; l=fBaxiLXHgG71xbTMBO5Blurza77t2Qdb8PVzaNbMiIEGa6sRtF_8SNCsTUSDSdtjgT50ietPDzebmdn275z38PsWHpfuKtyuJQJH8eM3N7AN.; isg=BNjYdGWNCLW2OyGM_1_gEB-MqQZqwTxLQ_EunxLKmZPGrXmXutLR2sJD5eWduPQj',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
    'x-requested-with': 'XMLHttpRequest',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

content = content.split('(')[1].split(')')[0]

with open('073_尚硅谷_爬虫_解析_jsonpath解析淘票票.json', 'w', encoding='utf-8') as fp:
    fp.write(content)

import json
import jsonpath

obj = json.load(open('073_尚硅谷_爬虫_解析_jsonpath解析淘票票.json', 'r', encoding='utf-8'))

city_list = jsonpath.jsonpath(obj, '$..regionName')

print(city_list)