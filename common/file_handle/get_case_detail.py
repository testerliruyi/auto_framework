"""
author: 李如意
func：获取yaml文件案例内容
"""

from common.file_handle. search_file import search_file
from common.file_handle.read_file import ReadFile
from config.setting import ConfigInfo


def get_Case_Detail(case_file_name: str):
    """
    :param case_file_name:  yaml案例文件名称
    :return:
    """
    #获取案例文件路径
    case_file_path = search_file(ConfigInfo.TEST_CASE_FILE, filename = case_file_name)
    #对案例文件名进行截取只获取文件名部分
    get_case_filename = case_file_name.split('.')[0]
    if case_file_path:
        case_body = ReadFile.read_yaml_file(case_file_path)
        for case in case_body:
            case['caseFileName'] = get_case_filename 
        return case_body
    else:
        raise ValueError("测试案例文件不存在，请检查文件名是否正确")