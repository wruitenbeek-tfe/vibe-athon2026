from fastapi import FastAPI

from app.api.routes.chat import router as chat_router
from app.core.config import get_settings

settings = get_settings()
app = FastAPI(title=settings.app_name, debug=settings.debug)


@app.get("/health", tags=["system"])
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", tags=["system"])
async def root() -> dict[str, str]:
    return {
        "message": f"{settings.bot_name} is running.",
        "docs": "/docs",
    }


app.include_router(chat_router, prefix="/api")
