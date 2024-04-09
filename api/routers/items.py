import logging
from fastapi import APIRouter, Path, Body, Query

from pydantic import ValidationError

from api.models.item import Item
from api.utils import handle_exception, handle_validation_error

router = APIRouter()

logger = logging.getLogger(__name__) #  __name__ is a special variable that holds the name of the current module

# an example api call URL looks like this: http://localhost:8000/items/123
@router.get("/items/{item_id}")
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

@router.put("/items/{item_id}")
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