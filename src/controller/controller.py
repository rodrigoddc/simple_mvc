from fastapi import APIRouter

from src.model.model_movie_info import retrieve_movie
from src.view.view_movie_info import movie_view, retrieve_publish_response

router = APIRouter()


@router.get("/filmes/{movie_id}")
def movie_info(movie_id: int):

    movie = retrieve_movie(movie_id)
    response = movie_view(movie)

    return response
