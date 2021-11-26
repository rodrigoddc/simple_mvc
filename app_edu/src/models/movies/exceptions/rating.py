class MovieRatingException(Exception):
    def __init__(self, message):
        self.message = f"MovieRatingException: {message}"
class MovieIdException(Exception):
    def __init__(self, message):
        self.message = f"MovieIdException: {message}"
