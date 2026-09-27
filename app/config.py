import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "Pocket Smart AI"

SECRET_KEY = os.getenv("SECRET_KEY", "pocket-smart-ai-secret-key")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")