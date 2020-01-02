"""
Success -
Request: http://127.0.0.1:8000/items/123?q=datta
Response:{
    "item_id": 123,
    "q": "datta"
}

Validation examples -
Request: http://127.0.0.1:8000/items/
Response:{
    "detail": "Not Found"
}

Request: http://127.0.0.1:8000/items/abc?q=1
Response: {
    "detail": [
        {
            "loc": [
                "path",
                "item_id"
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]
}
"""

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """
    Endpoint with url param (required) and query string param (optional).
    FastAPI validates item_id for int value (with the help of type hint)
    :param item_id:
    :param q:
    :return:
    """
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    """
        Run using: 
        python-fastapi>uvicorn url_path_example:app --reload
        http://127.0.0.1:8000 (Use browser)
    """
    uvicorn.run(app)
