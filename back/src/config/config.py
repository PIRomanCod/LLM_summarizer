from pydantic import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_database_url: str = 'postgresql+psycopg2://user:password@localhost:5432/postgres'
    data_folder: str = 'name'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()