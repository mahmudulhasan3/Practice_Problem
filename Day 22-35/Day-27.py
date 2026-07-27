from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    id: int
    name: str
    age: int
    marks: float


students_db = []


@app.post("/students")
def student(student: Student):
    for i in students_db:
        if i.id == student.id:
            raise ValueError("Student id is exist in database")
    students_db.append(student)
    return {
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "marks": student.marks,
    }


@app.get("/students")
def show_student():
    return students_db


@app.get("/students/{id}")
def get_student(id: int):
    for i in students_db:
        if id == i.id:
            return i


@app.put("/students/{id}")
def update_data(id: int, updated: Student):
    for index, i in enumerate(students_db):
        if i.id == id:
            students_db[index] = updated
            return updated
    return f"Error: student id not found"


@app.delete("/students/{id}")
def delete_data(id: int):
    for index, i in enumerate(students_db):
        if i.id == id:
            students_db.pop(index)
            return f"Student deleted"
    return "error, student not found"
