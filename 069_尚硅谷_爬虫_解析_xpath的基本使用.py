
from lxml import etree

# xpath解析
# （1）本地文件  etree.parse
# （2）服务器响应的数据 response.read().decode('utf-8')   etree.HTML()


tree = etree.parse('069_尚硅谷_爬虫_解析_xpath的基本使用.html')

# tree.xpath('xpath路径')

# 查找ul下面的li
# li_list = tree.xpath('//body//ul/li')

# 查找所有有id的属性的li标签
# text()：获取标签中的内容
# li_list = tree.xpath('//ul/li[@id]/text()')

# 找到id为l1的里标签   注意引号问题
# li_list = tree.xpath('//ul/li[@id="l1"]/text()')


# 查找到id为l1的标签的class的属性值
# li_list = tree.xpath('//ul/li[@id="l1"]/@class')

# 查找id中包含l的li标签
# li_list = tree.xpath('//ul/li[contains(@id,"l")]/text()')


# 查询id的值以l开头的li标签
# li_list = tree.xpath('//ul/li[starts-with(@id,"c")]/text()')

# 查询id为l1和class 为c1的标签
# li_list = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')

li_list = tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l2"]/text()')




# 判断列表的长度
print(li_list)
print(len(li_list))


