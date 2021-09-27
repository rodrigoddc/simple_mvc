from fastapi import APIRouter
from src.view.movie_view import movie_view
from src.model.movie_model import MovieInfo
from src.dependencies import api_key


router = APIRouter()


@router.get("/filmes/{movie_id}")
def movie_info(movie_id: int):

    movie = MovieInfo(movie_id)
    response = movie_view(movie)

    return response
