import secrets

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "MAILCHIMP"
    APP_DESCRIPTION: str = "A Mailchimp Integration For Telex"
    APP_VERSION: str = "0.0"
    DEBUG: bool = True
    ENV: str = "development"

    BASE_URL: str = "http://ec2-16-171-113-126.eu-north-1.compute.amazonaws.com/"
    API_PREFIX: str = "/api/v1"

    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALLOWED_HOSTS: str = "*"

    DATABASE_POOL_SIZE: int = 10
    DATABASE_TIMEOUT: int = 30
    DATABASE_HOST: str = "127:0:0:1"
    DATABASE_NAME: str = "testdatabase"
    DATABASE_PORT: int = 3306
    DATABASE_USER: str = "testuser"
    DATABASE_PASSWORD: str = "testpassword"

    @property
    def DATABASE_URL():
        url = f"mysql+aiomysql://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"
        return url

    
    class Config:
        env_file = ".env"  # Load from environment variables or a .env file

settings = Settings()
    