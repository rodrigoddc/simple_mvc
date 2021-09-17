from fastapi import FastAPI

app = FastAPI()

@app.get("/filme/1234")
def mostra_informações_do_filme():
    return {"Teste": "Foi?"}