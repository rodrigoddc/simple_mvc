import requests
from requests.sessions import session
from src.dependencies import api_key
import json


class MovieRating:
    def __init__(self, movie_id: int, rating: float):
        self.api_key = api_key
        self.movie_id = movie_id
        self.rating = {"rating": rating}
        self.headers = {"Content-Type": "application/json;charset=utf-8"}
        self.session = self.create_guest_session()
        self.publish_rating = self.publish_rating()

    def publish_rating(self):
        publish_request = requests.post(
            f"https://api.themoviedb.org/3/movie/{self.movie_id}/rating?api_key={self.api_key}&guest_session_id={self.session}",
            data=self.rating,
            headers=self.headers,
        ).json()

        return publish_request

    def create_guest_session(self):
        auth_response = requests.get(
            f"https://api.themoviedb.org/3/authentication/guest_session/new?api_key={self.api_key}"
        ).json()
        session_id = auth_response.get("guest_session_id")

        return session_id
