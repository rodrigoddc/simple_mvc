import requests
from src.dependencies import api_key
import json


class MovieRating:
    def __init__(self, movie_id: int, rating: float):
        self.api_key = api_key
        self.movie_id = movie_id
        self.rating = {"rating": rating}
        self.headers = {"Content-Type": "application/json;charset=utf-8"}
        self.publish_rating = self.publish_rating()

    def publish_rating(self):
        publish_request = requests.post(
            f"https://api.themoviedb.org/3/movie/{self.movie_id}/rating?api_key={self.api_key}",
            data=self.rating,
            headers=self.headers,
        )

        return publish_request
