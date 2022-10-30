# FastAPI
from typing import Optional
from fastapi import Body, FastAPI, Path, Query
from pydantic import Required

from person import Person
from location import Location

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
    name: Optional[str] = Query(
        default=None,
        min_length=1,
        max_length=50,
        title="Person Name",
        description="This is the person name."
    ),
    age: Optional[str] = Query(
        ...,  # Obligatory, this is not correct.
        title="Person age",
        description="This is the person age."
    )
):
    """Example validation query parameters

    Args:
        name (Optional[str], optional): person name. 
        age (Optional[str], optional): person age. 

    Returns:
        dict: json with the information-
    """
    return {name: age}


# Validation Path Parameters
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        Required,
        gt=0,
        title="Person id",
        description="This is the person id."
    )
):
    return {person_id: "It exists!"}


# Validation Query Parameters with Required
@app.get("/parameter/required")
async def read_items(q: str = Query(default=Required, min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Validation Request Body (2 jsons)
@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        Required,
        title="Person Id.",
        description="This is the person Id",
        gt=0
    ),
    person: Person = Body(Required),
    location: Location = Body(Required)
):
    # Union both dict and return
    results = person.dict()
    results.update(location.dict())
    return person


# Validation Request Body must be done in the MODEL.