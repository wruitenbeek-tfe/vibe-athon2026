import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.anyio
async def test_healthcheck() -> None:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.anyio
async def test_root_serves_multi_lane_ui() -> None:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/")

    assert response.status_code == 200
    assert "Choose a solution lane" in response.text
    assert "VibeBot" in response.text
    assert "/static/cv-upload.html" in response.text
    assert "/static/chat-intake.html" in response.text


@pytest.mark.anyio
async def test_chat_intake_endpoint() -> None:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post(
            "/api/match/chat-intake",
            json={"summary": "I know Python, want a senior role in Amsterdam, and prefer English."},
        )

    assert response.status_code == 200
    data = response.json()
    assert data["mode"] == "chat_intake"
    assert data["matches"] == []
    assert "No vacancy ranking is implemented yet." in data["reply"]


@pytest.mark.anyio
async def test_cv_upload_endpoint() -> None:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post(
            "/api/match/cv-upload",
            json={
                "filename": "cv.txt",
                "content": "Python SQL ETL senior Den Haag Engels",
                "notes": "Looking for backend or data role.",
            },
        )

    assert response.status_code == 200
    data = response.json()
    assert data["mode"] == "cv_upload"
    assert data["matches"] == []
    assert data["profile_preview"]
    assert "No vacancy ranking is implemented yet." in data["reply"]


@pytest.mark.anyio
async def test_custom_endpoint_is_not_available() -> None:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post("/api/match/custom", json={"anything": "x"})

    assert response.status_code == 404
