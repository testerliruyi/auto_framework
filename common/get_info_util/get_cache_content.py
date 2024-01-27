"""
func: 获取缓存目录文件内容
"""
from config.setting import ConfigInfo
from common.file_handle.read_file import ReadFile
import os


def get_cache_file_content(cache_file):
    file_name = cache_file + ".yaml"
    #组依赖案例响应结果文件路径
    cache_filepath = os.path.join(ConfigInfo.CASE_TMP_DIR, file_name)
    #获取依粮案例响应结果内容
    cachefile_content = ReadFile.read_yaml_file(cache_filepath)
    return cachefile_content
