"""
author: LiRuYi
desc： playwright 异步用法
"""
import asyncio
from typing import Optional, Literal, Union
from playwright.async_api import async_playwright, expect


class AsyncPlayWrightWrapper:

    def __init__(self, browser_type="chromium"):
        self.playwright = None
        self.browser_type = browser_type
        self.browser = None
        self.page = None
        self.expect = expect

    # 初始化浏览器
    async def initialize(self, param: Union[None, str] = None):
        # 指定启动浏览器方式
        if not param:
            print("current mode is: default")
            self.page = await self.__lunch_default_browser()

        elif param.lower() == "local":
            print("current mode is: local")
            self.page = await self.__lunch_local_browser()
        else:
            self.page = await self.__lunch_default_browser()

    # 默认方法启动浏览器
    async def __lunch_default_browser(self):
        self.playwright = await async_playwright().start()
        if self.browser_type == "chromium":
            self.browser = await self.playwright.chromium.launch(headless=False, timeout=100000,
                                                                 args=['--start-maximized'])
        elif self.browser_type == "firefox":
            self.browser = await self.playwright.firefox.launch(headless=False, timeout=100000,
                                                                args=['--start-maximized'])
        elif self.browser_type == "webkit":
            self.browser = await self.playwright.webkit.launch(headless=False, timeout=100000,
                                                               args=['--start-maximized'])
        context = await self.browser.new_context(no_viewport=True)
        self.page = await context.new_page()
        # return self.page

    # 指定本机已安装浏览器
    async def __lunch_local_browser(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch_persistent_context(
            # 指定本地缓存
            user_data_dir="D:\\selenium\\chrome_temp",
            # 指定本机chrome地址
            executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            accept_downloads=True,
            headless=False,
            bypass_csp=True,
            slow_mo=10,
            args=['--disable-blink-features=AutomationControlled', '--remote-debugging-port=9222', '--start-maximized']
        )
        self.page = await self.browser.new_page()
        # return self.page

    # 关闭浏览器
    async def close_browser(self):
        if self.browser:
            await self.browser.close()
            await self.playwright.stop()

    # 跳转页面
    async def goto_url(self, url, time=60000):
        # 设置加载超时时间为60
        await self.page.goto(url, timeout=time, wait_until="commit")

    # 使用locator方式定位元素
    async def get_locator(self, selector):
        locator = await self.page.locator(selector)
        return locator

    # 使用get_by方式定位元素
    async def get_by(self,
                     action: Optional[Literal["role", "text", "label", "placeholder", "alt_text", "title", "test_id"]],
                     content: Union[str, Literal[
                         "alert", "alertdialog", "application", "article", "banner", "blockquote", "button", "caption", "cell", "checkbox", "code", "columnheader", "combobox", "complementary", "contentinfo", "definition", "deletion", "dialog", "directory", "document", "emphasis", "feed", "figure", "form", "generic", "grid", "gridcell", "group", "heading", "img", "insertion", "link", "list", "listbox", "listitem", "log", "main", "marquee", "math", "menu", "menubar", "menuitem", "menuitemcheckbox", "menuitemradio", "meter", "navigation", "none", "note", "option", "paragraph", "presentation", "progressbar", "radio", "radiogroup", "region", "row", "rowgroup", "rowheader", "scrollbar", "search", "searchbox", "separator", "slider", "spinbutton", "status", "strong", "subscript", "superscript", "switch", "tab", "table", "tablist", "tabpanel", "term", "textbox", "time", "timer", "toolbar", "tooltip", "tree", "treegrid", "treeitem"]],
                     name=None,
                     exact=True):
        match action.lower():
            case "role":
                locator = await self.page.get_by_role(content, name=name, exact=exact)
                return locator
            case "text":
                locator = await self.page.get_by_text(content, exact=exact)
                return locator
            case "label":
                locator = await self.page.get_by_label(content, exact=exact)
                return locator
            case "placeholder":
                locator = await self.page.get_by_placeholder(content, exact=exact)
                return locator
            case "alt_text":
                locator = await self.page.get_by_alt_text(content, exact=exact)
                return locator
            case "title":
                locator = await self.page.get_by_title(content, exact=exact)
                return locator
            case "test_id":
                locator = await self.page.get_by_test_id(content)
                return locator

    # 点击元素
    async def click_element(self, selector):
        locator = await self.get_locator(selector)
        await locator.click()

    # 输入文本
    async def input_text(self, selector, text: str):
        locator = await self.get_locator(selector)
        await locator.fill(text)

    # 上传文件
    async def upload_file(self, selector, path: str):
        locator = await self.get_locator(selector)
        await locator.set_input_files(path)

    # 获取元素文本
    async def get_text_content(self, selector):
        element = await self.page.query_selector(selector)
        await element.inner_text()


# 入口函数
async def main(param=None):
    playwright_wrapper = AsyncPlayWrightWrapper()
    await playwright_wrapper.initialize(param)
    await playwright_wrapper.goto_url('https://yyw.com')




if __name__ == "__main__":
    asyncio.run(main())
