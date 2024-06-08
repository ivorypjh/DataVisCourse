from fastapi import FastAPI

# CORS 설정을 위함
from fastapi.middleware.cors import CORSMiddleware

# 라우터 추가
from todo import todo_router

# 허용할 URL을 list를 사용해서 작성
# 현재는 localhost만 사용
origins = [
    "http://localhost:8000",
]

app = FastAPI()
# 기본 요청이 오면 아래 함수를 수행해서 결과를 리턴
@app.get("/")
async def welcome() -> dict:
    return {
        "message": "start page"
}

# app이 처리하기 전에 미들웨어에 CORS 사용 여부를 설정
app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

app.include_router(todo_router)