from pydantic import BaseModel, Field

from app.schemas.vacancy import VacancyMatch


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="The user's message to the chatbot.")


class ChatResponse(BaseModel):
    reply: str
    matches: list[VacancyMatch]
