from fastapi import FastAPI

from src.controller.controller import router

app = FastAPI(
    title="Simple MVC API",
    contact={"name": "Rodrigo Azevedo", "e-mail": "razevedo.contato@gmail.com"},
)
app.include_router(router=router)
