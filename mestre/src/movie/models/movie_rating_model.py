from pydantic import BaseModel, validator

from src.exceptions.movie_exceptions import MovieRatingException
from src.movie.models.tmdb_api_caller import tmdb_api_caller


class Rating(BaseModel):
    nota: float

    @validator("nota")
    def validate_nota(cls, v):

        if v < 0.5 or v > 10:
            raise MovieRatingException(f"Valor fora do permitido: {v}")
        return v


def get_request_token():

    url = "authentication/token/new/"

    response = tmdb_api_caller(
        method="GET",
        url=url
    )

    return response.get("request_token")
