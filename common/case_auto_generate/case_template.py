"""
author: 李如意
func: py案例内容模板
"""
from common.params import Params
import os
from config.setting import ConfigInfo
def write_case(case_path, page):
    with open(case_path, 'w',encoding='utf-8') as f:
        f.write(page)

def write_testcase_file(allure_story,class_tile,func_title,case_path, file_name,yaml_file_name):
    """
    :param allure_story: 案例中值
    :param class_tile:
    :param func_title:
    :param case_path:
    :param file_name:
    :param yaml_file_name:
    :return:
    """
    nowTime = Params.date_formatter(Params().now_date,'%Y%m%d %H:%M:%S')
    real_time_update_test_cases=ConfigInfo.real_time_update_test_cases
    page = f"""
#_*_ coding:utf-8_*
# time:  {nowTime}
# author:   liruyi
# func:  测试案例执行
import pytest
import allure
import json
from commonUtil.getInfoUtil.getfaseDetail import get_Case_Detail
from commonUtil import commonTestApi as ct
from commonUtil.Assert.AssertControl import Assert
from commonUtil.getInfoUtil.get_data import get_fileData
\"""小提示:
dataInfo字段为需要从文件中读取数据批量执行案例时使用。
\"""
fh assertMethod_enum.py
i case template.py×
class Test {class_tile}:
@allure.story("{allure_story}")
#@pytest.mark.parametrize('dataInfo', get_fileData("creditCard.xlsx"))
@pytest.mark.parametrize("body", get_Case_Detail("{yaml_file_name}"))
def test_{func_title}(self,body):
#接口请求
ct.Comment_test_api().comRequest(body)
#数据库中获取响应结果
response_data = ct.Comment_test_api().get_CaseContent(body["caseFileName"],'reponse')
#案例断言
Assert(body["assert"]).assert_equality(json.loads(response_data))
pytest.main([r'{file_name}','-s','-W','ignore:Module already imported:pytest.Pytestwarning'])
"""

#根据开关状态判断是否为True，为true时重写所有案例，为false时，案例存在则不重写。
    if real_time_update_test_cases:
        write_case(case_path = case_path, page=page)
        print(f'案例：{file_name}已生成.')
    elif real_time_update_test_cases is False:
        if not os.path.exists(case_path):
            write_case(case_path=case_path, page=page)
            print(f'案例：{file_name}已生成。')
    else:
        raise ValueError("real_time_update_test_cases 配置不正确")


if __name__ == "__main__":
    print(Params.date_formatter(Params().now_date,'%Y%m%d %H:%M:%S'))