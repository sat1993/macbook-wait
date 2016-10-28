# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from macbook_wait.spiders.macbook_wait_spider import MacbookWaitSpider
from time import sleep

while (True):
    process = CrawlerProcess(get_project_settings())
    process.crawl(MacbookWaitSpider)
    process.start()
    sleep(300)
