from fastapi import FastAPI,HTTPException
app = FastAPI()

student_db = []

class FarmerNotFound(Exception):
    def __init__(self, farmer_id: int):
        self.farmer_id = farmer_id
        super().__init__(f"Farmer id with {self.farmer_id} not found")
@app.get("/student/{id}")
def student(id:int):
    if id not in student_db:
        raise HTTPException(status_code=404, detail="Student not found")
    return student_db[id]

