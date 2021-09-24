from src.views.movies import render_movie_info
from src.models.movie_info import MovieInfo
from fastapi import APIRouter


router = APIRouter()


@router.get("/movie_info/{movie_id}")
def movie_info(movie_id: str):

    movie = MovieInfo(movie_id)
    response = render_movie_info(movie)

    return response
