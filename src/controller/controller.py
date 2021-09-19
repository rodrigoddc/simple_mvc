from fastapi import APIRouter

from src.model.model import retrieve_movie
from src.view.view import movie_view, retrieve_publish_response

router = APIRouter()


@router.get("/filmes/{movie_id}")
def movie_info(movie_id: int):

    movie = retrieve_movie(movie_id)
    response = movie_view(movie)

    return response
