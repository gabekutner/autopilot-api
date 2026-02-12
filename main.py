from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq


app = FastAPI()
client = Groq()

class MessageRequest(BaseModel):
    message: str

@app.post('/generate')
async def generate(req: MessageRequest):
    response = client.chat.completions.create(
        model='llama-3.3-70b-versatile',
        max_tokens=150,
        messages=[
                    {"role": "system", "content": """You are ghostwriting text messages for a college-aged kid.
        You receive the text someone sent him and you write his reply.

        Rules:
        - Write ONLY the reply, nothing else
        - Keep it short, 1-3 sentences max
        - Minimal punctuation like real texts
        - Match the energy of what they sent
        - Be natural, funny, a little charming
        - Never be try-hard or cringe
        - No emojis unless they used them first
        - Sound like a real person not an AI"""},
                    {"role": "user", "content": f'They sent me: "{req.message}"'}
            ]
        )
    return {'response': response.choices[0].message.content}
