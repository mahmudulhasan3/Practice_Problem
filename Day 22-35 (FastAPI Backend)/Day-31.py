# from fastapi import FastAPI,BackgroundTasks
# import time

# app = FastAPI()

# def process(filename:str):
#     print("Processing")
#     time.sleep(5)
#     print("Precessing end")

# @app.post("/upload")
# def file_upload(filename:str, back:BackgroundTasks):
#     back.add_task(process, filename)
#     return{
#         "message": "file uploaded"
#     }

# from fastapi import FastAPI,UploadFile,File,BackgroundTasks
# import time, os

# app = FastAPI()

# def extract_file(file_path:str):
#     print(f"File extracting- {file_path}")
#     time.sleep(5)
#     print(f"End- {file_path}")

# @app.post("/upload")
# async def file_upload(background_task:BackgroundTasks, file:UploadFile = File(...)):
#     path = os.path.join("uploads",file.filename)
#     content = await file.read()

#     with open(path, "wb") as f:
#         f.write(content)
#     background_task.add_task(extract_file, path)
#     return {
#         "message": "file upload done"
#     }
