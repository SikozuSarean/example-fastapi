from pydantic_settings import BaseSettings  #pip install pydantic-settings # from pydantic import BaseSettings # OLD # NEW


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"
    # path: int
    # # database_password: str = "172.29.64.1"
    # database_user: str = "postgres"
    # secret_key: str = "164bdsjsdzjvbuweav"#fictiv

settings = Settings()

