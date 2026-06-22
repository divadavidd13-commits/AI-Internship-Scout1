from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def gemini_score(company, role):

    prompt = f"""
    Rate this internship from 1-100.

    Student interests:
    - AI
    - Machine Learning
    - Python
    - Cloud
    - Software Engineering

    Company: {company}
    Role: {role}

    Return ONLY a number.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()
