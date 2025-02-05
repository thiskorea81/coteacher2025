from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="교사 도우미 앱 백엔드")

# 프론트엔드와의 CORS 설정 (필요에 따라 수정)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "교사 도우미 앱 백엔드 실행 중임"}
