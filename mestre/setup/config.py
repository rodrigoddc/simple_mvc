from pydantic import BaseSettings


class Settings(BaseSettings):
    TMDB_URL_V3: str
    TMDB_API_KEY: str
    TMDB_BASE_IMAGE_URL: str
    TMDB_API_DEFAULT_TIMEOUT: int = 10

    class Config:
        env_file = ".env"


settings = Settings()