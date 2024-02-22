"""
@func: 用于接口fastapi 接口調用
"""
import allure
from ...common import common_test_api as ct
from ...common.assert_util.assert_control import Assert


class CommonFunctionApi:
    def __init__(self, request_content):
        self.content = request_content

    @allure.story("获取天气信息")
    def api_test_func(self):
        # 对案例报文进行处理，并发起接口请求
        response_data = ct.CommonTestApi(self.content).api_request()
        # 案例断言
        Assert(self.content["Assert"]).assert_equality(response_data)



if __name__ == "__main__":
    pass
