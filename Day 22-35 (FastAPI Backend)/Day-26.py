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


# from fastapi import FastAPI
# from pydantic import BaseModel, Field, field_validator, model_validator, EmailStr
# from typing import Optional
# from enum import Enum

# app = FastAPI()


# class CropType(Enum):
#     rice = ("rice",)
#     wheat = ("wheat",)
#     potato = "potato"


# class Farmer(BaseModel):
#     farmer_id: int = Field(..., gt = 0)
#     distict: str = Field(..., min_length= 3)
#     expected_yeild: Optional[float] = None
#     farmer_phone : str = Field(..., min_length=11, max_length=11)
#     season: str

#     @field_validator("farmer_phone")
#     @classmethod
#     def check_phone(cls,value: str) -> str:
#         if not value.isdigit():
#             raise ValueError("Phone number cann't be an alphabet")
#         return value

#     @field_validator("season")
#     @classmethod
#     def check(cls, value: str) -> str:
#         value = value.lower().strip()
#         if value not in ["rabi","kharif","monsoon"]:
#             raise ValueError("Season not matched")
#         return value

#     @model_validator(mode="after")
#     def check_season(self):
#         if self.season == "monsoon" and self.expected_yeild is None:
#             raise ValueError("Expected yeild must be added")
#         return self

# @app.post("/farmer", status_code= 202)
# def farmer(farmer:Farmer):
#     return {
#         "farmer_id": farmer.farmer_id,
#         "farmer_phone": farmer.farmer_phone,
#         "distict": farmer.distict,
#         "season": farmer.season,
#         "expected_yeild": farmer.expected_yeild
#     }
from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
app = FastAPI()

class CropType(str, Enum):
    rice = "rice"
    wheat = "wheat"
    potato = "potato"


class Farmer(BaseModel):
    farmer_name: str
    crop_name: CropType


@app.post("/farmer")
def farmer(farmer: Farmer):
    return {farmer.farmer_name: farmer.crop_name}
