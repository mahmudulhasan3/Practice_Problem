# from fastapi import FastAPI

# # app = FastAPI()
# # @app.get("/")
# # def home():
# #     return {"message": "Mahmud"}

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/greet/{name}")
# # def me():
# #     return {"message": "Welcome to my website", "name": "Mahmudul Hasan", "dept": "CSE"}


# def greet(name: str):
#     return {"message": f"My name is {name}"}


# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/square/{number}")
# def square(number: int):
#     return {
#         "Result": number**2
#         }

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/students")
# def student():
#     return [
#         {"name": "Rafi", "marks": 85},
#         {"name": "Sadia", "marks": 90},
#         {"name": "Mahmud", "marks": 78},
#     ]

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/add/{num1}/{num2}")
# def add(num1: int, num2: int):
#     return {"Sum": num1 + num2}

# from fastapi import FastAPI

# app = FastAPI()
# @app.get("/reverse/{word}")
# def reverse(word:str):
#    new = word[::-1]
#    return {"reverse": new}

# Boolean logic diye
# Ekta endpoint banao /is_even/{number} — number ta even naki odd check kore bolbe.

# /is_even/4  →  {"number": 4, "is_even": true}
# /is_even/7  →  {"number": 7, "is_even": false}

from fastapi import FastAPI

app = FastAPI()
@app.get("/is_even/{number}")
def even_odd(number:int):
    if number % 2 == 0:
        return {"number": number, "is_even" : True}
    else:
        return {"number": number, "is_even" : False}