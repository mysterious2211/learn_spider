import pymysql

DBHOST = 'localhost'
DBUSER = 'root'
DBPASS = '20020824'
DBNAME = 'spider_data'

try:
    db = pymysql.connect(host=DBHOST, user=DBUSER, password=DBPASS, db=DBNAME)
    print("连接成功")
    cur = db.cursor()

    # # 插入一条语句
    # sql = "INSERT INTO stock value(%s,%s)"
    # value = ('45614', '中国邮政')
    # # 执行sql语句
    # cur.execute(sql,value)
    # db.commit()
    # print('数据插入成功')

    # 查询数据
    # fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    # fetchall(): 接收全部的返回结果行.返回的是一个元组
    # rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数
    # sql1 = "select *  from stock"
    # cur.execute(sql1)
    # result = cur.fetchall()
    # # 循环打印
    # for row in result:
    #     code = row[0]
    #     name = row[1]
    #     print(f'股票代码为：{code},名字为:{name}')

    # 更新表中的数据
    # sql2 = "update stock set name = %s where code = %s"
    # value2 = ("中国银行",'45614')
    # cur.execute(sql2,value2)
    # db.commit()
    # print("更新成功")

    # 删除表中的数据
    sql3 = "delete from stock where code = %s"
    value3 = ('中国邮政')
    cur.execute(sql3, value3)
    db.commit()
    print("删除成功")

except pymysql.Error as e:
    print("连接失败")
    db.rollback()
