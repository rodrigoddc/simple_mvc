from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    app_name: str = "App do Edu"
    tmdb_api_key: str = Field(env='TMDB_API_KEY')
    class Config:
        env_file = '.env'

settings = Settings()
tmdb_api_key = settings.tmdb_api_key