from fastapi import FastAPI

from src.controllers.routes import router


app = FastAPI()
app.include_router(router=router)
