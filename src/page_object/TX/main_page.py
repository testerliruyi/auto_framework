import time

from common.selenium.selenium_base import DebugWebdriver, ActionChains, Action, WebDriverWait, EC


class WeixinChannel(DebugWebdriver):

    def click_submit_video_button(self):
        submitVideoButton = self.get_element("xpath", "//div/button[@type='button' and text()='发表视频']")
        # 等10秒
        try:
            self.wait_for_element_appear(submitVideoButton)
            # 链式点击按钮
            ActionChains(self.driver).move_to_element(submitVideoButton).click(submitVideoButton).perform()
            # return self
        except Exception as e:
            print('未定位到发表视频按钮')

    def input_video_path(self, videoInfo: dict) -> None:

        self.get_element('xpath', "//input[@type='file']", Action.INPUT, str(videoInfo.get('path')))
        # self.wait_for_element_disappear(self.get_element('xpath', '//div[text()="取消上传"]'),seconds=40)

    def input_video_desc(self, videoInfo: dict):
        WebDriverWait(self.driver, 150).until(
            EC.invisibility_of_element(('xpath', '//div[text()="取消上传"]')))
        # 输入视频描述
        self.get_element('xpath', '//div[@class="input-editor" and @data-placeholder="添加描述"]', Action.INPUT,
                         videoInfo['desc'])

        # 输入视频标题
        self.get_element('xpath', '//div[@class="post-short-title-wrap"]//input', Action.INPUT, videoInfo['title'])

    def select_locate(self):
        while True:
            # 点击下拉选项
            self.get_element('xpath', '//div[@class="post-position-wrap"]//span[contains(@class,"arrow-icon")]',
                             Action.CLICK)
            # 选择不在选项
            self.get_element('xpath',
                             '//div[@class="common-option-list-wrap"]//div[@class="name"][text()="不显示位置"]',
                             Action.CLICK)
            if self.get_element('xpath', '//div[@class="position-display"]//span[text()="不显示位置"]'):
                break
            else:
                continue

    # # 判断原创声明是否存在并进行点击
    def select_org_declare(self):
        # 定位原创声明复选框
        org_declare_checkbox_obj = self.get_element('xpath',
                                                    '//div/span[text()="声明原创"]/../following-sibling::div[1]//span/input')
        count = 0
        # 定位到则进行操作，否则退出
        if org_declare_checkbox_obj and org_declare_checkbox_obj.is_enabled():
            if org_declare_checkbox_obj.is_selected():
                pass
            else:
                self.click_element(org_declare_checkbox_obj)
                # 选择列表项
                while True:
                    try:
                        # 点击原创选项下拉列表
                        self.get_elements('css_selector', 'div.form-content dl dt')[0].click()
                        # js = "var q=document.getElementsByClassName('weui-desktop-dropdown__list')"
                        # self.driver.execute_script(js)
                        self.get_elements('xpath',
                                          '//ul/li[@class="weui-desktop-dropdown__list-ele"]//span[text()="科技"]')[
                            0].click()
                        text = self.get_element_text(self.get_elements('xpath',
                                                                       '//div[@class="form-content"]//dl[@class="weui-desktop-form__dropdown-label"]/dt//span')[
                                                         0])
                        if text == "科技":
                            # 原创权益页面复选框选择
                            self.get_elements('css_selector', 'div.original-proto-wrapper span input')[0].click()
                            # 点击声明原创按钮
                            self.get_elements('xpath',
                                              '//div[@class="weui-desktop-dialog__ft"]/div//button[text()="声明原创"]')[
                                0].click()
                            break
                        else:
                            count += 1
                            print(f"未选中科技选项，重试 第{count} 次")
                            if count <= 5:
                                continue
                            else:
                                break
                    except Exception as e:
                        print("出现异常，5秒后退出:", e)
                        time.sleep(5)
                        break


    def public_video(self):
        # 等待按钮消失 ,点击发表按钮
        while True:
            self.get_element('xpath', '//button[text()="发表"]', Action.CLICK)
            if self.get_element('xpath', '//*[text()="已发表"]'):
                break
            elif self.get_element("xpath", "//div/button[@type='button' and text()='发表视频']"):
                break
            else:
                continue

    def log_out(self):
        time.sleep(10)
        # 点击账号进行注销
        self.locate_element('xpath', '//div[@class="account-info"]').click()
        # 注销
        self.locate_element('xpath', '//div[text()="退出登录"]').click()
