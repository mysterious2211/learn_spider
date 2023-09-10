import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['car.autohome.com.cn']
    # 注意如果请求的接口是html结尾的 那么结尾不需要加/
    start_urls = ['https://car.autohome.com.cn/price/brand-15.html']

    def parse(self, response):
        print('++++++++++==============================')

        # 返回的name_list是一个selector对象类型的列表，可以遍历
        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        price_list = response.xpath('//div[@class="main-lever"]//span/span/text()')
        # for name in name_list:
        #     # <Selector xpath='//div[@class="main-title"]/a/text()' data='宝马1系'>
        #     # print(name)
        #     print(name.extract())

        for i in range(len(price_list)):
            name = name_list[i].extract()
            price = price_list[i].extract()
            # print(price)
            # print(price.extract())
            print(name, price)

        # print(name_list)
        # print(price_list)
