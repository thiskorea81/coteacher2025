# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import tasks  # 라우터 임포트

app = FastAPI()

# DB 테이블 생성 (없으면 생성)
Base.metadata.create_all(bind=engine)

# CORS 설정
origins = [
    "http://localhost:5173",  # Vue 개발 서버
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(tasks.router, prefix="/api/tasks", tags=["Tasks"])

@app.get("/")
def root():
    return {"message": "Coteacher Backend Running with SQLite3"}
