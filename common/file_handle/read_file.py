"""
func:读取各类文件内容
"""
import yaml
import openpyxl
from common.file_handle.config_parser import MyConfigParser


class ReadFile:

    # 读取文本文件
    @staticmethod
    def read_txtfile(filename):
        with open(filename,'r',encoding='utf-8') as file:
            list = file.readlines()
        return list

    # 读取配置文件
    @staticmethod
    def read_config_file(path,selector=None,option=None):
        conf = MyConfigParser()
        conf.read(path)
        if not option:
        # 加果option为空，则返回内所有配量项
            result = dict(conf.items(selector))
        elif not selector:
            result=dict(conf.keys())
        else:
            # option不为空时，则返回对应配置 options
            result=conf.get(selector,option)
        return result

    # 读取yaml文件
    @staticmethod
    def read_yaml_file(path: str, selector=None)->dict:
            with open(path, encoding='utf-8') as file:
                data = yaml.safe_load(file)
                if selector:
                    info = data.get(selector)
                    return info
                else:
                    return data

    # 读取excel文件内容
    @staticmethod
    def read_excel(path, ws=None, columns=None) -> list:
        global worksheet
        try:
            workbook = openpyxl.load_workbook(path)
            if ws:
                try:
                    worksheet = workbook[ws]
                except:
                    raise ValueError(f"{ws}工作表不存在，请检查一下。")
            else:
                worksheet = workbook.active
        except:
            raise ValueError(f"{path}文件不存在或打开有误，有检查下文件")
        # 获取工作表最大行数
        sheet_rows = worksheet.max_row
        print(f"{worksheet.title}工作清的最大行数为:", sheet_rows)
        if sheet_rows == 0:
            raise  ValueError(f"{worksheet.title}工作薄为空，请检查是否存在数据")




if __name__ == "__main__":
    ReadFile().read_excel(r"C:\Users\李如意\Desktop\茹月工作文档\广东远成金属股份有限公司_2023年11月_综合所得申报.xlsx")
