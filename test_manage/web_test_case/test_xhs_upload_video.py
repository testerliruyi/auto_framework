from src.page_object.XHS.main_page import MainPage
from common.file_handle.content_handle import content_handle
import pytest


@pytest.mark.parametrize('content', content_handle())
class TestXshUploadVide:

    def setup_class(self):
        MainPage.get_url(url='https://creator.xiaohongshu.com/creator/home')

    # 发布视频
    def test_click_upload_video_button(self,content):
        # 初始化
        driver = MainPage()
        # 点击首页发布按钮
        driver.public_button()
        # 输入视频路径
        driver.upload_video_input(content['path'])
        # 输入视频标题
        driver.video_title_input(content['title'])
        # 输入视频简介
        driver.video_desc_input(content['desc_split'])
        driver.video_topic_input(content['topic'])
        # 点击发布按钮
        driver.public_button_click()


if __name__ == "__main__":
    pytest.main(['-q','--pdb'])

