"""
author: liRuYi
desc: 使用ffmpeg 获取使用编码格式。
"""

import os, subprocess, re
from config.setting import ConfigInfo
from common.file_handle.get_file_list import get_files


def get_videos_info(path: str):
    """
    :param path:  video file path or  video directory
    :return:  None
    """
    add_path_command = ConfigInfo.ffmpeg_DIR
    os.environ['Path'] = add_path_command
    if os.path.isdir(path):
        files = get_files(path)
        count = 0
        for file in files:
            ffprobe_cmd = 'ffprobe -i' + ' ' + file
            result = subprocess.run(ffprobe_cmd, capture_output=True, text=True, encoding='utf-8')
            pattern = r"Video:[\s+]?\w+"
            res = re.findall(pattern, str(result))
            count += 1
            print(f"{count}、this file【{file}】format is:", res)
    elif os.path.isfile(path):
        ffprobe_cmd = 'ffprobe -i' + ' ' + path
        result = subprocess.run(ffprobe_cmd, capture_output=True, text=True, encoding='utf-8')
        pattern = r"Video:[\s+]?\w+"
        res = re.findall(pattern, str(result))
        print(f"this file【{path}】format is:", res)
    else:
        raise f"{path}:无效路径,请确认"


if __name__ == "__main__":
    get_videos_info(r"E:\视频目录\convert")
