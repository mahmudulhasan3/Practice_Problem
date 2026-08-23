# from fastapi import FastAPI, Request

# app = FastAPI()

# @app.middleware("http")
# async def my_middleware(request: Request, call_next):
#     print("before")
#     response = await call_next(request)
#     print("after")
#     return response

# from fastapi import FastAPI, Request

# app = FastAPI()

# @app.middleware("http")
# async def my_middleware(request: Request, call_next):
#     print(request.path_params)
#     response = await call_next(request)
#     print("After")
#     response.headers["X-App-Name"] = "MyAPI"
#     return response

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers= ["*"]
)
