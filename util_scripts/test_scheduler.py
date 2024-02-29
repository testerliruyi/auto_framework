import sys
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED, EVENT_JOB_MISSED
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from common.log.set_logger import file_logger_obj
from datetime import datetime
from common.playwright.sync_playwright_base import SyncPlayWrightWrapper


class VisitUrl(SyncPlayWrightWrapper):

    def visit_url(self, url):
        self.goto_url(url)
        return  self.page.context()


page = VisitUrl()


class TestVisitUrl:
    def test_visit_url(self):
        res = page.visit_url("https://yyw.com")
        assert res == 200


if __name__ == "__main__":
    jobstores = {"default": MemoryJobStore()}
    scheduler = BlockingScheduler(jobstores=jobstores)
    scheduler.add_job(my_job, "cron", hour="19", minute="55", id="测试自动化")
    scheduler._logger = file_logger_obj
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
