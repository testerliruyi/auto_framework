"""
func:  腾讯视频号上传视频流程
"""

from common.playwright.sync_playwright_base import SyncPlayWrightWrapper


class UploadVideoPage(SyncPlayWrightWrapper):

    def __init__(self):
        super().__init__('design')

    def open_url(self):
        url = "https://channels.weixin.qq.com/platform/"
        self.goto_url(url)

    def click_upload_button(self, info):
        self.page.get_by_role("button", name="发表视频", exact=True).click()
        self.page.locator(".upload-wrap input").set_input_files(info["path"])
        self.page.locator(".input-editor").type(info["desc"])
        self.page.locator(".position-display").click()
        # 选择不显示位置
        self.page.locator('//div[@class="location-filter-wrap"]//div[text()="不显示位置"]').click()
        self.page.locator('input[type="text"][placeholder*="概括视频主要内容"]').fill(info['title'])
        # 等待出现删除按钮，即为视频上传成功
        self.expect(self.page.locator("//div[@class='tag-inner'][text()='删除']")).to_be_visible()
        # 点击发布按钮
        self.page.locator('//button[text()="发表"]').click()
        # 判断发表成功
        self.expect(self.page.get_by_text("已发表")).to_be_visible()







