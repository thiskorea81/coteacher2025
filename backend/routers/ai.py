from fastapi import APIRouter
from openai import OpenAI

router = APIRouter()

client = OpenAI()

@router.post("/generate")
async def generate_text(prompt: str):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "시스템 메시지들 ..."},
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )

    return {"reponse": completion.choices[0].message}