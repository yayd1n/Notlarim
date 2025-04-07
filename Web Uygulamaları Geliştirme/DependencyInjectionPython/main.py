from fastapi import FastAPI, Depends
from typing import Annotated
app = FastAPI()


def hello_world():
    return "Hello, welcome to FastAPI!"


HelloDependency = Annotated[str, Depends(hello_world)]


def get_hello_world(hello: str = Depends(hello_world)):
    return f"Hello World service: {hello}"


@app.get("/hello")
def hello(message: str = Depends(get_hello_world)):
    return {"message": message}