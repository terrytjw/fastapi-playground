from typing import Union

from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: Union[str, None] = None
    price: float
    is_offer: Union[bool, None] = None