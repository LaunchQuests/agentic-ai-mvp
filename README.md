# agentic-ai-mvp
Goal -> Task Breakdown -> Single Analyst -> QA -> Output


# Agentic AI MVP - Phase 1
# Goal -> Task Breakdown -> Single Analyst -> QA -> Output

# =========================
# 📁 Repo Structure
# =========================
# agentic-ai-mvp/
# ├── app/
# │   ├── main.py
# │   ├── agents/
# │   │   ├── goal_agent.py
# │   │   ├── analyst_agent.py
# │   │   └── qa_agent.py
# │   ├── services/
# │   │   └── orchestrator.py
# │   └── models/
# │       └── schemas.py
# ├── requirements.txt
# └── README.md


# =========================
# 📦 requirements.txt
# =========================
fastapi
uvicorn
openai
pydantic



# =========================
# 📘 README.md
# =========================
# Agentic AI MVP

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Test API

POST http://127.0.0.1:8000/execute

Body:
{
  "goal": "Analyze why sales dropped last month"
}

## Next Steps
- Add multiple agents
- Add task queue (Celery/Redis)
- Add frontend (React)
- Add memory layer
