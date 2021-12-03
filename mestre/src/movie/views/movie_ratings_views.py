from mestre.src.movie.models.movie_rating_model import Rating


def movie_rating_view(movie_id: int, model: Rating):
    result = {
        "nota_publicada": model.nota,
        "id do filme": movie_id
    }
    return result
