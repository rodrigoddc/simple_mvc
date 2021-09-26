from fastapi import APIRouter

from src.view.movie_view import movie_view
from model.movie_model import MovieInfo

router = APIRouter()


@router.get("/filmes/{movie_id}")
def movie_info(movie_id: int):

    movie = retrieve_movie_info(movie_id)
    response = movie_view(movie)

    return response
