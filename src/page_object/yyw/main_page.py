"""
author：li ru yi
desc: yyw.com main page
"""
import time

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
            self.page.wait_for_selector("#txtUserName", state="visible", timeout=60000)
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

    def enter_goodsinfo_and_add_cart(self):
        self.expect(self.get_locator("css=div.resultpro"))
        self.get_locator("css=div.resultpro img").nth(1).click()
        time.sleep(1)
        # 切换到最新页面
        page = self.get_all_pages()[-1]
        print("current page is:",page)
        # print(self.get_all_pages()[-1].content())
        self.expect(page.locator("xpath=//a[text()='Add to Cart']"))
        page.locator("xpath=//a[text()='Add to Cart']").click()
        page.locator("xpath=//span[contains(text(), 'Cart')]").click()
        self.query_element("img[alt = 'Check Out']")
        page.locator("img[alt = 'Check Out']").click()


        # self.get_locator("xpath=//a[text()='Add to Cart']").click()







