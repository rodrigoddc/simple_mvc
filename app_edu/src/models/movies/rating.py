from setup.settings import Settings
import requests
from src.models.movies.exceptions.rating import MovieRatingException


class MovieRating:
    def __init__(self, movie_id, rating) -> None:
        self.movie_id = movie_id
        self.movie_rating = rating
        self.tmdb_api_key = Settings().tmdb_api_key
        self.base_movie_url = f"https://api.themoviedb.org/3/movie/{self.movie_id}/rating?api_key={self.tmdb_api_key}"

    def validate_movie_rating(self):
        if self.movie_rating not in range (0, 11):
            raise MovieRatingException(f"Rating {self.rating} was passed, but a rating must be between 0-10.")


    def publish_movie_rating(self):
        rating_data = {"value": self.rating}
        response = requests.post(self.base_movie_url, json=rating_data)
        return response

    def delete_movie_rating(self):
        response = requests.delete(self.base_movie_url)
        return response

    def update_movie_rating(self):
        self.delete_movie_rating()
        self.publish_movie_rating()

