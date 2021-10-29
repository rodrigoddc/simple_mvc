from fastapi import APIRouter

from src.movie.models.movie_rating_model import Rating
from src.movie.views.movie_ratings_views import movie_rating_view

router = APIRouter()


@router.post("/filme/{movie_id}")
def movie_rating(movie_id: int, rate: Rating):

    view = movie_rating_view(movie_id, rate)

    return view