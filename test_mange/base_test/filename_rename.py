import os
from common.file_handle.get_file_list import get_files


def rename_file(path: str, suffix=None):
    getFiles = get_files(path)
    for file in getFiles:
        file = str(file)
        filename = file.split("\\")[-1]
        fileSuffix = filename.split('.')[-1]
        newFileName = file.replace('y2mate.com -', '')
        if fileSuffix == suffix:
            os.rename(file, newFileName)


if __name__ == "__main__":
    rename_file(r"D:\youtube下载视频\20231111",'mp4')
