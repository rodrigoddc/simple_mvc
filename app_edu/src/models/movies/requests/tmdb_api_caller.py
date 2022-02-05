import aiohttp
from setup.settings import Settings
from src.models.movies.exceptions.notfound import MovieNotFoundException
import requests


def tmdb_api_caller(
        method: str,
        url: str,
        session: aiohttp.ClientSession = None,
        headers: dict = None,
        params: dict = None,
        data: dict = None,
        timeout: int = None
):

    api_key = Settings().tmdb_api_key
    base_url = Settings().info_request_base_url
    url_final = f"{base_url}{url}?api_key={api_key}"

    headers_default = headers

    if not headers:
        headers_default = {
            "content-type": "application/json",
        }

    timeout_default = timeout

    if not timeout:
        timeout_default = Settings().tmdb_api_timeout_default

    if session:
        raw_response = session.request(
            method=method,
            url=url_final,
            params=params,
            data=data,
            timeout=timeout_default,
            headers=headers_default,
        )

        return raw_response
    
    return requests.request(
            method=method,
            url=url_final,
            params=params,
            data=data,
            timeout=timeout_default,
            headers=headers_default,
        )


def tmdb_response_handler(response):

    try:
        status = response.status
    except:
        status = response.status_code

    if status == 404:
        raise MovieNotFoundException("Filme não encontrado")

    elif not response.ok:
        response.raise_for_status()

    return response.json()