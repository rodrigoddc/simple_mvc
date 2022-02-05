from setup.settings import Settings
from src.models.movies.info import MovieInfo
from src.views.movies.info import render_movie_info
from src.models.movies.requests.info import InfoRequest
from fastapi import APIRouter

STRATEGY = Settings().info_request_strategy
router = APIRouter()


@router.get("/movie_info/{movie_id}")
def movie_info(movie_id: int):
    
    data = InfoRequest(movie_id, STRATEGY).get_movie_info()
    model = MovieInfo(data)
    view = render_movie_info(model)

    return view