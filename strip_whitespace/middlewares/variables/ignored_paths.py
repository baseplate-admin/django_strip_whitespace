from typing import List
from django.conf import settings

STRIP_WHITESPACE_MINIFY_IGNORED_PATHS: List = getattr(
    settings,
    "STRIP_WHITESPACE_MINIFY_IGNORED_PATHS",
    [
        "/sitemap.xml",
    ],  # Ignore Sitemap.xml because our code mangles with it.
)
