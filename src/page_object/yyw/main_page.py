"""
author：li ru yi
desc: yyw.com main page
"""

from common.playwright.sync_playwright_base import SyncPlayWrightWrapper


class main_page_element(SyncPlayWrightWrapper):
    # 根据需要指定浏览器启动模式和使用那种类型浏览器
    def __init__(self):
        super().__init__('design')

    def go_url(self):
        self.goto_url("https://www.yyw.com")

    def login(self):
        self.page.wait_for_selector("css=span.color:nth-last-child(2)", state="visible", timeout=60000)
        login_info = self.query_element("css=span.color:nth-last-child(2)")
        if login_info:
            login_info.click()
            self.get_locator("#txtUserName").fill("liruyi0229@outlook.com")
            self.get_locator("//input[@id='txtPassword']").type('111111')
            self.get_locator("//button[@id='Login']").click()
            try:
                self.expect(self.get_locator("css=span.red")).to_be_visible()
                assert True
            except TimeoutError as e:
                assert False
        else:
            print("页面元素定位失败")
            assert False

    def search(self):
        self.input_text('//input[@name="keywords"]', 'beads')
        self.click_element('//input[@type="submit"]')
        resource = self.page.content()
        print(resource)




