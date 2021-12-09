import asyncio, aiohttp
from pydantic import BaseModel, root_validator
from mestre.setup.config import settings
from mestre.src.exceptions.movie_exceptions import MovieMissingDataFromTMDBAPIException
from mestre.src.movie.models.tmdb_api_caller import tmdb_api_caller, tmdb_response_handler


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

def _movie_details_url(movie_id: int):
    return f"movie/{movie_id}"

def _movie_crew_url(movie_id: int):
    return f"movie/{movie_id}/credits"

def get_tasks(urls, session):
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(
            tmdb_api_caller(
                url=url, 
                method="GET", 
                session=session
                )
            )
        )
    return tasks

async def fetch_movie_details_and_movie_crew(movie_id):
    urls = [
        _movie_details_url(movie_id), 
        _movie_crew_url(movie_id)
    ]
    async with aiohttp.ClientSession() as session:
        results = []
        tasks = get_tasks(urls, session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await tmdb_response_handler(response))
        
        return results
