from fastapi import FastAPI

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
