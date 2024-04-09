from typing import Union # Union is a type hint that allows for multiple types

from fastapi import FastAPI

# use the FastAPI() function to create a new instance of the FastAPI class
# this creates a new instance of the FastAPI app
app = FastAPI()

# define a route that handles GET requests to the root URL ("/")
# an example api call URL looks like this: http://localhost:8000/
@app.get("/")
def read_root():
    return {"Hello": "World"}

# an example api call URL looks like this: http://localhost:8000/items/123
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}