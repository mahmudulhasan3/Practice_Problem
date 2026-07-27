# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/student/{student_id}")
# def student(student_id: int):
#     return {"student_id": student_id}


# @app.get("/student")
# def student(limit: int = 10, active: bool= True):
#     return {"limit": limit, "active": active}

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/products/{product_id}")
# def product(product_id: int):
#     return {"product_id": product_id, "message": f"Product detail for id {product_id}"}


# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/search")
# def search(keyword: str, limit: int = 5):
#     return {"keyword": keyword, "limit": limit}


# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/courses/{course_id}/students")
# def course(course_id: int, min_marks: int = 0, sort_desc: bool = False):
#     return {"course_id": course_id, "min_marks": min_marks, "sort_desc": sort_desc}


# Mini-Project: Farmer Advisory Search API

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/crops/search")
def search(keyword: str, min_yeild: int = 0, page: int = 1, limit: int = 10):
    return {"keyword": keyword, "min_yeild": min_yeild, "page": page, "limit": limit}


@app.get("/crops/{crop_id}")
def crop(crop_id: int):
    return {"crop_id": crop_id, "message": f"Advisory for crop {crop_id}"}


@app.get("/crops/{crop_id}/advisory")
def advisory(
    crop_id: int, season: str = "current", language: str = "bn", detailed: bool = False
):
    if detailed == False:
        return {
            "crop_id": crop_id,
            "season": season,
            "language": language,
            "detailed": detailed,
        }
    elif detailed == True:
        return {
            "crop_id": crop_id,
            "season": season,
            "language": language,
            "detailed": detailed,
            "note": "Full details included",
        }
