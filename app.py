from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def greet_people():
    return {"Eae": "galerinha"}


