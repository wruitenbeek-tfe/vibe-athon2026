from app.core.config import get_settings


class ChatbotService:
    def __init__(self) -> None:
        self.settings = get_settings()

    def generate_reply(self, message: str) -> str:
        normalized = message.strip()
        return (
            f"{self.settings.bot_name}: I received '{normalized}'. "
            "Replace `ChatbotService.generate_reply` with your LLM integration."
        )
