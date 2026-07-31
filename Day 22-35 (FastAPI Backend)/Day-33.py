# from pwdlib import PasswordHash
# import jwt
# from datetime import datetime,timedelta

# password_hash = PasswordHash.recommended()

# secret_key = "hasan"
# ALGORITHM = "HS256"


# def pass_hash(password:str) -> str:
#     return password_hash.hash(password)

# def pass_verify(password:str, hashed:str) -> bool:
#     return password_hash.verify(password,hashed)

# def create_token(data):
#     payload = data.copy()
#     payload["exp"] = datetime.utcnow() + timedelta(minutes=30)
#     token = jwt.encode(
#         payload,
#         secret_key,
#         algorithm= ALGORITHM
#     )
#     return token

# def verify_token(token):
#     payload = jwt.decode(
#         token,
#         secret_key,
#         algorithms=[ALGORITHM]
#     )
#     return payload


from jose import jwt 
from datetime import datetime,timedelta
from pwdlib import PasswordHash

SECRET_KEY = "mahmudulHasan"
ALGORITHM = "HS256"

password_hash = PasswordHash.recommended()
def password(password:str) -> str:
    return password_hash.hash(password)

def verify(password:str, hashed:str) -> bool:
    return password_hash.verify(password,hashed)

hashed = password("Mahmud")

print(verify("Mahmud",hashed))
