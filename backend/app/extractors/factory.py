from app.utils.url_detector import detect_source_type

from app.extractors.website import WebsiteExtractor
from app.extractors.youtube import YouTubeExtractor
from app.extractors.instagram import InstagramExtractor


def get_extractor(url: str):

    source = detect_source_type(url)

    if source == "youtube":
        return YouTubeExtractor()

    elif source == "instagram":
        return InstagramExtractor()

    else:
        return WebsiteExtractor()