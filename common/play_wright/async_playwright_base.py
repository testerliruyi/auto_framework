from playwright.async_api import async_playwright
from typing import Union
import asyncio


class AsyncPlayWrightWrapper:
    """
    异步用法
    """

    def __init__(self, browser_type="chromium"):
        self.playWright = None
        self.browser_type = browser_type
        self.browser = None

        # # 指定启动浏览器方式
        # if not param:
        #     print("current mode is: default")
        #     self.page = self.lunch_default_browser()
        # elif param.lower() == "design":
        #     print("current mode is: design")
        #     self.page = self.lunch_design_browser()
        # elif param.lower() == "local":
        #     print("current mode is: local")
        #     self.page = self.lunch_local_browser()
        # else:
        #     self.page = self.lunch_default_browser()

    async def lunch_default_browser(self):
        self.playWright = await async_playwright().start()
        if self.browser_type == "chromium":
            self.browser = await self.playWright.chromium.launch(headless=False, timeout=100000, args=['--start-maximized'])


    # 默认方法启动浏览器
    # def lunch_default_browser(self):
    #     self.browser = self.playWright.chromium.launch(headless=False, timeout=100000, args=['--start-maximized'])
    #     context = self.browser.new_context(no_viewport=True)
    #     page = context.new_page()
    #     return page

    # 指定端口页面启动浏览器
    def lunch_design_browser(self):
        self.browser = self.playWright.chromium.connect_over_cdp("http://localhost:9222")
        context = self.browser.contexts[0]
        page = context.pages[0]
        return page

    # 指定本机已安装浏览器
    def lunch_local_browser(self):
        self.browser = self.playWright.chromium.launch_persistent_context(
            # 指定本地缓存
            user_data_dir="D:\selenium\chrome_temp",
            # 指定本机chrome地址
            executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe",
            accept_downloads=True,
            headless=False,
            bypass_csp=True,
            slow_mo=10,
            args=['--disable-blink-features=AutomationControlled', '--remote-debugging-port=9222', '--start-maximized']

        )
        page = self.browser.new_page()
        return page

    # 关闭浏览器
    def close_browser(self):
        if self.browser:
            self.browser.close()

    def goto_url(self, url, time=60000):
        # 设置加载超时时间为60
        self.page.goto(url, timeout=time)

    def click_element(self, selector):
        self.page.click(selector)

    def input_text(self, selector, text: str):
        self.page.fill(selector, text)

    def get_text_content(self, selector):
        element = self.page.query_selector(selector)
        return element.inner_text()
