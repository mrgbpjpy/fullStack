from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.exc import OperationalError
import time

from database import Base, engine, SessionLocal
from models import Message as MessageModel

# Pydantic schema
class Message(BaseModel):
    content: str

# Initialize FastAPI app
app = FastAPI()

# CORS config for React/Vite dev server
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

# Ensure DB is ready before continuing
retries = 10
for i in range(retries):
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Database connected and tables created.")
        break
    except OperationalError as e:
        print(f"❌ DB not ready (attempt {i + 1}/{retries}): {e}")
        time.sleep(2)
else:
    raise RuntimeError("🚨 Could not connect to the database after multiple attempts.")

@app.get("/")
def root():
    return {"message": "API running"}

@app.post("/messages")
async def post_message(msg: Message):
    db = SessionLocal()
    new_msg = MessageModel(content=msg.content)
    db.add(new_msg)
    db.commit()
    db.refresh(new_msg)
    db.close()
    return {"status": "Message saved", "id": new_msg.id}

@app.get("/messages")
async def get_messages():
    db = SessionLocal()
    messages = db.query(MessageModel).all()
    db.close()
    return {"messages": [m.content for m in messages]}
