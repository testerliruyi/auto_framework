"""
func:  腾讯视频号上传视频流程
"""
import time

from common.playwright.sync_playwright_base import SyncPlayWrightWrapper


class UploadVideoPage(SyncPlayWrightWrapper):

    def __init__(self):
        super().__init__('design')

    def open_url(self):
        url = "https://channels.weixin.qq.com/platform/"
        self.goto_url(url)
        time.sleep(2)
        self.context.cookies()

    def click_upload_button(self, info):
        self.page.get_by_role("button", name="发表视频", exact=True).click()
        self.page.locator(".upload-wrap input").set_input_files(info["path"])
        self.page.locator(".input-editor").fill(info["desc"])
        self.page.locator(".position-display").click()
        # 选择不显示位置
        self.page.wait_for_selector('//div[@class="location-filter-wrap"]//div[text()="不显示位置"]', timeout=60000, state="visible")
        self.page.locator('//div[@class="location-filter-wrap"]//div[text()="不显示位置"]').click()
        self.page.locator('input[type="text"][placeholder*="概括视频主要内容"]').fill(info['title'])

    def declare_click(self):
        declare_button = self.page.query_selector('.declare-original-checkbox input')
        if declare_button and declare_button.is_enabled():
            self.page.locator('.declare-original-checkbox input').click()
            locs = self.page.query_selector_all('.form-content dt')
            locs[0].click()
            self.page.wait_for_selector('//ul//li//div/span[text()="科技" and position()=1]')
            tecn = self.page.query_selector_all('//ul//li//div/span[text()="科技" and position()=1]')
            tecn[0].click()
            check_boxs = self.page.query_selector_all(".original-proto-wrapper input[type='checkbox']")
            check_boxs[0].click()
            check_boxs[0].is_checked()
            # 定位 声明原创按钮
            orgin_declare_button = self.page.query_selector_all("//button[text()='声明原创']")
            # 点击
            orgin_declare_button[0].click()
        else:
            pass

    def public_video(self):
        try:
            # 等待出现删除按钮，即为视频上传成功
            self.expect(self.locator("//div[text()='取消上传']")).to_be_hidden(timeout=30000)
            time.sleep(1)
            # 点击发布按钮
            self.page.locator('//button[text()="发表"]').click()
            # 判断发表成功
            self.expect(self.page.get_by_text("已发表")).to_be_visible()
        except AssertionError as err:
            print("错误信息:",err)
            self.expect(self.locator("//div[text()='取消上传']")).to_be_hidden(timeout=30000)
            time.sleep(1)
            # 点击发布按钮
            self.page.locator('//button[text()="发表"]').click()
            # 判断发表成功
            self.expect(self.page.get_by_text("已发表")).to_be_visible()

    def logout(self):
        time.sleep(5)
        self.page.locator('//div[@class="account-info"]').click()
        self.page.locator('//div[text()="退出登录"]').click()
