"""
@author: LiRuYi
@func:  router
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Union, Any
from api.module.common_api import CommonFunctionApi

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


class Item(BaseModel):
    case_common: Union[CaseCommon]
    case_title: str
    method: str
    url_ext: Union[str, None] = None
    test_data: str
    depend_case: Union[str, None] = None
    headers: Any
    data: Union[Data]
    Assert: Any


@api_router.post('/api')
async def api_test(item: Item):
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    # 使用参数进行请求并进行断言操作
    result = CommonFunctionApi(item).api_test_func()
    return result


if __name__ == "__main__":
    import sys
    print(sys.path)