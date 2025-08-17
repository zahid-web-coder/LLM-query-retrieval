import google.generativeai as genai
import os
from dotenv import load_dotenv

# ✅ Load environment variables from .env
load_dotenv()

# ✅ Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ Use Gemini 1.5 Flash or Gemini-Pro
model = genai.GenerativeModel("gemini-1.5-flash")  # You can change to "gemini-pro" if needed

def explain_clause(query: str, clause: str) -> str:
    """
    Uses Gemini to explain why a clause matches the user query.
    """
    prompt = f"""
    User query: "{query}"

    Clause from document: "{clause}"

    Explain in 2-3 sentences why this clause is relevant to the query, in simple English.
    Only explain if the clause is relevant.
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Explanation failed: {e}"
