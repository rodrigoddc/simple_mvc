from src.model.movie_model import MovieInfo


def movie_view(movie: MovieInfo):
    movie_view = {
        "title": movie.nome,
        "year": movie.release_year,
        "director": None,
        "backdrop": movie.backdrop,
    }

    return movie_view
