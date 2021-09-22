from fastapi import APIRouter

from view.view import movie_view_info
from model.model import MovieInfo

router = APIRouter()


@router.get("/filmes/{movie_id}")
def movie_info(movie_id: int):

    movie = retrieve_movie_info(movie_id)
    response = movie_view_info(movie)

    return response
