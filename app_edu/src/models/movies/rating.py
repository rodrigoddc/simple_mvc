from pydantic.class_validators import validator
from src.models.movies.exceptions.rating import MovieRatingException
from pydantic import BaseModel


class MovieRating(BaseModel):
    movie_id: int
    movie_rating: float

    @validator("movie_rating")
    def validate_movie_rating(cls, v):
        if v < 0 or v > 10:
            raise MovieRatingException(f"Rating {v} was passed, but a rating must be between 0-10.")
