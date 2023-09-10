

from selenium import webdriver

path = 'msedgedriver.exe'
browser = webdriver.Edge(path)

url = 'https://www.baidu.com'
browser.get(url)

input = browser.find_element_by_id('su')

# 获取标签的属性
print(input.get_attribute('class'))
# 获取标签的名字
print(input.tag_name)
# 获取元素文本
a = browser.find_element_by_link_text('贴吧')
print(a.text)

