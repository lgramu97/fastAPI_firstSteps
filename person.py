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
