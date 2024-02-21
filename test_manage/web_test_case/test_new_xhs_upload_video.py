"""
func: playwright 版小红书上传视频
"""

from src.page_object.XHS.upload_video import XhsUploadVideo
from common.file_handle.content_handle import content_handle
import pytest

# 初始化对象
page = XhsUploadVideo()


@pytest.mark.parametrize("info", content_handle())
class TestXhsUploadVideo:

    def setup_class(self):
        page.open_url()

    def test_upload_video(self, info):
        # 点击发布并上传视频
        page.click_upload(info)
        # 填写视频信息并发布
        page.upload_video(info)
