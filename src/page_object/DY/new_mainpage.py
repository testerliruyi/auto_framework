from common.play_wright.sync_playwright_base import SyncPlayWrightWrapper


class main_page_element(SyncPlayWrightWrapper):
    def __init__(self):
        super().__init__('design')

    def go_url(self):
        self.goto_url("https://creator.douyin.com/creator-micro/home")

    def click_btn_and_inputVideoPath(self, path):
        up_btn = self.get_by('role', 'button', '发布作品')
        self.expect(up_btn).to_be_visible()
        up_btn.click()
        try:
            self.upload_file("label>input[name='upload-btn']", path)
        except Exception as e:
            up_btn.click()
            self.upload_file("label>input[name='upload-btn']", path)

        # retry_count = 0
        # max_retries = 3
        # while retry_count <= max_retries:
        #     try:
        #         self.page.get_by_role('button', name='发布作品', exact=True).click()
        #         self.page.locator("label>input[name='upload-btn']").set_input_files(path)
        #         break
        #     except Exception as e:
        #         retry_count += 1
        #         continue

    def input_video_info(self, info):
        self.page.get_by_placeholder('好的作品标题可获得更多浏览').fill(info.get('title'))
        self.page.locator('.zone-container').type(info.get('desc_split'))
        for x in info.get('topic'):
            new_x = '#' + x
            self.page.locator('.zone-container').type(new_x)
            first_lab = self.get_by('text', content=x)
            self.expect(first_lab).to_be_visible()
            first_lab.click()

    def click_public_button(self):
        wait_element = self.get_by('text', "取消上传")
        self.expect(wait_element).to_be_hidden()
        self.page.get_by_role('button', name='发布', exact=True).click()
