# time:  20240217 10:44:36
# author:   LiRuYi
# func:  测试案例执行
import pytest
import allure
import json
from common.file_handle.get_case_detail import get_case_detail
from common import common_test_api as ct
from common.assert_util.assert_control import Assert
from common.file_handle.get_test_data import get_test_data
"""小提示:
dataInfo字段为需要从文件中读取数据批量执行案例时使用。
"""


class TestGetWeather:
    @allure.story("获取天气信息")
    # @pytest.mark.parametrize('dataInfo', get_test_data("creditCard.xlsx"))
    @pytest.mark.parametrize("body", get_case_detail("get_weather.yaml"))
    def test_get_weather(self, body):
        # 对案例报文进行处理，并发起接口请求
        ct.CommonTestApi(body).api_request()
        # 数据库中获取响应结果,用于进行断言验证
        response_data = ct.CommonTestApi(body).get_case_content(body["caseFileName"], 'response')
        # 案例断言
        Assert(body["assert"]).assert_equality(json.loads(response_data))


if __name__ == "__main__":
    pytest.main([r'test_get_weather.py', '-s', '-W'])
