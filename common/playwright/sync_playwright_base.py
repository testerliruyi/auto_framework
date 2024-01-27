from playwright.sync_api import sync_playwright, expect
from typing import Union, Optional, Literal
from config.setting import ConfigInfo
import os



class SyncPlayWrightWrapper:
    def __init__(self, param: Union[None, str] = None, browser_type="chromium"):
        self.playWright = sync_playwright().start()
        self.browser_type = browser_type
        self.browser = None
        self.expect = expect
        # 设置全局expect超时时间为30sec
        self.expect.set_options(timeout=60000)
        if param is None:
            print("current mode is: default")
            self.page = self.__lunch_default_browser()
        elif param.lower() == "design":
            print("current mode is: design")
            self.page = self.__lunch_design_browser()
        elif param.lower() == "local":
            print("current mode is: local")
            self.page = self.__lunch_local_browser()


    # 默认方法启动浏览器
    def __lunch_default_browser(self):
        if self.browser_type == "chromium":
            self.browser = self.playWright.chromium.launch(headless=False, timeout=100000, args=['--start-maximized'])
        elif self.browser_type == "firefox":
            self.browser = self.playWright.firefox.launch(headless=False, timeout=100000, args=['--start-maximized'])
        elif self.browser_type == "webkit":
            self.browser = self.playWright.webkit.launch(headless=False, timeout=100000, args=['--start-maximized'])
        context = self.browser.new_context(no_viewport=True)
        self.page = context.new_page()
        return self.page

    # 指定端口页面启动浏览器
    def __lunch_design_browser(self):
        if self.browser_type == "chromium":
            self.browser = self.playWright.chromium.connect_over_cdp("http://localhost:9222")

        self.context = self.browser.contexts[0]
        self.page = self.context.pages[0]
        return self.page

    # 指定本机已安装浏览器
    def __lunch_local_browser(self):
        if self.browser_type == "chromium":
            self.browser = self.playWright.chromium.launch_persistent_context(
                # 指定本地缓存
                user_data_dir="D:\selenium\chrome_temp",
                # 指定本机chrome地址
                executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe",
                accept_downloads=True,
                headless=False,
                bypass_csp=True,
                slow_mo=10,
                args=['--disable-blink-features=AutomationControlled', '--remote-debugging-port=9222',
                      '--start-maximized']

            )
        self.page = self.browser.new_page()
        return self.page

    # 关闭浏览器
    def close_browser(self):
        if self.browser:
            self.browser.close()

    # 跳转页面
    def goto_url(self, url, time=60000):
        # 设置加载超时时间为60
        self.page.goto(url, timeout=time, wait_until="commit")

    # 使用locator方式定位元素
    def get_locator(self, selector):
        return self.page.locator(selector)

    # 使用get_by方式定位元素
    def get_by(self, action: Optional[Literal["role", "text", "label", "placeholder", "alt_text", "title", "test_id"]],
               content: Union[str,Literal["alert", "alertdialog", "application", "article", "banner", "blockquote", "button", "caption", "cell", "checkbox", "code", "columnheader", "combobox", "complementary", "contentinfo", "definition", "deletion", "dialog", "directory", "document", "emphasis", "feed", "figure", "form", "generic", "grid", "gridcell", "group", "heading", "img", "insertion", "link", "list", "listbox", "listitem", "log", "main", "marquee", "math", "menu", "menubar", "menuitem", "menuitemcheckbox", "menuitemradio", "meter", "navigation", "none", "note", "option", "paragraph", "presentation", "progressbar", "radio", "radiogroup", "region", "row", "rowgroup", "rowheader", "scrollbar", "search", "searchbox", "separator", "slider", "spinbutton", "status", "strong", "subscript", "superscript", "switch", "tab", "table", "tablist", "tabpanel", "term", "textbox", "time", "timer", "toolbar", "tooltip", "tree", "treegrid", "treeitem"]],
               name=None,
               exact=True):
        match action.lower():
            case "role":
                return self.page.get_by_role(content, name=name, exact=exact)
            case "text":
                return self.page.get_by_text(content, exact=exact)
            case "label":
                return self.page.get_by_label(content, exact=exact)
            case "placeholder":
                return self.page.get_by_placeholder(content, exact=exact)
            case "alt_text":
                return self.page.get_by_alt_text(content, exact=exact)
            case "title":
                return self.page.get_by_title(content, exact=exact)
            case "test_id":
                return self.page.get_by_test_id(content)

    # 点击元素
    def click_element(self, selector):
        self.get_locator(selector).click()

    # 输入文本
    def input_text(self, selector, text: str):
        self.get_locator(selector).fill(text)

    # 查询元素
    def query_element(self, selector):
        element = self.page.query_selector(selector)
        return element
    # 上传文件
    def upload_file(self, selector, path: str):
        self.get_locator(selector).set_input_files(path)

    # 获取元素文本
    def get_text_content(self, selector):
        element = self.page.query_selector(selector)
        return element.inner_text()

    # 等待元素可见\隐藏,状态为可选项["attached", "detached", "hidden", "visible"],默认等待元素可见。
    def wait_element_state(self, selector,
                           state: Optional[Literal["attached", "detached", "hidden", "visible"]] = "visible",
                           timeout=10000):
        self.page.wait_for_selector(selector, state=state, timeout=timeout)
        
    # 浏览器存在打开新标签时，使用此方法等待新页面出现
    def wait_for_new_page(self):
        new_page = self.context.wait_for_event("page")
        return new_page
    
    # 获取浏览器上下文所有页面标签
    def get_all_pages(self):
        self.wait_for_new_page()
        all_pages = self.context.pages
        return all_pages

    # 截图并保存
    def save_screenshot(self, file_name: str, path: str = None):
        """
        :param path:  图片保存目录
        :param file_name: 图片文件名
        :return:
        """
        if path:
            path = os.path.join(path, file_name)
            self.page.screenshot(path=path, full_page=True)
        else:
            path = os.path.join(ConfigInfo.SAVE_TEST_RESULT_PATH, file_name)
            self.page.screenshot(path=path, full_page=True)

    #切换到最新标签
    def get_all_pages(self):
        return self.context.pages
    


if __name__ == "__main__":
    pass
