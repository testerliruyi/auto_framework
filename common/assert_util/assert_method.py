"""
assert 枚举类
"""

from enum import Enum, unique


@unique
class AssertMethod(Enum):
    # 等于
    equals = "=="

    # 大于
    less_than = "lt"

    # 小于等于
    less_than_or_equals = "le"

    # 大于
    greater_than = "gt"

    # 大于等于
    greater_than_or_equals = "ge"

    # 不等于
    not_equals = "not_eq"

    # 包含
    contains = "contains"



