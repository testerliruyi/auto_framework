"""
func: 获取yaml文件测试数据
"""

from config.setting import ConfigInfo
from common.file_handle.read_file import ReadFile
import os, typing


def get_fileData(filename: typing.Union[str], path=None, selector=None):
    """
    :param filename: 文件名
    :param path: none时来示从指定目录获取测试数据，非None时夹示获取指定陪径数播
    :param selector: 对应环境
    :return:
    """
    if path is None:
        try:
            if filename.endswith('yaml') == True:
                file_path = ConfigInfo.TEST_DATA_PATH + os.sep + filename
                data = ReadFile.read_yaml_file(file_path, ConfigInfo.ENV)
                return data
            elif filename.endswith('xlsx') == True:
                file_path = ConfigInfo.TEST_DATA_PATH + os.sep + filename
                data = ReadFile.read_excel(file_path, ConfigInfo.ENV)
                return data
        except Exception as err:
            raise FileNotFoundError("读取文件有误，请检查文件是否存在。", err)
    else:
        try:
            if filename.endswith('yaml') == True:
                file_path = path + os.sep + filename
                data = ReadFile.read_yaml_file(file_path, selector=selector)
                return data
            elif filename.endswith("xlsx") == True:
                file_path = ConfigInfo.TEST_DATA_PATH + os.sep + filename
                data = ReadFile.read_excel(file_path, ws=selector)
                return data

        except Exception as err:
            raise FileNotFoundError("读取文件有误，请检查文件是否存在。", err)


if __name__ == "__main__":
    pass
