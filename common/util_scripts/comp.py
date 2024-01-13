'''
func:用于对比元组或列表之间的差异,或获取两个列表之前共同的部分。
author:李如意
date:2023/10/09
'''
#获取两个列表差异的字段
def comp(baseData:list or tuple,diffData:list or tuple):
    '''
    :param baseDate:  基准数据
    :param diffData: 用于和基准数据进行对比的列表。
    :return: 返回列表
    '''
    result=[x for x in baseData if x not in diffData]
    return result

#获取两个列表共同的字段。
def both(baseData:list or tuple,diffData:list or tuple):
    '''
    :param baseData: 基准数据
    :param diffData: 用于对比数据
    :return: 返回列表
    '''
    result=list(set(baseData).intersection(diffData))
    return result
