from typing import Optional
from src.controllers.tmdb_requests import retrieve_movie_info_message, retrieve_cast_info_message


class TMDBMessage:
    def __init__(self, movie_id) -> None:
        self.movie_id: str = movie_id
        self.movie_message: dict = retrieve_movie_info_message(self.movie_id)
        self.cast_message: dict = retrieve_cast_info_message(self.movie_id)


class MovieInfo:
    def __init__(self, movie_id: str):
        self.movie = TMDBMessage(movie_id)
        self.title: str = self._get_title()
        self.year: int = self._get_year()
        self.director: str = self._get_director()
        self.backdrop: Optional[str] = self._get_backdrop()
    

    def _get_title(self):
        return self.movie.movie_message["title"]

    
    def _get_year(self):
        return int(self.movie.movie_message["release_date"][0:4])


    def _get_director(self):
        cast = self.movie.cast_message["cast"]
        for worker in cast:
            try:
                if worker["job"] == "Director":
                    return worker["name"] 
            except KeyError:
                continue


    def _get_backdrop(self):
        backdrop = self.movie.movie_message["backdrop_path"]
        if backdrop != "null":
            return backdrop
        else:
            return None
