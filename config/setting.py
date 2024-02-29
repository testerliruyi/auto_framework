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
    ENV = "test"

    # yaml文件测试案例保存目录
    TEST_CASE_FILE = os.path.join(BASE_DIR, "test_manage\\api_test_case_file")

    # py测试可执行案例保存目录
    TEST_CASE_PATH = os.path.join(BASE_DIR, "test_manage\\api_test_case")

    # test_data文件目录
    TEST_DATA_PATH = os.path.join(BASE_DIR, "test_manage\\test_data")

    # 不同环境测试使用链接配置文件
    ENV_CONFIG_FILE = os.path.join(BASE_DIR, "config\\env_config.yaml")

    # 数据库信息保存文件
    DATABASE_INFO_FILE = os.path.join(BASE_DIR, "config\\database_info.yaml")

    # 数据库
    DATABASE_SQLITE = os.path.join(BASE_DIR, "config\\autotest.sqlite")

    # 执行结果缓存目录
    CASE_TMP_DIR = os.path.join(BASE_DIR, "tmp")

    # 日志保存文件路径
    LOG_FILE_PATH = os.path.join(BASE_DIR,
                                 f"logs/test_{Params.date_formatter(Params().now_date, formatter='%Y%m%d')}.log")

    # 测试结果保存路径
    SAVE_TEST_RESULT_PATH = os.path.join(BASE_DIR, "test_report")
    # 视频存放路径
    videoPath = r"E:\视频目录\YYW.AI-2.28"

    # 循环次数
    loop_count = 5

    # yaml案例生成标志（True: 表示查询所有yaml案例文件重新生成py测试案例，False:仅处理未生成py测试案例的yaml文件）
    real_time_update_test_cases = True

    # 系统分隔符
    os_sep = os.sep

    # ffmpeg 安装地址
    ffmpeg_DIR = r"D:\ffmpeg-6.1.1\bin"


if __name__ == "__main__":
    # 获取文件列表
    for i in get_files(ConfigInfo.videoPath):
        print(i)
    # print(ConfigInfo.TEST_CASE_FILE)
