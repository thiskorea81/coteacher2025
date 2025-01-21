from fastapi import APIRouter
from openai import OpenAI

router = APIRouter()

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

@router.post("/generate_gemini")
async def generate_text(prompt: str):
    response = client.chat.completions.create(
        model="gemini-2.0-flash-exp",
        n=1,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Explain to me how AI works"
            }
        ]
    )

    return {"response": response.choices[0].message}