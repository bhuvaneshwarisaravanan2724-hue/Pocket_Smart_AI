from app.ai.gemini_service import get_ai_recommendation


def generate_budget_recommendation(
    income: float,
    expenses: float
) -> str:
    remaining = income - expenses

    prompt = f"""
You are Pocket Smart AI, a professional personal budgeting assistant.

Monthly income: ₹{income:.2f}
Monthly expenses: ₹{expenses:.2f}
Remaining budget: ₹{remaining:.2f}

Give a short, professional budget recommendation for a Word report.

Use this exact structure:

Budget Status:
Current Spending:
Remaining Budget:
Recommendation:

Keep the response within 4-5 short lines.
Do not use markdown symbols, headings with #, bullet points,
greetings, emojis, or unnecessary explanations.
"""

    return get_ai_recommendation(prompt)