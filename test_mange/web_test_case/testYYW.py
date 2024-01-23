from src.page_object.yyw.main_page import main_page_element

init_page = main_page_element()

class TestYYW:

    # def setup_class(self):
    #     init_page.goto_url("https://www.yyw.com")

    # def test_login(self):
    #     init_page.login()
    #
    # def test_search(self):
    #     init_page.search()

    def test_add_cart(self):
        init_page.enter_goodsinfo_and_add_cart()

