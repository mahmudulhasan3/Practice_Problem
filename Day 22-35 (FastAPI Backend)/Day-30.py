# import os
# from fastapi import FastAPI,UploadFile,File,HTTPException
# app = FastAPI()

# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR,exist_ok=True)
# @app.post("/upload")
# async def upload_pdf(file:UploadFile = File(...)):
#     if file.content_type != "application/pdf":
#         raise HTTPException(status_code=400, detail="Only pdf file can allow")
#     content = await file.read()
#     file_path = os.path.join(UPLOAD_DIR, file.filename)
#     with open(file_path, "wb") as f:
#         f.write(content)


#     return {
#         "filename": file.filename,
#         "content_type": file.content_type,
#         "message": "File received"
#     }

# from fastapi import FastAPI,UploadFile,File

# app = FastAPI()
# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     content = await file.read()
#     text = content.decode("utf-8")
#     return {
#         "text": text
#     }
# import uuid
# import os
# from fastapi import FastAPI,UploadFile,File
# app = FastAPI()

# @app.post("/uploads")
# async def pdf_upload(file:UploadFile = File(...)):
#     extension = os.path.splitext(file.filename)[1]
#     path = os.path.join("uploads", f"{uuid.uuid4()}{extension}")
#     content = await file.read()
#     with open(path, "wb") as f:
#         f.write(content)

#     return{
#         "message": "File saved"
#     }


import os
import uuid
from fastapi import FastAPI,UploadFile,File,HTTPException

app = FastAPI()

@app.post("/upload")
async def file_upload(file:UploadFile = File(...)):
    extention = os.path.splitext(file.filename)[1]
    path = os.path.join("uploads",f"{uuid.uuid4()}{extention}")
    content = await file.read()

    with open(path, "wb") as f:
        f.write(content)
    return {
        "message": "File uploaded successfully",
        "original_filename": file.filename,
        "stored_filename": path,
    }
