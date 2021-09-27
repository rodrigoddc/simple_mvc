from typing import Optional
from pydantic import BaseModel
import requests


class MovieInfo(BaseModel):
    nome: str
    release_year: int
    director: str
    backdrop: Optional[str] = None

    def retrieve_movie_info(self, movie_id, api_key):
        movie_response = requests.get(
            f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
        ).json()
        credits_response = requests.get(
            f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}"
        )
        self.nome = movie_response.get("title")
        self.release_year = movie_response.get("release_date")
        # self.director = credits_response.get()
        self.backdrop = movie_response.get("backdrop_path")
