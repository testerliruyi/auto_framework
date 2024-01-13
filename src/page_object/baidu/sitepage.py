import time

from common.play_wright.sync_playwright_base import SyncPlayWrightWrapper


class main_page_element(SyncPlayWrightWrapper):

    def serach_input(self):
        self.get_locator('#kw').type("beads")

    def click_search(self):
        self.get_locator('#su').click()
        time.sleep(60)
