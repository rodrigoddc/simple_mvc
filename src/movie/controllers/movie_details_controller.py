from fastapi import APIRouter

from src.movie.models.movie_detail_model import MovieDetail, get_movie_details
from src.movie.models.movie_detail_model import get_movie_crew_data
from src.movie.views.movie_detail_views import movie_detail_view

movie_detail_router = APIRouter()

@movie_detail_router.get("/filme/{movie_id}")
def movie_detail(movie_id: int):

    movie_data = get_movie_details(movie_id)
    crew_data = get_movie_crew_data(movie_id)
    needed_data = movie_data | crew_data
    model = MovieDetail(**needed_data)
    view = movie_details_view(movie_id, model)

    return view
