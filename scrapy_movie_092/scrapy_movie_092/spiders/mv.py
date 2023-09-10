import scrapy

from scrapy_movie_092.items import ScrapyMovie092Item


class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['https://www.dytt8.net/index2.htm']

    def parse(self, response):
        # print('+++++++++++++===============================')
        # 要第一页的名字 和 第二页的图片
        a_list = response.xpath('//div[@class="co_content8"]//td[1]//a[2]')

        for a in a_list:
            # 获取第一页的name 和 要点击的链接
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()

            # 第二页的地址是
            url = 'https://www.dytt8.net' + href
            print(name, url)

            # 对第二页的链接发起访问
            yield scrapy.Request(url=url, callback=self.parse_second,meta={'name':name})

    def parse_second(self, response):
        # 注意：如果拿不到数据的情况下 一定要检查你的xpath语法是否正确

        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        print(src)
        # 接收到请求的那个meta参数的值
        name = response.meta['name']

        movie = ScrapyMovie092Item(src=src,name=name)

        yield movie