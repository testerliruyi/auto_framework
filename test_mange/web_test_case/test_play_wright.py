# 导入公共包
import time
from Src.page_object.yyw.main_page import main_page_element

# 初始化页面对象
initPage = main_page_element()


class TestGetYyw:
    def test_search(self):
        initPage.go_url()
        initPage.search_input()
        initPage.click_button()
        time.sleep(20)





if __name__ == '__main__':
    pass
