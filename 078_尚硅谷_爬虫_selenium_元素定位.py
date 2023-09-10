

from selenium import webdriver

path = 'msedgedriver.exe'
browser = webdriver.Edge(path)

url = 'https://www.baidu.com'
browser.get(url)

# 元素定位

# 根据id来找到元素
# button = browser.find_element_by_id('su')
# button = browser.find_element('id','su')
# print(button)


# 根据标签属性的属性值获取对象
# button = browser.find_element_by_name('wd')
# print(button)

# 根据xpath语句来获取对象
# button = browser.find_element_by_xpath('//imput[@id="su"]')
# print(button)

# 根据标签的名字来获取对象
# button = browser.find_elements_by_tag_name('input')
# print(button)

# 使用bs4的语法来获取对象
# button = browser.find_elements_by_css_selector('#su')
# print(button)

button = browser.find_element_by_link_text('贴吧')
print(button)


