# standard library imports: part of Python's standard library (currently empty)

# third-party imports: not part of Python's standard library
from fastapi import FastAPI

# local imports: imports from modules that are part of your own application or project
from api.routers.root import router as root_router
from api.routers.items import router as items_router

# use the FastAPI() function to create a new instance of the FastAPI class
# this creates a new instance of the FastAPI app
app = FastAPI()

app.include_router(root_router)
app.include_router(items_router)

