# from argon2 import PasswordHasher
# from argon2.exceptions import VerifyMismatchError

# ph = PasswordHasher()

# def hash_password(password:str) -> str:
#     hashed = ph.hash(password)
#     return hashed
# def verify_password(password: str, hashed_password: str) -> bool:
#     try:
#         verify = ph.verify(hashed_password,password)
#         return True
#     except VerifyMismatchError:
#         return False
# password = hash_password("mahmud")
# print(verify_password("mahmud",password))

# from fastapi import FastAPI,HTTPException
# from sqlalchemy import create_engine,String
# from sqlalchemy.orm import DeclarativeBase,mapped_column, Mapped,sessionmaker
# import os
# from dotenv import load_dotenv
# app = FastAPI()
# load_dotenv()
# Database_URL = os.getenv("Databse_URL")
# if  not Database_URL:
#     raise ValueError("Database url not found")
# engine = create_engine(Database_URL)
# SessionLocal = sessionmaker(bind= engine)

