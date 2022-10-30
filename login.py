# Pydantic
from pydantic import BaseModel, Field, Required

class LoginOut(BaseModel):
    
    username : str = Field(
        Required,
        max_length=16,
        min_length=4,
        example="username"
    )
    
    message : str = Field(
        default="Login Succesfull",
        description="Loging message",
        example="User logged."
    )
    