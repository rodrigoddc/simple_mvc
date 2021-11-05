import requests
from config import tmdb_api_key

class MovieInfo:
    def __init__(self, movie_id: int):
        self.api_key = tmdb_api_key
        self.movie_id = movie_id
        self.movie_info = self.retrieve_movie_info()
        self.credits_info = self.retrieve_credits_info()

    def retrieve_movie_info(self):
        movie_response = requests.get(
            f"https://api.themoviedb.org/3/movie/{self.movie_id}?api_key={self.api_key}"
        ).json()

        return movie_response

    def retrieve_credits_info(self):
        credits_response = (
            requests.get(
                f"https://api.themoviedb.org/3/movie/{self.movie_id}/credits?api_key={self.api_key}"
            )
            .json()
            .get("crew")
        )

        for crew in credits_response:
            if crew.get("job") == "Director":
                return crew.get("name")
