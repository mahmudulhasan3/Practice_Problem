import os
import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from pwdlib import PasswordHash

load_dotenv()
def get_required_env(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise ValueError("Not found")
    return value

SECRET_KEY = get_required_env("JWT_SECRET_KEY")

password_hash = PasswordHash.recommended()


def hash_password(plain_password: str) -> str:
    return password_hash.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(hashed_password, plain_password)


def create_access_token(username: str, role: str) -> str:
    payload = {
        "sub": username,
        "role": role,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
    }

    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def decode_access_token(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
