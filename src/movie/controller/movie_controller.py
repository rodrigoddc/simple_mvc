from fastapi import APIRouter
from src.movie.view.movie_view import movie_view
from src.movie.model.movie_info_model import MovieInfo
from src.movie.model.movie_rating_model import MovieRating
import json


router = APIRouter()


@router.get("/filmes/{movie_id}")
def movie_info(movie_id: int):

    movie_info = MovieInfo(movie_id)
    response = movie_view(movie_info)

    return response


@router.post("/filmes/{movie_id}/rating/publish/{rating}")
def movie_rating(movie_id: int, rating: float):

    movie_rating = MovieRating(movie_id, rating)
    response = movie_rating.publish_rating

    return response
