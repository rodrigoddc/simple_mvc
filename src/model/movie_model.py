from typing import Optional
from pydantic import BaseModel


class MovieInfo(BaseModel):
    nome: str
    release_year: int
    director: str
    backdrop: Optional[str] = None
