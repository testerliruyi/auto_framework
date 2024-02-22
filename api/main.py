import uvicorn
from fastapi import FastAPI
from api.router import execute_api


app = FastAPI()

app.include_router(execute_api.api_router)


@app.get('/')
async def root():
    return {"message": "welcome my api test framework"}


if __name__ == "__main__":
    # command = "uvicorn api.main:app  --reload"
    # subprocess.run(command)
    uvicorn.run(app, host='127.0.0.1', port=8000,)
