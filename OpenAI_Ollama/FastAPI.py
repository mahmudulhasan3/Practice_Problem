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

