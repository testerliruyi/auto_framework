"""
func:用于对比元组或列表之间的差异,或获取两个列表之前共同的部分。
author:李如意
date:2023/10/09
"""
from typing import Union


# 获取两个列表差异的字段
def comp(base_data: Union[list, tuple], diff_data: Union[list, tuple]):
    """
    :param base_data: 基准数据
    :param diff_data: 用于和基准数据进行对比的列表。
    :return: 返回列表
    """
    result = [x for x in base_data if x not in diff_data]
    return result


# 获取两个列表共同的字段。
def both(base_data: Union[list, tuple], diff_data: Union[list, tuple]):
    """
    :param base_data: 基准数据
    :param diff_data: 用于和基准数据进行对比的列表。
    :return: 返回列表
    """
    result = list(set(base_data).intersection(diff_data))
    return result
