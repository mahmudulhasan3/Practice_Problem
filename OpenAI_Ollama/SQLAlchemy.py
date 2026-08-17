# from sqlalchemy import create_engine,String
# from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,sessionmaker

# engine = create_engine("postgresql://postgre:123456@localhost:5432/Practice_db")
# SessionLocal = sessionmaker(bind=engine)


# class Base(DeclarativeBase):
#     pass

# class User(Base):
#     __tablename__ = "users"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(100))

# Base.metadata.create_all(engine)
# new_user = User(id= 3, name= "Mahmud")
# with SessionLocal() as session:
#     session.add(new_user)
#     session.commit()


# from sqlalchemy import create_engine, String
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

# Database_URL = "postgresql://mahmud:CS2203009@localhost:5432/practice_db"

# engine = create_engine(Database_URL, echo=True)
# SessionLocal = sessionmaker(bind=engine)


# class Base(DeclarativeBase):
#     pass


# class User(Base):
#     __tablename__ = "users"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(100))
#     email: Mapped[str] = mapped_column(String(100))


# Base.metadata.create_all(engine)
# print("✅ Connected & table ready")

# with SessionLocal() as session:
#     new_user = User(name="Mahmud", email="mahmud@example.com")
#     session.add(new_user)
#     session.commit()
# print("✅ User created")

# from sqlalchemy import String,create_engine
# from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,sessionmaker
# engine = create_engine("postgresql://mahmud:CS2203009@localhost:5432/practice_db")

# SessionLocal = sessionmaker(bind=engine)

# class Base(DeclarativeBase):
#     pass

# class User(Base):
#     __tablename__ = "users"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(100))
#     email: Mapped[str] = mapped_column(String(100), unique= True)

# Base.metadata.create_all(engine)

# with SessionLocal() as session:
#     new_user = User(name = "Mahmud", email = "mhasns@gmail.com")
#     session.add(new_user)
#     session.commit()


from sqlalchemy import create_engine, String,select,delete
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase,sessionmaker

engine = create_engine("postgresql://mahmud:CS2203009@localhost:5432/practice_db")

SessionLocal = sessionmaker(bind= engine)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique= True)

Base.metadata.create_all(engine)

print("Table create successfully")
with SessionLocal() as session:
    new_user = User(name = "drrrddd", email= "hdh4ed444h@gmail.com")
    session.add(new_user)
    print("Data insert successfully")

    stmt = select(User).where(User.id == 1)
    result = session.execute(stmt).scalars().all()
    for u in result:
        print(u.id,u.name, u.email)
    user = session.get(User,1)
    if user:
        user.name = "Mahmud"
        session.commit()
        print("update done")
    user = session.get(User,1)
    if user:
        session.delete(user)
        session.commit()
        print("Delete done")
    user = session.get(User,2)
    if user:
        print(user.name, user.email)
    else:
        print("User not found")

    session.commit()
