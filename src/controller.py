from fastapi import APIRouter

from src.model import retrieve_movie
from src.view import movie_view, retrieve_publish_response

router = APIRouter()


@router.get("/filmes/{movie_id}")
def movie_info(movie_id: int):

    movie = retrieve_movie(movie_id)
    response = movie_view(movie)

    return response


@router.post("/filmes/{movie_id}")
def movie_info(movie_id: int):

    model = movie_view(movie)
    response = retrieve_publish_response(movie_id)

    return response

