import time
import pytest
from common.file_handle.file_content_handle import content_handle
from Src.page_object.DY.new_mainpage import main_page_element

pageObj = main_page_element()


@pytest.mark.parametrize("info", content_handle())
class TestDyVideoPublic:

    def setup_class(self):
        pageObj.go_url()

    def test_upload_video(self, info):
        pageObj.click_btn_and_inputVideoPath(info['path'])
        pageObj.input_video_info(info)
        pageObj.click_public_button()





