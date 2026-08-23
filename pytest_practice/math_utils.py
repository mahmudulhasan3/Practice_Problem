from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    username: str
    password: str


# fake in-memory "database" — শুধু demo-এর জন্য
fake_db = {}


@app.post("/register")
def register(user: User):
    if user.username in fake_db:
        raise HTTPException(status_code=400, detail="User already exists")
    fake_db[user.username] = user.password
    return {"message": "User registered successfully"}


@app.post("/login")
def login(user: User):
    if user.username not in fake_db or fake_db[user.username] != user.password:
        raise HTTPException(
            status_code=403, detail="Invalid credentials"
        )  # ← 401 এর জায়গায় 403 করলাম
    return {"access_token": "fake-jwt-token", "token_type": "bearer"}


@app.get("/profile")
def profile(authorization: str = Header(None)):
    if authorization != "Bearer fake-jwt-token":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"username": "test_user"}
