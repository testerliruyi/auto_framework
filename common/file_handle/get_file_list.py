import pathlib
from config.configInfo import ConfigInfo


def get_files(path=None) -> list or bool:
    if path is None:
        path = ConfigInfo.videoPath

    if pathlib.Path(path).exists():
        pathinfo = pathlib.Path(path).iterdir()
        paths = list(pathinfo)
        if paths == []:
            return False
        else:
            return paths
    else:
        Exception("路径不存在")


if __name__ == '__main__':
    for i in get_files(ConfigInfo.videoPath):
        print(i)
