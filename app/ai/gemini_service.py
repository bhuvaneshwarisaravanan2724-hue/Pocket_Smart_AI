from google import genai
from app.config import GEMINI_API_KEY


def get_ai_recommendation(prompt: str) -> str:
    if not GEMINI_API_KEY:
        return "AI recommendations are not configured yet."

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        return response.text

    except Exception:
        return (
            "AI recommendation is temporarily unavailable. "
            "Please try again later. Your budget report has still "
            "been generated successfully."
        )