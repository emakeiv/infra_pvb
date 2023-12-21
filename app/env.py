from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    environment: str
    airflow_uid: int

    aws_access_key_id: str
    aws_secret_access_key: str
    aws_s3_bucket: str

    mlflow_s3_endpoint_url: str
    mlflow_tracking_uri: str

    db_host: str
    driver: str

    postgres_user: str
    postgres_password: str
    postgres_db: str

    main_db: str
    airflow_db: str
    mlflow_db: str

    main_db_url: str

    cwd: str

    alpaca_api_key: str
    alpaca_sec_key: str

    oanda_api_key: str
    oanda_acc_id: str

    auth_secret: str
    auth_algo: str

    class Config:
        env_file = "../.env"
        env_file_encoding = 'utf-8'

settings = Settings()