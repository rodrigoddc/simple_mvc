from pydantic import BaseSettings, Field
from typing import Optional

class Settings(BaseSettings):
    app_name: str = "App do Edu"
    tmdb_api_key: str = Field(env="TMDB_API_KEY")
    class Config:
        env_file = ".env"