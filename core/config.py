from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///./db.sqlite3"
    db_echo: bool = False


settings = Setting()
