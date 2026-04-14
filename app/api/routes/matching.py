from fastapi import APIRouter

from app.schemas.matching import (
    ChatIntakeRequest,
    CVUploadRequest,
    MatchResponse,
)
from app.services.intake import IntakeService
from app.services.matcher import VacancyMatcherService

router = APIRouter(tags=["matching"])
intake_service = IntakeService()
matcher_service = VacancyMatcherService()


@router.post("/match/cv-upload", response_model=MatchResponse, response_model_by_alias=False)
async def match_from_cv_upload(payload: CVUploadRequest) -> MatchResponse:
    profile = intake_service.from_cv_upload(payload)
    return matcher_service.match(profile)


@router.post("/match/chat-intake", response_model=MatchResponse, response_model_by_alias=False)
async def match_from_chat(payload: ChatIntakeRequest) -> MatchResponse:
    profile = intake_service.from_chat_intake(payload)
    return matcher_service.match(profile)
