# from fastapi import FastAPI, Depends

# app = FastAPI()


# def fake_db():
#     return {"conection": "active"}


# @app.get("/status")
# def get_db_session(status: dict = Depends(fake_db)):
#     return status

from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker, mapped_column, Mapped
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

DATABASE_URL = os.getenv("Database_URL")
if not DATABASE_URL:
    raise ValueError("URL not found")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind= engine)
class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key= True)
    title: Mapped[str] = mapped_column(String(100))
    author: Mapped[str] = mapped_column(String(100))

Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/books")
def book(db= Depends(get_db)):
    books = db.query(Book).all()
    return books