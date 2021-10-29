from src.movie.models.movie_rating_model import Rating


def movie_rating_view(movie_id: int, rate: Rating):
    result = {
        "nota_publicada": rate.nota,
        "id do filme": movie_id
    }
    return result
