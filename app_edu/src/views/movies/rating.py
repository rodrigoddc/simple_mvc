from src.models.movies.rating import MovieRating


async def render_movie_rating(movie_rating: MovieRating):

    movie_rating = {
        "movie_id": movie_rating.movie_id,
        "rating": movie_rating.rating,
    }

    return movie_rating
