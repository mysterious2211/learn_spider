import requests
from bs4 import BeautifulSoup
from lxml import etree
import pymysql
from last_homework.poem import Book


def get_content():
    """
    获取网页源码
    :return:
    """
    url = "https://so.gushiwen.cn/guwen/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43',
    }

    response = requests.get(url=url, headers=headers)
    # response.encoding = 'utf-8'
    content = response.text
    return content


def get_data(content, db, cur):
    """
    获取要爬取的数据
    :param content:
    :return:
    """
    soup = BeautifulSoup(content, 'lxml')
    name_list = soup.select('.typecont > span')
    url_list = soup.select('.typecont > span > a')
    count = 0
    for i in range(len(name_list)):
        name = name_list[i].get_text().strip().split('(')[0]
        dynasty = name_list[i].get_text().strip().split('(')[1].replace(')', '')
        # 获得超链接的href属性，和https拼接成url
        url = 'https://so.gushiwen.cn/' + url_list[i].attrs.get('href')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43',
        }
        # 访问a表示超链接对应的网页，获取诗人简介
        content_two = requests.get(url=url, headers=headers).text
        # 返回简介
        synopsis = get_content_two_data(content_two)
        print(name, dynasty, synopsis)
        count += 1
        # 将爬取到的目标数据封装成封装类进行传递
        book_obj = Book(name, dynasty, synopsis)
        put_data_into_database(book_obj, db, cur)


def get_content_two_data(content_two):
    """
    根据传递过来的网页源码，获取到想要的数据
    :param content_two:
    :return: 书籍的简介
    """
    soup = BeautifulSoup(content_two, 'lxml')

    synopsis = soup.select('.cont > p')[0].get_text().strip().split('►')[0]
    return synopsis


def put_data_into_database(book_obj, db, cur):
    """
     将数据插入到数据库中
    :param name:
    :param author:
    :param poem:
    :return:
    """
    try:
        # 插入一条语句
        sql = "INSERT INTO book value(null,%s,%s,%s)"
        value = (book_obj.name, book_obj.dynasty, book_obj.synopsis)
        # 执行sql语句
        # cur.execute(sql, value)
        db.commit()
        print('数据插入成功')

    except pymysql.Error as e:
        print("插入失败")
        db.rollback()


def main():
    """
    主函数，确定要爬取的页数
    :return:
    """

    DBHOST = 'localhost'
    DBUSER = 'root'
    DBPASS = '20020824'
    DBNAME = 'spider_poem'
    try:
        db = pymysql.connect(host=DBHOST, user=DBUSER, password=DBPASS, db=DBNAME)
        cur = db.cursor()
    except pymysql.Error as e:
        print("连接失败")

    # 得到第一页的网页源码
    content = get_content()
    get_data(content, db, cur)


if __name__ == '__main__':
    main()
