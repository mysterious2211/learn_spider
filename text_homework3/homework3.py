import requests
from lxml import etree

url = "http://search.dangdang.com/?"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43',
}

data = {
    'key': 'java',
    'page_index': 3
}

response = requests.get(url=url, headers=headers, params=data)
# response.encoding = 'utf-8'
content = response.text
tree = etree.HTML(content)

name_list = tree.xpath('//div[@id="search_nature_rg"]//ul//li/a/@title')
price_list = tree.xpath('//div[@id="search_nature_rg"]//ul//li//p[@class="price"]/span[1]/text()')

for i in range(len(name_list)):
    print(name_list[i].strip() + '  ' + price_list[i].strip())
