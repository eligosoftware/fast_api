from pydantic import BaseSettings

class Settings(BaseSettings):
    flask_api_database_hostname: str
    flask_api_database_port: str
    flask_api_database_password: str
    flask_api_database_name: str
    flask_api_database_username: str    
    flask_api_secret_key: str
    flask_api_algorithm: str
    flask_api_access_token_expires: int

    class Config:
        env_file= ".env"

settings=Settings()