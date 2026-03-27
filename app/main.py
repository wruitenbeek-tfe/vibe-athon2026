from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.api.routes.chat import router as chat_router
from app.core.config import get_settings

settings = get_settings()
app = FastAPI(title=settings.app_name, debug=settings.debug)
static_dir = Path(__file__).parent / "static"
index_html = (static_dir / "index.html").read_text(encoding="utf-8")

app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/health", tags=["system"])
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", tags=["system"])
async def root() -> HTMLResponse:
    return HTMLResponse(index_html)


app.include_router(chat_router, prefix="/api")
