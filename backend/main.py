# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# 라우터 import
from routers import schedules
from routers import tasks
# ... 필요하다면 계속 import

load_dotenv()

app = FastAPI()

# CORS 설정
origins = [
    "http://localhost:8080",  # Vue.js dev server
    # 필요한 도메인 추가
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(schedules.router, prefix="/api/schedules", tags=["Schedules"])
app.include_router(tasks.router, prefix="/api/tasks", tags=["Tasks"])
# ...

@app.get("/")
def root():
    return {"message": "Coteacher Backend Running"}

# uvicorn 실행시
# uvicorn main:app --reload --host 0.0.0.0 --port 8000
