"""
author: 李如意
func: py案例内容模板
"""
from common.params import Params
import os
from config.setting import ConfigInfo


def write_case(case_path, page):
    with open(case_path, 'w', encoding='utf-8') as f:
        f.write(page)


def write_testcase_file(allure_story, class_tile, func_title, case_path, file_name, yaml_file_name):
    """
    :param allure_story: 案例story标题
    :param class_tile: 类名
    :param func_title: 函数名
    :param case_path: 案例路径
    :param file_name:
    :param yaml_file_name: yaml案例文件路径
    :return:
    """
    nowTime = Params.date_formatter(Params().now_date, '%Y%m%d %H:%M:%S')
    real_time_update_test_cases = ConfigInfo.real_time_update_test_cases
    page = f"""# time:  {nowTime}
# author:   LiRuYi
# func:  测试案例执行
import pytest
import allure
import json
from common.file_handle.get_case_detail import get_case_detail
from common import common_test_api as ct
from common.assert_util.assert_control import Assert
from common.file_handle.get_test_data import get_test_data
\"""小提示:
dataInfo字段为需要从文件中读取数据批量执行案例时使用。
\"""


class Test{class_tile}:
    @allure.story("{allure_story}")
    # @pytest.mark.parametrize('dataInfo', get_test_data("creditCard.xlsx"))
    @pytest.mark.parametrize("body", get_case_detail("{yaml_file_name}"))
    def test_{func_title}(self, body):
        # 对案例报文进行处理，并发起接口请求
        ct.CommonTestApi(body).api_request()
        # 数据库中获取响应结果,用于进行断言验证
        response_data = ct.CommonTestApi(body).get_case_content(body["caseFileName"], 'response')
        # 案例断言
        Assert(body["assert"]).assert_equality(json.loads(response_data))


if __name__ == "__main__":
    pytest.main([r'{file_name}', '-s', '-W'])
"""

    # 根据开关状态判断是否为True，为true时重写所有案例，为false时，案例存在则不重写。
    if real_time_update_test_cases:
        write_case(case_path=case_path, page=page)
        print(f'案例：{file_name}已生成.')
    elif real_time_update_test_cases is False:
        if not os.path.exists(case_path):
            write_case(case_path=case_path, page=page)
            print(f'案例：{file_name}已生成。')
    else:
        raise ValueError("real_time_update_test_cases 配置不正确")


if __name__ == "__main__":
    print(Params.date_formatter(Params().now_date, '%Y%m%d %H:%M:%S'))
