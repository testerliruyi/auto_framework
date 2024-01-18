"""
配置文件，项目常用配置信息
"""
import os
import pathlib

from common.file_handle.get_file_list import get_files
from common.params import Params


class ConfigInfo:
    # 项目根本目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 配置环境
    ENV = "YD02"

    # yaml文件测试案例保存目录
    TEST_CASE_FILE = os.path.join(BASE_DIR, "test_manage/test_case_file")

    # py测试可执行案例保存目录
    TEST_CASE_PATH = os.path.join(BASE_DIR, "test_manage/api_test_case")

    # test_data文件目录
    TEST_DATA_PATH = os.path.join(BASE_DIR, "test_manage/test_data")

    # 不同环境测试使用链接配置文件
    ENV_CONFIG_FILE = os.path.join(BASE_DIR, "config/env_config.ini")

    # 数据库信息保存文件
    DATABASE_INFO_FILE = os.path.join(BASE_DIR, "config/database_info.yaml")

    # 日志保存文件路径
    LOG_FILE_PATH = os.path.join(BASE_DIR, f"log\\test_{Params.date_formatter(formatter='%Y%m%d')}.log")

    # 视频存放路径
    videoPath = "E:\视频目录\YYW.AI-1.18"

    # 循环次数
    loop_count = 5

    # ffmpeg 安装地址
    ffmpeg_DIR = r"D:\ffmpeg-6.1.1\bin"



if __name__ == "__main__":
    # 获取文件列表
    # for i in get_files(ConfigInfo.videoPath):
    #     print(i)
    print(ConfigInfo.LOG_FILE_PATH)