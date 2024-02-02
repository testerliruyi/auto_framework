from config.configInfo import ConfigInfo
from common.file_handle.read_file_content import get_yaml_file_content
import time
from common.file_handle.get_file_list import get_files


class UploadVideo(DebugWebdriver):
    def __init__(self):
        super().__init__()
        self.videoDescAndTitle = get_yaml_file_content('../../config/describe.yaml')

    def login(self):
        self.driver.get(ConfigInfo.url)
        print("请进行扫码登录")
        count = 3
        i = 0
        while i <= count:
            i += 1
            if self.driver.current_url != ConfigInfo.url:
                break
            else:
                time.sleep(10)
                continue

    def up_load_video(self):
        # self.driver.get("https://channels.weixin.qq.com/platform")
        # 获取视频描述信息使用次数
        count = 0
        # 控制异常执行次数
        exec_count = 0
        # 获取视频路径
        paths = get_files(ConfigInfo.videoPath)
        # 路径返回为false ，目录为空则退出
        if not paths:
            raise Exception("视频路径获取内容为空，请检查")
        else:
            for path in paths:
                # 操作链方式点击发表视频按钮
                while True:
                    # allHandles = self.driver.window_handles
                    # # 获取最新的窗口
                    # currentHandle=self.driver.current_window_handle
                    # print("当前页面窗口:",currentHandle)
                    # print("所有页面窗口:",allHandles)
                    # # for handle in allHandles:
                    # #     if handle != currentHandle:
                    # self.driver.switch_to_window(currentHandle)

                    try:
                        # 定位发表视频按钮
                        submitVideoButton = self.get_element("xpath", "//div/button[@type='button' and text()='发表视频']")
                        time.sleep(1)
                        # 点击发表视频按钮
                        if submitVideoButton:
                            ActionChains(self.driver).move_to_element(submitVideoButton).click(submitVideoButton).perform()
                        else:
                            print("未定位到")
                            return False
                        break
                    except Exception as e:
                        if exec_count < 10:
                            time.sleep(1)
                            print("第一步：未定位到【发表视频】按钮，继续重试")
                            exec_count += 1
                            continue
                        else:
                            return "重试5次，未定位到发表视频按钮，流程结束。"

                # 等待视频上传完成
                while True:
                    # 使用视频路径上传视频文件
                    try:
                        self.locate_element('xpath', "//input[@type='file']").send_keys(str(path))
                        print("视频在上传中，请等待视频上传完成")
                        WebDriverWait(self.driver, 80).until(
                            EC.invisibility_of_element_located((By.XPATH, '//div[text()="取消上传"]')))
                        break
                    except Exception as e:
                        print("上传视频失败，继续重试。")
                        continue

                # # 点击确认封面
                # self.locate_element('xpath','//div[text()="更换封面"]').click()
                # # 确认封面
                # if self.is_element_exist('xpath','//div[@class="cover-set-footer"]//button[text()="确认"]'):
                #     self.locate_element('xpath','//div[@class="cover-set-footer"]//button[text()="确认"]').click()
                # else:
                #     pass

                # 输入视频描述
                self.locate_element('xpath', '//div[@class="input-editor" and @data-placeholder="添加描述"]').send_keys(
                    self.videoDescAndTitle[count]['desc'])
                # 输入视频标题
                self.locate_element('xpath', '//div[@class="post-short-title-wrap"]//input').send_keys(
                    self.videoDescAndTitle[count]['title'])
                # 视频描述信息获取次数
                count += 1
                # 选择不显示位置
                while True:
                    # 位置下拉选择
                    self.locate_element('xpath',
                                        '//div[@class="post-position-wrap"]//span[contains(@class,"arrow-icon")]').click()
                    # 不显示位置选项项
                    unselectEle = self.locate_element('xpath',
                                                      '//div[@class="common-option-list-wrap"]//div[@class="name"][text()="不显示位置"]')
                    try:
                        if not unselectEle:
                            continue
                        else:
                            unselectEle.click()
                            break
                    except Exception as e:
                        print(e)
                        continue
                # # 原创声明
                # declareCheckBox=self.locate_element('xpath','//div[@class=" flex-start"]')
                # if not declareCheckBox:
                #     pass
                # else:
                #     declareCheckBox.find_element(By.XPATH,'./label[@class="ant-checkbox-wrapper"]//input').click()
                # 循环定位发表视频按钮
                while True:
                    # 点击发表按钮
                    upButton = self.locate_element('xpath', '//button[text()="发表"]')
                    time.sleep(1)
                    try:
                        upButton.click()
                        if self.locate_element('xpath', '//*[text()="请上传视频"]'):
                            print("页面信息不完整或视频未上传完成，请稍候")
                            continue
                        else:
                            if self.locate_element('xpath', '//*[text()="已发表"]'):
                                break
                            else:
                                time.sleep(5)
                                break
                    except Exception as e:
                        continue
                    #     ActionChains(self.driver).move_to_element(upButton).click(upButton).perform()
                    #     if self.locate_element('xpath', '//*[text()="请上传视频"]'):
                    #         print("页面信息不完整或视频未上传完成，请稍候")
                    #         continue
                    #     else:
                    #         if self.locate_element('xpath', '//*[text()="已发表"]'):
                    #             break
                    #         else:
                    #             time.sleep(5)
                    #             break



    def logout(self):
        # while True:
        #     if self.get_element('xpath','//button[text()="发表视频"]'):
        # 点击账号进行注销
        self.locate_element('xpath', '//div[@class="account-info"]').click()
        # 注销
        self.locate_element('xpath', '//div[text()="退出登录"]').click()
            # else:
            #     time.sleep(1)
            #     continue

    def run(self):
        # self.login()
        self.up_load_video()

        self.logout()


if __name__ == "__main__":
    i = 1
    while i <= ConfigInfo.loop_count:
        i += 1
        UploadVideo().run()
        time.sleep(20)
