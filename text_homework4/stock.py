
import json
import requests
import pymysql


def create_content(page_str):
    url = "http://27.push2.eastmoney.com/api/qt/clist/get?"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43',
    }

    data = {
        'cb': 'jQuery112409836664075157247_1682313762074',
        'pn': page_str,
        'pz': '20',
        'po': '1',
        'np': '1',
        'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
        'fltt': '2',
        'invt': '2',
        'wbp2u': '|0|0|0|web',
        'fid': 'f3',
        'fs': 'm:0 t:6,m:0 t:80,m:1 t:2,m:1 t:23,m:0 t:81 s:2048',
        'fields': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152',
        '_': '1682313762362',

    }
    response = requests.get(url=url, headers=headers, params=data)
    content = response.text
    return content


def insert_into_database(code, name, db, cur):
    try:
        # 插入一条语句
        sql = "INSERT INTO stock value(%s,%s)"
        value = (code, name)
        # 执行sql语句
        cur.execute(sql, value)
        db.commit()
        print('数据插入成功')

    except pymysql.Error as e:
        print("插入失败")
        db.rollback()


if __name__ == '__main__':
    DBHOST = 'localhost'
    DBUSER = 'root'
    DBPASS = '20020824'
    DBNAME = 'spider_data'
    try:
        db = pymysql.connect(host=DBHOST, user=DBUSER, password=DBPASS, db=DBNAME)
        cur = db.cursor()
    except pymysql.Error as e:
        print("连接失败")
    # 获取数据
    for i in range(1, 3):
        page = i
        page_str = str(page)
        print(page_str)
        print(type(page_str))
        content = create_content(page_str)
        # response.encoding = 'utf-8'

        str2 = content.split('(')[1].split(')')[0]
        json_load = json.loads(str2)
        list_data = json_load['data']['diff']
        for x in list_data:
            code = x['f12']
            name = x['f14']
            insert_into_database(code, name, db, cur)
