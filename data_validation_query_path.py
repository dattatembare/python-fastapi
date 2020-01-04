import uvicorn
from fastapi import FastAPI, Query, Path

app = FastAPI(debug=True)
item_id: str


@app.get("/items/")
async def read_items(item_id: str = Query(..., min_length=2, max_length=10, regex="^Item\d{1,6}")):
    """
    Validate query string parameter values
    :param item_id:
    :return:
    """
    results = {"items": [{"item_id": "Pen"}, {"item_id": "Pencil"}]}
    results.update({"New Item": item_id})
    return {"item": item_id}


@app.get("/items/{item_id}")
async def get_items(item_id: int = Path(..., le=10, ge=2, title="Item Id")):
    """
    Validate Path parameter values.
    :param item_id:
    :return:
    """
    return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
