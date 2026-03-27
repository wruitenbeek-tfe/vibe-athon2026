# vibe-athon2026

Hackathon starter project for building a chatbot with a FastAPI backend and a simple browser UI.

## Stack

- Python 3.11+
- FastAPI
- Poetry
- Pytest
- Ruff

## Quick Start

Project Setup Guide

This guide explains how to set up and run the project on a completely new machine (macOS, Linux, or Windows). 

## macOS 🍏 

### 1. Install Homebrew (package manager) 

```bash
 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
 ```

Add Homebrew to your PATH (if prompted):

```bash
 echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile eval "$(/opt/homebrew/bin/brew shellenv)"
 ```

### 2. Install Python 
```bash
 brew install python
 ```

Verify installation:
```bash
 python3 --version
 ``` 

### 3. Install Poetry
```bash
 curl -sSL https://install.python-poetry.org | python3 -
 ``` 

Add Poetry to PATH:
```bash
 echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc source ~/.zshrc
 ``` 

Verify:
```bash
 poetry --version
 ``` 

 ### 4. Install dependencies
```bash
 cd your-project poetry install
 ``` 

 ### 5. Start development server 
```bash
 poetry run uvicorn app.main:app --reload
 ``` 

 ### 6. Open API docs
```text
 http://127.0.0.1:8000/docs
 ``` 

 ## Linux 🐧 (Ubuntu/Debian)
### 1. Update system 
```bash
 sudo apt update
 ``` 

 ### 2. Install Python and tools 
```bash
 sudo apt install -y python3 python3-pip python3-venv curl
 ```
Verify: 
```bash
 python3 --version
 ``` 

 ### 3. Install Poetry 
```bash
 curl -sSL https://install.python-poetry.org | python3 -
 ```

Add Poetry to PATH: 
```bash
 echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc source ~/.bashrc
 ```

Verify: 
```bash
 poetry --version
 ``` 

 ### 4. Install dependencies 
```bash
 cd your-project poetry install
 ``` 

 ### 5. Start development server 
```bash
 poetry run uvicorn app.main:app --reload
 ``` 

 ### 6. Open API docs
```text
http://127.0.0.1:8000/docs
 ``` 

 ## Windows 🪟 
### 1. Install Python 
- Download from: https://www.python.org/downloads/windows/ 
- Run the installer 
- ✅ Check **"Add Python to PATH"** 

Verify: 
```powershell
 python --version
 ``` 

### 2. Install Poetry (PowerShell) 
```powershell
 (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
``` 

 ### 3. Add Poetry to PATH Temporary (current session): 
```powershell
 $env:Path += ";$env:USERPROFILE\AppData\Roaming\Python\Scripts"
 ``` 

Permanent: 
- Open **Environment Variables** 
- Add:```C:\Users\<your-user>\AppData\Roaming\Python\Scripts```
- Verify:
```pwershell 
poetry --version
``` 

### 4. Install dependencies 
```powershell
 cd your-project poetry install
 ``` 

 ### 5. Start development server 
```powershell
 poetry run uvicorn app.main:app --reload
 ``` 

 ### 6. Open API docs
```text
 http://127.0.0.1:8000/docs
 ``` 

 ## Notes ⚠️ 
- Ensure `uvicorn` is included in `pyproject.toml`. 
- Restart terminal if `poetry` is not recognized. 
- Port `8000` must be available.

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
- The starter includes `ChatbotService.build_matching_prompt()` and `self.vacancies` as scaffolding for AI-based vacancy ranking. The repository does not implement matching logic for you.
- Add conversation memory, auth, rate limiting, or persistence as needed.
- Expand tests before teams start building features.
