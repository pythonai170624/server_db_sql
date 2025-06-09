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

# Define a POST endpoint
@app.post("/items/")
def create_item(item: Item):
    bl.insert_item(item)
    return {"message": "item successfully added"}

@app.delete("/delete-item")
def read_root():
    return {"message": "item deleted"}

@app.put("/update-item")
def read_root():
    return {"message": "item updated"}

