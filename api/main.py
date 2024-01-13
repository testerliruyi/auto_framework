from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from enum import Enum


class ModelName(str,Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
app = FastAPI()


@app.get('/')
async def root():
    return {"message": "hello world"}

@app.get('/models/{model_name}')
async def get_model(model_name:ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name":model_name,"message":"deep"}



@app.get("/item/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
