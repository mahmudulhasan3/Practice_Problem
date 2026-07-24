# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()

# class Student(BaseModel):
#     name: str
#     age: int
#     marks: float

# students_db = []

# @app.post("/student")
# def create_student(student:Student):
#     students_db.append(student)
#     return {
#         "message": f"{student.name} added successfully"
#     }
# @app.get("/students")
# def get_student():
#     return {
#         "messange": students_db
#     }

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
book_list = []


class Book(BaseModel):
    title: str
    author: str
    price: float
    in_stock: bool


@app.post("/book",status_code=201)
def books(book: Book):
    book_list.append(book)
    return {"message": f"{book.title} added successfully"}


@app.get("/book")
def book():
    return book_list
