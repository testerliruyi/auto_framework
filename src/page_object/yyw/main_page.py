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

    def search_input(self):
        self.input_text('//input[@name="keywords"]', 'beads')

    def click_button(self):
        self.click_element('//input[@type="submit"]')




