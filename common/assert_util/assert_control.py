"""
func: 案例断言内容处理函数
author: 李如意
"""
from common.assert_util.assert_method import AssertMethod
from common.assert_util.assert_type import *
from common.json_find import json_get_value


class Assert:
    def __init__(self, assert_data: dict):
        self.assert_data = assert_data

    @staticmethod
    def _assert_type(key: str, types: str, value: str):
        if str(types) == AssertMethod.equals.value:
            equals(check_value=key, expect_value=value)
        elif str(types) == AssertMethod.less_than.value:
            less_than(check_value=key, expect_value=value)
        elif str(types) == AssertMethod.less_than_or_equals.value:
            less_than_or_equals(check_value=key, expect_value=value)
        elif str(types) == AssertMethod.greater_than.value:
            greater_than(check_value=key, expect_value=value)
        elif str(types) == AssertMethod.greater_than_or_equals.value:
            greater_than_or_equals(check_value=key, expect_value=value)
        elif str(types) == AssertMethod.contains.value:
            contains(check_value=key, expect_value=value)
        elif str(types) == AssertMethod.not_equals.value:
            not_equals(check_value=key, expect_value=value)
        else:
            raise ValueError(f"断言失败，暂不支持{types}断言类型，如需新增断言方式，请联系管理员")

    def assert_type_handle(self, assert_type, key, assert_value, resp_key_value):
        """
        :param assert_type:  案例中断言类型
        :param key: 断言关键字
        :param assert_value: 断言关键字值
        :param resp_key_value: 响应报文关键字值
        :return:
        """
        # 判断断言类型
        if assert_type == 'SQL':
            pass
        elif assert_type is None:
            self._assert_type(types=self.assert_data[key]['Type'], key=resp_key_value, value=assert_value)
        else:
            raise ValueError("断言失败，目前只支持数据库断言和响应断言")

    def assert_equality(self, response_data: dict, status_code = None):
        for key, values in self.assert_data.items():
            if key == "status code":
                assert status_code == values
            else:
                # 获取期望值
                assert_value = self.assert_data[key]['value']
                # 获取判断类型
                assert_type = self.assert_data[key]['AssertType']
                # 从响应数据中提欣期望字段的值
                resp_key_value = json_get_value(response_data,key)
                # 如果数据获取失败，则返回false，判断获取成功再执行加下代码
                if resp_key_value:
                    # 案例断言处理
                    self.assert_type_handle(assert_type, key, assert_value, resp_key_value)
                else:
                    raise ValueError(f"响应报文中{key}值不存在")