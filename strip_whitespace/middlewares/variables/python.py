"""
    Variables from settings.py
    Default of everything is set to a sane value.
    If you want to modify any varibales. Refer to source.
        Source : https://github.com/juancarlospaco/css-html-js-minify/blob/master/css_html_js_minify/html_minifier.py
"""

from django.conf import settings

STRIP_WHITESPACE_PYTHON_REMOVE_COMMENTS: bool = getattr(
    settings,
    "STRIP_WHITESPACE_PYTHON_REMOVE_COMMENTS",
    False,  # We should really use Rust for this
)

STRIP_WHITESPACE_PYTHON_CONDENSE_STYLE_FROM_HTML: bool = getattr(
    settings, "STRIP_WHITESPACE_PYTHON_CONDENSE_STYLE_FROM_HTML", True
)

STRIP_WHITESPACE_PYTHON_CONDENSE_SCRIPT_FROM_HTML: bool = getattr(
    settings, "STRIP_WHITESPACE_PYTHON_CONDENSE_SCRIPT_FROM_HTML", True
)

STRIP_WHITESPACE_PYTHON_CLEAN_UNNEEDED_HTML_TAGS: bool = getattr(
    settings, "STRIP_WHITESPACE_PYTHON_CLEAN_UNNEEDED_HTML_TAGS", True
)

STRIP_WHITESPACE_PYTHON_CONDENSE_HTML_WHITESPACE: bool = getattr(
    settings,
    "STRIP_WHITESPACE_PYTHON_CONDENSE_HTML_WHITESPACE",
    True,  # WHATEVER YOU DO, DO NOT SET THIS TO FALSE. THIS IS WHERE THE MAGIC HAPPENS
)

STRIP_WHITESPACE_PYTHON_UNQUOTE_HTML_ATTRIBUTES: bool = getattr(
    settings, "STRIP_WHITESPACE_PYTHON_UNQUOTE_HTML_ATTRIBUTES", True
)
