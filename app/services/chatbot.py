from app.core.config import get_settings
from app.data.vacancies import load_vacancies
from app.schemas.vacancy import VacancyMatch


class ChatbotService:
    def __init__(self) -> None:
        self.settings = get_settings()
        self.vacancies = load_vacancies()

    def generate_reply(self, message: str) -> tuple[str, list[VacancyMatch]]:
        normalized = message.strip()
        reply = (
            f"{self.settings.bot_name}: I received '{normalized}'. "
            "Vacancy matching is intentionally not implemented here. "
            "Use `build_matching_prompt()` and `self.vacancies` to ask your AI model to rank vacancies "
            "and return `list[VacancyMatch]`."
        )
        return reply, []

    def build_matching_prompt(self, message: str) -> str:
        return f"""
{self.settings.default_system_prompt}

Task:
- Read the user request.
- Review the vacancy dataset.
- Select up to {self.settings.max_matches} relevant vacancies.
- Return JSON with:
  - `reply`: short explanation to the user
  - `matches`: array of objects with `vacancy`, `score`, and `reasons`
- Do not invent vacancies.

User request:
{message.strip()}

Vacancies:
{self._format_vacancies_for_prompt()}
""".strip()

    def _format_vacancies_for_prompt(self) -> str:
        formatted_vacancies: list[str] = []
        for index, vacancy in enumerate(self.vacancies, start=1):
            formatted_vacancies.append(
                "\n".join(
                    [
                        f"{index}. {vacancy.job_title}",
                        f"   location: {vacancy.location}",
                        f"   employment_type: {vacancy.employment_type}",
                        f"   experience_level: {vacancy.experience_level}",
                        f"   education_level: {vacancy.education_level}",
                        f"   languages_required: {', '.join(vacancy.languages_required)}",
                        f"   required_skills: {', '.join(vacancy.required_skills)}",
                        f"   job_description: {vacancy.job_description}",
                    ]
                )
            )
        return "\n\n".join(formatted_vacancies)
