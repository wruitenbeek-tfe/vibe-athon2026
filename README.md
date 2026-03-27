# vibe-athon2026

Hackathon starter project for building a chatbot with a FastAPI backend and a simple browser UI.

## Stack

- Python 3.11+
- FastAPI
- Poetry
- Pytest
- Ruff

## Quick Start

1. Install Poetry if it is not already available:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
2. Install dependencies:

```bash
poetry install
```

3. Start the development server:

```bash
poetry run uvicorn app.main:app --reload
```

4. Open the API docs:

```text
http://127.0.0.1:8000/docs
```

## Project Structure

```text
app/
  api/routes/      HTTP routes
  core/            Settings and shared config
  schemas/         Request and response models
  services/        Chatbot business logic
tests/             Starter test suite
```

## Available Endpoints

- `GET /` basic service info
- `GET /` chat web interface
- `GET /health` healthcheck
- `POST /api/chat` chatbot endpoint

Example request:

```bash
curl -X POST http://127.0.0.1:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"How do I win this hackathon?"}'
```

## Configuration

Environment variables can be added to a local `.env` file.

```env
APP_NAME="Hackathon Chatbot API"
DEBUG=false
BOT_NAME="VibeBot"
DEFAULT_SYSTEM_PROMPT="You are a helpful hackathon chatbot. Give concise, practical answers."
```

## Where To Extend

- Replace `app/services/chatbot.py` with an OpenAI, Anthropic, or local model integration.
- Add conversation memory, auth, rate limiting, or persistence as needed.
- Expand tests before teams start building features.
