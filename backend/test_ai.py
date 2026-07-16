from app.services.ai_service import generate_summary

text = """
FastAPI is a modern Python web framework.

It supports automatic validation,
dependency injection,
JWT authentication,
interactive API documentation,
and high performance.
"""

summary = generate_summary(text)

print(summary)