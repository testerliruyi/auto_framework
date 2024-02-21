# _*_ coding:utf-8_*
# time:  20240203 01:01:20
# author:   liruyi
# func:  测试案例执行

import pytest
import allure
import json
from common.file_handle.get_case_detail import get_case_detail
from common import common_test_api as ct
from common.assert_util.assert_control import Assert
from common.file_handle.get_test_data import get_test_data

"""
小提示:
dataInfo字段为需要从文件中读取数据批量执行案例时使用。
"""


class TestGetinfo:
    @allure.story("getinfo")
    # @pytest.mark.parametrize('dataInfo', get_test_data("creditCard.xlsx"))
    @pytest.mark.parametrize("body", get_case_detail("getinfo.yaml"))
    def test_getinfo(self, body):
        print(body)
        # 接口请求
        ct.CommonTestApi().api_request(body)
        # 数据库中获取响应结果
        response_data = ct.CommonTestApi().get_case_content(body["caseFileName"], 'reponse')
        # 案例断言
        Assert(body["Assert"]).assert_equality(json.loads(response_data))


if __name__ == "__main__":
    pytest.main([r'test_getinfo.py', '-s', '-W', 'ignore:Module already imported:pytest.Pytestwarning'])
