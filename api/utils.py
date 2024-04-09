from fastapi import HTTPException
from pydantic import ValidationError

def handle_validation_error(error: ValidationError):
    error_details = []
    for err in error.errors():
        field = ".".join([str(loc) for loc in err["loc"]])
        message = err["msg"]
        error_details.append(f"{field}: {message}")
    
    raise HTTPException(status_code=422, detail=error_details)

def handle_exception(exception: Exception):
    raise HTTPException(status_code=500, detail=str(exception))