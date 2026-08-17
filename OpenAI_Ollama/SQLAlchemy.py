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


# from sqlalchemy import create_engine, String,select
# from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase,sessionmaker

# engine = create_engine("postgresql://mahmud:CS2203009@localhost:5432/practice_db")

# SessionLocal = sessionmaker(bind= engine)

# class Base(DeclarativeBase):
#     pass

# class User(Base):
#     __tablename__ = "users"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(100))
#     email: Mapped[str] = mapped_column(String(100), unique= True)

# Base.metadata.create_all(engine)

# print("Table create successfully")
# with SessionLocal() as session:
#     new_user = User(name = "drrrddd", email= "hdh4ed444h@gmail.com")
#     session.add(new_user)
#     print("Data insert successfully")

#     stmt = select(User).where(User.id == 1)
#     result = session.execute(stmt).scalars().all()
#     for u in result:
#         print(u.id,u.name, u.email)
#     user = session.get(User,1)
#     if user:
#         user.name = "Mahmud"
#         session.commit()
#         print("update done")
#     user = session.get(User,1)
#     if user:
#         session.delete(user)
#         session.commit()
#         print("Delete done")
#     user = session.get(User,2)
#     if user:
#         print(user.name, user.email)
#     else:
#         print("User not found")

#     session.commit()


# from sqlalchemy import create_engine, String,Integer,select
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

# engine = create_engine("postgresql://mahmud:CS2203009@localhost:5432/practice_db")
# SessionLocal = sessionmaker(bind= engine)

# class Base(DeclarativeBase):
#     pass

# class Book(Base):
#     __tablename__ = "book"
#     id: Mapped[int] = mapped_column(primary_key= True)
#     title: Mapped[str] = mapped_column(String(100))
#     author: Mapped[str] = mapped_column(String(100))
#     price: Mapped[int] = mapped_column(Integer)

# Base.metadata.create_all(engine)
# print("Table created successfully")

# with SessionLocal() as session:
#     book_1 = Book(title="Atomic Habits", author="James Clear", price=450)
#     book_2 = Book(title= "The Alchemist", author= "Paulo Coelho", price= 380)
#     book_3 = Book(title= "Deep Work", author= "Cal Newport", price= 620)

#     session.add(book_1)
#     session.add(book_2)
#     session.add(book_3)
#     print("Book insert successfully")
#     session.commit()

#     book = session.get(Book,1)
#     if book:
#         print("Book list-")
#         print(book.id,book.title, book.author, book.price)

#     stmt = select(Book).where(Book.price > 500)
#     result = session.execute(stmt).scalars().all()

#     for book in result:
#         print(book.id, book.title, book.author, book.price)
#     book = session.get(Book,3)
#     if book:
#         book.price = 3455
#         session.commit()
#         print("Book updated")
#     else:
#         print("Book not found")
#     book = session.get(Book,3)
#     if book:
#         print("Book list-")
#         print(book.id,book.title, book.author, book.price)

#     book = session.get(Book,2)
#     if book:
#         session.delete(book)
#         session.commit()
#         print("Book deleted successfully")
#     else:
#         print("Book not found")

#     book = session.get(Book,2)
#     if book:
#         print(book.id)
#     else:
#         print("Book not found")


from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, relationship

engine = create_engine("postgresql://mahmud:CS2203009@localhost:5432/practice_db")

SessionLocal = sessionmaker()

class Base(DeclarativeBase):
    pass

class Department(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    students: Mapped[list["Student"]] = relationship(back_populates= "department")

class Student(Base):
    __tablename__ = "student"
    id: Mapped[int] = mapped_column(primary_key= True)
    name: Mapped[int] = mapped_column(String(100))
    department_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    department: Mapped["Department"] = relationship(back_populates= "student")

