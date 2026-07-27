import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from app.schemas.ai import AIResponse

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MAX_CHARS = 10000


def generate_ai_metadata(text: str) -> AIResponse:
    text = text[:MAX_CHARS]

    prompt = f"""
You are an AI assistant for a personal knowledge management system.

Analyze the following content.

Content:
{text}
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=AIResponse,
        ),
    )

    return response.parsed
def answer_with_context(
    question: str,
    context: str,
) -> str:

    prompt = f"""
You are an AI assistant for KnowledgeVault AI.

Answer ONLY using the information provided below.

If the answer cannot be found in the context, reply:

"I couldn't find that information in your knowledge base."

Context:

{context}

Question:

{question}
"""

    response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=prompt,
)

    return response.text