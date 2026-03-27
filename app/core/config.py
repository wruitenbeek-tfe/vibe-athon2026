from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Hackathon Chatbot API"
    debug: bool = False
    bot_name: str = "VibeBot"
    vacancies_path: str = "app/vacancies.json"
    max_matches: int = 3
    default_system_prompt: str = (
        "You are a helpful hackathon chatbot. Give concise, practical answers."
    )

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    return Settings()
