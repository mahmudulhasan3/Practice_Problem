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


from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

Database_URL = "postgresql://mahmud:CS2203009@localhost:5432/practice_db"

engine = create_engine(Database_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))


Base.metadata.create_all(engine)
print("✅ Connected & table ready")

with SessionLocal() as session:
    new_user = User(name="Mahmud", email="mahmud@example.com")
    session.add(new_user)
    session.commit()
print("✅ User created")
