import scrapy
from scrapy import Spider, cmdline
from tender.items import SiteItem
from tender.utils import date


# 招标网

class ZbzhaobiaoSpider(scrapy.Spider):
    name = 'zbzhaobiao'
    allowed_domains = ['zb.zhaobiao.cn']
    start_urls = [
        "https://zb.zhaobiao.cn/bidding_p_1.html",
    ]

    def parse(self, response):
        pubtime = ""
        nextPagehref = None
        detail = response.xpath('//*[@id="datatbody"]/tr')
        for temp in detail:
            item = SiteItem()
            item['title'] = temp.xpath('td/a/text()').extract_first().strip()
            item['link'] = temp.xpath('td/a/@href').extract_first().strip()
            item['pubtime'] = temp.xpath('td[3]/text()').extract()[0]
            pubtime = item['pubtime']
            yield item
        if response.xpath('//div/a[text()="下一页 >"]/@href'):
            nextPagehref = response.xpath('//div/a[text()="下一页 >"]/@href').extract_first().strip()
        if pubtime == date.get_curdate():
            if nextPagehref:
                yield scrapy.Request(nextPagehref, callback=self.parse)
