from simple_mvc.app_edu.src.models.movies.movie_rating import MovieRating
from src.views.movies.movie_info import render_movie_info
from src.models.movies.movie_info import MovieInfo
from fastapi import APIRouter


router = APIRouter()


@router.get("/movie_info/{movie_id}")
def movie_info(movie_id: int):

    movie = MovieInfo(movie_id)
    response = render_movie_info(movie)

    return response


@router.post("/movie_info/{movie_id}/{rating}")
def movie_rate(movie_id: int, rating: float):
    movie = MovieRating(movie_id, rating)
    response = movie.publish_movie_rating()
    
    return response


