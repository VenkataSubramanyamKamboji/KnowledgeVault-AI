import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_summary(text: str) -> str:

    prompt = f"""
Summarize the following content in 5 concise bullet points.

{text}
"""

    response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=prompt,
)

    return response.text