import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_summary(text: str) -> str:
    MAX_CHARS = 10000
    text = text[:MAX_CHARS]

    prompt = f"""
You are an AI assistant for a personal knowledge management system.

Analyze the following content and provide:

1. A concise summary (4-6 sentences).
2. Five key points as bullet points.
3. Three to five relevant tags.

Content:
{text}
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
    )

    return response.text