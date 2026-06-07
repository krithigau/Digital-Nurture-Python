"""
51. URL Shortener
• Objective: Use dictionaries, hashing, classes, and modules to build a simple URL
shortening service.
• Task: Create a basic URL shortener that can shorten URLs and retrieve the original URL
"""
import hashlib

class URLShortener:

    def __init__(self):

        self.url_map = {}

    def shorten_url(self, long_url):

        short_code = hashlib.md5(
            long_url.encode()
        ).hexdigest()[:6]

        self.url_map[short_code] = long_url

        return short_code

    def get_original_url(self, short_code):

        return self.url_map.get(
            short_code,
            "URL Not Found"
        )


shortener = URLShortener()

short_url = shortener.shorten_url(
    "https://www.cognizant.com"
)

print("Short URL:", short_url)

print(
    "Original URL:",
    shortener.get_original_url(short_url)
)