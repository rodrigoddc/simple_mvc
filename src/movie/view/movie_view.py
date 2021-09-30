from src.movie.model.movie_model import MovieInfo


def movie_view(movie: MovieInfo):
    movie_view = {
        "title": movie.movie_info.get("title"),
        "release_year": movie.movie_info.get("release_date"),
        "director": movie.credits_info,
        "backdrop": movie.movie_info.get("backdrop_path"),
    }

    return movie_view
