# 这是一个示例 Python 脚本。

# 自动生成py 测试案例。
# 根据 配置文件中【real_time_update_test_cases】 字段值，判断是否全量重新生成，或仅处理未生成py测试案例文件。
from config.setting import ConfigInfo
from common.case_auto_generate.case_automatic_control import TestCaseAutomaticGeneration
import uvicorn
from uvicorn.config import LOGGING_CONFIG
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from router import execute_api

LOGGING_CONFIG["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelprefix)s %(message)s"

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body})
    )


# 添加路由到app中
app.include_router(execute_api.api_router)


@app.get('/')
async def root():
    return {"message": "welcome my api test framework"}


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # 自动生成py测试案例执行脚本
    # TestCaseAutomaticGeneration().get_case_automatic()
    # uvicorn.run(app="main:app", host='127.0.0.1', port=8001, reload=True, log_level="debug")
    import sys
    print(sys.path)
