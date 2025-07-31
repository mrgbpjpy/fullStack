from sqlalchemy import Column, Integer, String
from database import Base  # ⬅ CHANGE THIS LINE

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
