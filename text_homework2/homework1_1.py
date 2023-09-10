import requests
from lxml import etree
# 第一页
url = 'https://www.shanghairanking.cn/rankings/bcur/2020'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43',
}
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
content = response.text
tree = etree.HTML(content)
ranking_list = tree.xpath('//table[@class="rk-table"]//tr/td[1]/div/text()')
name_list = tree.xpath('//table[@class="rk-table"]//tr//td//a[@class="name-cn"]/text()')
province_list = tree.xpath('//table[@class="rk-table"]//tr//td[3]/text()')
score_list = tree.xpath('//table[@class="rk-table"]//tr//td[5]/text()')


for i in range(len(ranking_list)):
    print(ranking_list[i].strip(), name_list[i].strip(), province_list[i].strip(), score_list[i].strip())
