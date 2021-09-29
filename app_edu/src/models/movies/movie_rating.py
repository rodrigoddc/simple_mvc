from setup.settings import Settings
import requests


class MovieRating:
    def __init__(self, movie_id, rating) -> None:
        self.movie_id = movie_id
        self.movie_rating = rating
        self.tmdb_api_key = Settings().tmdb_api_key

    def publish_movie_rating(self):
        movie_url = f"https://api.themoviedb.org/3/movie/{self.movie_id}/{self.movie_rating}?api_key={self.tmdb_api_key}"
        response = requests.post(movie_url)
        return response