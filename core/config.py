import secrets

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "MAILCHIMP"
    APP_DESCRIPTION: str = "A Mailchimp Integration For Telex"
    APP_VERSION: str = "0.0"
    DEBUG: bool = True
    ENV: str = "development"

    BASE_URL: str = "https://mailchimp-8err.onrender.com"
    API_PREFIX: str = "/api/v1"
    MAILCHIMP_KEY: str

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
    def DATABASE_URL(self):
        url = f"mysql+aiomysql://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
        return url

    
    class Config:
        env_file = ".env"  # Load from environment variables or a .env file

mysettings = Settings()
    