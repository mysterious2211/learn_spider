import requests
from bs4 import BeautifulSoup

url = "http://www.kulemi.com/zt/127/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43',
}

response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
content = response.text
# print(content)
soup = BeautifulSoup(content, 'lxml')

catalog_list = soup.select('body > div.container > div.left > div:nth-child(2) > div.c > ul > li')

with open('D:\\sanguo.txt', 'a', encoding='utf-8') as fp:
    for catalog in catalog_list:
        fp.write(catalog.get_text().strip())
        fp.write('\n')
