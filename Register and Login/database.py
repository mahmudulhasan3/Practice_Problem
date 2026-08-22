from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
Database_URL = os.getenv("Database_URL")
if not Database_URL:
    raise ValueError("Database URL not found")
engine = create_engine(Database_URL)
SessionLocal = sessionmaker(bind= engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()