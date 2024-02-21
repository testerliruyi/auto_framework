from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Any, Union, Optional


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


app = FastAPI()


@app.post("/api_test/")
async def api_test(item: Item):
    print(item)
    return item
