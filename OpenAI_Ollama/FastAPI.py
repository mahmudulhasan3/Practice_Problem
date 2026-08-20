# from fastapi import FastAPI,HTTPException

# app = FastAPI()

# book1 = {
#     "id": 9,
#     "title": "ICT",
#      "author": "Mahmud"
# }

# book2 = {
#     "id": 4,
#     "title": "Bangla",
#     "author": "Hasan"
# }

# book_list = [book1,book2]
# @app.get("/books")
# def book():
#     return book_list

# @app.get("/books/{book_id}")
# def second(book_id:int):
#     if book_id <= 0:
#         raise HTTPException(status_code=400, detail="Invalid student id")
#     for i in book_list:
#         if book_id == i["id"]:
#             return i
#     else:
#         raise HTTPException(status_code=404, detail="Something is wrong")

# students = [
#     {"id": 1, "name": "Rafi", "class": "10"},
#     {"id": 2, "name": "Tania", "class": "9"},
# ]

# @app.get("/students/{student_id}")
# def student(student_id: int):
#     for student in students:
#         if student["id"] == student_id:
#             return student
#     else:
#         raise HTTPException(status_code= 404, detail= "Student not found")

# @app.get("/students/search")
# def search(class_name:str = None):
#     result = []
#     if class_name:
#         for s in students:
#             if s["class"] == class_name:
#                 result.append(s)
#         return result
#     return students

# from fastapi import FastAPI,HTTPException
# from pydantic import BaseModel
# from typing import Optional

# app = FastAPI()

# class Student(BaseModel):
#     name: str
#     age: int
#     email: Optional[str] = None
#     cgpa: float


# @app.post("/student")
# async def student(s:Student):
#     return{
#         "name": s.name
#     }

from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Any, Optional

app = FastAPI()

class BookCreate(BaseModel):
    title: str 
    author: str
    price: float

@app.post("/books")
async def book(book: BookCreate):
    return{
        "title": book.title,
        "author": book.author,
        "price": book.price
    }

class UserCreate(BaseModel):
    username: str = Field(min_length= 3)
    age: int = Field(ge= 18)
    bio: Optional[str] = None


class UserResponse(BaseModel):
    username: str = Field(min_length= 3)
    age: int = Field(ge= 18)

@app.post("/users", response_model=UserResponse)
async def users(user:UserCreate):
    return{
        "username": user.username,
        "age": user.age
    }