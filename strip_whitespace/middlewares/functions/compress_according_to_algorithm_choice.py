from typing import Union


def compress(
    buffer: bytes,
    algorithm: Union[
        str("gzip"),
        str("br"),
        str("zstd"),
        str("plain"),
    ] = str("gzip"),
) -> bytes:

    return_buffer: bytes = b""

    if algorithm == str("gzip"):
        try:
            from python_strip_whitespace.functions.compressors.gzip import (
                compress as gz_compress,
            )

        except ImportError:
            raise ImportError(
                """
                'gz_compress' function is missing

                    Did you install the latest python_strip_whitespace?
                    
                    If not install it by:
                        python -m pip install python_strip_whitespace
                """
            )

        return_buffer = gz_compress(buffer)

    elif algorithm == str("br"):
        try:
            from python_strip_whitespace.functions.compressors.brotli import (
                compress as br_compress,
            )

        except ImportError:
            raise ImportError(
                """
                'br_compress' function is missing

                    Did you install the latest python_strip_whitespace?
                    
                    If not install it by:
                        python -m pip install python_strip_whitespace
                """
            )

        return_buffer = br_compress(buffer)

    elif algorithm == str("zstd"):

        try:
            from python_strip_whitespace.functions.compressors.zstd import (
                compress as zstd_compress,
            )

        except ImportError:
            raise ImportError(
                """
                'zstd_compress' function is missing

                    Did you install the latest python_strip_whitespace?
                    
                    If not install it by:
                        python -m pip install python_strip_whitespace
            """
            )

        return_buffer = zstd_compress(buffer)
    else:
        raise AttributeError

    return return_buffer
