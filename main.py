# 这是一个示例 Python 脚本。

# 自动生成py 测试案例。
# 根据 配置文件中【real_time_update_test_cases】 字段值，判断是否全量重新生成，或仅处理未生成py测试案例文件。
from config.setting import ConfigInfo
from common.case_auto_generate.case_automatic_control import TestCaseAutomaticGeneration


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    TestCaseAutomaticGeneration().get_case_automatic()


