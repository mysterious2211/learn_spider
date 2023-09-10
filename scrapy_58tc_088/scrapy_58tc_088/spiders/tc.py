import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['sh.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_C%2Cxiaoqu_word%2Chit_composition%2Cuuid_29d6ae40bddd4041b6d5e39520313686&search_uuid=29d6ae40bddd4041b6d5e39520313686']
    start_urls = ['http://sh.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_C%2Cxiaoqu_word%2Chit_composition%2Cuuid_29d6ae40bddd4041b6d5e39520313686&search_uuid=29d6ae40bddd4041b6d5e39520313686']

    def parse(self, response):
        print('++++++++++++++=======================================')
        # 字符串
        # content = response.text
        # 二进制数据
        # content = response.body
        # print(content)
        # print("别人我不知道，但是你……")

        span = response.xpath('//div[@class="tabs"]/a/span')[0]
        print(span)
        print(span.extract())