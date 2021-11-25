from src.movie.models.movie_detail_model import MovieDetail


def movie_detail_view(movie_id: int, model: MovieDetail):
    result = {
        "id": movie_id,
        "titulo": model.title,
        "ano de lançamento": model.release_date,
        "backdrop": model.backdrop,
        "diretor": model.director,
    }
    return result