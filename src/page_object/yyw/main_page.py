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
            self.locator("#txtUserName").fill("liruyi0229@outlook.com")
            self.locator("//input[@id='txtPassword']").type('111111')
            self.locator("//button[@id='Login']").click()
            try:
                self.expect(self.locator("css=span.red")).to_be_visible()
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

     # 进入商品详情并添加购物车
    def add_cart(self):
        self.expect(self.get_locator("css=div.resultpro"))
        self.locator("css=div.resultpro img").nth(2).click()
        # 切换到最新页面
        self.page = self.get_all_pages()[-1]
        print("current page is:", self.page)
        # print(self.get_all_pages()[-1].content())
        self.expect(self.page.locator("xpath=//a[text()='Add to Cart']")).to_be_visible()
        if self.query_element("xpath=//a[text()='Add to Cart']"):
            print("定位添加购物车按钮成功")
            self.page.locator("xpath=//a[text()='Add to Cart']").is_enabled(timeout=10000)
            self.page.locator("xpath=//a[text()='Add to Cart']").click()
            self.page.locator("xpath=//span[contains(text(), 'Cart')]").click()

    def check_out(self):
        self.page.query_selector("css=img[alt = 'Check Out']")
        self.page.locator("img[alt = 'Check Out']").click()
        # 待结算页面元素出现后进行截图
        self.expect(self.page.locator("css=.c0f6:nth-child(1)").first).to_be_visible()
        # 等待页面加载完成后 进行截图
        self.page.wait_for_load_state("load")
        self.save_screenshot("check_out.png")

    def submit_order(self):
        print("current page : ", self.page.frames)
        for i in self.page.frames:
            # iframe = self.page.frame_locator("iframe[name=\"\"]")
            try:
                i.get_by_role("link", name="PayPal").click()
                print("定位成功,", i)
            except Exception as e:
                print("定位失败")
                continue
        # iframe.get_by_role("link", name="PayPal").click()
        # self.page = self.get_all_pages()[-1]

        # key_words = "PayPal"
        # if key_words in self.page.title():
        #     self.save_screenshot("paypal_window")
        #     assert True








