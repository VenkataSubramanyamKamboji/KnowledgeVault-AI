from app.extractors.factory import get_extractor

youtube = get_extractor(
    "https://youtu.be/dQw4w9WgXcQ"
)

instagram = get_extractor(
    "https://www.instagram.com/reel/ABC123/"
)

website = get_extractor(
    "https://medium.com/article"
)

print(type(youtube).__name__)
print(type(instagram).__name__)
print(type(website).__name__)