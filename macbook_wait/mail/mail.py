import requests


class MailSender():
    def __init__(self, api_user, api_key, from_addr, to_addr):
        self.param={
            "api_user":api_user,
            "api_key":api_key,
            "from":from_addr,
            "to": to_addr,
            "fromname":"hello",
            "subject":"hello macbook pro",
        }
        self.url="https://sendcloud.sohu.com/webapi/mail.send.xml"

    def send_mail(self,msg):
        self.param.update({"html":msg})
        print requests.post(self.url,self.param).text
