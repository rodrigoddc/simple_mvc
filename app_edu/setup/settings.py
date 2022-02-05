from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    app_name: str = "App do Edu"
    tmdb_api_key: str = Field(env="TMDB_API_KEY")
    info_request_base_url: str = "https://api.themoviedb.org/3/"
    tmdb_api_timeout_default: int = 10
    info_request_strategy: str = "async"
    class Config:
        env_file = ".env"
        