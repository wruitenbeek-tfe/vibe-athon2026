from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chatbot import ChatbotService

router = APIRouter(tags=["chat"])
chatbot_service = ChatbotService()


@router.post("/chat", response_model=ChatResponse, response_model_by_alias=False)
async def chat(payload: ChatRequest) -> ChatResponse:
    reply, matches = chatbot_service.generate_reply(payload.message)
    return ChatResponse(reply=reply, matches=matches)
