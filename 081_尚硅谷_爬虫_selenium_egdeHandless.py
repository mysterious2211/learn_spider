
from selenium import webdriver
from time import sleep
# from selenium.webdriver.edge.options import Options

# edge_options = Options()
EDGE = {
    "browserName": "MicrosoftEdge",
    "version": "92.0.902.55",
    "platform": "WINDOWS",
    "ms:edgeOptions": {
        'extensions': [],
        'args': [
            '--headless',
            '--disable-gpu'
        ]}
}
browser = webdriver.Edge('msedgedriver.exe', capabilities=EDGE)

# 浏览器无可视化界面
url = 'https://www.baidu.com'
browser.get(url)

# 屏幕截图
browser.save_screenshot('baidu.png')

# 获取网页源码
# print(browser.page_source)
sleep(2)
browser.quit()


# 封装的handless
def share_browser():
    # from selenium.webdriver.edge.options import Options

    # edge_options = Options()
    EDGE = {
        "browserName": "MicrosoftEdge",
        "version": "92.0.902.55",
        "platform": "WINDOWS",
        "ms:edgeOptions": {
            'extensions': [],
            'args': [
                '--headless',
                '--disable-gpu'
            ]}
    }
    browser = webdriver.Edge('msedgedriver.exe', capabilities=EDGE)

    # 浏览器无可视化界面
    url = 'https://www.baidu.com'
    browser.get(url)

    # 屏幕截图
    browser.save_screenshot('baidu.png')

    # 获取网页源码
    # print(browser.page_source)
    sleep(2)

    # 返回浏览器对象
    return browser

