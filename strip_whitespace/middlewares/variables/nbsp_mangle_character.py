from django.conf import settings

STRIP_WHITESPACE_NBSP_MANGLE_CHARACTER: str = getattr(
    settings,
    "STRIP_WHITESPACE_NBSP_MANGLE_CHARACTER",
    "'অ'",  # Using a foreign character so there's almost 0 chance of messing up the translation.
)
