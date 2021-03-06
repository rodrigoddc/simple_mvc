from pydantic import BaseModel, root_validator

from mestre.setup.config import settings
from mestre.src.exceptions.movie_exceptions import MovieMissingDataFromTMDBAPIException
from mestre.src.movie.models.tmdb_api_caller import tmdb_api_caller


class MovieDetail(BaseModel):
    title: str
    release_date: str
    director: str
    backdrop: str

    @root_validator(pre=True)
    def build_movie_detail(cls, values):
        if not values["title"]:
            raise MovieMissingDataFromTMDBAPIException(
                f"Faltou o 'title' - A API do TMDB deixou a desejar com esse campo"
            )

        elif not values["release_date"]:
            raise MovieMissingDataFromTMDBAPIException(
                f"Faltou o 'release_date' - A API do TMDB deixou a desejar com esse campo"
            )

        elif not values["backdrop_path"]:
            raise MovieMissingDataFromTMDBAPIException(
                f"Faltou o 'backdrop' - A API do TMDB deixou a desejar com esse campo"
            )

        values["title"] = values["title"]
        values["backdrop"] = f'{settings.TMDB_BASE_IMAGE_URL}{values["backdrop_path"]}'
        values["release_date"] = values["release_date"]

        for crew_dict in values["crew"]:
            if crew_dict["job"] == "Director":
                values["director"] = crew_dict["name"]
                break

        if not values["director"]:
            raise MovieMissingDataFromTMDBAPIException(
                f"Faltou o 'director' - A API do TMDB deixou a desejar com esse campo"
            )

        return values


def get_movie_details(movie_id: int):
    url = f"movie/{movie_id}"

    response = tmdb_api_caller(
        method="GET",
        url=url
    )

    return response


def get_movie_crew_data(movie_id: int):
    url = f"movie/{movie_id}/credits"

    response = tmdb_api_caller(
        method="GET",
        url=url
    )

    return response