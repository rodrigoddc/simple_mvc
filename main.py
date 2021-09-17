from fastapi import FastAPI

app = FastAPI()

@app.get("/filme/1234")
def root():
    return {"Teste": "Foi?"}