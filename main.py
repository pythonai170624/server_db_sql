from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import HTMLResponse
import bl
from models import *

# Create FastAPI instance
app = FastAPI(title="Example API", description="A simple FastAPI with Swagger UI", version="1.0")

@app.get("/items/")
def get_all():
    result = bl.get_items()
    return {"result": result}

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    return bl.get_item_by_id(item_id)

# Define a POST endpoint
@app.post("/items/")
def create_item(item: Item):
    bl.insert_item(item)
    return {"message": "item successfully added"}

@app.delete("/items/{item_id}")
def read_root(item_id: int):
    bl.delete_item(item_id)
    return {"message": "item successfully added"}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id != item.id:
        # return Error
        pass

    bl.update_item(item_id, item)
    return {"message": "item updated"}
