from src.models.movies.movie_info import MovieInfo


def render_movie_info(movie: MovieInfo):

    movie_view = {
        "title": movie.title,
        "year": movie.year,
        "director": movie.director,
        "backdrop": movie.backdrop,
    }

    return movie_view
