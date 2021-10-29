from fastapi import FastAPI

from mestre.src.movie.controllers.movie_rating_controller import router

app = FastAPI()
app.include_router(router=router)
