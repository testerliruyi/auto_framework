"""
func: 小红书平台上传视频流程
"""
import time

from common.playwright.sync_playwright_base import SyncPlayWrightWrapper


class XhsUploadVideo(SyncPlayWrightWrapper):
    def __init__(self):
        super().__init__("design")

    def open_url(self):
        self.goto_url("https://creator.xiaohongshu.com/creator/notemanage")

    def click_upload(self, info):
        self.page.locator("a.btn").click()
        self.page.locator("input.upload-input[type='file']").set_input_files(info['path'])

    def upload_video(self, info):
        self.page.locator("css=input.c-input_inner").fill(info['title'])
        self.page.locator("p#post-textarea").type(info['desc_split'])
        # 输入topic并选择第一个
        for topic in info['topic']:
            topic = "#" + topic
            self.page.locator("p#post-textarea").type(topic)
            self.page.wait_for_selector("//div[@class='tribute-container']/ul/li[position()=1]")
            first_lab = self.locator("//div[@class='tribute-container']/ul/li[position()=1]")
            first_lab.click()
            time.sleep(0.5)
        self.expect(self.page.get_by_text("重新上传", exact=True)).to_be_visible()
        self.page.locator("//button//*[text()='发布']").click()
        self.expect(self.page.get_by_text("发布成功")).to_be_visible()



