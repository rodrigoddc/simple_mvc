class MovieNotFoundException(Exception):
    def __init__(self, message):
        self.message = f"MovieNotFoundException: {message}"