import requests
from bs4 import BeautifulSoup


url = 'http://www.kugou.com/yy/rank/home/1-8888.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43',
}

response = requests.get(url=url, headers=headers)

response.encoding = 'utf-8'

content = response.text

soup = BeautifulSoup(content, 'lxml')
# 根据类型选择器获取到排名
ranking_list = soup.select('.pc_temp_num')   # 根据子代选择器获取到歌曲名
sing_list = soup.select('div[class="pc_temp_songlist"] li')

for i in range(len(ranking_list)):
    print(ranking_list[i].get_text().strip(), sing_list[i].attrs.get('title'))

