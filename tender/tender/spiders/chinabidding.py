import scrapy

from tender.items import SiteItem
from tender.utils import date


# 中国采购与招标网招标爬虫

class ChinabiddingSpider(scrapy.Spider):
    name = 'chinabidding'
    allowed_domains = ['chinabidding.cn']
    start_urls = [
        "https://www.chinabidding.cn/zbxx/zbgg/",]

    def parse(self, response):
        pubtime = ""
        nextPagehref = None
        detail = response.xpath('//table[@id="list"]/tbody/tr[@class="yj_nei"]')
        for temp in detail:
            item = SiteItem()
            item['title'] = temp.xpath('td[@class="td_1"]/a/text()').extract_first().strip()
            item['link'] = "https://www.chinabidding.cn" + temp.xpath(
                'td[@class="td_1"]/a/@href').extract_first().strip()
            item['pubtime'] = temp.xpath('td[@class="td_2"]/text()').extract()[1].strip()

            pubtime = item['pubtime']
            yield item
        if response.xpath(u'//span[@class="Disabled"]/a[text()="下一页>>"]/@href').extract_first():
            nextPagehref = "https://www.chinabidding.cn/zbxx/zbgg/{}.html".format(
                response.xpath(
                    u'//span[@class="Disabled"]/a[text()="下一页>>"]/@href').extract_first().split("(")[1].split(")")[0])

        if pubtime == date.get_curdate():
            if nextPagehref:
                yield scrapy.Request(nextPagehref, callback=self.parse)
