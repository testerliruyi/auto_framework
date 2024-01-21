import pathlib

def get_files(path) -> list or bool:
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
    pass
