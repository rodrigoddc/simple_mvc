from pydantic import BaseModel, validator

from src.movie.exceptions import MovieRatingExceptions


class Rating(BaseModel):
    nota: float

    @validator("nota")
    def validate_nota(cls, v):

        if v < 0.5 or v > 10:
            raise MovieRatingExceptions("Valor fora do permitido")
        return v