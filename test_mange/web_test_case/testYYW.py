import time
from common.selenium import DebugWebdriver
# 导入键盘操作关键字
from selenium.webdriver.common.keys import Keys


class TestWeb(DebugWebdriver):
    def __init__(self):
        super().__init__()
        self.url = 'https://www.yyw.com/'
        # self.driver.implicitly_wait(15)

    def runtest(self) -> None:
        self.driver.get(self.url)
        self.locate_element('xpath', '//*[@id="Login_S"]/li[1]/a/span[1]').click()
        self.locate_element('xpath', "//input[@id='txtUserName']").send_keys(Keys.CLEAR)
        self.locate_element('xpath', "//input[@id='txtUserName']").send_keys('18588512607@163.com')
        self.locate_element('xpath', "//*[@id='form1']/input[@type='password']").send_keys('111111')
        self.locate_element('xpath', "//button[@id='Login']").click()

if __name__ == '__main__':
    cls = TestWeb()
    cls.runtest()
