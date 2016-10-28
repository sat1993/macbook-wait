# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

from datetime import datetime

from scrapy import log

import mail_conf
from macbook_wait.mail.mail import MailSender


class InfoPipeline(object):
    def __init__(self):
        self.file = codecs.open("macbook_wait.json", mode='ab', encoding='utf-8')
        self.result = u'{"is_text":["新款-经批准后发售"],"submit_button":["disabled"]}'
        self.mail_sender = MailSender(mail_conf.api_user, mail_conf.api_key, mail_conf.from_addr, mail_conf.to_addr)

    def process_item(self, item, spider):
        info = dict(item)
        # 需要再研究下python list与str的转码的关系，这里的中文给我弄晕了= =
        jsonstr = json.dumps(info).decode('unicode_escape').replace(" ", "").replace("\n", "")
        log.msg(jsonstr)
        self.file.write(
            "%s,%s,%s\n" % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), jsonstr, str(jsonstr == self.result)))
        if (item['is_text'] == ''):
            return item
        if (jsonstr != self.result):
            self.mail_sender.send_mail(jsonstr)
            self.file.write(
                "sendmail!")
        return item
