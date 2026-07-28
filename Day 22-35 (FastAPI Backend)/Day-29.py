from fastapi import FastAPI
from Day27 import router

app = FastAPI()
app.include_router(router)