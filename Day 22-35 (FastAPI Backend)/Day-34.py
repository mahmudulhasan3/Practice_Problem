# from pwdlib import PasswordHash
# from jose import jwt
# from datetime import datetime,timedelta,timezone

# SECRET_KEY = "hdgttsgb321"
# ALGORITHM = "HS256"

# password_hash = PasswordHash.recommended()

# def create_token(data:dict, expires_minutes: int = 30) -> str:
#     payload = data.copy()


# def hash_password(password:str) -> str:
#     return password_hash.hash(password)

# def verify_password(password:str, hashed_password:str) -> bool:
#     return password_hash.verify(password,hashed_password)

# hashed = hash_password("Mahmud")
# print(verify_password("Mahmud",hashed))
# print(hashed)

from datetime import datetime, timedelta, timezone
from jose import jwt
from pwdlib import PasswordHash
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

class LogInRequest(BaseModel):
    email: str
    password: str

SECRET_KEY = "hdhuebs34dn"
ALGORITHM = "HS256"

password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)

fake_users_db = {
    "farmer1": {
        "username": "farmer1",
        "hashed_password": hash_password("mypassword123"),
    }
}

def create_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode["exp"] = expire

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

@app.post("/hashing")
def login(request: LogInRequest):
    if request.email not in fake_users_db:
        raise HTTPException(status_code=401, detail="User not found")

    user = fake_users_db[request.email]
    verify = verify_password(request.password, user["hashed_password"])
    if not verify:
        raise HTTPException(status_code=401, detail="Password not match")
    token = create_token({"sub": request.email})
    return {"access_toke": token, "token_type": "brearer"}
