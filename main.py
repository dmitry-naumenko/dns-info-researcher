"""Main."""
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """[summary].

    Returns:
        [type]: [description]
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, some_q: Optional[str] = None):
    """[summary].

    Args:
        item_id (int): [description]
        some_q (Optional[str], optional): [description]. Defaults to None.

    Returns:
        [type]: [description]
    """
    return {"item_id": item_id, "some_q": some_q}
