"""
@author Liruyi
func: 自动生成自动化测试中的test_case代码！
"""

import os
from common.case_auto_generate.case_template import write_testcase_file
from config.setting import ConfigInfo
from common.file_handle import read_file, search_file


class TestCaseAutomaticGeneration:
    @classmethod
    def case_file_path(cls) -> str:
        """
       :return: 返回yaml测试案例文件路径
       """
        return ConfigInfo.TEST_CASE_FILE

    @classmethod
    def case_path(cls) -> str:
        """
        :return: 返回py案例文件路径
        """
        return ConfigInfo.TEST_CASE_PATH

    def file_name(self, file_path: str) -> str:
        """
        通过yaml文件名称：将名称转换为py文件名称
        param file_path :yaml 文件路径
        :return 示例：DateDemo.py
        """
        length = len(self.case_file_path())
        yaml_path = file_path[length:]
        file_name = None
        if '.yaml' in yaml_path:
            file_name = yaml_path.replace('.yaml', '.Py')
        elif '.yml' in yaml_path:
            file_name = yaml_path.replace('.yml', "-py")
        return file_name

    def get_case_path(self, file_path: str) -> tuple:
        """
        根据yaml中的用例，生成对位testCase层代码路径
        :param file_path: yaml用例路径
        :return:
        """
        # 通过'\\‘符号进行分隔，提取出来文件名称
        path = self.file_name(file_path).split(ConfigInfo.os_sep)
        # 判断生成的testCase文件名称，需要以test开头
        case_name = path[-1] = path[-1].replace(path[-1], 'test_' + path[-1])
        new_case_name = ConfigInfo.os_sep.join(path)
        return ConfigInfo.TEST_CASE_PATH + new_case_name, case_name,

    def get_test_class_title(self, file_path: str) -> str:
        """
        func: 自动生成类名称
        :param file_path: py 案例路径
        :return: sup
        """
        file_name = os.path.split(self.file_name(file_path))[1][:-3]
        name = file_name.split('_')
        for i in range(len(name)):
            name[i] = name[i].capitalize()
            _class_name = ''.join(name)
        return _class_name

    @classmethod
    def error_message(cls, param_name, file_path):
        """
        func:  用例中填写不正确的相关提示
        :param param_name:
        :param file_path:
        :return:
        """
        msg = f"""用例中未找到{param_name}参数值，请检查新增的用例中是否填写对应的参数内容,如已填写，可能是yaml参数缩进不正确\n
            用例路径：{file_path}"""
        return msg

    def func_title(self, file_path) -> str:
        """
        :param file_path:
        :return:
        """
        _file_name = os.path.split(self.file_name(file_path))[1][:-3]
        return _file_name

    @classmethod
    def allure_story(cls, case_data: dict, file_path) -> str:
        """
        func: 用于allure报告装饰器中的内容 @ allure.story(“测试功能”)
        :param case_data:
        :param file_path:
        :return:
        """
        try:
            return case_data['case_common']['allureStory']
        except KeyError:
            raise KeyError(cls.error_message(
                param_name="allureStory",
                file_path=file_path))

    def mk_dir(self, file_path: str) -> None:
        """
        func: 判断生成自动化代码的文件夹路径是否存在，加果不存在，则自动创建
        :param file_path:
        :return:
        """
        # _LibDirPath = os.path.split(self.libPagePath(filePath))[0]
        _CaseDirPath = os.path.split(self.get_case_path(file_path)[0])[0]
        if not os.path.exists(_CaseDirPath):
            os.makedirs(_CaseDirPath)

    def yaml_path(self, file_path: str) -> str:
        """
        func:生成动态yaml路径，主要处理业务分层场景
        :param file_path:   如业务有多个层级，则获取到每一层 / test_demo / DateDemo.py
        :return:
        """
        i = len(self.case_file_path())
        # 景容linux和 window 操作路径
        yaml_path = file_path[i:].replace("\\", "/")
        return yaml_path

    def get_case_automatic(self):
        """
        自动生成测试代码
        :return:
        """
        file_path = search_file.search_file(path=self.case_file_path())
        for file in file_path:
            # 获取yaml文件名为
            yaml_file_name = os.path.split(file)[-1]
            # 判断文件名等于”case_template.yaml时则略过。case_template.yaml文件为案例模板文件
            if yaml_file_name == 'case_template.yaml':
                pass
            else:
                # 判断用例需要用的文件夹路径是否存在，不存在则创建
                self.mk_dir(file)
                yaml_case_info = read_file.ReadFile.read_yaml_file(file)
                write_testcase_file(allure_story=self.allure_story(case_data=yaml_case_info[0], file_path=file),
                                    class_tile=self.get_test_class_title(file),
                                    func_title=self.func_title(file),
                                    case_path=self.get_case_path(file)[0],
                                    file_name=self.get_case_path(file)[1],
                                    yaml_file_name=yaml_file_name)
        print("Done，自动生成接口测试案例执行完成^_^")


if "__name__" == '_main_':
    TestCaseAutomaticGeneration().get_case_automatic()
