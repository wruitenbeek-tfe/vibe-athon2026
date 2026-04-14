from enum import Enum

from pydantic import BaseModel, Field, model_validator

from app.schemas.vacancy import VacancyMatch


class MatchMode(str, Enum):
    cv_upload = "cv_upload"
    chat_intake = "chat_intake"


class CandidateProfile(BaseModel):
    mode: MatchMode
    text: str = Field(..., min_length=1, description="Normalized text used for matching.")


class CVUploadRequest(BaseModel):
    filename: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1, description="Plain-text CV content.")
    notes: str = Field(default="", description="Optional extra preferences from the candidate.")


class ChatQuestionAnswer(BaseModel):
    question: str = Field(..., min_length=1)
    answer: str = Field(..., min_length=1)


class ChatIntakeRequest(BaseModel):
    summary: str = Field(
        default="",
        description="One free-form chat message that summarizes candidate preferences.",
    )
    answers: list[ChatQuestionAnswer] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_payload(self) -> "ChatIntakeRequest":
        if self.summary.strip() or self.answers:
            return self
        msg = "Provide `summary` or at least one `answers` entry."
        raise ValueError(msg)


class MatchResponse(BaseModel):
    mode: MatchMode
    reply: str
    profile_preview: str
    matches: list[VacancyMatch]
