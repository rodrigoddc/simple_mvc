from requests import request

from setup.config import settings
from src.exceptions.movie_exceptions import MovieNotFoundException


def tmdb_api_caller(
        method: str,
        url: str,
        headers: dict = None,
        params: dict = None,
        data: dict = None,
        timeout: int = None
):

    base_url = settings.TMDB_URL_V3
    api_key = settings.TMDB_API_KEY
    url_final = f"{base_url}{url}?api_key={api_key}"

    headers_default = headers

    if not headers:
        headers_default = {
            "content-type": "application/json",
        }

    timeout_deafult = timeout

    if not timeout:
        timeout_deafult = settings.TMDB_API_DEFAULT_TIMEOUT

    raw_response = request(
        method=method,
        headers=headers_default,
        url=url_final,
        params=params,
        data=data,
        timeout=timeout_deafult
    )

    response = tmdb_response_handler(raw_response)

    return response


def tmdb_response_handler(response):

    if response.status_code == 404:
        raise MovieNotFoundException("Filme não encontrado")

    elif not response.ok:
        response.raise_for_status()

    return response.json()