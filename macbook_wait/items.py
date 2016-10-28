# -*- coding: utf-8 -*-
"""
获取借出列表信息。
待收款、收款中、已还清信息
"""
from scrapy.item import Item, Field


class Info(Item):
    submit_button = Field()
    is_text = Field()
