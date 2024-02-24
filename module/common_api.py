"""
@func: 用于接口fastapi 接口調用
"""
import allure
from common.common_test_api import CommonTestApi
from common.assert_util.assert_control import Assert


class CommonFunctionApi:
    def __init__(self, request_content):
        self.content = request_content

    def api_reqeust(self):
        # 对案例报文进行处理，并发起接口请求
        response_data = CommonTestApi(self.content).api_request()
        return response_data

    def api_assert(self, response_data):
        # 案例断言
        return Assert(self.content["Assert"]).assert_equality(response_data)



if __name__ == "__main__":
    import sys

    print(sys.path)
