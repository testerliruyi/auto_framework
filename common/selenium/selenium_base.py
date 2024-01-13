from selenium import webdriver
from typing import Any, Union, Optional
from selenium.common.exceptions import NoSuchElementException, TimeoutException,StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Action:
    """
               set of element action.
    """
    CLICK = "click"
    INPUT = "input"
    GET_TEXT = "get_text"


# 初始化webDriver
class DebugWebdriver:

    def __init__(self):
        self.driver = self.__start_webdriver()
        # # self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        # if url is not None:
        #     self.driver.get(url)

    @staticmethod
    def get_url(url):
        DebugWebdriver().driver.get(url)


    @staticmethod
    def __start_webdriver():
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def __get_locater(self, key: str) -> str:

        match key.lower():
            case "id":
                return By.ID
            case "name":
                return By.NAME
            case "class_name":
                return By.CLASS_NAME
            case "xpath":
                return By.XPATH
            case "tag_name":
                return By.TAG_NAME
            case "css_selector":
                return By.CSS_SELECTOR
            case "link_text":
                return By.LINK_TEXT
            case "partial_link_text":
                return By.PARTIAL_LINK_TEXT

    # 获取单个元素
    def get_element(self, key, value, action=None, info=None):
        try:
            ele = self.driver.find_element(self.__get_locater(key), value)
            if action == 'click':
                self.click_element(ele)
            elif action == 'get_text':
                self.get_element_text(ele)
            elif action == 'input':
                ele.send_keys(info)
            elif action is None:
                return ele
        except Exception as err:
            print(f"未定位到元素:{err}")
            return False

    # 获取多个元素
    def get_elements(self, key, value):
        try:
            return self.driver.find_elements(self.__get_locater(key), value)
        except Exception as err:
            print(err)
            return False

    def locate_element(self, key, value):
        try:
            if key == 'id':
                return self.driver.find_element(By.ID, value)
            elif key == 'name':
                return self.driver.find_element(By.NAME, value)
            elif key == 'class_name':
                return self.driver.find_element(By.CLASS_NAME, value)
            elif key == 'tag_name':
                return self.driver.find_element(By.TAG_NAME, value)
            elif key == 'link_text':
                return self.driver.find_element(By.LINK_TEXT, value)
            elif key == 'partial_link_text':
                return self.driver.find_element(By.PARTIAL_LINK_TEXT, value)
            elif key == 'xpath':
                return self.driver.find_element(By.XPATH, value)
            elif key == 'css_selector':
                return self.driver.find_element(By.CSS_SELECTOR, value)
        except Exception as e:
            print(f"未定位到元素:{e}")
            # 未找到元素返回false
            # return False

    # 跳转到最新窗口
    def switch_to_last_window(self):
        lastWindowIndex = len(self.driver.window_handles) - 1
        self.driver.switch_to.window(self.driver.window_handles[lastWindowIndex])

    # 等待元素消失
    def wait_for_element_disappear(self, value: str, seconds=10):
        WebDriverWait(self.driver, seconds).until(EC.invisibility_of_element(('xpath', value)))

    # 等待元素出现
    def wait_for_element_appear(self, get_element_func, seconds=10):
        WebDriverWait(self.driver, seconds).until(lambda d: get_element_func)

    # 等待元素可点击
    def wait_for_element_enable(self, element: Optional[tuple], seconds=10) -> bool:
        return WebDriverWait(self.driver, seconds).until(EC.element_to_be_clickable((element[0], element[1])))
        # print("判断元素可点击成功")

    def click(self, key, value):
        # 定位元素
        el = self.locate_element(key, value)
        # 进行点击操作
        el.click()

    # 点击元素
    @staticmethod
    def click_element(ele):
        ele.click()

    # 获取元素文本
    @staticmethod
    def get_element_text(ele):
        return ele.text

    def get_text(self, key, value):
        ele = self.locate_element(key, value)
        return ele.text

    def get_attribute(self, ele, name: Any) -> str:
        return ele.get_attribute(name)


if __name__ == "__main__":
    # print(DebugWebdriver().get_locater("ID"))
    pass
