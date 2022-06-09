from pydantic import BaseSettings


class Settings(BaseSettings):
    database_ip: str
    database_name: str
    database_user: str
    database_password: str

    class Config:
        env_file = ".env"


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')