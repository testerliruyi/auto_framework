"""
@author: LiRuYi
@func:  router
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Union, Any
from module.common_api import CommonFunctionApi
from common.log.set_logger import file_logger_obj
import json

api_router = APIRouter(
    prefix="/test",
    tags=['test_api'],
    responses={404: {"description": "Not Found"}}
)


class CaseCommon(BaseModel):
    allureStory: str


class Data(BaseModel):
    key: str
    city: str


# 定义请求体模型
class Item(BaseModel):
    case_common: Union[CaseCommon]
    case_title: str
    request_url: str
    method: str
    url_ext: Union[str, None] = None
    test_data: str
    depend_case: Union[str, None] = None
    headers: Any
    data: Union[Data]
    Assert: Any
    caseFileName: str


# 定义响应模型
class response_model(BaseModel):
    response: dict
    assert_result: dict


@api_router.post('/api', response_model=response_model)
async def create_request(item: Item):
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    # 请求体转为dict,方便其他函数使用.
    item_dict = item.model_dump()
    request_func = CommonFunctionApi(item_dict)
    # 进行接口请求
    response_result = request_func.api_reqeust()
    # 使用参数进行请求并进行断言操作
    assert_result = request_func.api_assert(response_result)
    final_dict = {"response": response_result, "assert_result": assert_result}
    return final_dict


if __name__ == "__main__":
    import sys

    print(sys.path)
