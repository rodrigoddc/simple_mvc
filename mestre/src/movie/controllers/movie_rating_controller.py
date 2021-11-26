from fastapi import APIRouter

from fastapi import Request

from src.movie.models.movie_rating_model import Rating
from src.movie.views.movie_ratings_views import movie_rating_view

movie_rating_router = APIRouter()


@movie_rating_router.post("/filme/{movie_id}")
async def movie_rating(movie_id: int, request: Request):

    data = await request.json()
    model = Rating(**data)
    view = movie_rating_view(movie_id, model)

    return view