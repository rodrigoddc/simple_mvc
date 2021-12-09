from fastapi import APIRouter
import asyncio
from mestre.src.movie.models.movie_detail_model import MovieDetail, fetch_movie_details_and_movie_crew
from mestre.src.movie.views.movie_detail_views import movie_detail_view

movie_detail_router = APIRouter()


@movie_detail_router.get("/filme/{movie_id}")
def movie_detail(movie_id: int):
    movie_data, crew_data = asyncio.run(
        fetch_movie_details_and_movie_crew(movie_id)
    )
    needed_data = movie_data | crew_data
    model = MovieDetail(**needed_data)
    view = movie_detail_view(movie_id, model)

    return view