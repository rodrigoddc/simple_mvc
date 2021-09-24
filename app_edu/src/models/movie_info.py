from typing import Optional
import requests


class TMDBMessage:
    def __init__(self, movie_id) -> None:
        self.movie_id: str = movie_id
        self.movie_message: dict = self.retrieve_movie_info_message(self.movie_id)
        self.credits_message: dict = self.retrieve_credits_info_message(self.movie_id)

    def retrieve_movie_info_message(self, movie_id: str):
        movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api_key}"
        response = requests.get(movie_url).json()
        return response


    def retrieve_credits_info_message(self, movie_id: str):
        credits_url = (
            f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={tmdb_api_key}"
        )
        response = requests.get(credits_url).json()
        return response


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
        crew = self.movie.credits_message["crew"]

        for worker in crew:
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
