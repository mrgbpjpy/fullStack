# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data schema
class Message(BaseModel):
    content: str

# In-memory "DB"
messages = ["Hello from FastAPI!"]

@app.get("/messages")
def get_messages():
    return {"messages": messages}

@app.post("/messages")
def post_message(msg: Message):
    messages.append(msg.content)
    return {"message": "Message received!"}
