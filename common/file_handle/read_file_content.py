import os.path
import yaml
from config.setting import ConfigInfo
# 读取yaml文件内容
def get_yaml_file_content(file_path=None) -> list:
    if file_path is None:
        file_path = os.path.join(ConfigInfo.BASE_DIR,'config','describe.yaml')
    with open(file_path,'r',encoding='utf-8') as f:
        content = yaml.safe_load(f)

    return content






if __name__=="__main__":


    print(get_yaml_file_content())