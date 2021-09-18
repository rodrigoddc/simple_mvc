import requests
from setup.settings import tmdb_api_key


def retrieve_movie_info_message(movie_id: str):
    movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api_key}"
    response = requests.get(movie_url).json()
    return response


def retrieve_cast_info_message(movie_id: str):
    cast_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={tmdb_api_key}"
    response = requests.get(cast_url).json()
    return response
