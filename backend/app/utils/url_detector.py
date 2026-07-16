from urllib.parse import urlparse


def detect_source_type(url: str) -> str:
    parsed_url = urlparse(url)

    domain = parsed_url.netloc.lower()

    if "youtube.com" in domain or "youtu.be" in domain:
        return "youtube"

    elif "instagram.com" in domain:
        return "instagram"

    else:
        return "website"