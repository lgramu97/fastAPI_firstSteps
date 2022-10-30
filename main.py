# FastAPI
from fastapi import Body, FastAPI

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
def create_person(person: Person = Body(...)): # Body(...) obligatory
    return person
