from dotenv import load_dotenv
import os
import google.generativeai as genai

# ✅ Load from .env file
load_dotenv()

# ✅ Get API key
api_key = os.getenv("GEMINI_API_KEY")

# ✅ Configure Gemini
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

prompt = """
User query: "46-year-old male, knee surgery in Pune, 3-month-old insurance policy"

Clause: "Knee replacement is covered only after 90 days of policy activation."

Explain if the clause is relevant to the user query, in simple English.
"""


try:
    response = model.generate_content(prompt)
    print("✅ Gemini Response:\n")
    print(response.text)
except Exception as e:
    print(f"❌ Failed:\n  {e}")
