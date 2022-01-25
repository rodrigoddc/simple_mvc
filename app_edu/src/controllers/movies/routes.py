import asyncio
from src.models.movies.rating import MovieRating
from src.models.movies.info import MovieInfo
from src.views.movies.info import render_movie_info
from src.views.movies.rating import render_movie_rating
from src.models.movies.requests.info import InfoRequest
from fastapi import APIRouter
router = APIRouter()

@router.get("/movie_info/{movie_id}")
def movie_info(movie_id: int):
    movie_data, crew_data = asyncio.run(
        InfoRequest(movie_id).fetch_movie_details_and_movie_crew()
    )
    needed_data = movie_data | crew_data
    model = MovieInfo(needed_data)
    view = render_movie_info(model)

    return view

"""
@router.post("/movie_rating/publish/{movie_id}")
async def movie_rating_post(movie_id: int, rating: MovieRating):
    movie_rating = MovieRating(movie_id, rating)
    response = render_movie_rating(movie_rating)
    await response


@router.put("/movie_rating/update/{movie_id}/")
def movie_rating_update(movie_id: int, rating: float):
    movie = MovieRating(movie_id, rating)
    response = movie.update_movie_rating()

    return response
"""
