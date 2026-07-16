from app.extractors.website import WebsiteExtractor

extractor = WebsiteExtractor()

result = extractor.extract(
    "https://fastapi.tiangolo.com/"
)

print(result["title"])

print("-" * 50)

print(result["raw_text"][:1000])