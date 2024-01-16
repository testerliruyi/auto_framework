"""
author: liRuYi
desc: 使用ffmpeg相关工具，获取视频编码格式，转换视频编码。
"""

import os, subprocess, re
from config.setting import ConfigInfo
from common.file_handle.get_file_list import get_files


class video_handle:
    def __init__(self, video_format: str = "h264"):
        self.add_path_command = ConfigInfo.ffmpeg_DIR
        os.environ['Path'] = self.add_path_command
        self.format = video_format

    @staticmethod
    def get_videos_format(path: str):
        """
        :param path:  video file path or  video directory
        :return:  None
        """
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

    def convert_video_format(self, file_path, output_file_dir):
        """
        :param file_path: 视频文件路径
        :param output_file_dir:  输出视频文件保存目录
        :return:
        """
        if os.path.isdir(file_path):
            files = get_files(file_path)
            count = 0
            print(">>>开始视频处理...")
            for file in files:
                file_basename = os.path.basename(file)
                output_file_name = file_basename.split('.')[0] + f'_{self.format}' + '.' + file_basename.split('.')[1]
                output_file_path = os.path.join(output_file_dir, output_file_name)
                ffmpeg_cmd = 'ffmpeg -i' + ' ' + file + ' ' + f'-vcodec {self.format}' + ' ' + str(output_file_path)
                result = subprocess.run(ffmpeg_cmd, capture_output=True, text=True, encoding='utf-8')
                # pattern = r"Video:[\s+]?\w+"
                # res = re.findall(pattern, str(result))
                count += 1
                print(f"{count}、", result)
        elif os.path.isfile(file_path):
            file_basename = os.path.basename(file_path)
            output_file_name = file_basename.split('.')[0] + f'_{self.format}' + '.' + file_basename.split('.')[1]
            output_file_path = os.path.join(output_file_dir, output_file_name)
            ffmpeg_cmd = 'ffmpeg -i' + ' ' + file_path + f'-vcodec {self.format}' + ' ' + str(output_file_path)
            result = subprocess.run(ffmpeg_cmd, capture_output=True, text=True, encoding='utf-8')
            print(result)

        else:
            raise f"{file_path}:无效路径,请确认"


if __name__ == "__main__":
    video_handle().convert_video_format(r"E:\视频目录\convert", "E:\视频目录\output")
