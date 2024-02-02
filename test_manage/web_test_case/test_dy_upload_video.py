import time
from src.page_object.DY.main_page import MainPage
from common.file_handle.read_file_content import get_yaml_file_content
import pytest

driver = MainPage()


@pytest.mark.parametrize("info", get_yaml_file_content())
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



