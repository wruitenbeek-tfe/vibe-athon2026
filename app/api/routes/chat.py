from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chatbot import ChatbotService

router = APIRouter(tags=["chat"])
chatbot_service = ChatbotService()


@router.post("/chat", response_model=ChatResponse)
async def chat(payload: ChatRequest) -> ChatResponse:
    reply = chatbot_service.generate_reply(payload.message)
    return ChatResponse(reply=reply)
