import aiohttp
from mestre.setup.config import settings
from mestre.src.exceptions.movie_exceptions import MovieNotFoundException


def tmdb_api_caller(
        method: str,
        url: str,
        session: aiohttp.ClientSession,
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

    timeout_default = timeout

    if not timeout:
        timeout_default = settings.TMDB_API_DEFAULT_TIMEOUT

    raw_response = session.request(
        method=method,
        url=url_final,
        params=params,
        data=data,
        timeout=timeout_default,
        headers=headers_default,
    )

    return raw_response


def tmdb_response_handler(response):

    if response.status == 404:
        raise MovieNotFoundException("Filme não encontrado")

    elif not response.ok:
        response.raise_for_status()

    return response.json()