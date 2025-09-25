from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    text: str
    is_done: bool = False


items = []

# Test


@app.get("/")
def root():
    return {"Hello": "World"}

# Get items


@app.get("/items", response_model=List[Item])
def return_items(limit: int = 10):
    return items[0:limit]

# Get specific item from items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        item = items[item_id]
        return item
    else:
        raise HTTPException(status_code=404, detail="[404]: Item not found")

# Post a Item into Items


@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

# Delete a Item from Items


@app.delete("/items")
def delete_item(item: Item):
    if item in items:
        items.remove(item)
        return items
    else:
        return f"{item} is not in items list"
