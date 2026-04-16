# =========================
# 🧠 app/agents/goal_agent.py
# =========================
from openai import OpenAI

client = OpenAI()

def breakdown_goal(goal: str):
    prompt = f"""
    Break this goal into 3-5 actionable tasks:
    Goal: {goal}
    Return as a numbered list.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content
    tasks = [t.strip() for t in text.split("\n") if t.strip()]
    return tasks