from src.models.movie import Movie
from src.views.movies import movie_view
from app import app
from src.models.movie import Movie
from fastapi.routing import APIRoute

@app.get("/")
def get_movie_info(movie: Movie):
    return movie_view(movie)
