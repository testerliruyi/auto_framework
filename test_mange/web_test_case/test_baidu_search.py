import time

import pytest
from src.page_object.baidu.sitepage import main_page_element

page = main_page_element()

class TestBaiduSearch:

    def setup_class(self):
        page.goto_url("https://www.baidu.com")

    def test_search(self):
        page.serach_input()
        page.click_search()