from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# In-memory store (for demo only)
messages = []

class Message(BaseModel):
    content: str

app = FastAPI()

# CORS for React/Vite
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API running"}

@app.post("/messages")
async def post_message(msg: Message):
    messages.append(msg.content)
    return {"status": "Message received"}

# ✅ THIS IS WHAT YOU'RE MISSING
@app.get("/messages")
async def get_messages():
    return {"messages": messages}
