from typing import Union
from django.conf import settings

STRIP_WHITESPACE_COMPRESSION_TYPE: Union[
    str("compressed"), str("decompressed")
] = getattr(
    settings,
    "STRIP_WHITESPACE_COMPRESSION_TYPE",
    str("decompressed"),  # By default it should be decompressed
)
