# Python
from typing import Optional
from enum import Enum
# Pydantic
from pydantic import BaseModel, Field, Required

# Optional[type expected] or None


class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"


# Field for validation.
class Person(BaseModel):

    first_name: str = Field(
        Required,
        min_length=1,
        max_length=50,
    )
    last_name: str = Field(
        Required,
        min_length=1,
        max_length=50,
    )
    age: int = Field(
        Required,
        gt=0,
        lt=115,
    )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[str] = Field(default=None)
    password: str = Field(
        Required,
        min_length=8,
        max_length=16
    )

    # Create Config file to test endpoints in the API.
    class Config:
        schema_extra = {
            "example": {
                "first_name": "Lautaro",
                "last_name": "Gramuglia",
                "age": 25,
                "hair_color": "brown",
                "is_married": False,
                "password": "12345678"  # WARNING! THIS IS A BIG ERROR.
            }
        }


# Response Model (No password)
class PersonOut(BaseModel):
    first_name: str = Field(
        Required,
        min_length=1,
        max_length=50,
    )
    last_name: str = Field(
        Required,
        min_length=1,
        max_length=50,
    )
    age: int = Field(
        Required,
        gt=0,
        lt=115,
    )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[str] = Field(default=None)
