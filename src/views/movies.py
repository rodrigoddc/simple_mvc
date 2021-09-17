from src.models.movie import Movie


class MovieViews:
    @staticmethod
    def _setup_movie_view(movie: Movie):
        movie.titulo = "api_call_titulo"
        movie.ano = "api_call_ano"
        movie.diretor = "api_call_diretor"
        movie.backdrop = "api_call_backdrop"

    def movie_view(self, movie: Movie):
        return self._setup_movie_view(movie)
