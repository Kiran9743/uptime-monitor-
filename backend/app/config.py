from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///./uptime.db"
    monitor_interval: int = 60
    request_timeout: float = 10.0
    concurrency_limit: int = 10
    retries: int = 1
    retry_backoff_sec: float = 0.5

    class Config:
        env_file = ".env"


settings = Settings()
