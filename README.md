# 监控苹果官网2016款macbookpro是否开售。
使用python scrapy进行爬虫。
监控www.apple.com/cn Macbook是否批准通过可以购买。
通过邮件的方式发送通知。
> mail_conf.py
api_user="test_api_user"
api_key="test_api_key"
from_addr="test@mail.com"
to_addr="to_test@mail.com"

> 已成功预订，订单生效~,11月17日到11月24日发货。从2016-11-01 22:30:00官网状态变了就感觉要预售了。改了状态判断之后，30秒一次，上厕所的时候邮件就来了，激动死了，感谢sendcloud。