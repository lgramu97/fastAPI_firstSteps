# Python
from typing import Optional
# Pydantic
from pydantic import BaseModel

# Optional[type expected] or None


class Person(BaseModel):

    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[str] = None
