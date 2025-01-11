from fastapi import APIRouter
import os
import openai
from dotenv import load_dotenv

router = APIRouter()

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@router.post("/generate")
async def generate_text(prompt: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[ 
                {"role": "system", "content": "시스템 메시지들..."},
                {"role": "user", "content": prompt}
            ]
        )
        return {"response": response.choices[0].message["content"]}
    except Exception as e:
        return {"error": str(e)}
