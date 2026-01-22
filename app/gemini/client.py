import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai import GenerativeModel

# Force-load .env from project root
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"), override=True)

_model = None

def get_gemini_model():
    global _model

    if _model is not None:
        return _model

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key or not api_key.startswith("AIza"):
        raise RuntimeError(
            f"GEMINI_API_KEY invalid or missing. Value seen: {api_key}"
        )

    genai.configure(api_key=api_key)

    _model = GenerativeModel("gemini-3-flash-preview")
    return _model
