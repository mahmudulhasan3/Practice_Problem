from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import Base, get_db, engine
from models import User
from schemes import RegisterUser, UserLogIn, UserResponse
from auth import password_hash, verify_password

app = FastAPI()
Base.metadata.create_all(engine)


@app.post("/register", response_model=UserResponse)
def register(user: RegisterUser, db: Session = Depends(get_db)):
    existing_user = (
        db.query(User)
        .filter((User.username == user.username) | (User.email == user.email))
        .first()
    )
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    hashed = password_hash(user.password)

    new_user = User(username=user.username, email=user.email, hashed_password=hashed)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.post("/login")
def login(user: UserLogIn, db: Session = Depends(get_db)):
    db_user = db.query(User).filter((User.username == user.username)).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    verify = verify_password(user.password, db_user.hashed_password)
    if not verify:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login Successfull"}