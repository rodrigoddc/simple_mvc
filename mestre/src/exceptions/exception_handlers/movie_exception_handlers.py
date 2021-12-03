from fastapi import Request
from fastapi.responses import JSONResponse

from mestre.src.exceptions.movie_exceptions import MovieRatingException, MovieNotFoundException, \
    MovieMissingDataFromTMDBAPIException


def movie_exception_handler(request: Request, exc: MovieRatingException):
    return JSONResponse(
        status_code=400,
        content={"error": f"Oops, algo de errado não está certo! {exc} "}
    )


def movie_not_found_exception_handler(request: Request, exc: MovieNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"error": f"Oops, algo de errado não está certo! {exc} "}
    )


def movie_missing_data_exception_handler(request: Request, exc: MovieMissingDataFromTMDBAPIException):
    return JSONResponse(
        status_code=409,
        content={"error": f"Oops, algo de errado não está certo! {exc} "}
    )