import scrapy
from myspider.items import MyspiderItem

class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = ["https://www.itcast.cn/channel/teacher.shtml#ajavaee"]

    def parse(self, response):
        teacher_list = response.xpath('//div[@class="li_txt"]')
        # print(len(teacher_list))
        for teacher in teacher_list:
             # temp = {}
             item = MyspiderItem()
             item['name'] = teacher.xpath('./h3/text()').extract()
             item['title'] = teacher.xpath('./h4/text()').extract()
             item['detail'] = teacher.xpath('./p/text()').extract()
             yield item
