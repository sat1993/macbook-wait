# -*- coding: utf-8 -*-
import time
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from scrapy.utils.project import get_project_settings
from macbook_wait.spiders.macbook_wait_spider import MacbookWaitSpider
configure_logging()
runner = CrawlerRunner(settings=get_project_settings())

@defer.inlineCallbacks
def crawl():
    while True:
        yield runner.crawl(MacbookWaitSpider)
        time.sleep(30)
    reactor.stop()

crawl()
reactor.run() # the script will block here until the last crawl call is finished
