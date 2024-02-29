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
    item = {"case_common": {"allureStory": "获取天气信息"}, "case_title": "获取天气信息_广州", "method": "get",
            "request_url": "api_url", "url_ext": "", "test_data": "datainfo.city", "depend_case": "",
            "headers": {"content-type": "json"},
            "data": {"key": "8d2ea6e26f01172769a75f81e053693f", "city": "${yuanqu}"},
            "Assert": {"status": {"Type": "==", "value": "0", "AssertType": ""}}, "caseFileName": "get_weather"}
    res = CommonFunctionApi(item).api_reqeust()
    print(res)
