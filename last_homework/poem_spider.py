import requests
from bs4 import BeautifulSoup
from lxml import etree
import pymysql

from last_homework.poem import Poem


def get_content(page, form):
    """
    获取网页源码
    :param page: 页数
    :param form: 古诗的类型
    :return: 返回网页源码
    """
    url = "https://so.gushiwen.cn/shiwens/default.aspx?"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43',
    }

    data = {
        'page': page,
        'xstr': form
    }
    response = requests.get(url=url, headers=headers, params=data)
    # response.encoding = 'utf-8'
    content = response.text
    return content


def get_data(content, form1, db, cur):
    """
    获取要爬取的数据
    :param content: 网页源码
    :param form1: 古诗类型
    :return: 无返回值
    """
    soup = BeautifulSoup(content, 'lxml')
    name_list = soup.select('#leftZhankai div[class="sons"] div[class="cont"] > div > p:nth-child(1)')
    author_list = soup.select('.source')
    poem_list = soup.select('.contson')
    for i in range(len(poem_list)):
        name = name_list[i].get_text().strip()
        author = author_list[i].get_text().strip().split('〔')[0]
        dynasty = author_list[i].get_text().strip().split('〔')[1].split('〕')[0]
        form = form1
        poem = poem_list[i].get_text().strip().replace('\n', '').replace(' ', '')
        print(name, author, dynasty, form, poem)
        # 将要用到的参数封装到Poem类中，传递给函数
        poem_obj = Poem(name, author, dynasty, form, poem)
        put_data_into_database(poem_obj, db, cur)


def put_data_into_database(poem_obj, db, cur):
    """
    将数据插入到数据库中
    :param poem_obj: 封装的数据
    :param db: 数据库连接
    :param cur: 数据连接
    :return: 无返回值
    """
    try:
        # 插入一条语句
        sql = "INSERT INTO poem value(null,%s,%s,%s,%s,%s)"
        value = (poem_obj.name, poem_obj.author, poem_obj.dynasty, poem_obj.form, poem_obj.poem)
        # 执行sql语句
        # cur.execute(sql, value)
        # db.commit()
        print('数据插入成功')

    except pymysql.Error as e:
        print("插入失败")
        db.rollback()


def main():
    """
    主函数，确定要爬取的页数
    :return:
    """
    # 最多只有8页
    start_page = int(input('请输入起始的页码：'))
    end_page = int(input('请输入结束的页码：'))

    # 数据库的账号密码和数据库名称
    DBHOST = 'localhost'
    DBUSER = 'root'
    DBPASS = '20020824'
    DBNAME = 'spider_poem'
    try:
        db = pymysql.connect(host=DBHOST, user=DBUSER, password=DBPASS, db=DBNAME)
        cur = db.cursor()
    except pymysql.Error as e:
        print("连接失败")

    # 要爬取的古诗类型
    form_list = ['诗', '词', '曲']
    for i in range(3):
        for page in range(start_page, end_page + 1):
            content = get_content(page, form_list[i])
            get_data(content, form_list[i], db, cur)


if __name__ == '__main__':
    main()
