from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

def password_hash(plain_password: str) -> str:
    hashed = ph.hash(plain_password)
    return hashed
def verify_password(password: str, hashed_password: str) -> bool:
    try:
        verify = ph.verify(hashed_password, password)
        return True
    except VerifyMismatchError:
        return False