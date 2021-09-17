from fastapi import FastAPI

app = FastAPI()

@app.get("/filme/1234")
def read_item():
    return {"filme": "Oi cara de boi"}


