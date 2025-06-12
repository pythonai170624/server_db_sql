
import dal
from models import *

def get_items():
    return dal.get_items()

def get_item_by_id(id: int):
    return dal.get_item_by_id(id)

def insert_item(item: Item):
    dal.insert_item(item)

def update_item(id: int, item: Item):
    return dal.update_item(id, item)

def delete_item(id: int):
    return dal.delete_item(id)