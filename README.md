# vibe-athon2026

2-hour hackathon starter for AI-assisted vacancy matching.

Teams can implement one of two solution lanes:
1. CV Upload
2. Chat Intake

## What You Get

- FastAPI backend with ready-to-use endpoints
- Simple frontend: one lane selector page + separate page per lane
- Enriched vacancy dataset (`app/vacancies.json`)
- Mock CV set including strong outliers (`mock-cvs/`)

## Installation

Prerequisites:
- Python 3.11+ (installation guide: https://www.python.org/downloads/)
- Poetry (installation guide: https://python-poetry.org/docs/#installing-with-the-official-installer)

Install dependencies (make sure you're in /vibe-athon2026):

```bash
poetry install
```

## Run Locally

```bash
poetry run uvicorn app.main:app --reload
```

Open:
- `http://127.0.0.1:8000/` (lane selector)
- `http://127.0.0.1:8000/docs` (OpenAPI docs)

## UI Pages

- `http://127.0.0.1:8000/static/cv-upload.html`
- `http://127.0.0.1:8000/static/chat-intake.html`

Both pages submit candidate intake successfully, but vacancy matching is intentionally left as
starter placeholder logic in `app/services/matcher.py`.

## API Endpoints

- `GET /health`
- `POST /api/match/cv-upload`
- `POST /api/match/chat-intake`

## Example Requests

```bash
curl -X POST http://127.0.0.1:8000/api/match/chat-intake \
  -H "Content-Type: application/json" \
  -d '{"summary":"I know Python and SQL, prefer English, and want a senior role in Amsterdam."}'
```

The starter response intentionally returns no ranked vacancies until your team implements the
matching logic.

## Data Model Notes

Vacancies include baseline + richer optional fields:
- baseline: `jobTitle`, `requiredSkills`, `experienceLevel`, `languagesRequired`, etc.
- richer: `mustHaveSkills`, `niceToHaveSkills`, `remotePolicy`, `salaryMin/salaryMax`, `industry`, `companyStage`, `visaSponsorship`, `languageLevel`, `postedAt`

This is intentional: enough structure for better AI matching, but still messy enough for hackathon realism.

## Mock CVs

Use files in `mock-cvs/` for testing.
- Includes normal profiles and heavy outliers (OCR noise, sparse CVs, contradictory timeline, keyword spam, injection-style text).

## Suggested 2-Hour Approach

1. Pick one lane.
2. Improve extraction/normalization for that lane.
3. Replace scoring in `app/services/matcher.py` with your AI strategy.
4. Add one visible improvement in UI or explainability.

## Project Structure

```text
app/
  api/routes/      lane endpoints
  schemas/         request/response models
  services/        intake normalization + matching
  static/          lane selector + per-lane pages
  vacancies.json   enriched vacancy dataset
mock-cvs/          sample and outlier CVs
tests/             starter test suite
```

## Config

Optional `.env` (Place in root, and DON'T COMMIT!):

```env
APP_NAME="Hackathon Matching API"
DEBUG=false
BOT_NAME="VibeBot"
```

## Quality Check

```bash
poetry run ruff check .
poetry run pytest -q
```

## Codex Installation

Via Terminal:

Prequisites:
- NPM (https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

```bash
npm i -g @openai/codex
```

Via IDE:
- `vscode:extension/openai.chatgpt`
- `https://blog.jetbrains.com/ai/2026/01/codex-in-jetbrains-ides/`