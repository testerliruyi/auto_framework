import pytest
from src.page_object.TX.main_page import WeixinChannel
from common.file_handle.content_handle import content_handle


@pytest.mark.parametrize('info', content_handle())
class TestWeiXinChannel:
    # def setup_class(self):
    #     WeixinChannel.get_url(url='https://channels.weixin.qq.com/platform/post/list')
    # @pytest.mark.repeat(2)
    def test_click_upload_video(self, info):
        driver = WeixinChannel()

        driver.click_submit_video_button()

        driver.input_video_path(info)

        driver.input_video_desc(info)

        driver.select_locate()

        # 判断是否存在原创声明，并进行点击
        driver.select_org_declare()

        driver.public_video()

    def teardown_class(self) -> None:
        WeixinChannel().log_out()


if __name__ == '__main__':
    pass
