# -*- coding: utf-8 -*-

from scrapy.selector import Selector
from scrapy.spiders import Spider

from macbook_wait.items import Info


class MacbookWaitSpider(Spider):
    name = "macbook_wait"
    macbookpro15_url = "http://www.apple.com/cn/shop/buy-mac/macbook-pro/15-inch"
    download_delay = 1
    start_urls = [
        macbookpro15_url,
    ]
    post_headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "referer": "https://www.ppdai.com"
    }

    def __init__(self, *args, **kwargs):
        super(MacbookWaitSpider, self).__init__(*args, **kwargs)

    """
    开始获取数据
    """

    def parse(self, response):
        item = Info()
        result = Selector(response)
        # 获取文字提示
        #
        is_text = result.xpath(
            '//*[@id="model-selection"]/div/bundle-selection/div[3]/div[3]/div[2]/div[2]/div/div[@data-render="bundle-selector"]/div[3]/div[1]/div/div[1]/ul/li/text()').extract()
        item['is_text'] = [n.encode('utf-8') for n in is_text]
        submit_button = result.xpath(
            '//*[@id="model-selection"]/div/bundle-selection/div[3]/div[3]/div[2]/div[2]/div/div[@data-render="bundle-selector"]/div[3]/div[1]/div/div[3]/div/span/button//@disabled').extract()
        item['submit_button'] = [n.encode('utf-8') for n in submit_button]
        return item
