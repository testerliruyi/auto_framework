# time:  20240222 14:19:52
# author:   LiRuYi
# func:  测试案例执行
import pytest
import allure
from common.file_handle.get_case_detail import get_case_detail
from common import common_test_api as ct
from common.assert_util.assert_control import Assert
from common.file_handle.get_test_data import get_test_data
"""小提示:
dataInfo字段为需要从文件中读取数据批量执行案例时使用。
"""


class TestGetinfo:
    @allure.story("getinfo")
    # @pytest.mark.parametrize('dataInfo', get_test_data("creditCard.xlsx"))
    @pytest.mark.parametrize("body", get_case_detail("getinfo.yaml"))
    def test_getinfo(self, body):
        # 对案例报文进行处理，并发起接口请求
        response_data = ct.CommonTestApi(body).api_request()
        # 案例断言
        Assert(body["Assert"]).assert_equality(response_data)


if __name__ == "__main__":
    pytest.main([r'test_getinfo.py', '-s', '-W'])
