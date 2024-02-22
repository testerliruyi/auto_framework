# """
# func: 初始化字符串中的模板内容
# """
# from common.file_handle.read_file import ReadFile
# from string import Template
# from common.params import Params
# from config import setting
#
#
# def string_init(datainfo: str or list, data_file_path:str,genFilePath=None):
#     """
#     :param datainfo:
#     :param dataFilePath:
#     :param genFilePath:
#     :return:
#     """
#     count=0
#     # 获取数据
#     content = ReadFile.read_excel(data_file_path)
#     if not genFilePath:
#         for data in content:
#             #公用参数生成
#             count += 1
#             params = Params.commonParam(count)
#             if type(initData) is list:
#             print(￡">>>>{count}、组装后的sq1语句为：“）
#             for key in initData:
#                 res = Template(key).safe_substitute(data)res = Template(res).safe_substitute(params)print(f"
#                 {res}")
#                 res = Template(initData).safe_substitute(data)
#                 res = Template(res).safe_substitute(params)
#                 print(￡">>>>{count}、组装后的sq1语句为”，res)
#     else: