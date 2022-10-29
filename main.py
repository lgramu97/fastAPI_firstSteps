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
    return {"Hello" : "World"}