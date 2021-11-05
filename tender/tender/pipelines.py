# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os


import pymongo

from tender.common.consts import const
from tender.utils import date


class TenderPipeline:
    def process_item(self, item):
        return item


class MongoPipeline:
    def __init__(self, mongo_uri, mongo_db, mongo_port):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_port = mongo_port
        self.client = None
        self.db = None
        # 从配置文件keyword.conf获取关键字字典值
        self.keywordsDict = dict()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=const.MONGO_URI,
            mongo_db=const.MONGO_DATABASE,
            mongo_port=const.MONGODB_PORT
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        pubtime = item['pubtime']
        title = item['title']
        self.getKeywords()
        keywordStr = self.keywordsDict.get(spider.name)
        if self.checkTitle(title, keywordStr) and date.get_curdate() == pubtime:
            self.db[spider.name].insert(dict(item))
        return item

    def checkTitle(self, title, keywordStr):
        title = str(title)
        keywords = keywordStr.split(",")
        t = []
        for k in keywords:
            if k in title:
                t.append(True)
        if len(t) > 0:
            return True
        else:
            return False

    def close_spider(self, spider):
        self.client.close()

    def getKeywords(self):
        # 从配置文件中读取关键字
        curpath = os.getcwd()
        fk = open(curpath + '\\' + const.KEYWORD_CONF, 'r', encoding='utf-8')
        while True:
            line = fk.readline()

            if line:
                config = line.split('===')
                self.keywordsDict[config[0]] = config[1]
            else:
                break
        fk.close()



