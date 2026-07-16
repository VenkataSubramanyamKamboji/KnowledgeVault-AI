from app.utils.url_detector import detect_source_type

print(
    detect_source_type(
        "https://youtu.be/dQw4w9WgXcQ"
    )
)

print(
    detect_source_type(
        "https://www.instagram.com/reel/DM12345/"
    )
)

print(
    detect_source_type(
        "https://medium.com/@someone/awesome-article"
    )
)