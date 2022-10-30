# FastAPI
from typing import Optional
from fastapi import Body, FastAPI, Query
from pydantic import Required

from person import Person

# Create an instance
app = FastAPI()

# Path Operatorion Decorator.


@app.get("/")
# Path Operation Function
def home():
    """Main page.

    Returns:
        json: dictionary (json) hello world.
    """
    return {"Hello": "World"}


# Path Operation with path Parameters.
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """Example route with path parameter.

    Args:
        item_id (int): number of item.

    Returns:
        dictionary: json with the item id.
    """
    return {"item_id": item_id}


# Path Operation with optional parameters.
@app.get("/cards/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    """Example route with optional parameters.

    Args:
        item_id (str): id.
        q (str | None, optional): optional question. Defaults to None.

    Returns:
        dictionary: json with the information.
    """
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# Request and Response.
@app.post("/person/new")
def create_person(person: Person = Body(...)):  # Body(...) obligatory
    """Example Request and Response Body using pydantic BaseModel.

    Args:
        person (Person, optional): obligatory person. Defaults to Body(...).

    Returns:
        Person: person object.
    """
    return person


# Validation Query Parameters
@app.get("/person/detail")
def show_person(
    name : Optional[str] = Query(default=None, min_length=1, max_length=50),
    age : Optional[str] = Query(...) #Obligatory, this is not correct.
):
    """Example validation Query Parameters.

    Args:
        name (Optional[str], optional): person name. Defaults to Query(default=None, min_length=1, max_length=50).
        age (Optional[str], optional): person age. Defaults to Query(...)#Obligatory.

    Returns:
        dict: json with the data.
    """
    return {name : age}


# Validation Query Parameters with Required
@app.get("/parameter/required")
async def read_items(q: str = Query(default=Required, min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results