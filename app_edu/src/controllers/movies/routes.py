from src.models.movies.rating import MovieRating
from src.models.movies.info import MovieInfo
from src.views.movies.info import render_movie_info
from fastapi import APIRouter

router = APIRouter()

@router.get("/movie_info/{movie_id}")
def movie_info(movie_id: int):

    movie = MovieInfo(movie_id)
    response = render_movie_info(movie)

    return response


@router.post("/movie_rating/{movie_id}/publish/")
def movie_rating_post(movie_id: int, rating: MovieRating):

    return {}

@router.put("/movie_rating/{movie_id}/update/")
def movie_rating_update(movie_id: int, rating: float):
    movie = MovieRating(movie_id, rating)
    response = movie.update_movie_rating()

    return response