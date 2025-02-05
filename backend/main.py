from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "교사 도우미 앱 백엔드 실행 중임"}
