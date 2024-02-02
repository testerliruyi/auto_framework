"""
func: json 字符串格式化展示
"""

import json

def json_formatter(json_str: str):
    res = json.dumps(json_str, sort_keys=True, indent=4,ensure_ascii=False)
    return  res