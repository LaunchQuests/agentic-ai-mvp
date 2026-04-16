# =========================
# 🧠 app/agents/analyst_agent.py
# =========================
from openai import OpenAI

client = OpenAI()

def execute_task(task: str):
    prompt = f"""
    Perform this task as an analyst:
    Task: {task}
    Provide a clear result.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content