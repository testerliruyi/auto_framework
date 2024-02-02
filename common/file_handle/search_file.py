"""
func:获取目录下相应的文件，并返回路径
"""

import os


def search_file(path, filename=None) -> list or str:
    file_path = []
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path, topdown=True):
            # print(files)
            if filename:
                if filename in files:
                    return os.path.abspath(os.path.join(root, filename))
                else:
                    for next_dir in dirs:
                        dir_path = os.path.join(path, next_dir)
                        search_file(dir_path, filename)
            else:
                for file in files:
                    path = os.path.abspath(os.path.join(root, file))
                    file_path.append(path)
        return file_path


if __name__ == "__main__":
    from config.setting import ConfigInfo
    print(ConfigInfo.TEST_CASE_FILE)
    print(search_file(ConfigInfo.TEST_CASE_FILE))