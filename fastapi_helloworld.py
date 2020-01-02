import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == '__main__':
    """
    Run using: 
    python-fastapi>uvicorn fastapi_helloworld:app --reload
    http://127.0.0.1:8000 (Use browser)
    """
    uvicorn.run(app)
