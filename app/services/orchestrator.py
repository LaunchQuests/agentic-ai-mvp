# =========================
# ⚙️ app/services/orchestrator.py
# =========================
from app.agents.goal_agent import breakdown_goal
from app.agents.analyst_agent import execute_task
from app.agents.qa_agent import validate_output


def run_workflow(goal: str):
    tasks = breakdown_goal(goal)

    results = []

    for task in tasks:
        output = execute_task(task)

        if not validate_output(task, output):
            output = execute_task(task)  # retry once

        results.append({
            "task": task,
            "result": output
        })

    final_output = "\n\n".join([r["result"] for r in results])

    return {
        "goal": goal,
        "tasks": tasks,
        "results": results,
        "final_output": final_output
    }