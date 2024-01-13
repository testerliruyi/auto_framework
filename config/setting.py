import os
# 配置信息
class Setting:
    # 项目根本目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 视频存放路径
    videoPath = r"E:\视频目录\12.25压缩包"
    # 视频号url
    url = "https://channels.weixin.qq.com/login.html"

    # 循环次数
    loop_count = 5


if __name__ == "__main__":
    print(ConfigInfo.BASE_DIR)
