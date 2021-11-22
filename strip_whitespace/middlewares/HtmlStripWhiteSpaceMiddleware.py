"""
This module strips unnecessary whitespaces from HTML.
    Author : Baseplate-Admin
"""

import asyncio
from typing import List

try:
    from python_strip_whitespace import minify_html
except ImportError:
    raise ImportError(
        """
            Did you install the latest python_strip_whitespace?
            
            If not install it by:
                python -m pip install python_strip_whitespace
        """
    )

from django.conf import settings
from django.utils.decorators import sync_and_async_middleware
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from .variables import *

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
            accepted_encodings = request.META.get("HTTP_ACCEPT_ENCODING", "")

            if not response.streaming and not request.path in ignored_paths:
                content = minify_html(
                    response.content,
                    # Rust
                    STRIP_WHITESPACE_RUST_DO_NOT_MINIFY_DOCTYPE,
                    STRIP_WHITESPACE_RUST_ENSURE_SPEC_CONPLIANT_UNQUOTED_ATTRIBUTE_VALUES,
                    STRIP_WHITESPACE_RUST_KEEP_CLOSING_TAGS,
                    STRIP_WHITESPACE_RUST_KEEP_COMMENTS,
                    STRIP_WHITESPACE_RUST_KEEP_HTML_AND_HEAD_OPENING_TAGS,
                    STRIP_WHITESPACE_RUST_KEEP_SPACES_BETWEEN_ATTRIBUTES,
                    STRIP_WHITESPACE_RUST_MINIFY_CSS,
                    STRIP_WHITESPACE_RUST_MINIFY_JS,
                    STRIP_WHITESPACE_RUST_REMOVE_BANGS,
                    STRIP_WHITESPACE_RUST_REMOVE_PROCESSING_INSTRUCTIONS,
                    # Python
                    STRIP_WHITESPACE_PYTHON_REMOVE_COMMENTS,
                    STRIP_WHITESPACE_PYTHON_CONDENSE_STYLE_FROM_HTML,
                    STRIP_WHITESPACE_PYTHON_CONDENSE_SCRIPT_FROM_HTML,
                    STRIP_WHITESPACE_PYTHON_CLEAN_UNNEEDED_HTML_TAGS,
                    STRIP_WHITESPACE_PYTHON_CONDENSE_HTML_WHITESPACE,
                    STRIP_WHITESPACE_PYTHON_UNQUOTE_HTML_ATTRIBUTES,
                    # NBSP char
                    STRIP_WHITESPACE_NBSP_MANGLE_CHARACTER,
                    # Compression Settings
                    STRIP_WHITESPACE_COMPRESSION_TYPE,
                )
                response.content = content
            return response

    else:
        # Sync
        def middleware(request: HttpRequest) -> HttpResponse:
            # Do something here!
            response = get_response(request)
            if not response.streaming and not request.path in ignored_paths:
                content = minify_html(
                    response.content,
                    # Rust
                    STRIP_WHITESPACE_RUST_DO_NOT_MINIFY_DOCTYPE,
                    STRIP_WHITESPACE_RUST_ENSURE_SPEC_CONPLIANT_UNQUOTED_ATTRIBUTE_VALUES,
                    STRIP_WHITESPACE_RUST_KEEP_CLOSING_TAGS,
                    STRIP_WHITESPACE_RUST_KEEP_COMMENTS,
                    STRIP_WHITESPACE_RUST_KEEP_HTML_AND_HEAD_OPENING_TAGS,
                    STRIP_WHITESPACE_RUST_KEEP_SPACES_BETWEEN_ATTRIBUTES,
                    STRIP_WHITESPACE_RUST_MINIFY_CSS,
                    STRIP_WHITESPACE_RUST_MINIFY_JS,
                    STRIP_WHITESPACE_RUST_REMOVE_BANGS,
                    STRIP_WHITESPACE_RUST_REMOVE_PROCESSING_INSTRUCTIONS,
                    # Python
                    STRIP_WHITESPACE_PYTHON_REMOVE_COMMENTS,
                    STRIP_WHITESPACE_PYTHON_CONDENSE_STYLE_FROM_HTML,
                    STRIP_WHITESPACE_PYTHON_CONDENSE_SCRIPT_FROM_HTML,
                    STRIP_WHITESPACE_PYTHON_CLEAN_UNNEEDED_HTML_TAGS,
                    STRIP_WHITESPACE_PYTHON_CONDENSE_HTML_WHITESPACE,
                    STRIP_WHITESPACE_PYTHON_UNQUOTE_HTML_ATTRIBUTES,
                    # NBSP char
                    STRIP_WHITESPACE_NBSP_MANGLE_CHARACTER,
                )
                response.content = content
            return response

    return middleware
