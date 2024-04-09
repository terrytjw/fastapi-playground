# standard library imports: part of Python's standard library
import logging
from typing import Dict, Union # Union is a type hint that allows for multiple types

# third-party imports: not part of Python's standard library
from fastapi import FastAPI, HTTPException, Path, Body, Query
from pydantic import ValidationError

# local imports: imports from modules that are part of your own application or project
from src.models import Item

# use the FastAPI() function to create a new instance of the FastAPI class
# this creates a new instance of the FastAPI app
app = FastAPI()

logger = logging.getLogger(__name__) #  __name__ is a special variable that holds the name of the current module

def handle_validation_error(error: ValidationError):
    error_details = []
    for err in error.errors():
        field = ".".join([str(loc) for loc in err["loc"]])
        message = err["msg"]
        error_details.append(f"{field}: {message}")
    
    raise HTTPException(status_code=422, detail=error_details)

def handle_exception(exception: Exception):
    raise HTTPException(status_code=500, detail=str(exception))

# define a route that handles GET requests to the root URL ("/")
# an example api call URL looks like this: http://localhost:8000/
@app.get("/")
def read_root() -> Dict[str, str]:
    """
    Root endpoint that returns a simple greeting.
    """
    return {"Hello": "World"}

# an example api call URL looks like this: http://localhost:8000/items/123
@app.get("/items/{item_id}")
def read_item(item_id: int = Path(..., title="The ID of the item to retrieve"),
              name: str = Query(None, title="The name of the item (optional)")):
    """
    Retrieve an item by ID.
    """
    try:
        # Perform the retrieval operation (e.g., fetch item from database)
        # Replace this with your actual retrieval logic
        item = Item(id=item_id, name=name, price=10.0, is_offer=True)
        logger.info(f"Retrieved item with ID: {item_id}")
        
        return {"item_id": item_id, "item": item}
    
    except ValidationError as e:
        logger.error(f"Validation error retrieving item with ID {item_id}: {str(e)}")
        handle_validation_error(e)
    
    except Exception as e:
        logger.error(f"Error retrieving item with ID {item_id}: {str(e)}")
        handle_exception(e)

@app.put("/items/{item_id}")
def update_item(item_id: int = Path(..., title="The ID of the item to update"),
                item: Item = Body(..., embed=True, title="The updated item data")):
    """
    Update an item by ID.
    """
    try:
        # Validate the input data against the Item model
        item = Item(**item.model_dump())
        
        # Perform the update operation (e.g., update item in database)
        # ...
        
        return {"item_id": item_id, "item": item}
    
    except ValidationError as e:
        logger.error(f"Validation error updating item with ID {item_id}: {str(e)}")
        handle_validation_error(e)
    
    except Exception as e:
        logger.error(f"Error updating item with ID {item_id}: {str(e)}")
        handle_exception(e)