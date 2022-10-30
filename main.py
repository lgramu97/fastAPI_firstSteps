# Python
from typing import Optional
# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body, Cookie,  File, Form, Header, Path, Query, UploadFile
from fastapi import HTTPException
# Pydantic
from pydantic import EmailStr, Required
from login import LoginOut

# Custom
from person import Person, PersonOut
from location import Location


# Create an instance
app = FastAPI()

# Path Operatorion Decorator.


@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"]
)
# Path Operation Function
def home():
    """Main page.

    Returns:
        json: dictionary (json) hello world.
    """
    return {"Hello": "World"}


# Path Operation with path Parameters.
@app.get(
    path="/items/{item_id}",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Items"]
)
async def read_item(item_id: int):
    """Example route with path parameter.

    Args:
        item_id (int): number of item.

    Returns:
        dictionary: json with the item id.
    """
    return {"item_id": item_id}


# Path Operation with optional parameters.
@app.get(
    path="/cards/{item_id}",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Items"]
)
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

# Here return all the data in Person, but not the password.
# Request and Response.


@app.post(
    path="/person/new",
    response_model=PersonOut,
    status_code=status.HTTP_201_CREATED,
    tags=["person"],
    summary="Create person in the app"
)
def create_person(person: Person = Body(...)):  # Body(...) obligatory
    """
    This path operation creates a person in the app and save information
    in the database.

    Args:  
    - **person** (Person, optional): a Person model with all the info.

    Returns:
    - **dict**: return a json with the person model information.
    """
    return person


# Validation Query Parameters
@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK,
    tags=["person"],
    deprecated=True
)
def show_person(
    name: Optional[str] = Query(
        default=None,
        min_length=1,
        max_length=50,
        title="Person Name",
        description="This is the person name.",
        example="Maradona"
    ),
    age: Optional[str] = Query(
        ...,  # Obligatory, this is not correct.
        title="Person age",
        description="This is the person age.",
        example=62
    )
):
    """
    Example validation query parameters

    Args:
        **name** (Optional[str], optional): person name.   
        **age** (Optional[str], optional): person age.   

    Returns:
        **dict**: json with the information.    
    """
    return {name: age}


# HTTP exception
person = [1, 2, 3, 4, 5]
# Validation Path Parameters
@app.get(
    path="/person/detail/{person_id}",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["person"]
)
def show_person(
    person_id: int = Path(
        Required,
        gt=0,
        title="Person id",
        description="This is the person id.",
        example=123
    )
):
    if person_id not in person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The person doesn't exist."
        )
    return {person_id: "It exists!"}


# Validation Query Parameters with Required
@app.get(
    path="/parameter/required",
    status_code=status.HTTP_200_OK,
    tags=["Items"]
)
async def read_items(q: str = Query(default=Required, min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Validation Request Body (2 jsons)
@app.put(
    path="/person/{person_id}",
    response_model=PersonOut,
    status_code=status.HTTP_202_ACCEPTED,
    tags=["person"]
)
def update_person(
    person_id: int = Path(
        Required,
        title="Person Id.",
        description="This is the person Id",
        gt=0,
        example=123
    ),
    person: Person = Body(Required),
    location: Location = Body(Required)
):
    # Union both dict and return
    results = person.dict()
    results.update(location.dict())
    return person


# Working with Forms.
@app.post(
    path="/login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
    tags=["person"]
)
def login(username: str = Form(Required), password: str = Form(Required)):
    return LoginOut(username=username)


# Cookies and Headers Parameters.
@app.post(
    path="/contact",
    status_code=status.HTTP_200_OK,
    tags=["Contact"]
)
def contact(
    first_name: str = Form(
        Required,
        max_length=20,
        min_length=1
    ),
    last_name: str = Form(
        Required,
        max_length=20,
        min_length=1
    ),
    email: EmailStr = Form(Required),
    message: str = Form(
        Required,
        min_length=20
    ),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)
):
    return user_agent


# Files. type: UploadFile, use File from fastApi.
@app.post(
    path="/post-image",
    tags=["Files"]
)
def post_image(
    image: UploadFile = File(Required)
):
    """Example working with files.

    Args:
        image (UploadFile, optional): _description_. Defaults to File(Required).

    Returns:
        dict: json with the file information.
    """
    return {
        "Filename": image.filename,
        "Format": image.content_type,
        "Size(kb)": round(len(image.file.read())/1024, ndigits=2)
    }
