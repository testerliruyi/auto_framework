import time
from Src.page_object.DY.main_page import MainPage
from common.file_handle.file_content_handle import content_handle
import pytest

driver = MainPage()


@pytest.mark.parametrize("info", content_handle())
class TestDyVideoPublic:

    # def setup_class(self):
    #     MainPage(url="https://creator.douyin.com/creator-micro/home")

    def test_upload_video(self, info):
        driver.click_public_button()
        driver.input_video_path(info['path'])
        driver.input_video_info(info)
        driver.public_button_click()

    def teardown_class(self):
        driver.scan_video_public()
        driver.switch_other_account()



