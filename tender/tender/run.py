from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from tender.common.consts import const
from tender.my_email import Handle_Send_Email
from tender.utils import date

settings = get_project_settings()
configure_logging(settings)
runner = CrawlerRunner(settings)
file_list = []
# 运行所有的spider
for spider_name in runner.spider_loader.list():
    file_list.append('excel\\tender-{}-{}.xlsx'.format(date.get_curdate(), spider_name))
    runner.crawl(spider_name)

d = runner.join()
d.addBoth(lambda _: reactor.stop())

reactor.run()


client = Handle_Send_Email()
client.send_email(const.EMAIL_CONF, file_list)
