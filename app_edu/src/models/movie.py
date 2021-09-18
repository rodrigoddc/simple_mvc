from typing import Optional
from src.controllers.api_calls import retrieve_movie_message


class Movie:
    def __init__(self) -> None:
        title: str
        year: int
        # director: str
        backdrop: Optional[str]

    def setup_movie(self, movie_message: dict):
        self.title = movie_message["title"]
        self.year = self._get_year(movie_message)
        # self.director = movie_message["diretor"]
        self.backdrop = self._get_backdrop(movie_message)

    @staticmethod
    def _get_backdrop(movie_message: dict):
        backdrop = movie_message["backdrop_path"]
        if backdrop is not "null":
            return backdrop
        else:
            return None

    @staticmethod
    def _get_year(movie_message: dict):
        return int(movie_message["release_date"][0:4])


def _setup_movie_info(movie_message: dict):
    movie = Movie()
    movie.setup_movie(movie_message)
    return movie


def retrieve_movie_info(movie_id: str):
    message = retrieve_movie_message(movie_id)
    return _setup_movie_info(message)
