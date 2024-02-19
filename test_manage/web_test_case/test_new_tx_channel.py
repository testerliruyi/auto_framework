from src.page_object.TX.upload_video import UploadVideoPage
import pytest
from common.file_handle.content_handle import content_handle

page = UploadVideoPage()


@pytest.mark.parametrize("info", content_handle())
class TestTxUploadVideo:

    # def setup_class(self):
    #     # 打开网址
    #     page.open_url()

    # 点击发布视频按钮
    def test_upload_video(self, info):
        # 点击发布视频按钮
        page.click_upload_button(info)
        # 判断原创声明是否存在，存在则点击，否则略过
        # page.declare_click()
