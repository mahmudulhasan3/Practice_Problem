# from fastapi import FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI()
# class Farmer(BaseModel):
#     name: str = Field(..., min_length= 2, max_length= 20)
#     age: int = Field(..., gt=0)
#     land_size: float = Field(..., gt=0)

# @app.post("/crop",status_code=422)
# def farmer(farmar:Farmer):
#     return {
#         "name": farmar.name,
#         "age": farmar.age,
#         "land_field": farmar.land_size
#     }


# from fastapi import FastAPI
# from pydantic import BaseModel, Field, field_validator, model_validator
# from typing import Optional

# app = FastAPI()

# allowed = ["rice","mango","banana"]
# class Farmer(BaseModel):
#     farmer_name: str
#     land_size_acres: float = Field(..., gt=0)
#     crop_name: str = Field(..., min_length=1)
#     contact_number: Optional[int] = None

#     @field_validator("crop_name")
#     @classmethod
#     def check(cls, value: str) -> str:
#         value = value.lower().strip()
#         if value not in allowed:
#             raise ValueError(f"{value} is not in {allowed}")
#         return value


# @app.post("/crop")
# def farmer(farmer:Farmer):
#     return {
#         "Name": farmer.farmer_name,
#         "Land Size": farmer.land_size_acres,
#         "Crop name": farmer.crop_name,
#         "Contact number": farmer.contact_number
#     }

# from fastapi import FastAPI
# app = FastAPI()
# from pydantic import BaseModel,model_validator,EmailStr


# class SignUp(BaseModel):
#     password: str
#     confirm_pass: str

#     @model_validator(mode="after")
#     def check(self):
#         if self.password != self.confirm_pass:
#             raise ValueError("Password dont matched")
#         return self

# class Email(BaseModel):
#     famername: str
#     email: EmailStr

# @app.post("/mahmdu")
# def mahmud(cook:Email):
#     return {
#         cook.email : cook.famername
#     }


# from fastapi import FastAPI
# from pydantic import BaseModel, Field, field_validator, model_validator, EmailStr
# from typing import Optional

# app = FastAPI()


# class Farmer(BaseModel):
#     farmer_name: str
#     phone: str = Field(..., min_length=11, max_length=11)
#     land_size: float = Field(..., gt=0)
#     notes: Optional[str] = None
#     farmer_email : EmailStr
#     crop_name: str

#     @field_validator("crop_name")
#     @classmethod
#     def check(cls, value:str) -> str:
#         value = value.lower().strip()
#         if value not in ["rice", "wheat", "potato"]:
#             raise ValueError("Dont matched")
#         return value

#     @model_validator(mode="after")
#     def land(self):
#         if self.land_size > 20 and self.notes is None:
#             raise ValueError("Need a note")
#         return self


# @app.post("/farmer")
# def farmer_def(farmer: Farmer):
#     return {
#         "farmer_name": farmer.farmer_name,
#         "phone": farmer.phone,
#         "land-size": farmer.land_size,
#         "farmer_email": farmer.farmer_email,
#         "notes": farmer.notes,
#         "crop_name": farmer.crop_name,
#     }


from fastapi import FastAPI
from pydantic import BaseModel, 