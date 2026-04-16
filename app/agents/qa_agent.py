# =========================
# 🧠 app/agents/qa_agent.py
# =========================
from openai import OpenAI

client = OpenAI()

def validate_output(task: str, output: str):
    prompt = f"""
    Validate this output.
    Task: {task}
    Output: {output}
    Return ONLY 'PASS' or 'FAIL'.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content.strip()
    return result == "PASS"