from typing import Union
from django.conf import settings

STRIP_WHITESPACE_COMPRESSION_TYPE: Union[
    str("compressed"), str("decompressed")
] = getattr(
    settings,
    "STRIP_WHITESPACE_COMPRESSION_TYPE",
    str("decompressed"),  # By default it should be decompressed
)

STRIP_WHITESPACE_COMPRESSION_ALGORITHM: Union[
    str("gzip"),
    str("br"),
    str("zstd"),
    str("plain"),
] = str(
    "gzip",  # By default set it to GZ because its a python stdlib
)
