from typing import Optional
from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str = Field(...)
    country: str = Field(...)


class UpdateAddressModel(BaseModel):
    city: Optional[str]
    country: Optional[str]


class StudentSchema(BaseModel):
    name: str = Field(...)
    age: int = Field(..., gt=0, description="Age must be greater than 0")
    address: Address = Field(...)


class UpdateStudentModel(BaseModel):
    name: Optional[str]
    age: Optional[int] = Field(None, gt=0, description="Age must be greater than 0")
    address: Optional[UpdateAddressModel]


def ErrorResponseModel(code, message):
    return {"code": code, "message": message}
