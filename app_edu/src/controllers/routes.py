from src.views.movies import render_movie_info_view
from src.models.movie import retrieve_movie_info
from fastapi import APIRouter


router = APIRouter()


@router.get("/movie_info/{movie_id}")
def movie_info(movie_id: str):

    movie = retrieve_movie_info(movie_id)
    response = render_movie_info_view(movie)

    return response
