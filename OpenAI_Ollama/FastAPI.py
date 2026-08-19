from fastapi import FastAPI

app = FastAPI()

book1 = {
    "id": 9,
    "title": "ICT",
     "author": "Mahmud"
}

book2 = {
    "id": 4,
    "title": "Bangla",
    "author": "Hasan"
}

book_list = [book1,book2]
@app.get("/books")
def book():
    return book_list
