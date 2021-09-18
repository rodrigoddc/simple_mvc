def render_movie_info_view(movie: dict):

    movie_view = {
        "title": movie.title,
        "year": movie.year,
        "director": movie.director,
        "backdrop": movie.backdrop,
    }

    return movie_view
