import requests
import time
class ScanCode():
    def __init__(self,url):
        self.url=url
        self.session=requests.session()
    def get_token(self):
        data={"timestamp": ''.join(str(time.time()).split('.')), "_log_finder_uin": "", "_log_finder_id":"", "rawKeyBuff":""}
        url_data=self.session.post(url=self.url,data=data).json()
        return url_data







if __name__=="__main__":
    cls=ScanCode("https://channels.weixin.qq.com/cgi-bin/mmfinderassistant-bin/auth/auth_login_code")
    print(cls.get_token())