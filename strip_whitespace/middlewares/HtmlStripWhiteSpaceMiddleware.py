"""
This module strips unnecessary whitespaces from HTML.
    Author : Baseplate-Admin
"""

import asyncio
from typing import List

from python_strip_whitespace import minify_html

from django.conf import settings
from django.utils.decorators import sync_and_async_middleware
from django.http.request import HttpRequest
from django.http.response import HttpResponse

STRIP_WHITESPACE_MINIFY_IGNORED_PATHS: List = getattr(
    settings,
    "STRIP_WHITESPACE_MINIFY_IGNORED_PATHS",
    ["/sitemap.xml"],
)


@sync_and_async_middleware
def html_strip_whitespace(get_response):
    # One-time configuration and initialization goes here.

    ignored_paths: List = STRIP_WHITESPACE_MINIFY_IGNORED_PATHS
    if asyncio.iscoroutinefunction(get_response):

        async def middleware(request: HttpRequest):
            # Do something here!
            response = await get_response(request)
            if not response.streaming and not request.path in ignored_paths:
                content = minify_html(response.content)
                response.content = content
            return response

    else:
        # Sync
        def middleware(request: HttpRequest) -> HttpResponse:
            # Do something here!
            response = get_response(request)
            if not response.streaming and not request.path in ignored_paths:
                content = minify_html(response.content)
                response.content = content
            return response

    return middleware
