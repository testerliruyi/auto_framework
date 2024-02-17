"""
func: 用于yaml案例中，对指定依赖案例的参数进行替换。
"""

import re
from common.json_find import json_get_value


def special_template_init(pattern, content: str, response: dict):
    """
    :param pattern:  正则表达式匹配规则
    :param content: 需要处理的json报文体，字符串格式。
    :param response: 用于替换content中符合pattern的字段内容。
    :return: 参数后处理后的报文内容
    """
    patt = re.compile(pattern)
    # 按正则素达式匹配的字段
    template_key = re.findall(patt, content)
    if template_key:
        if pattern == r'\${DepRep\((\w+)\)}':
            for key in template_key:
                if json_get_value(response, key):
                    try:
                        content = content.replace("${DepRep(%s)}" % key,
                                                  str(json_get_value(response, key)))
                    except Exception as err:
                        raise KeyError(f'{key}未拽索到，请排查下')
                else:
                    pass
        elif pattern == r'\${DepReq\((\w+)\)}':
            for key in template_key:
                if json_get_value(response, key):
                    try:
                        content = content.replace("${DepReq(%s)}" % key,
                                                  str(json_get_value(response, key)))
                    except Exception as err:
                        raise KeyError(f'{key}未拽索到，请排查下')
                else:
                    pass


if __name__ == "__main__":
    pass
