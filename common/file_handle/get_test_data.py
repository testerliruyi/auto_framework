"""
func: 获取yaml 或者 excel 工作表测试数据
"""

from config.setting import ConfigInfo
from common.file_handle.read_file import ReadFile
import os
import typing


def get_test_data(file_path: typing.Union[str], key=None):
    """
    :param key: 测试数据关键字
    :param file_path: 文件名
    :param key: 对应的关键字
    :return:
    """
    try:
        if file_path.endswith('yaml'):
            if key:
                data = ReadFile.read_yaml_file(file_path, selector=ConfigInfo.ENV)
                return data.get(key)
            else:
                data = ReadFile.read_yaml_file(file_path, selector=ConfigInfo.ENV)
                return data
        elif file_path.endswith('xlsx'):
            file_path = ConfigInfo.TEST_DATA_PATH + os.sep + file_path
            data = ReadFile.read_excel(file_path, ConfigInfo.ENV)
            return data
    except Exception as err:
        raise FileNotFoundError("读取文件有误，请检查文件是否存在。", err)


if __name__ == "__main__":
    print(get_test_data("datainfo.yaml", key='city'))
