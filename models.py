from pydantic import BaseModel

DB_NAME = "mydata.db"

class Item(BaseModel):
    id: int | None = None
    name: str
    price: float