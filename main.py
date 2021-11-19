from fastapi import FastAPI

from mestre.src.movie.controllers.movie_rating_controller import movie_rating_router
from mestre.src.movie.controllers.movie_details_controller import movie_detail_router
from src.exceptions.exception_handlers.movie_exception_handlers import movie_exception_handler, \
    movie_not_found_exception_handler, movie_missing_data_exception_handler
from src.exceptions.movie_exceptions import MovieRatingException, MovieNotFoundException, \
    MovieMissingDataFromTMDBAPIException

app = FastAPI()
app.include_router(router=movie_rating_router)
app.include_router(router=movie_detail_router)
app.add_exception_handler(MovieRatingException, movie_exception_handler)
app.add_exception_handler(MovieNotFoundException, movie_not_found_exception_handler)
app.add_exception_handler(MovieMissingDataFromTMDBAPIException, movie_missing_data_exception_handler)