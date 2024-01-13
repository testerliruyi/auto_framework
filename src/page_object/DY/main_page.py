import time

from common.selenium.selenium_base import DebugWebdriver, Action, StaleElementReferenceException


class MainPage(DebugWebdriver):

    def click_public_button(self):

        self.wait_for_element_appear(self.get_element('xpath',"//span[@class='semi-button-content']//span[text()='发布作品']"),10)
        self.get_element('xpath',"//span[@class='semi-button-content']//span[text()='发布作品']", Action.CLICK)

    def input_video_path(self, path):
        self.get_element('xpath', "//input[@name='upload-btn']", Action.INPUT, path)

    def input_video_info(self, info: dict):
        # 输入视频标题
        self.get_element('xpath', "//div[@class='container--3NFPK']//input[@type='text']", Action.INPUT, info.get('title'))
        # 输入视频描述
        self.get_element('xpath', '//div[@class="ace-line"]//span/span', Action.INPUT, info.get('desc'))
        # 获取下拉列表第一个元素 并点击
        first_lab = self.get_element('xpath', '//div[@class="mention-suggest-mount-dom"]//div[@class="tag--A0IFC tag-hash--2MMb4" and position()=1]')
        # 重试次数
        attemp_count = 0
        while attemp_count < 3:
            try:
                self.wait_for_element_appear(first_lab)
            # ActionChains(self.driver).move_to_element(first_lab).click(first_lab).perform()
                self.click_element(first_lab)
                break
            except StaleElementReferenceException as E:
                attemp_count += 1

    def public_button_click(self):
        self.wait_for_element_disappear('//div//p[text()="取消上传"]', 100)
        self.get_element('xpath', '//button[text()="发布"]', Action.CLICK)
        time.sleep(1)

    def scan_video_public(self):
        self.get_element('xpath', "//*[text()='内容管理']", Action.CLICK)
        self.wait_for_element_appear(self.get_element('xpath', "//*[text()='作品管理']"))
        self.get_element('xpath', "//*[text()='作品管理']", Action.CLICK)
        time.sleep(5)

    def switch_other_account(self):
        self.get_element("xpath", "//div[@id='header-avatar']/div", Action.CLICK)
        switch_account_ele = self.get_element('xpath',"//*[text()='账号切换']")
        self.wait_for_element_appear(switch_account_ele)
        self.click_element(switch_account_ele)


