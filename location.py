# Pydantic
from pydantic import BaseModel, Field, Required


class Location(BaseModel):
    city: str = Field(
        Required,
        example="Tandil"
    )
    state: str = Field(
        Required,
        example="Buenos Aires"
    )
    country: str = Field(
        Required,
        example="Argentina"
    )
