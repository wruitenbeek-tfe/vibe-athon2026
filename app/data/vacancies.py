import json
from functools import lru_cache
from pathlib import Path

from app.core.config import get_settings
from app.schemas.vacancy import Vacancy


@lru_cache
def load_vacancies() -> list[Vacancy]:
    settings = get_settings()
    dataset_path = Path(settings.vacancies_path)
    raw_vacancies = json.loads(dataset_path.read_text(encoding="utf-8"))
    return [Vacancy.model_validate(item) for item in raw_vacancies]
