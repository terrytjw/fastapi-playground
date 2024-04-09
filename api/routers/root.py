from fastapi import APIRouter

router = APIRouter()

# define a route that handles GET requests to the root URL ("/")
# an example api call URL looks like this: http://localhost:8000/
@router.get("/")
def read_root():
    """
    Root endpoint that returns a simple greeting.
    """
    return {"Hello": "World"}