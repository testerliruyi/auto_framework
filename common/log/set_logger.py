"""
func:设置log格式，返回日志对象
"""
import logging
import traceback
from config.setting import ConfigInfo


class SetLogger(ConfigInfo):

    def __init__(self):
        self.file = ConfigInfo.LOG_FILE_PATH
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.INFO)

    @staticmethod
    def set_formatter():
        formatter_1 = logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")
        return formatter_1

    # 日志文件设置
    def set_file_handler(self):
        file_handler = logging.FileHandler(filename=self.file, mode='w', encoding='utf-8')
        file_handler.setFormatter(self.set_formatter())
        file_handler.setLevel(logging.INFO)
        self.log.addHandler(file_handler)

    def set_Stream_handler(self):
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(self.set_formatter())
        stream_handler.setLevel(logging.INFO)
        self.log.addHandler(stream_handler)

    def get_file_logger(self):
        self.set_file_handler()
        return self.log

    def get_stream_logger(self):
        self.set_Stream_handler()
        return self.log


def file_logger_obj():
    logger = SetLogger().get_file_logger()
    return logger


def stream_logger_obj():
    logger = SetLogger().get_stream_logger()
    return logger


if __name__ == "__main__":
    file_logger_obj()
