from pydantic.class_validators import validator
from src.models.movies.info import MovieInfo
from src.models.movies.exceptions.rating import MovieRatingException, MovieIdException
from pydantic import BaseModel

class MovieRating(BaseModel):
    rating: float

    @validator("rating", pre=True)
    def validate_movie_rating(cls, v):
        if v < 0.5 or v > 10.0:
            raise MovieRatingException(f"Rating {v} was passed, but a rating must be between 0.5-10.0")
