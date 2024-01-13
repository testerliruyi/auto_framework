import time
from common.selenium.selenium_base import DebugWebdriver


# 小红书发布视频首页元素
class MainPage(DebugWebdriver):
    def public_button(self):
        self.wait_for_element_appear(self.get_element('xpath', '//a[text()="发布笔记"]'), 10)
        return self.get_element('xpath', '//a[text()="发布笔记"]', 'click')

    def upload_video(self):
        return self.get_element('xpath', '//input[@class="upload-input"]')

    def upload_video_input(self, path):
        self.upload_video().send_keys(path)

    def video_title_input(self, info):
        self.get_element('xpath', "//div[@class='c-input titleInput']/input", action='input', info=info)

    def video_desc_input(self, info):
        self.get_element('xpath', "//div[@class='topic-container']/p[@id='post-textarea']", action='input', info=info)

    def video_topic_input(self, info: list):
        for x in info:
            x = '#' + x
            self.get_element('xpath', "//div[@class='topic-container']/p[@id='post-textarea']", action='input', info=x)
            first_lab = self.get_element('xpath', '//div[@class="tribute-container"]/ul/li[position()=1]')
            self.wait_for_element_appear(first_lab)
            time.sleep(1)
            self.get_element('xpath', '//div[@class="tribute-container"]/ul/li[position()=1]', action="click")

    def public_button_click(self):
        self.wait_for_element_disappear('//div/p[text()="视频正在上传中"]', 150)
        # 等待元素可点击，可点击后即进行发布
        self.wait_for_element_enable(('xpath',"//div[@class='submit']/button[1]"))
        self.get_element('xpath', "//div[@class='submit']/button[1]", action='click')


