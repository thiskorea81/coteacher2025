# backend/database.py

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DB_URL = os.getenv("DB_URL", "sqlite:///./default.db")  
# .env에 DB_URL이 없을 시 "default.db" 사용

engine = create_engine(
    DB_URL,
    echo=True,          # 쿼리 등을 콘솔에 출력 (디버그용)
    connect_args={"check_same_thread": False}  
    # SQLite 특성상, 단일 스레드만 접근 허용. FastAPI 개발용엔 이 설정이 필요
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()  # 모든 SQLAlchemy 모델들의 베이스 클래스
