from os import name
from fastapi import FastAPI
from src.controllers.movies.routes import router

app = FastAPI(debug=True, title="App do Edu")
app.include_router(router=router)
