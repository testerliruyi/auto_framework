from playwright.sync_api import Route

from common.playwright.sync_playwright_base import SyncPlayWrightWrapper


class Playwright_func(SyncPlayWrightWrapper):

    # def __init__(self):
    #     super().__init__("design")

    def test_mock(self):
        def handle(route: Route):
            request = route.request
            print(request)
            response = route.fetch()
            json = response.json()
            json.append({"name": "Loquat", "id": 100})
            route.fulfill(response=response, json=json)

        self.page.route("https://demo.playwright.dev/api-mocking/api/v1/fruits", handle)
        self.page.goto("https://demo.playwright.dev/api-mocking")
        self.expect(self.page.get_by_text("Loquat", exact=True)).to_be_visible()

    def record_har_file(self):
        self.page.route_from_har("../test_result/fruit.har", url="*/**/api/v1/fruits", update=False)
        self.page.goto("https://demo.playwright.dev/api-mocking")
        self.expect(self.page.get_by_text("Strawberry")).to_be_visible()

    # 监听页面事件
    def get_status_code(self):
        self.page.on("request", lambda request: print(request))
        self.page.on("response", lambda response: print(response))
        self.page.goto("https://example.com")

    def filter_img(self):
        self.page.on("request", lambda request: print(f"Request_url:{request.url}"))
        self.page.on("response", lambda response: print(f"Response_status:{response.status}, response url:{response.url}"))
        self.page.goto("https://www.gets.com/", wait_until="load", timeout=100000)
#
# from playwright.sync_api import sync_playwright
#
# def main():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, timeout=100000, args=['--start-maximized'],
#                                     executable_path=r"E:\playwright_driver\chromium-1097\chrome-win\chrome.exe")
#         page = browser.new_page()
#
#         async def log_request(request):
#             print(f"Request: {request.method} - {request.url}")
#
#         async def log_response(response):
#             print(f"Response: {response.status} - {response.url}")
#
#         page.on('request', lambda request: log_request(request))
#         page.on('response', lambda response: log_response(response))
#         page.goto('https://www.gets.com/', wait_until="networkidle", timeout=100000)
#
#         browser.close()


if __name__ == '__main__':
    Playwright_func().filter_img()
