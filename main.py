from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}



@app.get("/items/{item_id}")
async def read_item(item_id:int, page:Optional[str]=None, len:Optional[int]=None):
    return {"item_id": item_id, "page":page, "len":len}