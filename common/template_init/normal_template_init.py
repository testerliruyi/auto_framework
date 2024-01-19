"""
func:
对案例中的常用参数模板进行进行初始化操作
例：${sendNo}普换为真实流水号
"""
import json
from string import Template


def normal_Template_init(resource, variable: dict):
    # 字典格式时，最终返回字典
    if isinstance(resource, dict):
        Source = json.dumps(resource)
        result = Template(Source).safe_substitute(variable)
        result = json.loads(result)
    # 字符串格式时，返回字待串格式
    else:
        result = Template(resource).safe_substitute(variable)
    return result
