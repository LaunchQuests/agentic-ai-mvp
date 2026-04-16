# =========================
# 🚀 app/main.py
# =========================
from fastapi import FastAPI
from app.models.schemas import GoalRequest
from app.services.orchestrator import run_workflow

app = FastAPI()

@app.get("/")
def health():
    return {"status": "Agentic AI MVP Running"}

@app.post("/execute")
def execute_goal(request: GoalRequest):
    result = run_workflow(request.goal)
    return result