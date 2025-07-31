# backend/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# This matches the docker-compose.yml DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:secret@db:5432/fastapi_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
