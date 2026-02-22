# AI Resume Intelligence Engine

## Features
- Resume → Structured JSON using Qwen2.5-1.5B-Instruct
- Job Description Matching Score
- FastAPI backend
- Docker deployment

## Run Locally

pip install -r requirements.txt
uvicorn app.main:app --reload

Visit:
http://127.0.0.1:8000/docs